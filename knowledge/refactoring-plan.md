# Refactoring-Plan: Python Scripts

**Status:** Für Session 3 geplant
**Datum:** 2026-01-10
**Kontext:** Analyse nach Session 2 (Epic-Validierung)

---

## Übersicht

Nach 4 Foundation-Scripts (`analyze_data.py`, `explore_personalkategorien.py`, `validate_all_stories.py`, `validate_epic_vetmeduni.py`) zeigen sich klare Code-Duplikate und Verbesserungspotenziale.

**Ziel:** Code-Wartbarkeit erhöhen, DRY-Prinzip anwenden, Testbarkeit vorbereiten.

---

## 1. Gemeinsame Basis-Funktionen auslagern

**Priorität:** HOCH
**Aufwand:** ~1 Stunde
**Impact:** Reduziert ~60 Zeilen Code

### Problem

Alle 4 Scripts haben identische Code-Duplikate:

**JSON-Loading:**
```python
# In allen Scripts:
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
JSON_DIR = PROJECT_ROOT / "data" / "json"

with open(filepath, 'r', encoding='utf-8') as f:
    return json.load(f)
```

**Output-Verzeichnis-Erstellung:**
```python
# In allen Scripts:
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
```

**CSV-Writing:**
```python
# In analyze_data.py:
with open(filepath, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(headers)
    writer.writerows(rows)
```

### Lösung

**Neue Datei:** `scripts/shared_utils.py`

```python
"""
Gemeinsame Utility-Funktionen für Exploration-Scripts.

Provides:
- JSON-Loading mit standardisierten Pfaden
- Output-Verzeichnis-Verwaltung
- CSV-Writing mit UTF-8-BOM und Semikolon-Trennung
"""

import json
from pathlib import Path
from typing import Optional, List
import csv

# Pfad-Konstanten
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
JSON_DIR = PROJECT_ROOT / "data" / "json"
OUTPUT_TABLES_DIR = PROJECT_ROOT / "outputs" / "tables"
OUTPUT_REPORTS_DIR = PROJECT_ROOT / "outputs" / "reports"
OUTPUT_FIGURES_DIR = PROJECT_ROOT / "outputs" / "figures"


def load_kennzahl(filename: str) -> Optional[dict]:
    """
    Lädt eine Kennzahl-JSON-Datei.

    Args:
        filename: Name der JSON-Datei (mit .json Extension)

    Returns:
        dict mit 'metadata' und 'data' oder None wenn nicht gefunden
    """
    filepath = JSON_DIR / filename
    if not filepath.exists():
        return None

    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def ensure_output_dir(subdir: str) -> Path:
    """
    Erstellt Output-Verzeichnis falls nicht vorhanden.

    Args:
        subdir: 'tables', 'reports' oder 'figures'

    Returns:
        Path zum Output-Verzeichnis
    """
    output_dir = PROJECT_ROOT / "outputs" / subdir
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def write_csv(filepath: Path, headers: List[str], rows: List[List]):
    """
    Schreibt CSV-Datei mit Semikolon-Trennung und UTF-8-BOM.

    Args:
        filepath: Vollständiger Pfad zur CSV-Datei
        headers: Liste der Spaltenüberschriften
        rows: Liste von Listen mit Zeilendaten
    """
    with open(filepath, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"✓ Erstellt: {filepath}")
```

### Anpassung bestehender Scripts

**Vorher (in jedem Script):**
```python
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
JSON_DIR = PROJECT_ROOT / "data" / "json"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "tables"

def load_json_files():
    # 15 Zeilen Code...
```

**Nachher:**
```python
from shared_utils import load_kennzahl, ensure_output_dir, write_csv

OUTPUT_DIR = ensure_output_dir('tables')
```

**Betroffene Dateien:**
- `scripts/analyze_data.py` - Zeilen 38-65 → 3 Zeilen
- `scripts/validate_epic_vetmeduni.py` - Zeilen 22-34 → 2 Zeilen
- `scripts/validate_all_stories.py` - (ähnlich)
- `scripts/explore_personalkategorien.py` - Zeilen 25-28 → 2 Zeilen

---

## 2. Konstanten zentralisieren

**Priorität:** MITTEL
**Aufwand:** ~15 Minuten
**Impact:** Single Source of Truth

### Problem

Magic Values verstreut in allen Scripts:

```python
# analyze_data.py:
EXCLUDE_FILES = {'validation_report.json', 'batch_conversion_report.json'}

# validate_epic_vetmeduni.py:
if entry['jahr'] == 2024  # Hardcoded Jahr
if entry['universität_code'] == 'UV'  # VetMedUni Code
[2022, 2023, 2024]  # Dreijahresvergleich-Jahre

# validate_all_stories.py:
epic_wert = 17.6  # Betreuungsrelation VetMedUni
```

### Lösung

**Neue Datei:** `scripts/constants.py`

```python
"""
Projekt-Konstanten für Wissensbilanz-Datenanalyse.
"""

# JSON-Dateien zum Ausschließen
EXCLUDE_FILES = {
    'validation_report.json',
    'batch_conversion_report.json'
}

# Universitäts-Codes
VETMEDUNI_CODE = 'UV'
MEDIZIN_UNI_CODES = ['US', 'UT', 'UU', 'UV']  # Medizin-Unis für Vergleichsgruppe

# Zeiträume
AKTUELLES_JAHR = 2024
DREIJAHRESVERGLEICH_JAHRE = [2022, 2023, 2024]

# VetMedUni Epic-Werte (zur Validierung)
EPIC_BETREUUNGSRELATION = 17.6
EPIC_PRUEFUNGSAKTIVE_QUOTE = 90.0  # >90%

# CSV-Format
CSV_DELIMITER = ';'
CSV_ENCODING = 'utf-8-sig'  # UTF-8 mit BOM für Excel
```

### Verwendung

```python
from constants import VETMEDUNI_CODE, AKTUELLES_JAHR

# Vorher:
if entry['universität_code'] == 'UV' and entry['jahr'] == 2024:

# Nachher:
if entry['universität_code'] == VETMEDUNI_CODE and entry['jahr'] == AKTUELLES_JAHR:
```

---

## 3. Report-Generierung vereinheitlichen

**Priorität:** NIEDRIG
**Aufwand:** ~2 Stunden
**Impact:** Erhöht Lesbarkeit, nur sinnvoll wenn >5 Reports

### Problem

`validate_epic_vetmeduni.py` hat 300 Zeilen Template-String-Formatting (Zeilen 228-526):

```python
report = """# Epic VetMedUni Machbarkeitsanalyse

**Datum:** {datum}
...
{betr_status} | {betr_detail}
...
""".format(datum=datum, betr_status=betr_status, ...)
```

**Nachteile:**
- Schwer lesbar (Code + Markdown gemischt)
- Fehleranfällig bei Format-Keys
- Nicht testbar (Markdown-Struktur)

### Lösung (Optional, nur wenn weitere Reports kommen)

**Option A: Jinja2-Templates** (wenn >5 Reports geplant)
```python
from jinja2 import Template

template = Template(Path('templates/epic_report.md').read_text())
report = template.render(checks=checks, datum=datum)
```

**Option B: Dict-basiertes Template-System** (einfacher)
```python
def generate_report(checks: dict) -> str:
    sections = [
        generate_executive_summary(checks),
        generate_betreuungsrelation_section(checks['betreuungsrelation']),
        generate_qs_ranking_section(checks['qs_ranking']),
        # ...
    ]
    return '\n\n---\n\n'.join(sections)
```

**Empfehlung:** NICHT umsetzen vor Session 3. Erst bei >5 Reports sinnvoll.

---

## 4. Validation-Checks als Klasse strukturieren

**Priorität:** NIEDRIG
**Aufwand:** ~3 Stunden
**Impact:** Nur sinnvoll bei >10 Validation-Checks

### Problem

`validate_epic_vetmeduni.py` hat 6 separate `check_*()` Funktionen (Zeilen 37-226):
```python
def check_betreuungsrelation():
    # ...
    return {'machbar': True, 'details': ...}

def check_qs_ranking():
    # ...
    return {'in_daten': False, 'grund': ...}
```

**Nachteile:**
- Kein standardisiertes Return-Format
- Keine Wiederverwendung zwischen Scripts
- Nicht testbar als Unit

### Lösung (Optional)

```python
class ValidationCheck:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def run(self) -> dict:
        raise NotImplementedError

    def format_result(self, result: dict) -> str:
        """Standardisierte Markdown-Ausgabe."""
        raise NotImplementedError


class BetreuungsrelationCheck(ValidationCheck):
    def run(self) -> dict:
        # Logik hier
        return {
            'machbar': True,
            'wert_berechnet': 11.1,
            'wert_epic': 17.6,
            'abweichung': 6.5
        }

    def format_result(self, result: dict) -> str:
        return f"**Berechnet:** 1:{result['wert_berechnet']}"
```

**Empfehlung:** NICHT umsetzen. Overkill für 4 Scripts. Erst bei Test-Framework sinnvoll.

---

## 5. Error-Handling verbessern

**Priorität:** NIEDRIG
**Aufwand:** ~30 Minuten
**Impact:** Bessere Fehlerdiagnose

### Problem

```python
# analyze_data.py:
if not json_files:
    print(f"FEHLER: Keine JSON-Dateien gefunden in {JSON_DIR}")
    sys.exit(1)

# explore_personalkategorien.py:
if not filepath.exists():
    print(f"FEHLER: {filename} nicht gefunden")
    return  # Macht weiter, obwohl Fehler
```

### Lösung

```python
# In shared_utils.py:
class KennzahlNotFoundError(Exception):
    """Raised when a required Kennzahl JSON file is missing."""
    pass

class InvalidDataFormatError(Exception):
    """Raised when JSON structure is unexpected."""
    pass
```

**Empfehlung:** NICHT dringend. Erst bei Production-Deployment relevant.

---

## Empfehlung für Session 3

### Durchführen:

1. ✅ **Shared Utils** (`scripts/shared_utils.py`)
   - Grund: Sofort umsetzbar, hoher Impact, reduziert Duplikate
   - Aufwand: 1 Stunde
   - Files betroffen: Alle 4 Scripts

2. ✅ **Konstanten** (`scripts/constants.py`)
   - Grund: Niedriger Aufwand, verhindert Magic Values
   - Aufwand: 15 Minuten
   - Files betroffen: validate_epic_vetmeduni.py, validate_all_stories.py

### NICHT durchführen (noch nicht):

3. ❌ **Template-System** - Erst bei >5 Reports
4. ❌ **Validation-Klassen** - Erst bei >10 Checks oder Test-Framework
5. ❌ **Error-Handling** - Nice-to-have, nicht dringend

---

## Nächste Schritte

**Für Session 3:**
1. `scripts/shared_utils.py` erstellen
2. `scripts/constants.py` erstellen
3. Alle 4 Scripts refactoren (Import anpassen)
4. Test: Alle Scripts ausführen, Output vergleichen

**Nach Refactoring:**
- Phase 2 fortsetzen: Deskriptive, vergleichende, relationale Analysen
- Phase 4 vorbereiten: `knowledge/design.md` für Dashboard-Konzept

---

**Dokumentiert:** 2026-01-10
**Review vor Umsetzung:** Session 3
