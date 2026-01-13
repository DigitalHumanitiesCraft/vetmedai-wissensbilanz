# Session 2 Summary: Epic-Validierung & User-Story-Anpassung

**Datum:** 2026-01-10
**Dauer:** Fortsetzung von Session 1 (selber Tag)
**Fokus:** Daten-Machbarkeit für VetMedUni-spezifische Anforderungen

---

## Was wurde erreicht?

### 1. Epic VetMedUni vollständig validiert

**Neues Script:** `scripts/validate_epic_vetmeduni.py`

**6 Validierungs-Checks durchgeführt:**
- ✅ VetMedUni in Daten vorhanden (17/21 Kennzahlen)
- ⚠️ Betreuungsrelation berechenbar (mit Abweichung 6.5!)
- ⚠️ Prüfungsaktive Quote berechenbar (Definition unklar)
- ✅ Dreijahresvergleich verfügbar (12/21 Kennzahlen)
- ✅ Vergleichsgruppe MedUnis verfügbar (4 Unis)
- ❌ QS Ranking NICHT in UniData

---

## Kritische Befunde

### 1. Betreuungsrelation - Formel nicht verifizierbar

**Problem:**
- Berechnet mit UniData: **1:11.1**
- Epic-Angabe VetMedUni: **1:17.6**
- **Abweichung: 6.5** (sehr hoch!)

**Grund:**
Personalkategorien (Professor, Dozent, Assoziierte Professoren) sind in UniData NICHT differenziert.

**Konsequenz:**
Formel aus Epic/Recherche nicht mit vorhandenen Daten umsetzbar.

**Workshop-Klärung ZWINGEND:**
- Welche exakte Formel nutzt VetMedUni für 1:17.6?
- Nutzt VetMedUni interne Datenquellen (nicht aus UniData)?
- Sind "Professoren + Dozenten + Assoz.Prof" = "ProfessorInnen & Äquivalente"?

---

### 2. Prüfungsaktive Quote - Definition unklar

**Problem:**
- Berechnet: **73.7%** (Prüfungsaktive / Ordentliche Studierende)
- Epic-Angabe: **>90%** (im Diplomstudium)

**Grund:**
"Diplomstudium" ist in UniData nicht als separate Dimension vorhanden.

**Workshop-Klärung:**
- Ist "Diplomstudium" eine Teilmenge von "Prüfungsaktive Studien"?
- Ist die 73.7%-Berechnung (alle Studien) vergleichbar?

---

### 3. QS Ranking - Externe Datenquelle

**Problem:**
QS Ranking Platz 28 ist NICHT in UniData-Kennzahlen enthalten.

**Konsequenz:**
- Manuelle Eingabe erforderlich ODER
- Integration externer Datenquelle ODER
- Feature aus Epic entfernen

**Workshop-Klärung:**
- Ist QS Ranking-Integration erforderlich oder manuelle Pflege akzeptabel?

---

### 4. VetMedUni unvollständig im Datensatz

**Problem:**
VetMedUni fehlt in 4/21 Kennzahlen.

**Konsequenz:**
Dashboard muss fehlende Daten explizit anzeigen.

---

## Angepasste Dokumente

### `knowledge/user-stories.md`

**Neu hinzugefügt:**
- Machbarkeitsanalyse-Sektion am Anfang
- Tabelle mit Feasibility-Status für alle User Stories
- Links zu beiden Feasibility-Reports

**D-03 Betreuungsrelation komplett überarbeitet:**
- Kritischer Validierungsbefund integriert
- Berechnete vs. Epic-Werte dokumentiert
- Workshop-Klärungsfragen formuliert (ZWINGEND erforderlich)
- Disclaimer für Implementierung ohne Klärung

---

## Generierte Outputs

### Reports

1. **`outputs/reports/epic_vetmeduni_feasibility.md`** (400 Zeilen)
   - Executive Summary mit Status-Tabelle
   - 6 detaillierte Validierungs-Checks
   - Kritische Erkenntnisse für Workshop
   - Empfehlungen für Epic-Anpassungen

2. **`outputs/reports/user_story_feasibility.md`** (existiert bereits)
   - Allgemeine Machbarkeit aller User Stories
   - Verlinkung aus user-stories.md

### Scripts

- **`scripts/validate_epic_vetmeduni.py`** - Epic-Validierung mit 6 Checks
  - Dokumentiert in `scripts/README.md`

### Knowledge Documents

- **`knowledge/refactoring-plan.md`** - Refactoring-Empfehlungen für Session 3
- **`knowledge/journal.md`** - Aktualisiert mit Session 2
- **`knowledge/INDEX.md`** - Aktualisiert mit neuen Dokumenten und Erkenntnissen

---

## Methodischer Fortschritt

### Data-Driven Validation Framework

**Neu etabliert:**
Für jede Epic-Anforderung:
1. Daten-Check: Sind erforderliche Kennzahlen vorhanden?
2. Formel-Verifizierung: Können wir den angegebenen Wert nachrechnen?
3. Vollständigkeits-Check: Ist VetMedUni vollständig im Datensatz?
4. Feasibility-Rating: OK / WARN / FAIL

**Vorteil:**
- Workshop-Teilnehmer erhalten konkrete Befunde (nicht Vermutungen)
- Kritische Fragen sind datenbasiert formuliert
- Implementierung beginnt nur mit verifizierten Features

---

## Lesson Learned für Promptotyping

**Epic-Validierung FRÜH durchführen** (vor Workshop, nicht nach!):
- ✅ Unrealistische Erwartungen korrigieren
- ✅ Konkrete Klärungsfragen formulieren
- ✅ Workshop-Zeit auf tatsächliche Blocker fokussieren

**Negativ-Befunde sind wertvoll:**
- "Personalkategorien NICHT differenziert" verhindert falsche Implementierung
- "Abweichung 6.5" zeigt, dass Formel-Annahme falsch war
- "QS Ranking extern" klärt Scope früh

---

## Kritische Workshop-Fragen (11.02.2026)

Diese Fragen MÜSSEN im Workshop geklärt werden:

### 1. Betreuungsrelation (KRITISCH)
- Welche exakte Formel nutzt VetMedUni für 1:17.6?
- Nutzt VetMedUni interne Datenquellen (nicht aus UniData)?
- Sind "Professoren + Dozenten + Assoz.Prof" identisch mit "ProfessorInnen & Äquivalente"?

### 2. Prüfungsaktive Quote
- Was bedeutet "Diplomstudium" in der Epic-Angabe >90%?
- Ist das eine Teilmenge von "Prüfungsaktive Studien"?
- Ist die 73.7%-Berechnung (alle Studien) vergleichbar?

### 3. QS Ranking
- Ist Integration von QS Ranking erforderlich?
- Manuelle Pflege akzeptabel oder automatisierte Datenquelle notwendig?

### 4. Zeitreihen-Methodologie
- Welche Zeiträume sind tatsächlich vergleichbar?
- Dokumentation zu Erhebungsmethoden-Änderungen verfügbar?

---

## Nächste Schritte (Session 3)

### 1. Code-Refactoring (geplant)
- `scripts/shared_utils.py` erstellen (gemeinsame Basis-Funktionen)
- `scripts/constants.py` erstellen (Konstanten zentralisieren)
- Alle 4 Scripts refactoren

Details siehe: `knowledge/refactoring-plan.md`

### 2. Phase 4 vorbereiten
- `knowledge/design.md` für Dashboard-Konzept erstellen

### 3. Phase 2 fortsetzen
- Deskriptive Statistiken
- Vergleichende Analysen
- Relationale Analysen

---

## Dateien-Übersicht

### Neu erstellt:
```
scripts/validate_epic_vetmeduni.py
outputs/reports/epic_vetmeduni_feasibility.md
knowledge/refactoring-plan.md
SESSION_2_SUMMARY.md
```

### Aktualisiert:
```
knowledge/user-stories.md
knowledge/journal.md
knowledge/INDEX.md
scripts/README.md
```

---

## Promptotyping-Status

**Phase 1: Preparation** ✅ Abgeschlossen (Session 1)
**Phase 2: Exploration** 🔄 Fortgesetzt (Session 1+2, Foundation Scripts komplett)
**Phase 3: Destillation** ✅ Iteration abgeschlossen (Session 2)
**Phase 4: Implementation** ⏳ Geplant (Session 3+)

---

**Session 2 abgeschlossen:** 2026-01-10
**Nächste Session:** Refactoring & Design (TBD)
