# Validierungs-Plan für Session 2

**Status:** Geplant
**Quelle:** VetMedAI-2 Validation Framework
**Phase:** Phase 2 (Exploration) - Datenqualitäts-Analyse

---

## Validierungs-Checks (6)

### 1. Summen-Validierung (Sum Validation)
**Frage:** Stimmen Teilsummen mit Gesamtwerten überein?

**Beispiele:**
- 1-A-2 Berufungen: Frauen + Männer = Gesamt?
- 2-A-6 Prüfungsaktive: Frauen + Männer = Gesamt?
- 2-A-8/9 Mobilität: EU + Drittstaaten = Gesamt?

**Methode:**
```python
# Filter auf gleiche Universität/Jahr
gesamt = df[df['display_label'] == 'Gesamt']['wert']
frauen = df[df['display_label'] == 'Frauen']['wert']
männer = df[df['display_label'] == 'Männer']['wert']
# Prüfe: abs(gesamt - (frauen + männer)) < epsilon
```

**Output:**
- `outputs/reports/validation_sum_violations.csv` - Verstöße gegen Summenregel

---

### 2. VZÄ ≤ Köpfe (Equivalence Check)
**Frage:** Ist VZÄ immer kleiner oder gleich Köpfe?

**Anwendbar auf:**
- 1-A-1 Personal: Köpfe vs. VZÄ (separate Dateien)

**Methode:**
```python
# Join 1_A_1_personal_koepfe.json + 1_A_1_personal_vzae.json
# Gruppiert nach universität_code + jahr + dimensionen.personalkategorie
# Prüfe: vzae <= koepfe
```

**Output:**
- `outputs/reports/validation_vzae_violations.csv` - Fälle wo VZÄ > Köpfe

---

### 3. Prozent-Validierung (Percentage Validation)
**Frage:** Sind Prozent-Werte im gültigen Bereich [0, 100]?

**Anwendbar auf:**
- 1-A-3 Frauenquote in Kollegialorganen
- 1-A-4 Gender Pay Gap
- 2-A-3 Studienabschlussquote

**Methode:**
```python
# Filter einheit == "Prozent"
# Prüfe: 0 <= wert <= 100
```

**Output:**
- `outputs/reports/validation_percent_violations.csv` - Prozent-Werte außerhalb [0, 100]

---

### 4. Null-Werte-Analyse (Missing Data Analysis)
**Frage:** Wie vollständig sind die Daten pro Universität/Kennzahl?

**Methode:**
```python
# Gruppiere nach universität_code + kennzahl_id
# Zähle: anzahl_null, anzahl_gültig, prozent_vollständigkeit
# Gruppiere nach null_reason (invalid_format, not_applicable, data_missing)
```

**Output:**
- `outputs/reports/data_completeness.csv` - Vollständigkeits-Matrix (22 Unis × 21 Kennzahlen)
- `outputs/reports/null_reasons_summary.csv` - Null-Grund-Analyse

---

### 5. Subset-Validierung (Subset Validation)
**Frage:** Sind bekannte Subset-Beziehungen konsistent?

**Bekannte Subsets:**
- 2-A-6 Prüfungsaktive ⊂ 2-A-5 Studierende (Prüfungsaktive sind Subset der Studierenden)
- 2-A-8/9 Mobilität ⊂ 2-A-5 Studierende (Outgoing/Incoming sind Subset)

**Methode:**
```python
# Join 2-A-5 (Studierende) + 2-A-6 (Prüfungsaktive)
# Filter auf display_label = "Gesamt", gleiche universität_code + jahr
# Prüfe: pruefungsaktive <= studierende
```

**Output:**
- `outputs/reports/validation_subset_violations.csv` - Subset-Verstöße

---

### 6. Zeitreihen-Konsistenz (Temporal Consistency)
**Frage:** Gibt es extreme Ausreißer in Zeitreihen?

**Methode:**
```python
# Gruppiere nach universität_code + display_label
# Sortiere nach jahr
# Berechne: year-over-year percentage change
# Flag: changes > 50% als potenzielle Ausreißer
```

**Output:**
- `outputs/reports/temporal_outliers.csv` - Zeitreihen mit extremen Sprüngen

---

## Implementierungs-Reihenfolge (Session 2)

1. **Script 01: Summen-Validierung**
   - `scripts/01_descriptive/validate_sums.py`
   - Einfachste Validierung, keine Joins erforderlich

2. **Script 02: Prozent-Validierung**
   - `scripts/01_descriptive/validate_percentages.py`
   - Ebenfalls einfach, innerhalb einer Kennzahl

3. **Script 03: Null-Werte-Analyse**
   - `scripts/01_descriptive/analyze_completeness.py`
   - Keine Validierung, nur Analyse (keine Fails)

4. **Script 04: VZÄ ≤ Köpfe**
   - `scripts/02_comparative/validate_vzae_koepfe.py`
   - Erfordert Join zwischen zwei Dateien

5. **Script 05: Subset-Validierung**
   - `scripts/02_comparative/validate_subsets.py`
   - Erfordert komplexere Joins

6. **Script 06: Zeitreihen-Konsistenz**
   - `scripts/02_comparative/analyze_temporal_outliers.py`
   - Statistische Analyse, keine harte Validierung

---

## Erfolgs-Kriterien

- Alle 6 Validierungs-Scripts implementiert
- Alle Scripts laufen fehlerfrei
- Violation-Reports dokumentieren Probleme (kein Fehlschlag bei Violations!)
- Erkenntnisse in `knowledge/journal.md` dokumentiert
- Violations werden NICHT in Daten korrigiert (nur Dokumentation)

---

## Nicht-Ziele

- Daten NICHT korrigieren (nur Analyse)
- Keine neuen Validierungs-Checks erfinden (nur die 6 aus Framework)
- Keine statistischen Tests (außer Zeitreihen-Ausreißer)

---

## Nächster Schritt

Session 2: Implementierung von `scripts/01_descriptive/validate_sums.py` als erstes Script.
