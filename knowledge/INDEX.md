# Wissensbilanz Knowledge Vault

**Projekt:** Wissensbilanz-Datenanalyse österreichischer Universitäten
**Methodik:** Promptotyping (4-Phasen-Modell)
**Status:** Phase 2 (Exploration) begonnen, Phase 3 (Destillation) abgeschlossen

---

## Promptotyping Documents (für LLM-Kontext)

### Datenmodell & Strukturen
- [[data]] - Vollständige Datenmodell-Spezifikation (22 Unis, 21 Kennzahlen, 3.274 Datenpunkte)
- [[exploration-framework]] - Methodik für Exploration-Script-Entwicklung

### Projektziele & Anforderungen
- [[requirements]] - Forschungsfragen & Projektziele (komprimiert)

---

## Prozess-Dokumentation (für Menschen)

- [[journal]] - Chronologische Session-Dokumentation mit Promptotyping-Phasen

---

## Wichtigste Erkenntnisse (Quick Reference)

**Datenstruktur:**
- 22 Universitäten in 5 Typen (volluniversität, technisch, kunst, medizinisch, weiterbildung)
- 21 Kennzahlen in 4 Kategorien (Personal, Studierende, Studien, Abschlüsse)
- **Kritisch:** `display_label` ist primäre Dimension (nicht `dimensionen`-Objekt!)
- 4 Einheiten: Personen, Anzahl, Prozent, VZÄ
- 3 Zeitdimensionen: jahr, semester, studienjahr

**Methodologische Hinweise:**
- Zeitreihen nicht direkt vergleichbar (Erhebungsmethoden geändert)
- Prozent-Kennzahlen nicht einfach summierbar
- 3-A-3 (Auslandsaufenthalt) hat 0 Datenpunkte

**Exploration-Status:**
- ✅ Foundation: Metadaten-Extraktion (`scripts/analyze_data.py`)
- 🔄 Descriptive: TODO (Verteilungen, Null-Werte, Vollständigkeit)
- 🔄 Comparative: TODO (Uni-Typen, Trends, Bundesländer)
- 🔄 Relational: TODO (Korrelationen, Beziehungen)

---

## Vault-Struktur

```
knowledge/          # Promptotyping Documents & Prozess-Dokumentation
scripts/            # Exploration-Scripts (Phase 2)
data/
  ├── json/         # 21 konvertierte Kennzahl-Dateien
  └── *.xlsx        # 74 Excel-Rohdateien
outputs/
  ├── tables/       # CSV-Referenzdaten (Metadaten-Extraktion)
  ├── figures/      # Visualisierungen (noch leer)
  └── reports/      # Analyse-Reports (noch leer)
```

---

## Tags

#promptotyping #phase-2-exploration #phase-3-destillation
#wissensbilanz #datenmodell #österreich-universitäten

---

## Nächste Schritte

1. **Phase 2 fortsetzen:** Weitere Exploration-Scripts entwickeln
2. **Phase 3 iterieren:** Erkenntnisse in `insights.md` destillieren
3. **Phase 4 vorbereiten:** Dashboard-Konzept in `design.md` skizzieren
