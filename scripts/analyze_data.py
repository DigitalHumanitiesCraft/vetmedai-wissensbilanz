import json
import os
from collections import defaultdict
from pathlib import Path

# Pfad zu den JSON-Dateien
json_dir = Path(r"C:\Users\chris\Documents\GitHub\DHCraft\vetmedai-wissensbilanz\data\json")

# Dateien zum Ausschließen
exclude_files = {'validation_report.json', 'batch_conversion_report.json'}

# Datenstrukturen für die Analyse
universitaeten = {}
dimensionen_per_kennzahl = defaultdict(lambda: defaultdict(set))
display_labels = defaultdict(set)
time_types = set()
einheiten = set()

# Alle JSON-Dateien durchlaufen
json_files = [f for f in json_dir.glob("*.json") if f.name not in exclude_files]

print(f"Analysiere {len(json_files)} JSON-Dateien...\n")

for json_file in sorted(json_files):
    kennzahl_name = json_file.stem
    print(f"Verarbeite: {kennzahl_name}")

    with open(json_file, 'r', encoding='utf-8') as f:
        file_content = json.load(f)

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

        # Time type sammeln
        if 'time_type' in entry:
            time_types.add(entry['time_type'])

        # Einheiten sammeln
        if 'einheit' in entry:
            einheiten.add(entry['einheit'])

        # Display labels sammeln
        if 'display_label' in entry:
            display_labels[kennzahl_name].add(entry['display_label'])

        # Dimensionen analysieren
        if 'dimensionen' in entry and entry['dimensionen']:
            dims = entry['dimensionen']
            for key, value in dims.items():
                dimensionen_per_kennzahl[kennzahl_name][key].add(str(value))

print("\n" + "="*80)
print("1. UNIVERSITÄTEN")
print("="*80)
print(f"{'Code':<10} {'Name':<50} {'Typ':<10} {'Bundesland':<15}")
print("-"*80)
for code in sorted(universitaeten.keys()):
    uni = universitaeten[code]
    print(f"{code:<10} {uni['name']:<50} {uni['type']:<10} {uni['bundesland']:<15}")

print("\n" + "="*80)
print("2. DIMENSIONEN PRO KENNZAHL")
print("="*80)
for kennzahl in sorted(dimensionen_per_kennzahl.keys()):
    print(f"\n{kennzahl}:")
    dims = dimensionen_per_kennzahl[kennzahl]
    for key in sorted(dims.keys()):
        values = sorted(dims[key])
        if len(values) <= 10:
            print(f"  {key}: {', '.join(values)}")
        else:
            print(f"  {key}: {len(values)} eindeutige Werte")
            print(f"    Beispiele: {', '.join(list(values)[:5])}")

print("\n" + "="*80)
print("3. DISPLAY LABELS PRO KENNZAHL")
print("="*80)
for kennzahl in sorted(display_labels.keys()):
    labels = sorted(display_labels[kennzahl])
    print(f"\n{kennzahl}:")
    for label in labels:
        print(f"  - {label}")

print("\n" + "="*80)
print("4. TIME TYPES")
print("="*80)
for tt in sorted(time_types):
    print(f"  - {tt}")

print("\n" + "="*80)
print("5. EINHEITEN")
print("="*80)
for einheit in sorted(einheiten):
    print(f"  - {einheit}")

print("\n" + "="*80)
print("ZUSAMMENFASSUNG")
print("="*80)
print(f"Anzahl Universitäten: {len(universitaeten)}")
print(f"Anzahl Kennzahlen: {len(dimensionen_per_kennzahl)}")
print(f"Anzahl Time Types: {len(time_types)}")
print(f"Anzahl Einheiten: {len(einheiten)}")
