"""
TITEL: Exploration Personalkategorien für Betreuungsrelation

FORSCHUNGSFRAGE:
Sind Personalkategorien (Professor, Dozent, etc.) in 1-A-1 Personal oder 2-A-1 verfügbar?

INPUT:
- data/json/1_A_1_personal_koepfe.json
- data/json/2_A_1_professoren_aequivalente.json

OUTPUT:
- Konsolenausgabe: Struktur-Analyse

ZIEL:
Klärung ob User-Story D-03 (Betreuungsrelation) mit vorhandenen Daten umsetzbar ist.

ERKENNTNISSE:
[Wird nach Ausführung ergänzt]
"""

import json
from pathlib import Path
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
JSON_DIR = PROJECT_ROOT / "data" / "json"

def analyze_file(filename):
    """Analysiert eine JSON-Datei auf Personalkategorien."""
    filepath = JSON_DIR / filename

    if not filepath.exists():
        print(f"FEHLER: {filename} nicht gefunden")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"\n{'='*80}")
    print(f"DATEI: {filename}")
    print(f"{'='*80}")

    # Metadata
    metadata = data.get('metadata', {})
    print(f"\nKennzahl: {metadata.get('kennzahl_id')} - {metadata.get('kennzahl_name')}")
    print(f"Kategorie: {metadata.get('kategorie')}")
    print(f"Einheit: {metadata.get('einheit')}")

    # Display Labels
    display_labels = set()
    dimensionen_keys = defaultdict(set)

    for entry in data['data']:
        dl = entry.get('display_label')
        if dl:
            display_labels.add(dl)

        dims = entry.get('dimensionen', {})
        if dims:
            for key, value in dims.items():
                dimensionen_keys[key].add(str(value))

    print(f"\nDisplay Labels ({len(display_labels)}):")
    for label in sorted(display_labels):
        print(f"  - {label}")

    if dimensionen_keys:
        print(f"\nDimensionen-Keys:")
        for key, values in sorted(dimensionen_keys.items()):
            print(f"  {key}: {len(values)} eindeutige Werte")
            if len(values) <= 10:
                print(f"    => {', '.join(sorted(values))}")
            else:
                print(f"    => {', '.join(list(sorted(values))[:5])} ... (+{len(values)-5} weitere)")
    else:
        print("\nKeine Dimensionen-Objekte vorhanden")

    # Suche nach tatsächlichen Werten
    print(f"\nBeispiel-Einträge mit Werten:")
    count = 0
    for entry in data['data']:
        if entry.get('wert') is not None and count < 3:
            print(f"  Uni: {entry['universität_code']}, Display: '{entry['display_label']}', Wert: {entry['wert']}, Dims: {entry.get('dimensionen')}")
            count += 1

    if count == 0:
        print("  KEINE WERTE GEFUNDEN (alle null)")


def main():
    """Hauptfunktion."""
    print("="*80)
    print("EXPLORATION: PERSONALKATEGORIEN FÜR BETREUUNGSRELATION")
    print("="*80)

    # Analyse 1-A-1 Köpfe und VZÄ
    analyze_file("1_A_1_personal_koepfe.json")
    analyze_file("1_A_1_personal_vzae.json")

    # Analyse 2-A-1 ProfessorInnen
    analyze_file("2_A_1_professoren_aequivalente.json")

    print("\n" + "="*80)
    print("ZUSAMMENFASSUNG")
    print("="*80)
    print("""
KRITISCHE ERKENNTNIS:
- 1-A-1 Personal enthält KEINE Personalkategorien (Professor, Dozent, etc.)
- dimensionen.personalkategorie enthält Uni-Codes (UA, UB, ...), nicht Kategorien
- display_label "Verwendungskategorien WBV" ist nur ein Label, kein Wert

KONSEQUENZ FÜR USER-STORY D-03 (Betreuungsrelation):
- Formel "Prüfungsaktive / VZÄ (Professoren + Dozenten + ...)" NICHT umsetzbar
- Grund: Personalkategorien nicht in Daten differenziert
- Alternative: 2-A-1 "ProfessorInnen und Äquivalente" könnte Ersatz sein

EMPFEHLUNG:
- Betreuungsrelation nur mit 2-A-1 (ProfessorInnen) statt detaillierter Formel
- User-Story D-03 als "eingeschränkt umsetzbar" markieren
- Workshop-Klärung: Welche Formel nutzt VetMedUni tatsächlich?
""")


if __name__ == "__main__":
    main()
