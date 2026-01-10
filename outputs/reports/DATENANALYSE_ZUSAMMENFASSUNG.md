# Datenanalyse: Wissensbilanz JSON-Dateien

**Analysiert:** 21 JSON-Dateien im Verzeichnis `data/json`
**Datum:** 2026-01-10

---

## 1. UNIVERSITÄTEN (22 Einträge)

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

### Verteilung nach Typ:
- **volluniversität**: 8 (UA, UB, UC, UD, UE, UF, UJ, UW)
- **technisch**: 3 (UG, UH, UI)
- **kunst**: 6 (UK, UL, UM, UN, UO, UQ)
- **medizinisch**: 4 (US, UT, UU, UV)
- **weiterbildung**: 1 (UR)

---

## 2. KENNZAHLEN ÜBERSICHT (21 Kennzahlen)

| Dateiname | ID | Name | Kategorie | Einheit | Datensätze | Dimensionen |
|-----------|----|----- |-----------|---------|------------|-------------|
| 1_A_1_personal_koepfe | 1-A-1 | Personal - Köpfe | Personal | Personen | 132 | ✓ |
| 1_A_1_personal_vzae | 1-A-1 | Personal - VZÄ | Personal | VZÄ | 132 | ✓ |
| 1_A_2_berufungen | 1-A-2 | Berufungen an die Universität | Personal | Anzahl | 242 | - |
| 1_A_3_frauenquote_kollegialorgane | 1-A-3 | Frauenquote in Kollegialorganen | Personal | Prozent | 440 | - |
| 1_A_4_gender_pay_gap | 1-A-4 | Gender Pay Gap | Personal | Prozent | 374 | - |
| 1_A_5_frauen_berufungsverfahren | 1-A-5 | Repräsentanz von Frauen in Berufungsverfahren | Personal | Prozent | 12 | - |
| 2_A_1_professoren_aequivalente | 2-A-1 | ProfessorInnen und Äquivalente | Personal | VZÄ | 105 | ✓ |
| 2_A_2_eingerichtete_studien | 2-A-2 | Eingerichtete Studien | Studien | Anzahl | 110 | - |
| 2_A_3_studienabschlussquote | 2-A-3 | Studienabschlussquote | Studierende | Prozent | 231 | - |
| 2_A_4_zulassungsbedingungen | 2-A-4 | Besondere Zulassungsbedingungen | Studien | Anzahl | 231 | - |
| 2_A_5_anzahl_studierenden | 2-A-5 | Anzahl Studierenden | Studierende | Personen | 242 | ✓ |
| 2_A_6_pruefungsaktive | 2-A-6 | Anzahl Prüfungsaktive | Studierende | Personen | 231 | - |
| 2_A_7_belegte_studien | 2-A-7 | Anzahl belegte ordentliche Studien | Studierende | Anzahl | 110 | - |
| 2_A_7_universitaetslehrgaenge | 2-A-7 | Anzahl belegte Universitätslehrgänge | Studierende | Anzahl | 48 | - |
| 2_A_8_outgoing | 2-A-8 | Ordentliche Studierende (outgoing) | Mobilität | Personen | 231 | - |
| 2_A_9_incoming | 2-A-9 | Ordentliche Studierende (incoming) | Mobilität | Personen | 231 | - |
| 2_B_1_doktoratsstudierende | 2-B-1 | Doktoratsstudierende mit BV zur Universität | Studierende | Personen | 242 | - |
| 3_A_1_studienabschluesse_ausserordentlich | 3-A-1 | Außerordentliche Studienabschlüsse | Abschlüsse | Anzahl | 48 | - |
| 3_A_1_studienabschluesse_ordentlich | 3-A-1 | Ordentliche Studienabschlüsse | Abschlüsse | Anzahl | 110 | - |
| 3_A_2_toleranzstudiendauer | 3-A-2 | Studienabschlüsse in der Toleranzstudiendauer | Abschlüsse | Anzahl | 105 | - |
| 3_A_3_auslandsaufenthalt | 3-A-3 | Studienabschlüsse mit studienbezogenem Auslandsaufenthalt | Abschlüsse | Anzahl | **0** | - |

**Hinweis:** `3_A_3_auslandsaufenthalt` enthält keine Daten (data: []).

---

## 3. DIMENSIONEN PRO KENNZAHL (Detailliert)

Nur **4 von 21 Kennzahlen** verwenden das `dimensionen`-Objekt zur Differenzierung:

### 3.1 Personal - Köpfe (1_A_1_personal_koepfe)
- **ID:** 1-A-1
- **Einheit:** Personen
- **Dimensionen:**
  - `parent_category`: 1 Wert → `None`
  - `personalkategorie`: 22 Werte → Alle Universitätscodes (UA bis UW)

### 3.2 Personal - VZÄ (1_A_1_personal_vzae)
- **ID:** 1-A-1
- **Einheit:** VZÄ
- **Dimensionen:**
  - `parent_category`: 1 Wert → `None`
  - `personalkategorie`: 22 Werte → Alle Universitätscodes (UA bis UW)

### 3.3 ProfessorInnen und Äquivalente (2_A_1_professoren_aequivalente)
- **ID:** 2-A-1
- **Einheit:** VZÄ
- **Dimensionen:**
  - `parent_category`: 1 Wert → `None`
  - `personalkategorie`: 21 Werte → Alle Universitätscodes außer einem (UA bis UW, -1)

### 3.4 Anzahl Studierenden (2_A_5_anzahl_studierenden)
- **ID:** 2-A-5
- **Einheit:** Personen
- **Dimensionen:**
  - `geschlecht`: 1 Wert → `gesamt`

### Kennzahlen OHNE `dimensionen`-Objekt:
Bei den folgenden 17 Kennzahlen ist das `dimensionen`-Objekt leer (`{}`). Die Differenzierung erfolgt stattdessen über `display_label`:

1. 1_A_2_berufungen
2. 1_A_3_frauenquote_kollegialorgane
3. 1_A_4_gender_pay_gap
4. 1_A_5_frauen_berufungsverfahren
5. 2_A_2_eingerichtete_studien
6. 2_A_3_studienabschlussquote
7. 2_A_4_zulassungsbedingungen
8. 2_A_6_pruefungsaktive
9. 2_A_7_belegte_studien
10. 2_A_7_universitaetslehrgaenge
11. 2_A_8_outgoing
12. 2_A_9_incoming
13. 2_B_1_doktoratsstudierende
14. 3_A_1_studienabschluesse_ausserordentlich
15. 3_A_1_studienabschluesse_ordentlich
16. 3_A_2_toleranzstudiendauer
17. 3_A_3_auslandsaufenthalt (keine Daten)

---

## 4. DISPLAY LABELS (Gruppiert nach Kennzahl)

### Muster 1: Universität + Gender-Differenzierung
**Kennzahlen:** 1_A_2_berufungen, 1_A_4_gender_pay_gap, 2_A_3_studienabschlussquote, 2_A_4_zulassungsbedingungen, 2_A_6_pruefungsaktive, 2_A_8_outgoing, 2_A_9_incoming, 2_B_1_doktoratsstudierende

**Display Labels:**
- `Universität (Codex)`
- `Universität (Langtext)`
- `Frauen`
- `Männer`
- `Gesamt`

**Variante Mobilität (2_A_8_outgoing, 2_A_9_incoming):**
- `Universität (Codex)`
- `Universität (Langtext)`
- `EU`
- `Drittstaaten`
- `Gesamt`

### Muster 2: Universität + Personalkategorie + Zeitreihe
**Kennzahlen:** 1_A_1_personal_koepfe, 1_A_1_personal_vzae

**Display Labels:**
- `Universität (Codex)`
- `Universität (Langtext)`
- `Verwendungskategorien WBV`
- `Wintersemester 2022 (Stichtag: 31.12.2022)`
- `Wintersemester 2023 (Stichtag: 31.12.2023)`
- `Wintersemester 2024 (Stichtag: 31.12.2024)`

### Muster 3: Universität + Kollegialorgan-Details
**Kennzahl:** 1_A_3_frauenquote_kollegialorgane

**Display Labels:**
- `Universität (Codex)`
- `Universität (Langtext)`
- `Köpfe Frauen`
- `Köpfe Männer`
- `Köpfe Gesamt`
- `Frauen in %`
- `Männer in %`
- `Organe mit erfüllter Quote`

### Muster 4: Universität + Zeitreihe (Semester)
**Kennzahl:** 2_A_7_belegte_studien

**Display Labels:**
- `Universität (Codex)`
- `Universität (Langtext)`
- `Wintersemester 2022 (Stichtag: 28.02.2023)`
- `Wintersemester 2023 (Stichtag: 28.02.2024)`
- `Wintersemester 2024 (Stichtag: 03.01.2025)`

### Muster 5: Universität + Zeitreihe (Studienjahr)
**Kennzahlen:** 3_A_1_studienabschluesse_ordentlich, 3_A_2_toleranzstudiendauer

**Display Labels:**
- `Universität (Codex)`
- `Universität (Langtext)`
- `Studienjahr 2021/22`
- `Studienjahr 2022/23`
- `Studienjahr 2023/24`

### Muster 6: Universität + Staatengruppe
**Kennzahlen:** 2_A_7_universitaetslehrgaenge, 3_A_1_studienabschluesse_ausserordentlich

**Display Labels:**
- `Universität (Codex)`
- `Universität (Langtext)`
- `Staatengruppe (Ö, EU, andere)`
- `Studien` (nur bei universitaetslehrgaenge)
- `Außerordentliche Studienabschlüsse` (nur bei ausserordentlich)

### Muster 7: Nur Universität + Art
**Kennzahlen:** 2_A_2_eingerichtete_studien, 2_A_5_anzahl_studierenden

**Display Labels:**
- `Universität (Codex)`
- `Universität (Langtext)`
- `Gesamt`
- Spezifische Labels:
  - 2_A_5: `ordentliche Studierende`, `außerordentliche Studierende`

### Muster 8: Professoren-spezifisch
**Kennzahl:** 2_A_1_professoren_aequivalente

**Display Labels:**
- `Universität (Codex)`
- `Universität (Langtext)`
- `ProfessorInnen und Äquivalente`

### Muster 9: Sonderfälle
**Kennzahl:** 1_A_5_frauen_berufungsverfahren (nur 12 Datensätze)

**Display Labels:**
- `Jahr`
- `Studienjahr (Kurzbezeichnung)`
- `Measures`

---

## 5. TIME TYPES (3 eindeutige Werte)

| time_type | Beschreibung |
|-----------|--------------|
| `jahr` | Kalenderjahr |
| `semester` | Semester (Winter/Sommer) |
| `studienjahr` | Studienjahr (z.B. 2021/22) |

**Verwendung in Kennzahlen:**
- **jahr**: Die meisten Kennzahlen
- **semester**: Kennzahlen mit Semesterbezug (z.B. belegte Studien)
- **studienjahr**: Abschluss-bezogene Kennzahlen (3_A_x)

---

## 6. EINHEITEN (4 eindeutige Werte)

| Einheit | Verwendung |
|---------|------------|
| `Anzahl` | Zählbare Ereignisse (Berufungen, Studienabschlüsse, etc.) |
| `Personen` | Personenzahlen (Studierende, Personal als Köpfe) |
| `Prozent` | Quoten und Anteile (Frauenquote, Gender Pay Gap, etc.) |
| `VZÄ` | Vollzeitäquivalente (Personal, ProfessorInnen) |

---

## 7. WICHTIGE ERKENNTNISSE

### 7.1 Datenstruktur-Muster
Die JSON-Dateien folgen einem konsistenten Schema:
```json
{
  "metadata": {
    "kennzahl_id": "...",
    "kennzahl_name": "...",
    "kategorie": "...",
    "einheit": "...",
    "beschreibung": "...",
    "aggregation_rule": "sum|avg|..."
  },
  "data": [
    {
      "kennzahl_id": "...",
      "universität_code": "...",
      "universität_name": "...",
      "uni_type": "...",
      "bundesland": "...",
      "jahr": 2024,
      "reference_year": 2024,
      "time_type": "jahr|semester|studienjahr",
      "display_label": "...",
      "dimensionen": { /* oder {} */ },
      "wert": 123.45,
      "einheit": "...",
      "applicable": true,
      "provenance": { ... }
    }
  ]
}
```

### 7.2 Dimensionen vs. Display Labels
- **Dimensionen-Objekt**: Wird nur bei 4 Kennzahlen genutzt (hauptsächlich Personal-Kennzahlen mit `personalkategorie`)
- **Display Labels**: Hauptmethode zur Differenzierung der Daten (Gender, Zeitreihen, Kategorien)
- Die `personalkategorie` in den Dimensionen entspricht genau den Universitätscodes

### 7.3 Fehlende Daten
- `3_A_3_auslandsaufenthalt` hat ein leeres `data`-Array (0 Datensätze)
- `1_A_5_frauen_berufungsverfahren` hat nur 12 Datensätze (ungewöhnlich wenig)

### 7.4 Kategorisierung
**Nach Kategorie:**
- **Personal**: 6 Kennzahlen (1-A-1 bis 1-A-5, 2-A-1)
- **Studien**: 2 Kennzahlen (2-A-2, 2-A-4)
- **Studierende**: 6 Kennzahlen (2-A-3, 2-A-5 bis 2-A-7 x2, 2-B-1)
- **Mobilität**: 2 Kennzahlen (2-A-8, 2-A-9)
- **Abschlüsse**: 4 Kennzahlen (3-A-1 x2, 3-A-2, 3-A-3)

---

## 8. CSV-EXPORT

Die Analyseergebnisse wurden in folgende CSV-Dateien exportiert:

1. **`universitaeten.csv`** - Vollständige Liste aller Universitäten
2. **`kennzahlen_uebersicht.csv`** - Übersicht aller 21 Kennzahlen
3. **`dimensionen_detailliert.csv`** - Detaillierte Dimensionen-Analyse
4. **`display_labels.csv`** - Alle Display Labels pro Kennzahl
5. **`meta_values.csv`** - Time Types und Einheiten

Alle CSV-Dateien verwenden **Semikolon (;)** als Trennzeichen und **UTF-8-BOM** Encoding für Excel-Kompatibilität.
