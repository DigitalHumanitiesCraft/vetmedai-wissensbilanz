# Projekt Journal: Wissensbilanz-Datenanalyse

**Methodik:** Promptotyping (4-Phasen-Modell)

---

## Session 1: 2026-01-10 - Preparation & Exploration

### Promptotyping-Phasen

**Phase 1: Preparation** ✅
- Sammlung Rohmaterialien: 74 Excel-Dateien, 21 JSON-Dateien (3.274 Datenpunkte)
- Dokumentation: WBV/UHSBV als rechtliche Grundlagen
- Implizites Domänenwissen: Wissensbilanz-Kennzahlen österreichischer Universitäten

**Phase 2: Exploration & Mapping** 🔄 Begonnen
- Sondierung Datenstruktur: Schema-Analyse mehrerer JSON-Dateien
- Mapping: Identifikation gemeinsamer Strukturen über alle 21 Kennzahlen
- Negative Erkenntnisse: `dimensionen`-Objekt wird kaum genutzt (nur 4/21), `display_label` ist Hauptdifferenzierung
- Erstes Exploration-Script: `analyze_data.py` (Metadaten-Extraktion)
- **Fortsetzung nächste Session:** Weitere Exploration (deskriptiv, vergleichend, relational)

**Phase 3: Destillation** ✅
- Context Compression in `knowledge/data.md`: Kompakte Datenmodell-Spezifikation (NUR verifizierte Daten)
- Strukturierte Referenztabellen: Universitäten (22), Kennzahlen (21), Display Labels (99)
- Vault-Struktur etabliert: `knowledge/` als Wissensbasis, `scripts/` für Exploration
- Promptotyping-Documents: `data.md`, `exploration-framework.md`, `INDEX.md`, `requirements.md`

**Phase 4: Implementation** → Spätere Session (Dashboard-Entwicklung)

### Zentrale Erkenntnisse

**Datenstruktur:**
- Standardisiertes Schema über alle Kennzahlen
- 22 Universitäten in 5 Typen
- 3 Zeitdimensionen: jahr, semester, studienjahr
- **Kritisch:** Display Labels als primäre Dimension (nicht `dimensionen`-Objekt)

**Methodologisches:**
- Zeitreihen nicht direkt vergleichbar (Erhebungsmethoden geändert)
- 3-A-3 hat keine Daten (0 Datenpunkte)
- Prozent-Kennzahlen nicht einfach summierbar

### Output

**Destillierte Dokumente:**
- `knowledge/data.md`: Datenmodell-Spezifikation
- `knowledge/journal.md`: Prozessdokumentation

**Exploration-Scripts:**
- `scripts/analyze_data.py`: Metadaten-Extraktion aus allen JSON-Dateien
- `scripts/README.md`: Script-Dokumentation

**Referenzdaten (generiert):**
- `universitaeten.csv`, `kennzahlen_uebersicht.csv`, `display_labels.csv`
- `dimensionen_detailliert.csv`, `meta_values.csv`

### Nächste Schritte

**Phase 2: Exploration & Mapping** (Fortsetzung)
- Weitere Exploration-Scripts: Deskriptive Statistiken, Vergleiche, Korrelationen
- Forschungsfragen explorativ beantworten: Was ist visualisierbar? Welche Muster existieren?
- Negative Erkenntnisse sammeln: Was funktioniert NICHT mit den Daten?

**Phase 3: Destillation** (Iteration)
- Erkenntnisse aus Exploration → `knowledge/insights.md`
- Design-Entscheidungen → `knowledge/design.md` (Dashboard-Konzept)

**Phase 4: Implementation**
- Dashboard-Entwicklung basierend auf Exploration-Erkenntnissen
- Iterative Prototyp-Entwicklung mit LLM-Unterstützung

---
