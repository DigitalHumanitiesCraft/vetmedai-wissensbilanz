# Wissensbilanz-Daten: Datenmodell

**Datenstand:** 2024 | **Quelle:** WBV/UHSBV | **Datenpunkte:** 3.274

---

## Quick Reference

### Datenstruktur
```json
{
  "metadata": { kennzahl_id, kennzahl_name, kategorie, einheit, beschreibung, ... },
  "data": [
    { universität_code, universität_name, jahr, wert, einheit, dimensionen, display_label, ... }
  ]
}
```

### Kernfelder (alle Kennzahlen)
| Feld | Typ | Beispiel | Beschreibung |
|------|-----|----------|--------------|
| `kennzahl_id` | String | "1-A-1" | Kennzahl-Identifikator |
| `universität_code` | String | "UA" | Universitätscode (siehe Tabelle unten) |
| `jahr` | Integer | 2024 | Bezugsjahr |
| `wert` | Float/Null | 185.0 | Messwert |
| `einheit` | String | "Personen" | Maßeinheit |
| `display_label` | String | "Gesamt" | Anzeige-Label (wichtigste Dimension!) |
| `dimensionen` | Object | `{}` | Zusätzliche Dimensionen (meist leer) |
| `applicable` | Boolean | true | Kennzahl anwendbar? |

---

## Universitäten (22)

| Code | Name | Typ | Bundesland |
|------|------|-----|------------|
| UA | Universität Wien | volluniversität | Wien |
| UB | Universität Graz | volluniversität | Steiermark |
| UC | Universität Innsbruck | volluniversität | Tirol |
| UD | Universität Salzburg | volluniversität | Salzburg |
| UE | Universität Klagenfurt | volluniversität | Kärnten |
| UF | Universität Linz | volluniversität | Oberösterreich |
| UG | Technische Universität Wien | technisch | Wien |
| UH | Technische Universität Graz | technisch | Steiermark |
| UI | Montanuniversität Leoben | technisch | Steiermark |
| UJ | Universität für Bodenkultur Wien | volluniversität | Wien |
| UK | Universität für künstlerische und industrielle Gestaltung Linz | kunst | Oberösterreich |
| UL | Universität Mozarteum Salzburg | kunst | Salzburg |
| UM | Universität für Musik und darstellende Kunst Wien | kunst | Wien |
| UN | Universität für Musik und darstellende Kunst Graz | kunst | Steiermark |
| UO | Akademie der bildenden Künste Wien | kunst | Wien |
| UQ | Universität für angewandte Kunst Wien | kunst | Wien |
| UR | Universität für Weiterbildung Krems | weiterbildung | Niederösterreich |
| US | Medizinische Universität Wien | medizinisch | Wien |
| UT | Medizinische Universität Graz | medizinisch | Steiermark |
| UU | Medizinische Universität Innsbruck | medizinisch | Tirol |
| UV | Veterinärmedizinische Universität Wien | medizinisch | Wien |
| UW | Wirtschaftsuniversität Wien | volluniversität | Wien |

**Typen:** volluniversität (8), kunst (6), medizinisch (4), technisch (3), weiterbildung (1)

---

## Kennzahlen (21)

| ID | Name | Kategorie | Einheit | Datenpunkte |
|----|------|-----------|---------|-------------|
| 1-A-1 | Personal - Köpfe | Personal | Personen | 132 |
| 1-A-1 | Personal - VZÄ | Personal | VZÄ | 132 |
| 1-A-2 | Berufungen an die Universität | Personal | Anzahl | 242 |
| 1-A-3 | Frauenquote in Kollegialorganen | Personal | Prozent | 440 |
| 1-A-4 | Gender Pay Gap | Personal | Prozent | 374 |
| 1-A-5 | Repräsentanz von Frauen in Berufungsverfahren | Personal | Anzahl | 12 |
| 2-A-1 | ProfessorInnen und Äquivalente | Studierende | Personen | 105 |
| 2-A-2 | Eingerichtete Studien | Studien | Anzahl | 110 |
| 2-A-3 | Studienabschlussquote | Studierende | Prozent | 231 |
| 2-A-4 | Besondere Zulassungsbedingungen | Studien | Anzahl | 231 |
| 2-A-5 | Anzahl Studierenden | Studierende | Personen | 242 |
| 2-A-6 | Anzahl Prüfungsaktive | Studierende | Personen | 231 |
| 2-A-7 | Anzahl belegte ordentliche Studien | Studierende | Anzahl | 110 |
| 2-A-7 | Anzahl belegte Universitätslehrgänge | Studierende | Anzahl | 48 |
| 2-A-8 | Ordentliche Studierende (outgoing) | Studierende | Personen | 231 |
| 2-A-9 | Ordentliche Studierende (incoming) | Studierende | Personen | 231 |
| 2-B-1 | Doktoratsstudierende mit BV zur Universität | Studierende | Personen | 242 |
| 3-A-1 | Ordentliche Studienabschlüsse | Abschlüsse | Anzahl | 110 |
| 3-A-1 | Außerordentliche Studienabschlüsse | Abschlüsse | Anzahl | 48 |
| 3-A-2 | Studienabschlüsse in der Toleranzstudiendauer | Abschlüsse | Anzahl | 105 |
| 3-A-3 | Studienabschlüsse mit Auslandsaufenthalt | Abschlüsse | Anzahl | 0 |

**Kategorien:** Personal (6), Studierende (11), Studien (2), Abschlüsse (4)
**Einheiten:** Anzahl (8), Personen (6), Prozent (4), VZÄ (3)

---

## Dimensionen

**Wichtig:** Nur 4 von 21 Kennzahlen nutzen das `dimensionen`-Objekt. Bei allen anderen ist `dimensionen: {}` leer.

### Kennzahlen MIT Dimensionen

| Kennzahl | Dimensions-Keys | Werte |
|----------|-----------------|-------|
| 1-A-1 Personal Köpfe | `personalkategorie` | UA, UB, UC, ..., UW (alle 22 Uni-Codes) |
|  | `parent_category` | null |
| 1-A-1 Personal VZÄ | `personalkategorie` | UA, UB, UC, ..., UW (alle 22 Uni-Codes) |
|  | `parent_category` | null |
| 2-A-1 ProfessorInnen | `personalkategorie` | UA, UB, UC, ..., UW (21 Uni-Codes) |
|  | `parent_category` | null |
| 2-A-5 Studierende | `geschlecht` | gesamt |

### Display Labels (Hauptdifferenzierung)

**Die meisten Kennzahlen nutzen `display_label` statt `dimensionen` zur Aufschlüsselung:**

#### Standard-Labels (häufigste)
- `Universität (Codex)` - Universitätscode
- `Universität (Langtext)` - Universitätsname
- `Gesamt` - Gesamtwert
- `Frauen` - Frauenanteil
- `Männer` - Männeranteil

#### Mobilität (2-A-8, 2-A-9)
- `EU` - EU-Länder
- `Drittstaaten` - Nicht-EU-Länder

#### Zeitreihen (Semester)
- `Wintersemester 2022 (Stichtag: 31.12.2022)`
- `Wintersemester 2023 (Stichtag: 31.12.2023)`
- `Wintersemester 2024 (Stichtag: 31.12.2024)`

#### Zeitreihen (Studienjahr)
- `Studienjahr 2021/22`
- `Studienjahr 2022/23`
- `Studienjahr 2023/24`

#### Kollegialorgane (1-A-3)
- `Köpfe Frauen`, `Köpfe Männer`, `Köpfe Gesamt`
- `Frauen in %`, `Männer in %`
- `Organe mit erfüllter Quote`

**Vollständige Liste:** Siehe `display_labels.csv` (99 eindeutige Labels)

---

## Zeitdimensionen

### Time Types (3 Werte)

| time_type | Bedeutung | Beispiel in `jahr` |
|-----------|-----------|-------------------|
| `jahr` | Kalenderjahr | 2024 |
| `semester` | Semester | 2024 (siehe `display_label` für Details) |
| `studienjahr` | Studienjahr | 2023 (= 2023/24) |

**Wichtig:** Bei `studienjahr` steht in `jahr` das Startjahr. Das vollständige Studienjahr steht in `display_label`.

---

## Join-Strategien

### Join-Keys

**Universität:** `universität_code` (Primary Key)
**Kennzahl:** `kennzahl_id` (Primary Key)
**Zeit:** Composite Key aus `jahr` + `time_type`

### Beispiel: Personal Köpfe ↔ VZÄ
```python
# Beide Dateien haben identische Struktur
join_key = (universität_code, jahr, dimensionen.personalkategorie)
```

### Beispiel: Studierende ↔ Abschlüsse
```python
# Filter auf display_label = "Gesamt"
join_key = (universität_code, jahr)
```

### Beziehungen

- **1-A-1 Köpfe ↔ 1-A-1 VZÄ**: Gleiche Personen, unterschiedliche Zählweise
- **2-A-5 Studierende ⊃ 2-A-6 Prüfungsaktive**: Subset-Beziehung
- **2-A-5 Studierende → 3-A-1 Abschlüsse**: Studierende → Abschlüsse
- **2-A-8/9 Mobilität ⊂ 2-A-5 Studierende**: Subset

---

## Aggregation

### Regel
`metadata.aggregation_rule: "sum"` bei allen Kennzahlen

**Bedeutung:**
- Werte können über Universitäten summiert werden
- Bei `display_label = "Gesamt"` sind bereits Summen

### Ausnahmen: Prozent-Kennzahlen

**1-A-3, 1-A-4, 2-A-3** (Einheit: Prozent)
- **NICHT** einfach summierbar
- Gewichteter Durchschnitt erforderlich
- Basis-Werte aus Kennzahl-Kontext notwendig

---

## Datenqualität

### Null-Werte

| `null_reason` | Bedeutung |
|---------------|-----------|
| `invalid_format` | Daten in Quelle nicht korrekt formatiert |
| `not_applicable` | Kennzahl für diese Uni nicht anwendbar |
| `data_missing` | Daten nicht gemeldet |

**Prüfung:** `applicable: false` → Kennzahl nicht anwendbar

### Wichtige Hinweise

**Alle Kennzahlen:**
> "Aufgrund von Änderungen in den Erhebungsmethoden sind die Indikatorwerte im zeitlichen Verlauf nicht immer direkt vergleichbar."

**1-A-3 (Frauenquote):**
> "Auswahl Gesamt bei Monitoringkategorie führt zu nicht verwertbaren Ergebnissen."

**1-A-4 (Gender Pay Gap):**
> "Auswahl Gesamt bei Personalkategorie führt zu nicht verwertbaren Ergebnissen."

**3-A-2 (Toleranzstudiendauer):**
> "Entfällt für Universität für Weiterbildung Krems."

**3-A-3 (Auslandsaufenthalt):**
> **KEINE DATEN** (0 Datenpunkte)

---

## Provenance-Tracking

Jeder Datenpunkt enthält:

| Feld | Beschreibung |
|------|--------------|
| `provenance.source_file` | Excel-Dateiname |
| `provenance.source_sheet` | Sheet-Name |
| `provenance.source_row` | Zeilennummer |
| `provenance.parsed_at` | ISO 8601 Timestamp |
| `provenance.parser_version` | "1.0" |

---

## Verwendung für Algorithmen

### Für Gesamtwerte filtern
```python
df[df['display_label'] == 'Gesamt']
```

### Zeitreihen extrahieren
```python
# Nach time_type gruppieren
df.groupby(['universität_code', 'time_type', 'jahr'])
```

### Gender-Analyse
```python
# Filter auf Frauen/Männer Labels
df[df['display_label'].isin(['Frauen', 'Männer'])]
```

### Null-Werte behandeln
```python
# Nur gültige Werte
df[(df['wert'].notna()) & (df['applicable'] == True)]
```

---

## Referenzdateien

Alle extrahierten Metadaten verfügbar in:

- `outputs/tables/universitaeten.csv` - Universitätsliste
- `outputs/tables/kennzahlen_uebersicht.csv` - Kennzahlen-Übersicht
- `outputs/tables/display_labels.csv` - Alle Display Labels
- `outputs/tables/dimensionen_detailliert.csv` - Dimensionen-Analyse
- `outputs/tables/meta_values.csv` - Time Types & Einheiten

**Generiert durch:** `scripts/analyze_data.py`

---

## Rechtliche Grundlagen

- **WBV**: Wissensbilanz-Verordnung
- **UHSBV**: Universitäts-Haushaltsbilanz-Verordnung

**Details:** Siehe Arbeitsbehelf zur Wissensbilanz-Verordnung
