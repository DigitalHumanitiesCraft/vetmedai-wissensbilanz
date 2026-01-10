# Exploration Framework

Systematische Struktur für Exploration-Scripts während Phase 2 & 4 des Promptotyping.

---

## Prinzipien

1. **Ein Script = Eine Frage**: Jedes Script beantwortet eine spezifische Forschungsfrage
2. **Reproduzierbar**: Klare Inputs/Outputs, dokumentierte Annahmen
3. **Inkrementell**: Scripts bauen aufeinander auf
4. **Selbstdokumentierend**: Code + inline Kommentare + Output-Interpretation

---

## Verzeichnisstruktur

```
scripts/
├── README.md                    # Übersicht aller Scripts
├── 00_foundation/               # Basis-Scripts (bereits vorhanden)
│   └── analyze_data.py          # Metadaten-Extraktion
├── 01_descriptive/              # Deskriptive Statistiken
│   ├── univariate.py            # Einzelne Kennzahlen
│   └── distributions.py         # Verteilungen über Unis/Zeit
├── 02_comparative/              # Vergleichende Analysen
│   ├── uni_rankings.py          # Universitäts-Vergleiche
│   └── temporal_trends.py       # Zeitreihen-Analysen
├── 03_relational/               # Beziehungen zwischen Kennzahlen
│   ├── correlations.py          # Korrelationen
│   └── join_patterns.py         # Daten-Joins explorieren
└── outputs/                     # Generierte Outputs
    ├── figures/                 # Visualisierungen
    ├── tables/                  # CSV/Tabellen
    └── reports/                 # Markdown-Reports
```

---

## Script-Template

Jedes Script folgt diesem Muster:

```python
"""
TITEL: [Kurzbeschreibung]

FORSCHUNGSFRAGE:
[Konkrete Frage, die das Script beantwortet]

INPUT:
- data/json/[welche Dateien]

OUTPUT:
- outputs/[wohin, was]

ANNAHMEN:
- [Welche methodologischen Annahmen werden getroffen]
- [Wie werden Null-Werte behandelt]
- [Wie werden display_labels gefiltert]

ERKENNTNISSE:
[Werden am Ende des Scripts als Kommentar ergänzt]
"""

# Imports
# Konfiguration
# Daten laden
# Transformation
# Analyse
# Output
# Interpretation (als Print-Statements)
```

---

## Script-Katalog (in scripts/README.md)

Für jeden Ordner:
- **Zweck**: Was erforschen wir?
- **Scripts**: Liste mit Kurzbeschreibung
- **Abhängigkeiten**: Welche Scripts bauen aufeinander auf?
- **Wichtigste Erkenntnisse**: Was haben wir gelernt?

---

## Output-Management

### Namenskonvention
```
[script-name]_[kennzahl-id]_[datum].csv
univariate_1-A-1_20260110.csv
```

### Metadata-Tracking
Jeder Output erhält eine begleitende `.meta.json`:
```json
{
  "generated_by": "scripts/01_descriptive/univariate.py",
  "generated_at": "2026-01-10T14:30:00",
  "input_files": ["data/json/1_A_1_personal_koepfe.json"],
  "parameters": {"filter": "display_label == 'Gesamt'"},
  "description": "Deskriptive Statistiken für Personal Köpfe"
}
```

---

## Integration mit Knowledge Base

Nach jeder Exploration-Session:

1. **Negative Erkenntnisse** → `knowledge/data.md` (Was funktioniert NICHT)
2. **Erfolgreiche Muster** → `scripts/README.md` (Best Practices)
3. **Forschungsfragen** → `knowledge/research-questions.md` (Neue Fragen)
4. **Prozess** → `knowledge/journal.md` (Chronologie)

---

## Beispiel-Workflow

```bash
# 1. Basis-Exploration (bereits erfolgt)
python scripts/00_foundation/analyze_data.py

# 2. Erste deskriptive Analyse
python scripts/01_descriptive/univariate.py --kennzahl 1-A-1

# 3. Erkenntnisse dokumentieren in journal.md

# 4. Neue Fragen in research-questions.md aufnehmen

# 5. Nächstes Script basierend auf Erkenntnissen entwickeln
```

---

## Review-Kriterien

Bevor ein Script als "fertig" gilt:

- [ ] Forschungsfrage klar formuliert
- [ ] Input/Output dokumentiert
- [ ] Annahmen explizit gemacht
- [ ] Output interpretiert (inline oder als Report)
- [ ] Erkenntnisse in `scripts/README.md` eingetragen
- [ ] Bei wichtigen Findings: Destillation in `knowledge/`
