# User Story Machbarkeitsanalyse

**Datum:** 2026-01-10
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
6 von 21 Kennzahlen haben Zeit-Labels (Wintersemester, Studienjahr).

**Beispiel-Kennzahlen:** 1_A_1_personal_koepfe, 1_A_1_personal_vzae, 1_A_5_frauen_berufungsverfahren

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
22 Universitäten vorhanden, VetMedUni (UV) + 3 MedUnis (US, UT, UU) in Daten

**Kritische Einschränkung:**
Durchschnitt bei Prozent-Kennzahlen nur gewichtet möglich (benötigt Basis-Werte)

**Dashboard-Anforderung:**
- Filter nach uni_type = "medizinisch" für VetMedUni-Vergleichsgruppe
- Multi-Select für manuelle Uni-Auswahl
- Durchschnitt NUR bei Einheit=Anzahl/Personen/VZÄ, NICHT bei Prozent

---

### D-03: Betreuungsrelation berechnen ⚠

**Status:** Eingeschränkt umsetzbar

**Problem:**
Personalkategorien (Professor, Dozent, Assoziierte Prof.) NICHT in Daten differenziert

**Verifiziert in:**
- scripts/explore_personalkategorien.py
- knowledge/data.md (Abschnitt "Dimensionen")

**Original-Formel (aus User-Story):**
```
Prüfungsaktive / VZÄ (Professoren + Dozenten + Assoz. Prof.)
```

**Mögliche Formel (mit vorhandenen Daten):**
```
Prüfungsaktive (2-A-6 Gesamt) / ProfessorInnen & Äquivalente (2-A-1)
```

**Daten-Verfügbarkeit:**
- 2-A-6 Prüfungsaktive: True
- 2-A-1 ProfessorInnen: True

**Workshop-Klärung erforderlich:**
1. Nutzt VetMedUni tatsächlich die detaillierte Formel?
2. Ist 2-A-1 "ProfessorInnen & Äquivalente" ausreichend?
3. Gibt es andere Datenquellen für Personalkategorien?

---

### D-04: Abweichungen identifizieren ✓

**Status:** Umsetzbar

**Begründung:**
Year-over-year Berechnung mit Zeit-Labels möglich

**Einschränkung:**
Erhebungsmethoden-Änderungen können "falsche" Abweichungen erzeugen

**Dashboard-Anforderung:**
- Schwellwert konfigurierbar (z.B. >10%)
- Filterung nach Richtung (Anstieg/Rückgang)
- Hinweis auf methodologische Änderungen

---

### D-05: Datenqualität prüfen ✓

**Status:** Vollständig umsetzbar

**Validierungen implementierbar:**
- **Summenvalidierung:** 8 Kennzahlen mit Frauen/Männer/Gesamt
- **Null-Werte:** null_reason Feld in allen Datenpunkten vorhanden
- **Prozent-Range:** 4 Kennzahlen mit Einheit=Prozent identifiziert

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
LLM-basiert, keine Daten-Einschränkung

**Voraussetzung:**
Phase 2 Exploration muss Muster zeigen (für Template-Entwicklung)

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
**Letzte Aktualisierung:** 2026-01-10
