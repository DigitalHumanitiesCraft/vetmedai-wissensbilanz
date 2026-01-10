# Scripts Übersicht

**Zweck:** Systematische Exploration der Wissensbilanz-Daten (Promptotyping Phase 2)

**Framework:** Siehe `../knowledge/exploration-framework.md`

---

## 00_foundation - Basis-Scripts

### `analyze_data.py`
**Forschungsfrage:** Welche Metadaten-Strukturen existieren in den JSON-Dateien?

**Input:**
- `data/json/*.json` (21 Kennzahl-Dateien)

**Output:**
- `outputs/tables/universitaeten.csv` - 22 Universitäten mit Codes, Typen, Bundesländern
- `outputs/tables/kennzahlen_uebersicht.csv` - 21 Kennzahlen-Übersicht
- `outputs/tables/dimensionen_detailliert.csv` - Dimensionen-Analyse (4 Kennzahlen nutzen Dimensionen)
- `outputs/tables/display_labels.csv` - 99 eindeutige Display Labels
- `outputs/tables/meta_values.csv` - Time Types (3) und Einheiten (4)

**Verwendung:**
```bash
python scripts/analyze_data.py
```

**Wichtigste Erkenntnis:**
Display Labels sind primäre Differenzierung (nicht `dimensionen`-Objekt). Nur 4/21 Kennzahlen nutzen Dimensionen.

---

## 01_descriptive - Deskriptive Statistiken
*Noch keine Scripts*

**Geplante Forschungsfragen:**
- Wie sind Werte innerhalb einer Kennzahl verteilt?
- Welche Universitäten haben fehlende Werte (null)?
- Wie vollständig sind die Zeitreihen?

---

## 02_comparative - Vergleichende Analysen
*Noch keine Scripts*

**Geplante Forschungsfragen:**
- Wie unterscheiden sich Universitätstypen (volluniversität vs. technisch)?
- Welche temporalen Trends sind erkennbar?
- Gibt es systematische Unterschiede zwischen Bundesländern?

---

## 03_relational - Beziehungsanalysen
*Noch keine Scripts*

**Geplante Forschungsfragen:**
- Korreliert Personal (Köpfe) mit Studierendenzahlen?
- Gibt es Zusammenhänge zwischen Berufungen und Gender Pay Gap?
- Wie verhält sich Mobilität (outgoing/incoming) zu Gesamtstudierendenzahlen?

---

## Konventionen

- **Eingabedaten:** Immer aus `../data/` relativ zum Script-Ordner
- **Ausgabedaten:** `../outputs/[figures|tables|reports]/`
- **Encoding:** UTF-8-BOM für CSV-Dateien (Excel-Kompatibilität)
- **CSV-Separator:** Semikolon (`;`)
- **Namenskonvention:** `[script-name]_[kennzahl-id]_[datum].[ext]`

---

## Dependencies

**Alle Scripts:**
- Python 3.8+
- json, csv (stdlib)

**Visualisierung (sobald benötigt):**
- matplotlib, seaborn
- pandas

**Installation:**
```bash
pip install -r requirements.txt
```
