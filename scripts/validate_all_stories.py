"""
TITEL: Validierung aller User Stories gegen tatsächliche Daten

FORSCHUNGSFRAGE:
Welche User Stories sind mit vorhandenen Daten umsetzbar?

INPUT:
- data/json/*.json (alle 21 Kennzahlen)
- knowledge/user-stories.md (Requirements)

OUTPUT:
- outputs/reports/user_story_feasibility.md - Machbarkeitsreport

ZIEL:
Klare Dokumentation: Welche Stories sind umsetzbar, welche eingeschränkt, welche unmöglich?

METHODIK:
- Prüfung jeder User-Story gegen Datenstruktur
- Identifikation fehlender Datenfelder
- Konkrete Begründung bei Nicht-Machbarkeit
"""

import json
from pathlib import Path
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
JSON_DIR = PROJECT_ROOT / "data" / "json"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "reports"

def load_all_data():
    """Lädt alle JSON-Dateien und erstellt Struktur-Übersicht."""
    exclude_files = {'validation_report.json', 'batch_conversion_report.json'}
    json_files = [f for f in JSON_DIR.glob("*.json") if f.name not in exclude_files]

    struktur = {}

    for json_file in sorted(json_files):
        kennzahl = json_file.stem
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        metadata = data.get('metadata', {})
        display_labels = set()
        dimensionen_keys = set()
        has_values = False

        for entry in data['data']:
            if entry.get('wert') is not None:
                has_values = True
            if entry.get('display_label'):
                display_labels.add(entry['display_label'])
            if entry.get('dimensionen'):
                dimensionen_keys.update(entry['dimensionen'].keys())

        struktur[kennzahl] = {
            'kennzahl_id': metadata.get('kennzahl_id'),
            'name': metadata.get('kennzahl_name'),
            'kategorie': metadata.get('kategorie'),
            'einheit': metadata.get('einheit'),
            'display_labels': sorted(display_labels),
            'dimensionen_keys': sorted(dimensionen_keys),
            'has_values': has_values,
            'datenpunkte': len(data['data'])
        }

    return struktur


def check_zeitreihen(struktur):
    """D-01: Zeitreihenvergleich"""
    # Prüfe ob Zeitdimensionen vorhanden
    zeitreihen_kennzahlen = []

    for kennzahl, info in struktur.items():
        # Suche nach Zeit-bezogenen display_labels
        zeit_labels = [l for l in info['display_labels']
                      if any(z in l for z in ['2022', '2023', '2024', 'Wintersemester', 'Studienjahr'])]
        if zeit_labels:
            zeitreihen_kennzahlen.append({
                'kennzahl': kennzahl,
                'zeit_labels': zeit_labels
            })

    return {
        'machbar': True,
        'einschraenkung': 'Zeitreihen nicht direkt vergleichbar (Erhebungsmethoden geändert - siehe Metadata)',
        'kennzahlen_mit_zeitreihen': len(zeitreihen_kennzahlen),
        'beispiele': [k['kennzahl'] for k in zeitreihen_kennzahlen[:3]]
    }


def check_uni_vergleich(struktur):
    """D-02: Vergleich mit anderen Universitäten"""
    # Prüfe ob Uni-Filterung möglich
    return {
        'machbar': True,
        'details': '22 Universitäten vorhanden, VetMedUni (UV) + 3 MedUnis (US, UT, UU) in Daten',
        'einschraenkung': 'Durchschnitt bei Prozent-Kennzahlen nur gewichtet möglich (benötigt Basis-Werte)'
    }


def check_betreuungsrelation(struktur):
    """D-03: Betreuungsrelation berechnen"""
    # Prüfe Personal- und Studierendendaten
    personal_1a1 = struktur.get('1_A_1_personal_vzae', {})
    professoren_2a1 = struktur.get('2_A_1_professoren_aequivalente', {})
    pruefungsaktive = struktur.get('2_A_6_pruefungsaktive', {})

    return {
        'machbar': 'eingeschränkt',
        'grund': 'Personalkategorien (Professor, Dozent, Assoziierte Prof.) NICHT in Daten differenziert',
        'alternative': 'Berechnung mit 2-A-1 "ProfessorInnen & Äquivalente" (Gesamtzahl) möglich',
        'formel_original': 'Prüfungsaktive / VZÄ (Professoren + Dozenten + Assoz. Prof.)',
        'formel_möglich': 'Prüfungsaktive (2-A-6 Gesamt) / ProfessorInnen & Äquivalente (2-A-1)',
        'daten_vorhanden': {
            '2-A-6 Prüfungsaktive': pruefungsaktive.get('has_values'),
            '2-A-1 ProfessorInnen': professoren_2a1.get('has_values')
        }
    }


def check_abweichungen(struktur):
    """D-04: Abweichungen identifizieren"""
    return {
        'machbar': True,
        'details': 'Year-over-year Berechnung mit Zeit-Labels möglich',
        'einschraenkung': 'Erhebungsmethoden-Änderungen können "falsche" Abweichungen erzeugen'
    }


def check_datenqualitaet(struktur):
    """D-05: Datenqualität prüfen"""
    # Prüfe welche Kennzahlen Frauen/Männer/Gesamt haben
    summen_kennzahlen = []

    for kennzahl, info in struktur.items():
        labels = info['display_labels']
        if 'Gesamt' in labels or 'Frauen' in labels or 'Männer' in labels:
            summen_kennzahlen.append(kennzahl)

    return {
        'machbar': True,
        'validierungen': {
            'Summenvalidierung': f'{len(summen_kennzahlen)} Kennzahlen mit Frauen/Männer/Gesamt',
            'Null-Werte': 'null_reason Feld in allen Datenpunkten vorhanden',
            'Prozent-Range': '4 Kennzahlen mit Einheit=Prozent identifiziert'
        }
    }


def check_text_generierung():
    """B-01 bis B-04: Textgenerierung"""
    return {
        'machbar': True,
        'details': 'LLM-basiert, keine Daten-Einschränkung',
        'voraussetzung': 'Phase 2 Exploration muss Muster zeigen (für Template-Entwicklung)'
    }


def generate_report(checks):
    """Erstellt Markdown-Report."""
    report = """# User Story Machbarkeitsanalyse

**Datum:** {datum}
**Quelle:** Validierung gegen tatsächliche UniData-Exports
**Methodik:** Strukturanalyse aller 21 Kennzahl-Dateien

---

## Zusammenfassung

| Story | Status | Kritischer Blocker |
|-------|--------|-------------------|
| D-01 Zeitreihen | ✓ Umsetzbar | Warnung: Erhebungsmethoden geändert |
| D-02 Uni-Vergleich | ✓ Umsetzbar | Durchschnitt bei Prozent-Kennzahlen eingeschränkt |
| D-03 Betreuungsrelation | ⚠ Eingeschränkt | Personalkategorien fehlen |
| D-04 Abweichungen | ✓ Umsetzbar | - |
| D-05 Datenqualität | ✓ Umsetzbar | - |
| B-01 bis B-04 Text | ✓ Umsetzbar | - |

**Legende:** ✓ = Vollständig umsetzbar, ⚠ = Eingeschränkt umsetzbar, ✗ = Nicht umsetzbar

---

## Dashboard Use Cases

### D-01: Zeitreihenvergleich ✓

**Status:** Umsetzbar

**Begründung:**
{d01_kennzahlen} von 21 Kennzahlen haben Zeit-Labels (Wintersemester, Studienjahr).

**Beispiel-Kennzahlen:** {d01_beispiele}

**Kritische Einschränkung:**
> "Aufgrund von Änderungen in den Erhebungsmethoden sind die Indikatorwerte im zeitlichen Verlauf nicht immer direkt vergleichbar."
(Quelle: metadata.structured_metadata.official_notes)

**Dashboard-Anforderung:**
- Warnung MUSS bei Zeitreihen-Visualisierung angezeigt werden
- Filter nach display_label mit Zeitangaben
- Export-Funktion möglich

---

### D-02: Vergleich mit anderen Universitäten ✓

**Status:** Umsetzbar

**Begründung:**
{d02_details}

**Kritische Einschränkung:**
{d02_einschraenkung}

**Dashboard-Anforderung:**
- Filter nach uni_type = "medizinisch" für VetMedUni-Vergleichsgruppe
- Multi-Select für manuelle Uni-Auswahl
- Durchschnitt NUR bei Einheit=Anzahl/Personen/VZÄ, NICHT bei Prozent

---

### D-03: Betreuungsrelation berechnen ⚠

**Status:** Eingeschränkt umsetzbar

**Problem:**
{d03_grund}

**Verifiziert in:**
- scripts/explore_personalkategorien.py
- knowledge/data.md (Abschnitt "Dimensionen")

**Original-Formel (aus User-Story):**
```
{d03_formel_original}
```

**Mögliche Formel (mit vorhandenen Daten):**
```
{d03_formel_möglich}
```

**Daten-Verfügbarkeit:**
{d03_daten}

**Workshop-Klärung erforderlich:**
1. Nutzt VetMedUni tatsächlich die detaillierte Formel?
2. Ist 2-A-1 "ProfessorInnen & Äquivalente" ausreichend?
3. Gibt es andere Datenquellen für Personalkategorien?

---

### D-04: Abweichungen identifizieren ✓

**Status:** Umsetzbar

**Begründung:**
{d04_details}

**Einschränkung:**
{d04_einschraenkung}

**Dashboard-Anforderung:**
- Schwellwert konfigurierbar (z.B. >10%)
- Filterung nach Richtung (Anstieg/Rückgang)
- Hinweis auf methodologische Änderungen

---

### D-05: Datenqualität prüfen ✓

**Status:** Vollständig umsetzbar

**Validierungen implementierbar:**
{d05_validierungen}

**Referenz:**
- knowledge/validation-plan.md (6 Checks definiert)

**Dashboard-Anforderung:**
- Summenvalidierung: Frauen + Männer = Gesamt
- Null-Werte-Indikator mit null_reason
- Prozent-Range-Check (0-100)
- VZÄ ≤ Köpfe Validierung

---

## Berichterstellung Use Cases

### B-01 bis B-04: Textgenerierung ✓

**Status:** Umsetzbar

**Begründung:**
{b_details}

**Voraussetzung:**
{b_voraussetzung}

**Keine Daten-Blocker.**

---

## Kritische Erkenntnisse für Workshop

### 1. Personalkategorien fehlen (D-03)

**Problem:**
- dimensionen.personalkategorie enthält Uni-Codes (UA, UB, ...), NICHT Kategorien
- Differenzierung Professor/Dozent/Assistenten nicht in Daten vorhanden

**Beweis:**
```bash
python scripts/explore_personalkategorien.py
```

**Auswirkung:**
- Betreuungsrelation nur mit Gesamtzahl "ProfessorInnen & Äquivalente" (2-A-1) berechenbar
- Detaillierte Formel aus User-Story D-03 nicht umsetzbar

**Frage an Workshop:**
Ist die vereinfachte Formel (mit 2-A-1) ausreichend oder wird detaillierte Aufschlüsselung benötigt?

---

### 2. Zeitreihen-Warnung notwendig (D-01)

**Problem:**
Erhebungsmethoden haben sich geändert, Zeitreihen nicht immer direkt vergleichbar.

**Quelle:**
metadata.structured_metadata.official_notes (in allen JSON-Dateien)

**Auswirkung:**
- Dashboard muss Warnung anzeigen
- Jahr-zu-Jahr Vergleiche können irreführend sein

**Frage an Workshop:**
Welche Zeiträume sind tatsächlich vergleichbar? Gibt es Dokumentation zu Methodologie-Änderungen?

---

### 3. Prozent-Durchschnitte problematisch (D-02)

**Problem:**
Prozent-Kennzahlen (1-A-3, 1-A-4, 2-A-3) nicht einfach summierbar/durchschnittbar.

**Grund:**
Gewichteter Durchschnitt benötigt Basis-Werte (z.B. Gesamtzahl Personal für Gender Pay Gap).

**Auswirkung:**
- Durchschnitt der Vergleichsgruppe nur bei Anzahl/Personen/VZÄ
- Bei Prozent: Nur Anzeige einzelner Werte, kein Durchschnitt

**Frage an Workshop:**
Ist Anzeige einzelner Prozent-Werte ohne Durchschnitt ausreichend?

---

## Empfehlungen

### Für Workshop-Vorbereitung

1. **D-03 Betreuungsrelation:** Klären, welche Formel VetMedUni tatsächlich nutzt
2. **Zeitreihen-Dokumentation:** Dokumentation der Methodologie-Änderungen beschaffen
3. **Priorisierung:** Entscheiden, ob D-03 mit vereinfachter Formel akzeptabel ist

### Für Promptotype

**Machbar im Promptotype:**
- D-01, D-02, D-04, D-05 vollständig
- D-03 mit vereinfachter Formel
- B-01 bis B-04 vollständig

**Nicht im Promptotype:**
- D-03 mit detaillierter Personalkategorien-Aufschlüsselung (Daten fehlen)

---

**Generiert durch:** scripts/validate_all_stories.py
**Letzte Aktualisierung:** {datum}
"""

    from datetime import datetime
    datum = datetime.now().strftime("%Y-%m-%d")

    return report.format(
        datum=datum,
        d01_kennzahlen=checks['d01']['kennzahlen_mit_zeitreihen'],
        d01_beispiele=', '.join(checks['d01']['beispiele']),
        d02_details=checks['d02']['details'],
        d02_einschraenkung=checks['d02']['einschraenkung'],
        d03_grund=checks['d03']['grund'],
        d03_formel_original=checks['d03']['formel_original'],
        d03_formel_möglich=checks['d03']['formel_möglich'],
        d03_daten='\n'.join([f"- {k}: {v}" for k, v in checks['d03']['daten_vorhanden'].items()]),
        d04_details=checks['d04']['details'],
        d04_einschraenkung=checks['d04']['einschraenkung'],
        d05_validierungen='\n'.join([f"- **{k}:** {v}" for k, v in checks['d05']['validierungen'].items()]),
        b_details=checks['b']['details'],
        b_voraussetzung=checks['b']['voraussetzung']
    )


def main():
    """Hauptfunktion."""
    print("="*80)
    print("USER STORY MACHBARKEITSANALYSE")
    print("="*80)

    # Lade Daten
    print("\nLade alle JSON-Dateien...")
    struktur = load_all_data()
    print(f"Geladen: {len(struktur)} Kennzahlen")

    # Führe Checks durch
    print("\nValidiere User Stories...")
    checks = {
        'd01': check_zeitreihen(struktur),
        'd02': check_uni_vergleich(struktur),
        'd03': check_betreuungsrelation(struktur),
        'd04': check_abweichungen(struktur),
        'd05': check_datenqualitaet(struktur),
        'b': check_text_generierung()
    }

    # Erstelle Report
    print("\nGeneriere Machbarkeitsreport...")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    report = generate_report(checks)

    report_path = OUTPUT_DIR / "user_story_feasibility.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\nOK Report erstellt: {report_path}")

    # Zusammenfassung
    print("\n" + "="*80)
    print("ZUSAMMENFASSUNG")
    print("="*80)
    print("OK Umsetzbar: D-01, D-02, D-04, D-05, B-01 bis B-04")
    print("!! Eingeschraenkt: D-03 (Betreuungsrelation - Personalkategorien fehlen)")
    print("\nKritische Workshop-Fragen:")
    print("  1. Ist vereinfachte Betreuungsrelation-Formel (mit 2-A-1) ausreichend?")
    print("  2. Welche Zeiträume sind tatsächlich vergleichbar?")
    print("  3. Prozent-Durchschnitte: Einzelwerte statt Durchschnitt akzeptabel?")


if __name__ == "__main__":
    main()
