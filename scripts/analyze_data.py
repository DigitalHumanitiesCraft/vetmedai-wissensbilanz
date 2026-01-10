"""
TITEL: Metadaten-Extraktion aus Wissensbilanz-JSON

FORSCHUNGSFRAGE:
Welche Metadaten-Strukturen existieren in den JSON-Dateien?

INPUT:
- data/json/*.json (21 Kennzahl-Dateien, ohne validation_report & batch_conversion_report)

OUTPUT:
- outputs/tables/universitaeten.csv - 22 Universitäten mit Codes, Typen, Bundesländern
- outputs/tables/kennzahlen_uebersicht.csv - 21 Kennzahlen-Übersicht
- outputs/tables/dimensionen_detailliert.csv - Dimensionen-Analyse
- outputs/tables/display_labels.csv - 99 eindeutige Display Labels
- outputs/tables/meta_values.csv - Time Types (3) & Einheiten (4)

ANNAHMEN:
- JSON-Dateien folgen standardisiertem Schema (metadata + data)
- UTF-8 Encoding für alle Dateien
- Ausschluss von validation_report.json und batch_conversion_report.json
- Null-Werte in dimensionen werden als leeres Dict behandelt

ERKENNTNISSE:
- Display Labels sind primäre Differenzierung (nicht dimensionen-Objekt!)
- Nur 4/21 Kennzahlen nutzen Dimensionen-Objekt
- 22 Universitäten in 5 Typen
- 99 eindeutige Display Labels
- 3 Time Types: jahr, semester, studienjahr
- 4 Einheiten: Personen, Anzahl, Prozent, VZÄ
"""

import json
import csv
from collections import defaultdict
from pathlib import Path
import sys

# Relative Pfade vom Script-Ordner aus
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
JSON_DIR = PROJECT_ROOT / "data" / "json"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "tables"

# Dateien zum Ausschließen
EXCLUDE_FILES = {'validation_report.json', 'batch_conversion_report.json'}


def ensure_output_dir():
    """Erstellt Output-Verzeichnis falls nicht vorhanden."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_json_files():
    """Lädt alle relevanten JSON-Dateien."""
    if not JSON_DIR.exists():
        print(f"FEHLER: JSON-Verzeichnis nicht gefunden: {JSON_DIR}")
        sys.exit(1)

    json_files = [f for f in JSON_DIR.glob("*.json") if f.name not in EXCLUDE_FILES]

    if not json_files:
        print(f"FEHLER: Keine JSON-Dateien gefunden in {JSON_DIR}")
        sys.exit(1)

    return sorted(json_files)


def extract_metadata(json_files):
    """Extrahiert Metadaten aus allen JSON-Dateien."""
    universitaeten = {}
    dimensionen_per_kennzahl = defaultdict(lambda: defaultdict(set))
    display_labels = defaultdict(set)
    time_types = set()
    einheiten = set()
    kennzahlen_info = {}

    print(f"Analysiere {len(json_files)} JSON-Dateien...\n")

    for json_file in json_files:
        kennzahl_name = json_file.stem
        print(f"Verarbeite: {kennzahl_name}")

        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                file_content = json.load(f)
        except Exception as e:
            print(f"  FEHLER beim Laden: {e}")
            continue

        # Metadata speichern
        metadata = file_content.get('metadata', {})
        kennzahlen_info[kennzahl_name] = {
            'kennzahl_id': metadata.get('kennzahl_id'),
            'kennzahl_name': metadata.get('kennzahl_name'),
            'kategorie': metadata.get('kategorie'),
            'einheit': metadata.get('einheit'),
            'datenpunkte': len(file_content.get('data', []))
        }

        # Extrahiere das data-Array
        data = file_content.get('data', [])

        # Durchlaufe alle Einträge
        for entry in data:
            # Universitätsinformationen sammeln
            uni_code = entry.get('universität_code')
            uni_name = entry.get('universität_name')
            uni_type = entry.get('uni_type')
            bundesland = entry.get('bundesland')

            if uni_code and uni_code not in universitaeten:
                universitaeten[uni_code] = {
                    'name': uni_name,
                    'type': uni_type,
                    'bundesland': bundesland
                }

            # Time types sammeln
            if 'time_type' in entry and entry['time_type']:
                time_types.add(entry['time_type'])

            # Einheiten sammeln
            if 'einheit' in entry and entry['einheit']:
                einheiten.add(entry['einheit'])

            # Display labels sammeln
            if 'display_label' in entry and entry['display_label']:
                display_labels[kennzahl_name].add(entry['display_label'])

            # Dimensionen analysieren
            if 'dimensionen' in entry and entry['dimensionen']:
                dims = entry['dimensionen']
                for key, value in dims.items():
                    dimensionen_per_kennzahl[kennzahl_name][key].add(str(value))

    return universitaeten, dimensionen_per_kennzahl, display_labels, time_types, einheiten, kennzahlen_info


def write_csv(filename, headers, rows):
    """Schreibt CSV-Datei mit Semikolon-Trennung und UTF-8-BOM."""
    filepath = OUTPUT_DIR / filename
    with open(filepath, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"✓ Erstellt: {filepath}")


def export_universitaeten(universitaeten):
    """Exportiert Universitäten-Tabelle."""
    headers = ['Code', 'Name', 'Typ', 'Bundesland']
    rows = [
        [code, uni['name'], uni['type'], uni['bundesland']]
        for code in sorted(universitaeten.keys())
    ]
    write_csv('universitaeten.csv', headers, rows)


def export_kennzahlen(kennzahlen_info):
    """Exportiert Kennzahlen-Übersicht."""
    headers = ['Dateiname', 'ID', 'Name', 'Kategorie', 'Einheit', 'Datenpunkte']
    rows = [
        [name, info['kennzahl_id'], info['kennzahl_name'],
         info['kategorie'], info['einheit'], info['datenpunkte']]
        for name, info in sorted(kennzahlen_info.items())
    ]
    write_csv('kennzahlen_uebersicht.csv', headers, rows)


def export_dimensionen(dimensionen_per_kennzahl):
    """Exportiert Dimensionen-Detailanalyse."""
    headers = ['Kennzahl', 'Dimension_Key', 'Anzahl_Werte', 'Beispiel_Werte']
    rows = []
    for kennzahl in sorted(dimensionen_per_kennzahl.keys()):
        dims = dimensionen_per_kennzahl[kennzahl]
        for key in sorted(dims.keys()):
            values = sorted(dims[key])
            beispiele = ', '.join(list(values)[:5])
            rows.append([kennzahl, key, len(values), beispiele])
    write_csv('dimensionen_detailliert.csv', headers, rows)


def export_display_labels(display_labels):
    """Exportiert Display Labels."""
    headers = ['Kennzahl', 'Display_Label']
    rows = []
    for kennzahl in sorted(display_labels.keys()):
        for label in sorted(display_labels[kennzahl]):
            rows.append([kennzahl, label])
    write_csv('display_labels.csv', headers, rows)


def export_meta_values(time_types, einheiten):
    """Exportiert Time Types und Einheiten."""
    headers = ['Typ', 'Wert']
    rows = []
    for tt in sorted(time_types):
        rows.append(['time_type', tt])
    for einheit in sorted(einheiten):
        rows.append(['einheit', einheit])
    write_csv('meta_values.csv', headers, rows)


def print_summary(universitaeten, kennzahlen_info, dimensionen_per_kennzahl,
                  display_labels, time_types, einheiten):
    """Druckt Zusammenfassung der Analyse."""
    print("\n" + "="*80)
    print("ZUSAMMENFASSUNG")
    print("="*80)
    print(f"Universitäten: {len(universitaeten)}")
    print(f"Kennzahlen: {len(kennzahlen_info)}")
    print(f"Kennzahlen mit Dimensionen: {len(dimensionen_per_kennzahl)}")
    print(f"Eindeutige Display Labels: {sum(len(labels) for labels in display_labels.values())}")
    print(f"Time Types: {len(time_types)} - {', '.join(sorted(time_types))}")
    print(f"Einheiten: {len(einheiten)} - {', '.join(sorted(einheiten))}")
    print("\nKritische Erkenntnis:")
    print(f"  → Nur {len(dimensionen_per_kennzahl)}/{len(kennzahlen_info)} Kennzahlen nutzen 'dimensionen'-Objekt")
    print(f"  → Display Labels sind primäre Differenzierung!")


def main():
    """Hauptfunktion."""
    print("=" * 80)
    print("WISSENSBILANZ METADATEN-EXTRAKTION")
    print("=" * 80)

    # Output-Verzeichnis vorbereiten
    ensure_output_dir()

    # JSON-Dateien laden
    json_files = load_json_files()

    # Metadaten extrahieren
    universitaeten, dimensionen_per_kennzahl, display_labels, time_types, einheiten, kennzahlen_info = extract_metadata(json_files)

    # CSV-Dateien schreiben
    print("\n" + "="*80)
    print("EXPORTIERE CSV-DATEIEN")
    print("="*80)
    export_universitaeten(universitaeten)
    export_kennzahlen(kennzahlen_info)
    export_dimensionen(dimensionen_per_kennzahl)
    export_display_labels(display_labels)
    export_meta_values(time_types, einheiten)

    # Zusammenfassung
    print_summary(universitaeten, kennzahlen_info, dimensionen_per_kennzahl,
                  display_labels, time_types, einheiten)

    print("\n✓ Analyse abgeschlossen!")


if __name__ == "__main__":
    main()
