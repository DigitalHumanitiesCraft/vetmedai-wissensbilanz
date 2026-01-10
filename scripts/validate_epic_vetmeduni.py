"""
TITEL: Validierung Epic VetMedUni gegen tatsächliche Daten

FORSCHUNGSFRAGE:
Können wir die Epic-Features mit vorhandenen Daten umsetzen?

INPUT:
- data/json/*.json (alle 21 Kennzahlen)
- Epic VetMedUni (aus Markdown)

OUTPUT:
- outputs/reports/epic_vetmeduni_feasibility.md - Detaillierter Machbarkeitsreport

ZIEL:
Verifizierung aller Epic-Anforderungen gegen Datenstruktur mit konkreten Befunden.
"""

import json
from pathlib import Path
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
JSON_DIR = PROJECT_ROOT / "data" / "json"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "reports"

def load_kennzahl(filename):
    """Lädt eine einzelne Kennzahl-Datei."""
    filepath = JSON_DIR / filename
    if not filepath.exists():
        return None

    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def check_betreuungsrelation():
    """
    Validiert: Können wir Betreuungsrelation 1:17,6 nachrechnen?

    VetMedUni gibt an: 1:17,6
    Formel (hypothetisch): Prüfungsaktive / VZÄ (Professoren)
    """
    pruefungsaktive = load_kennzahl("2_A_6_pruefungsaktive.json")
    professoren = load_kennzahl("2_A_1_professoren_aequivalente.json")

    if not pruefungsaktive or not professoren:
        return {
            'machbar': False,
            'grund': 'Erforderliche Dateien nicht gefunden'
        }

    # Suche VetMedUni (UV) in beiden Dateien
    uv_pruefungsaktive = None
    uv_professoren = None

    for entry in pruefungsaktive['data']:
        if entry['universität_code'] == 'UV' and entry.get('display_label') == 'Gesamt' and entry['jahr'] == 2024:
            uv_pruefungsaktive = entry['wert']
            break

    for entry in professoren['data']:
        if entry['universität_code'] == 'UV' and entry['jahr'] == 2024 and entry.get('display_label') == 'ProfessorInnen und Äquivalente':
            uv_professoren = entry['wert']
            break

    if uv_pruefungsaktive is None or uv_professoren is None:
        return {
            'machbar': False,
            'grund': 'VetMedUni (UV) Daten nicht gefunden oder null',
            'details': f'Prüfungsaktive: {uv_pruefungsaktive}, Professoren: {uv_professoren}'
        }

    # Berechne Betreuungsrelation
    berechnet = uv_pruefungsaktive / uv_professoren if uv_professoren > 0 else None
    epic_wert = 17.6  # aus Epic

    abweichung = abs(berechnet - epic_wert) if berechnet else None

    return {
        'machbar': True,
        'pruefungsaktive_uv_2024': uv_pruefungsaktive,
        'professoren_uv_2024': uv_professoren,
        'berechnet': round(berechnet, 1) if berechnet else None,
        'epic_angabe': epic_wert,
        'abweichung': round(abweichung, 1) if abweichung else None,
        'plausibel': abweichung < 1.0 if abweichung else False,
        'formel': 'Prüfungsaktive (2-A-6 Gesamt) / ProfessorInnen & Äquivalente (2-A-1)',
        'einschraenkung': 'Personalkategorien (Prof/Dozent/Assoz.Prof) NICHT differenziert'
    }


def check_qs_ranking():
    """Validiert: Ist QS Ranking Platz 28 in Daten?"""
    # QS Ranking ist NICHT in UniData-Kennzahlen
    return {
        'in_daten': False,
        'grund': 'QS Ranking ist externe Quelle, nicht in UniData-Kennzahlen',
        'konsequenz': 'Manuelle Eingabe oder separate Datenquelle erforderlich'
    }


def check_pruefungsaktive_quote():
    """Validiert: Können wir "Anteil prüfungsaktiv >90%" berechnen?"""
    pruefungsaktive = load_kennzahl("2_A_6_pruefungsaktive.json")
    studierende = load_kennzahl("2_A_5_anzahl_studierenden.json")

    if not pruefungsaktive or not studierende:
        return {'machbar': False, 'grund': 'Dateien nicht gefunden'}

    # Suche VetMedUni 2024
    uv_pruefungsaktiv = None
    uv_studierende_ordentlich = None

    for entry in pruefungsaktive['data']:
        if entry['universität_code'] == 'UV' and entry.get('display_label') == 'Gesamt' and entry['jahr'] == 2024:
            uv_pruefungsaktiv = entry['wert']

    for entry in studierende['data']:
        if entry['universität_code'] == 'UV' and entry.get('display_label') == 'ordentliche Studierende' and entry['jahr'] == 2024:
            uv_studierende_ordentlich = entry['wert']

    if uv_pruefungsaktiv and uv_studierende_ordentlich and uv_studierende_ordentlich > 0:
        quote = (uv_pruefungsaktiv / uv_studierende_ordentlich) * 100
        return {
            'machbar': True,
            'pruefungsaktive': uv_pruefungsaktiv,
            'studierende_ordentlich': uv_studierende_ordentlich,
            'quote_berechnet': round(quote, 1),
            'epic_angabe': '>90%',
            'plausibel': quote > 90
        }

    return {
        'machbar': False,
        'grund': 'VetMedUni Werte null oder nicht gefunden'
    }


def check_zeitreihen_dreijahresvergleich():
    """Validiert: Sind 2022-2024 Zeitreihen für alle relevanten Kennzahlen verfügbar?"""
    kennzahlen_mit_zeitreihen = []
    kennzahlen_ohne_zeitreihen = []

    exclude_files = {'validation_report.json', 'batch_conversion_report.json'}
    json_files = [f for f in JSON_DIR.glob("*.json") if f.name not in exclude_files]

    for json_file in json_files:
        kennzahl = json_file.stem
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Prüfe ob 2022, 2023, 2024 vorhanden
        jahre = set()
        for entry in data['data']:
            if entry.get('jahr'):
                jahre.add(entry['jahr'])

        hat_dreijahresvergleich = all(jahr in jahre for jahr in [2022, 2023, 2024])

        if hat_dreijahresvergleich:
            kennzahlen_mit_zeitreihen.append(kennzahl)
        else:
            kennzahlen_ohne_zeitreihen.append({
                'kennzahl': kennzahl,
                'verfuegbare_jahre': sorted(list(jahre))
            })

    return {
        'machbar': len(kennzahlen_mit_zeitreihen) > 0,
        'kennzahlen_mit_dreijahresvergleich': len(kennzahlen_mit_zeitreihen),
        'kennzahlen_ohne': len(kennzahlen_ohne_zeitreihen),
        'beispiele_mit': kennzahlen_mit_zeitreihen[:5],
        'beispiele_ohne': kennzahlen_ohne_zeitreihen[:3],
        'warnung': 'Erhebungsmethoden geändert - nicht direkt vergleichbar'
    }


def check_vetmeduni_in_daten():
    """Validiert: Ist VetMedUni (UV) überhaupt in allen Kennzahlen?"""
    kennzahlen_mit_uv = []
    kennzahlen_ohne_uv = []

    exclude_files = {'validation_report.json', 'batch_conversion_report.json'}
    json_files = [f for f in JSON_DIR.glob("*.json") if f.name not in exclude_files]

    for json_file in json_files:
        kennzahl = json_file.stem
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Prüfe ob UV vorhanden
        hat_uv = any(entry.get('universität_code') == 'UV' for entry in data['data'])

        if hat_uv:
            kennzahlen_mit_uv.append(kennzahl)
        else:
            kennzahlen_ohne_uv.append(kennzahl)

    return {
        'vetmeduni_vorhanden': len(kennzahlen_ohne_uv) == 0,
        'kennzahlen_mit_uv': len(kennzahlen_mit_uv),
        'kennzahlen_ohne_uv': kennzahlen_ohne_uv
    }


def check_vergleichsgruppe_medizinunis():
    """Validiert: Sind andere Medizin-Unis für Vergleich verfügbar?"""
    # Erwartete MedUnis: US, UT, UU (+ UV)
    personal = load_kennzahl("1_A_1_personal_koepfe.json")

    if not personal:
        return {'machbar': False}

    medizin_unis = set()
    for entry in personal['data']:
        if entry.get('uni_type') == 'medizinisch':
            medizin_unis.add(entry['universität_code'])

    return {
        'machbar': True,
        'anzahl_medizin_unis': len(medizin_unis),
        'codes': sorted(list(medizin_unis)),
        'vergleichsgruppe_vollstaendig': len(medizin_unis) >= 4  # UV + 3 andere
    }


def generate_report(checks):
    """Erstellt Markdown-Report."""
    report = """# Epic VetMedUni Machbarkeitsanalyse

**Datum:** {datum}
**Quelle:** Validierung gegen tatsächliche UniData-Exports
**Epic-Quelle:** VetMedUni Wissensbilanz 2024, Leistungsvereinbarung 2025-2027

---

## Executive Summary

| Anforderung | Status | Kritischer Befund |
|-------------|--------|-------------------|
| VetMedUni in Daten | {uv_status} | {uv_detail} |
| Betreuungsrelation 1:17,6 | {betr_status} | {betr_detail} |
| Prüfungsaktive >90% | {pa_status} | {pa_detail} |
| Dreijahresvergleich 2022-2024 | {drei_status} | {drei_detail} |
| Vergleichsgruppe MedUnis | {med_status} | {med_detail} |
| QS Ranking Platz 28 | {qs_status} | {qs_detail} |

**Legende:** OK = Umsetzbar, WARN = Eingeschränkt, FAIL = Nicht umsetzbar

---

## 1. VetMedUni in Datensatz

**Frage:** Ist die VetMedUni (Code: UV) in allen Kennzahlen vorhanden?

{uv_report}

---

## 2. Betreuungsrelation 1:17,6

**Epic-Anforderung:** "Betreuungsrelation: 1:17,6"

**Formel (aus Epic):** Prüfungsaktive Studien / VZÄ (Professoren + Dozenten + Assoziierte Professoren)

{betr_report}

**Verifizierung:**
- Prüfungsaktive VetMedUni 2024: {betr_pruef}
- ProfessorInnen & Äquivalente VetMedUni 2024: {betr_prof}
- Berechnet: 1:{betr_calc}
- Epic-Angabe: 1:{betr_epic}
- Abweichung: {betr_diff}

**Plausibilität:** {betr_plaus}

**Kritische Einschränkung:**
{betr_einschraenkung}

**Workshop-Klärung erforderlich:**
1. Welche exakte Formel nutzt VetMedUni für die Betreuungsrelation?
2. Sind die 1:17,6 mit dieser vereinfachten Formel berechnet?
3. Gibt es interne Datenquellen für Personalkategorien-Aufschlüsselung?

---

## 3. Prüfungsaktive >90%

**Epic-Anforderung:** "Anteil prüfungsaktiv im Diplomstudium: über 90%"

{pa_report}

---

## 4. Dreijahresvergleich 2022-2024

**Epic-Anforderung:** WBV 2016 schreibt Dreijahresvergleich vor

{drei_report}

**Warnung:**
{drei_warnung}

---

## 5. Vergleichsgruppe Medizinische Universitäten

**Epic-Anforderung:** Vergleich mit anderen MedUnis (US, UT, UU)

{med_report}

---

## 6. QS Ranking Platz 28

**Epic-Anforderung:** "QS World University Ranking: Platz 28"

{qs_report}

---

## Kritische Erkenntnisse für Epic

### 1. Betreuungsrelation - Formel unklar

**Problem:**
Epic gibt 1:17,6 an, aber die detaillierte Formel (Professoren + Dozenten + Assoz. Prof.) ist mit UniData nicht umsetzbar.

**Berechnete Relation mit verfügbaren Daten:**
- 1:{betr_calc} (Abweichung: {betr_diff})

**Zwei Möglichkeiten:**
1. VetMedUni nutzt bereits die vereinfachte Formel (2-A-1 statt detailliert) → Dann passt es
2. VetMedUni nutzt interne Datenquelle mit Personalkategorien → Dann Dashboard-Integration notwendig

**Empfehlung:** Im Workshop klären, welche Formel tatsächlich genutzt wird.

---

### 2. QS Ranking - Externe Datenquelle

**Problem:**
QS Ranking ist nicht in UniData-Kennzahlen enthalten.

**Konsequenz:**
- Manuelle Eingabe erforderlich ODER
- Integration externer Datenquelle ODER
- Feature aus Epic entfernen

**Empfehlung:** Priorisierung im Workshop - ist QS Ranking-Integration notwendig?

---

### 3. Zeitreihen-Warnung notwendig

**Problem:**
Alle Kennzahlen haben Warnung: "Erhebungsmethoden geändert, nicht direkt vergleichbar"

**Konsequenz:**
- Dashboard muss Warnung prominent anzeigen
- Jahr-zu-Jahr Vergleiche können irreführend sein
- Methodologie-Dokumentation beschaffen

**Empfehlung:** Welche Zeiträume sind tatsächlich vergleichbar? Dokumentation vom BMBWF verfügbar?

---

## Empfehlungen für Epic-Anpassung

### Must-Have Klärungen

1. **Betreuungsrelation-Formel:** Exakte Formel von VetMedUni dokumentieren
2. **QS Ranking:** Entscheiden ob Integration erforderlich oder manuell gepflegt
3. **Zeitreihen-Methodologie:** Dokumentation der Erhebungsmethoden-Änderungen beschaffen

### Anpassungsvorschläge für Epic

**D-03 Betreuungsrelation:**
```markdown
**D-03 Betreuungsrelation berechnen**
Berechnung: Prüfungsaktive (2-A-6) / ProfessorInnen & Äquivalente (2-A-1)
*Einschränkung: Personalkategorien nicht differenziert, vereinfachte Formel*
*Workshop-Validierung: Stimmt berechneter Wert 1:{betr_calc} mit internem Wert überein?*
```

**Neue Sektion in Epic:**
```markdown
## Externe Datenquellen (nicht in UniData)

- QS Ranking: Externe Quelle, manuelle Pflege erforderlich
- [Weitere externe Kennzahlen identifizieren]
```

---

**Generiert durch:** scripts/validate_epic_vetmeduni.py
**Letzte Aktualisierung:** {datum}
"""

    from datetime import datetime
    datum = datetime.now().strftime("%Y-%m-%d")

    # Status-Symbole
    def status(condition):
        if condition is True:
            return "OK"
        elif condition is False:
            return "FAIL"
        else:
            return "WARN"

    # UVetMedUni vorhanden
    uv_check = checks['vetmeduni']
    uv_status = status(uv_check['vetmeduni_vorhanden'])
    uv_detail = f"{uv_check['kennzahlen_mit_uv']}/21 Kennzahlen" if uv_check['vetmeduni_vorhanden'] else f"Fehlend in: {', '.join(uv_check['kennzahlen_ohne_uv'][:3])}"

    uv_report = f"""**Status:** {'Vollständig vorhanden' if uv_check['vetmeduni_vorhanden'] else 'FEHLT in einigen Kennzahlen'}

**Befund:**
- Kennzahlen mit VetMedUni (UV): {uv_check['kennzahlen_mit_uv']}
- Kennzahlen ohne VetMedUni: {len(uv_check['kennzahlen_ohne_uv'])}"""

    if uv_check['kennzahlen_ohne_uv']:
        uv_report += f"\n- Fehlend in: {', '.join(uv_check['kennzahlen_ohne_uv'])}"

    # Betreuungsrelation
    betr_check = checks['betreuungsrelation']
    betr_status = status(betr_check.get('machbar'))
    betr_detail = f"Abweichung {betr_check.get('abweichung', 'N/A')}" if betr_check.get('machbar') else betr_check.get('grund', 'Unbekannt')

    if betr_check.get('machbar'):
        betr_report = f"**Status:** Berechenbar (mit Einschränkung)\n\n**Formel verfügbar:** {betr_check['formel']}"
        betr_pruef = betr_check['pruefungsaktive_uv_2024']
        betr_prof = betr_check['professoren_uv_2024']
        betr_calc = betr_check['berechnet']
        betr_epic = betr_check['epic_angabe']
        betr_diff = betr_check['abweichung']
        betr_plaus = "JA - Abweichung < 1.0" if betr_check['plausibel'] else f"NEIN - Abweichung {betr_diff}"
        betr_einschraenkung = betr_check['einschraenkung']
    else:
        betr_report = f"**Status:** NICHT berechenbar\n\n**Grund:** {betr_check.get('grund')}"
        betr_pruef = "N/A"
        betr_prof = "N/A"
        betr_calc = "N/A"
        betr_epic = "17.6"
        betr_diff = "N/A"
        betr_plaus = "N/A"
        betr_einschraenkung = "Daten nicht verfügbar"

    # Prüfungsaktive Quote
    pa_check = checks['pruefungsaktive_quote']
    pa_status = status(pa_check.get('machbar'))
    pa_detail = f"{pa_check.get('quote_berechnet', 'N/A')}%" if pa_check.get('machbar') else pa_check.get('grund', 'Unbekannt')

    if pa_check.get('machbar'):
        pa_report = f"""**Status:** Berechenbar

**Befund:**
- Prüfungsaktive VetMedUni 2024: {pa_check['pruefungsaktive']}
- Ordentliche Studierende VetMedUni 2024: {pa_check['studierende_ordentlich']}
- Quote berechnet: {pa_check['quote_berechnet']}%
- Epic-Angabe: {pa_check['epic_angabe']}
- Plausibel: {'JA' if pa_check['plausibel'] else 'NEIN'}"""
    else:
        pa_report = f"**Status:** NICHT berechenbar\n\n**Grund:** {pa_check.get('grund')}"

    # Dreijahresvergleich
    drei_check = checks['dreijahresvergleich']
    drei_status = status(drei_check.get('machbar'))
    drei_detail = f"{drei_check.get('kennzahlen_mit_dreijahresvergleich', 0)}/21 Kennzahlen"

    drei_report = f"""**Status:** {'Verfügbar' if drei_check.get('machbar') else 'NICHT verfügbar'}

**Befund:**
- Kennzahlen mit 2022-2024: {drei_check['kennzahlen_mit_dreijahresvergleich']}
- Kennzahlen ohne vollständigen Dreijahresvergleich: {drei_check['kennzahlen_ohne']}

**Beispiele mit Dreijahresvergleich:**
{chr(10).join([f'- {k}' for k in drei_check['beispiele_mit']])}

**Beispiele ohne:**
{chr(10).join([f"- {item['kennzahl']}: {item['verfuegbare_jahre']}" for item in drei_check['beispiele_ohne']])}"""

    drei_warnung = drei_check['warnung']

    # Medizin-Unis Vergleichsgruppe
    med_check = checks['vergleichsgruppe']
    med_status = status(med_check.get('machbar'))
    med_detail = f"{med_check.get('anzahl_medizin_unis', 0)} MedUnis" if med_check.get('machbar') else "N/A"

    if med_check.get('machbar'):
        med_report = f"""**Status:** Verfügbar

**Befund:**
- Anzahl medizinische Universitäten: {med_check['anzahl_medizin_unis']}
- Codes: {', '.join(med_check['codes'])}
- Vergleichsgruppe vollständig: {'JA (4+ Unis)' if med_check['vergleichsgruppe_vollstaendig'] else 'NEIN'}"""
    else:
        med_report = "**Status:** NICHT verfügbar"

    # QS Ranking
    qs_check = checks['qs_ranking']
    qs_status = "FAIL"
    qs_detail = "Externe Quelle"
    qs_report = f"""**Status:** NICHT in UniData

**Befund:**
{qs_check['grund']}

**Konsequenz:**
{qs_check['konsequenz']}"""

    return report.format(
        datum=datum,
        uv_status=uv_status, uv_detail=uv_detail, uv_report=uv_report,
        betr_status=betr_status, betr_detail=betr_detail, betr_report=betr_report,
        betr_pruef=betr_pruef, betr_prof=betr_prof, betr_calc=betr_calc,
        betr_epic=betr_epic, betr_diff=betr_diff, betr_plaus=betr_plaus,
        betr_einschraenkung=betr_einschraenkung,
        pa_status=pa_status, pa_detail=pa_detail, pa_report=pa_report,
        drei_status=drei_status, drei_detail=drei_detail, drei_report=drei_report,
        drei_warnung=drei_warnung,
        med_status=med_status, med_detail=med_detail, med_report=med_report,
        qs_status=qs_status, qs_detail=qs_detail, qs_report=qs_report
    )


def main():
    """Hauptfunktion."""
    print("="*80)
    print("EPIC VETMEDUNI MACHBARKEITSANALYSE")
    print("="*80)

    print("\nValidiere Epic-Anforderungen...")

    checks = {
        'vetmeduni': check_vetmeduni_in_daten(),
        'betreuungsrelation': check_betreuungsrelation(),
        'pruefungsaktive_quote': check_pruefungsaktive_quote(),
        'dreijahresvergleich': check_zeitreihen_dreijahresvergleich(),
        'vergleichsgruppe': check_vergleichsgruppe_medizinunis(),
        'qs_ranking': check_qs_ranking()
    }

    print("\nGeneriere Epic-Machbarkeitsreport...")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    report = generate_report(checks)

    report_path = OUTPUT_DIR / "epic_vetmeduni_feasibility.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\nOK Report erstellt: {report_path}")

    # Zusammenfassung
    print("\n" + "="*80)
    print("ZUSAMMENFASSUNG")
    print("="*80)

    betr = checks['betreuungsrelation']
    if betr.get('machbar'):
        print(f"Betreuungsrelation: Berechnet 1:{betr['berechnet']}, Epic 1:{betr['epic_angabe']}, Abweichung {betr['abweichung']}")

    pa = checks['pruefungsaktive_quote']
    if pa.get('machbar'):
        print(f"Pruefungsaktive Quote: {pa['quote_berechnet']}% (Epic: >90%)")

    print(f"\nVetMedUni in {checks['vetmeduni']['kennzahlen_mit_uv']}/21 Kennzahlen")
    print(f"Dreijahresvergleich: {checks['dreijahresvergleich']['kennzahlen_mit_dreijahresvergleich']}/21 Kennzahlen")
    print(f"MedUni-Vergleichsgruppe: {checks['vergleichsgruppe']['anzahl_medizin_unis']} Universitaeten")
    print(f"\nQS Ranking: NICHT in UniData (externe Quelle)")

    print("\nKritische Workshop-Fragen:")
    print("  1. Welche Formel nutzt VetMedUni fuer Betreuungsrelation?")
    print("  2. Ist QS Ranking-Integration erforderlich?")
    print("  3. Welche Zeitraeume sind tatsaechlich vergleichbar?")


if __name__ == "__main__":
    main()
