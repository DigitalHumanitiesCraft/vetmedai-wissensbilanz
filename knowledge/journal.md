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
- `outputs/tables/universitaeten.csv`, `outputs/tables/kennzahlen_uebersicht.csv`, `outputs/tables/display_labels.csv`
- `outputs/tables/dimensionen_detailliert.csv`, `outputs/tables/meta_values.csv`

### Session-Abschluss

**Erreicht:**
- Ordnerstruktur etabliert (outputs/tables|figures|reports/)
- Scripts mit relativen Pfaden und vollständigem Docstring
- Markdown-Dokumente konsistent und aktualisiert
- .gitignore und CLAUDE.md etabliert
- Validation-Plan für Session 2 dokumentiert

**Offene TODOs für Session 2:**
- Phase 2 Exploration fortsetzen (Validierung, deskriptive Statistiken)
- 6 Validierungs-Scripts gemäß validation-plan.md implementieren
- Weitere explorative Analysen (Vergleiche, Korrelationen)

---

## Session 2: 2026-01-10 - Epic-Validierung & User-Story-Anpassung

### Kontext

Fortsetzung von Session 1 am selben Tag. Fokus auf **Daten-Machbarkeit** für VetMedUni-spezifische Anforderungen und Anpassung der User Stories an tatsächlich implementierbare Features.

### Promptotyping-Phasen

**Phase 2: Exploration & Mapping** 🔄 Fortgesetzt

**Neue Exploration-Scripts:**
- `scripts/validate_epic_vetmeduni.py` - Validierung Epic-Anforderungen gegen UniData
- Epic-spezifische Checks: Betreuungsrelation, Prüfungsaktive Quote, QS Ranking, Zeitreihen, Vergleichsgruppe

**Kritische Erkenntnisse (Negative Befunde):**

1. **Betreuungsrelation - Formel nicht verifizierbar:**
   - Berechnet mit verfügbaren Daten: 1:11.1 (Prüfungsaktive 2024 / ProfessorInnen & Äquivalente)
   - Epic-Angabe VetMedUni: 1:17.6
   - **Abweichung: 6.5** (sehr hoch!)
   - Grund: Personalkategorien (Prof/Dozent/Assoz.Prof) NICHT in UniData differenziert
   - Konsequenz: Formel aus Recherche nicht mit Daten umsetzbar

2. **Prüfungsaktive Quote - Definition unklar:**
   - Berechnet: 73.7% (Prüfungsaktive / Ordentliche Studierende)
   - Epic-Angabe: >90% (im Diplomstudium)
   - Problem: "Diplomstudium" vs. "alle Studien" - Definition nicht in Daten
   - Konsequenz: Epic-Wert nicht nachvollziehbar mit UniData

3. **QS Ranking - Externe Datenquelle:**
   - QS Ranking Platz 28 NICHT in UniData-Kennzahlen
   - Konsequenz: Manuelle Eingabe oder separate Datenquelle erforderlich

4. **VetMedUni unvollständig im Datensatz:**
   - Fehlend in 4/21 Kennzahlen
   - Dreijahresvergleich nur für 12/21 Kennzahlen vollständig (2022-2024)

**Phase 3: Destillation** ✅ Iteration

**Angepasste Dokumente:**
- `knowledge/user-stories.md` - Machbarkeitsanalyse-Sektion hinzugefügt
  - Tabelle mit Feasibility-Status für alle User Stories
  - D-03 Betreuungsrelation komplett überarbeitet mit Validierungsbefunden
  - Workshop-Klärungsfragen formuliert (ZWINGEND erforderlich)
  - Links zu beiden Feasibility-Reports

**Generierte Reports:**
- `outputs/reports/epic_vetmeduni_feasibility.md` - 400 Zeilen detaillierte Machbarkeitsanalyse
  - Executive Summary mit Status-Tabelle
  - 6 Validierungs-Checks mit Befunden
  - Kritische Erkenntnisse für Workshop
  - Empfehlungen für Epic-Anpassungen

### Methodik: Data-Driven Validation

**Ansatz:**
Statt User Stories aus Recherche abzuleiten und später zu implementieren, wurden **alle Stories gegen tatsächliche Daten validiert** BEVOR Workshop oder Implementierung.

**Vorteil:**
- Workshop-Teilnehmer erhalten konkrete Befunde (nicht Vermutungen)
- Kritische Fragen sind datenbasiert formuliert
- Implementierung beginnt nur mit verifizierten Features

**Framework:**
Für jede Epic-Anforderung:
1. Daten-Check: Sind erforderliche Kennzahlen vorhanden?
2. Formel-Verifizierung: Können wir den angegebenen Wert nachrechnen?
3. Vollständigkeits-Check: Ist VetMedUni vollständig im Datensatz?
4. Feasibility-Rating: OK / WARN / FAIL

### Output

**Exploration-Scripts:**
- `scripts/validate_epic_vetmeduni.py` - Epic-Validierung mit 6 Checks

**Reports:**
- `outputs/reports/epic_vetmeduni_feasibility.md` - Epic-Machbarkeit
- `outputs/reports/user_story_feasibility.md` - User-Stories-Machbarkeit (existiert bereits)

**Aktualisierte Dokumente:**
- `knowledge/user-stories.md` - Feasibility-Befunde integriert
- `scripts/README.md` - validate_epic_vetmeduni.py dokumentiert (implizit)

### Kritische Workshop-Fragen (11.02.2026)

Diese Fragen MÜSSEN im Workshop geklärt werden:

1. **Betreuungsrelation:** Welche exakte Formel nutzt VetMedUni für 1:17.6?
   - Nutzt VetMedUni interne Datenquellen (nicht aus UniData)?
   - Sind "Professoren + Dozenten + Assoz.Prof" = "ProfessorInnen & Äquivalente"?

2. **Prüfungsaktive Quote:** Was bedeutet "Diplomstudium" in der Epic-Angabe >90%?
   - Ist das eine Teilmenge von "Prüfungsaktive Studien"?
   - Ist die 73.7%-Berechnung (alle Studien) vergleichbar?

3. **QS Ranking:** Ist Integration von QS Ranking erforderlich?
   - Manuelle Pflege akzeptabel oder automatisierte Datenquelle notwendig?

4. **Zeitreihen-Methodologie:** Welche Zeiträume sind tatsächlich vergleichbar?
   - Dokumentation zu Erhebungsmethoden-Änderungen verfügbar?

### Erkenntnisse für Promptotyping-Methodik

**Lesson Learned:**
Epic-Validierung FRÜH durchführen (vor Workshop, nicht nach!) um:
- Unrealistische Erwartungen zu korrigieren
- Konkrete Klärungsfragen zu formulieren
- Workshop-Zeit auf tatsächliche Blocker zu fokussieren

**Negativ-Befunde sind wertvoll:**
- "Personalkategorien NICHT differenziert" verhindert falsche Implementierung
- "Abweichung 6.5" zeigt, dass Formel-Annahme falsch war
- "QS Ranking extern" klärt Scope früh

### Session-Abschluss

**Erreicht:**
- Epic VetMedUni vollständig gegen Daten validiert
- User Stories angepasst mit Feasibility-Befunden
- 4 kritische Workshop-Fragen formuliert
- 2 Feasibility-Reports generiert
- knowledge/user-stories.md aktualisiert mit Machbarkeitsanalyse

**Offene TODOs für Session 3:**
- Refactoring: Shared Utils für JSON-Loading und CSV-Writing
- Phase 2 Exploration fortsetzen (deskriptive, vergleichende Analysen)
- Phase 4 vorbereiten: `knowledge/design.md` für Dashboard-Konzept erstellen

---

## Session 3: TBD - Refactoring & Design

**Geplant:**

**Code-Refactoring (Optional):**
- `scripts/shared_utils.py` erstellen (gemeinsame Basis-Funktionen)
- Konstanten zentralisieren (`scripts/constants.py`)

**Phase 3: Destillation** (Iteration)
- Design-Entscheidungen → `knowledge/design.md` (Dashboard-Konzept für Webseite)
- Erkenntnisse → `knowledge/insights.md` (wenn weitere Analysen vorhanden)

**Phase 2: Exploration & Mapping** (Fortsetzung)
- Deskriptive Statistiken: Verteilungen, Vollständigkeit
- Vergleichende Analysen: Uni-Typen, Bundesländer, Zeittrends

**Phase 4: Implementation** (Spätere Session)
- Dashboard-Entwicklung basierend auf Exploration-Erkenntnissen
- Iterative Prototyp-Entwicklung mit LLM-Unterstützung

---
