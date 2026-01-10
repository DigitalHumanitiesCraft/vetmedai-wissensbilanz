# Epic VetMedUni Machbarkeitsanalyse

**Datum:** 2026-01-10
**Quelle:** Validierung gegen tatsächliche UniData-Exports
**Epic-Quelle:** VetMedUni Wissensbilanz 2024, Leistungsvereinbarung 2025-2027

---

## Executive Summary

| Anforderung | Status | Kritischer Befund |
|-------------|--------|-------------------|
| VetMedUni in Daten | FAIL | Fehlend in: 1_A_5_frauen_berufungsverfahren, 2_A_7_universitaetslehrgaenge, 3_A_1_studienabschluesse_ausserordentlich |
| Betreuungsrelation 1:17,6 | OK | Abweichung 6.5 |
| Prüfungsaktive >90% | OK | 73.7% |
| Dreijahresvergleich 2022-2024 | OK | 12/21 Kennzahlen |
| Vergleichsgruppe MedUnis | OK | 4 MedUnis |
| QS Ranking Platz 28 | FAIL | Externe Quelle |

**Legende:** OK = Umsetzbar, WARN = Eingeschränkt, FAIL = Nicht umsetzbar

---

## 1. VetMedUni in Datensatz

**Frage:** Ist die VetMedUni (Code: UV) in allen Kennzahlen vorhanden?

**Status:** FEHLT in einigen Kennzahlen

**Befund:**
- Kennzahlen mit VetMedUni (UV): 17
- Kennzahlen ohne VetMedUni: 4
- Fehlend in: 1_A_5_frauen_berufungsverfahren, 2_A_7_universitaetslehrgaenge, 3_A_1_studienabschluesse_ausserordentlich, 3_A_3_auslandsaufenthalt

---

## 2. Betreuungsrelation 1:17,6

**Epic-Anforderung:** "Betreuungsrelation: 1:17,6"

**Formel (aus Epic):** Prüfungsaktive Studien / VZÄ (Professoren + Dozenten + Assoziierte Professoren)

**Status:** Berechenbar (mit Einschränkung)

**Formel verfügbar:** Prüfungsaktive (2-A-6 Gesamt) / ProfessorInnen & Äquivalente (2-A-1)

**Verifizierung:**
- Prüfungsaktive VetMedUni 2024: 1416.988829473671
- ProfessorInnen & Äquivalente VetMedUni 2024: 127.36
- Berechnet: 1:11.1
- Epic-Angabe: 1:17.6
- Abweichung: 6.5

**Plausibilität:** NEIN - Abweichung 6.5

**Kritische Einschränkung:**
Personalkategorien (Prof/Dozent/Assoz.Prof) NICHT differenziert

**Workshop-Klärung erforderlich:**
1. Welche exakte Formel nutzt VetMedUni für die Betreuungsrelation?
2. Sind die 1:17,6 mit dieser vereinfachten Formel berechnet?
3. Gibt es interne Datenquellen für Personalkategorien-Aufschlüsselung?

---

## 3. Prüfungsaktive >90%

**Epic-Anforderung:** "Anteil prüfungsaktiv im Diplomstudium: über 90%"

**Status:** Berechenbar

**Befund:**
- Prüfungsaktive VetMedUni 2024: 1438.8643163169866
- Ordentliche Studierende VetMedUni 2024: 1953.0
- Quote berechnet: 73.7%
- Epic-Angabe: >90%
- Plausibel: NEIN

---

## 4. Dreijahresvergleich 2022-2024

**Epic-Anforderung:** WBV 2016 schreibt Dreijahresvergleich vor

**Status:** Verfügbar

**Befund:**
- Kennzahlen mit 2022-2024: 12
- Kennzahlen ohne vollständigen Dreijahresvergleich: 9

**Beispiele mit Dreijahresvergleich:**
- 1_A_1_personal_koepfe
- 1_A_1_personal_vzae
- 1_A_2_berufungen
- 1_A_3_frauenquote_kollegialorgane
- 1_A_4_gender_pay_gap

**Beispiele ohne:**
- 1_A_5_frauen_berufungsverfahren: [2024]
- 2_A_3_studienabschlussquote: [2024]
- 2_A_5_anzahl_studierenden: [2024]

**Warnung:**
Erhebungsmethoden geändert - nicht direkt vergleichbar

---

## 5. Vergleichsgruppe Medizinische Universitäten

**Epic-Anforderung:** Vergleich mit anderen MedUnis (US, UT, UU)

**Status:** Verfügbar

**Befund:**
- Anzahl medizinische Universitäten: 4
- Codes: US, UT, UU, UV
- Vergleichsgruppe vollständig: JA (4+ Unis)

---

## 6. QS Ranking Platz 28

**Epic-Anforderung:** "QS World University Ranking: Platz 28"

**Status:** NICHT in UniData

**Befund:**
QS Ranking ist externe Quelle, nicht in UniData-Kennzahlen

**Konsequenz:**
Manuelle Eingabe oder separate Datenquelle erforderlich

---

## Kritische Erkenntnisse für Epic

### 1. Betreuungsrelation - Formel unklar

**Problem:**
Epic gibt 1:17,6 an, aber die detaillierte Formel (Professoren + Dozenten + Assoz. Prof.) ist mit UniData nicht umsetzbar.

**Berechnete Relation mit verfügbaren Daten:**
- 1:11.1 (Abweichung: 6.5)

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
*Workshop-Validierung: Stimmt berechneter Wert 1:11.1 mit internem Wert überein?*
```

**Neue Sektion in Epic:**
```markdown
## Externe Datenquellen (nicht in UniData)

- QS Ranking: Externe Quelle, manuelle Pflege erforderlich
- [Weitere externe Kennzahlen identifizieren]
```

---

**Generiert durch:** scripts/validate_epic_vetmeduni.py
**Letzte Aktualisierung:** 2026-01-10
