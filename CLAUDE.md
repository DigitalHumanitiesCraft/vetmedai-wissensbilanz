# Claude Collaboration Rules

Regeln für die Zusammenarbeit zwischen Mensch und Claude in diesem Projekt.

---

## Kommunikationsstil

### NIEMALS verwenden:
- **Emojis** (weder in Text noch in Commits)
- Übertriebene Superlative ("großartig", "fantastisch", "perfekt")
- Emotionale Validierung ("Sie haben absolut recht")
- Marketing-Sprache

### IMMER verwenden:
- Sachliche, präzise Sprache
- Direkte Antworten ohne Füllwörter
- Konstruktive Kritik (ehrlich, nicht beschönigend)
- Fachterminologie korrekt

---

## Arbeitsprinzipien

### 1. Keine Hypothesen
- **NUR verifizierte Daten** aus tatsächlichen Dateien
- Keine Beispielwerte oder Platzhalter
- Bei Unsicherheit: Explizit als "unklar" markieren

### 2. Ehrlichkeit vor Optimismus
- Probleme direkt benennen
- "Das funktioniert nicht" > "Das könnte schwierig werden"
- Kritische Analyse vor Implementierung

### 3. Promptotyping-Methodik
- Phase 1: Preparation (Rohmaterial sammeln)
- Phase 2: Exploration (Sondieren, Negative Erkenntnisse)
- Phase 3: Destillation (Context Compression)
- Phase 4: Implementation (Iterativ mit LLM)

### 4. Phasen NICHT überspringen
- Phase 2 muss vor Phase 4 fertig sein
- Exploration vor Design-Entscheidungen
- Validierung vor Dashboard

---

## Dokumentation

### Markdown-Konventionen
- **Keine Emojis** in Headings, Listen, oder Text
- Klare hierarchische Struktur (##, ###)
- Code-Blöcke mit Sprachbezeichnung
- Tabellen für strukturierte Daten

### Commit-Messages
- **Keine Emojis** in Commit-Messages
- Conventional Commits: `feat:`, `fix:`, `docs:`, `refactor:`
- Erste Zeile: max 72 Zeichen
- Body: Was & Warum (nicht Wie)

### Code-Kommentare
- Docstrings nach Template (siehe exploration-framework.md)
- Inline-Kommentare nur bei komplexer Logik
- **KEINE** TODO-Kommentare (nutze issues oder knowledge/*)

---

## Code-Standards

### Python
- Relative Pfade (nie hardcoded absolute Pfade)
- Error-Handling für File I/O
- Type Hints wo sinnvoll
- Docstring-Format: siehe exploration-framework.md

### Git
- `.gitignore` für generierte Dateien
- Kleine, atomare Commits
- Branch: `main` (kein `master`)

---

## Projekt-Spezifisch

### Daten
- JSON-Dateien in `data/json/` (Input)
- Generierte Outputs in `outputs/tables|figures|reports/`
- **NIEMALS** Root als Output-Verzeichnis

### Scripts
- Ordnerstruktur: `scripts/00_foundation`, `01_descriptive`, etc.
- Ein Script = Eine Forschungsfrage
- Reproduzierbar (relative Pfade, dokumentierte Dependencies)

### Knowledge Vault
- `knowledge/` als Obsidian-kompatibler Vault
- Promptotyping-Documents für LLM-Kontext
- `journal.md` für Menschen (Prozess-Chronologie)

---

## Session-Management

### Vor Session-Ende:
1. Offene TODOs in TodoWrite abschließen oder dokumentieren
2. `journal.md` aktualisieren
3. Sauberer Git-Status (commit oder stash)
4. Nächste Schritte klar definieren

### Session-Start:
1. `journal.md` lesen (letzte Session)
2. `INDEX.md` lesen (Vault-Übersicht)
3. Git Status prüfen
4. TODOs aus letzter Session aufnehmen

---

## Anti-Patterns (VERMEIDEN)

- Duplikate erstellen statt vorhandenen Code zu nutzen
- Outputs im Root-Verzeichnis
- Hypothetische Daten in Dokumentation
- Scripts ohne Docstring
- Markdown-Dokumente mit veralteten Pfaden
- "Das könnte funktionieren" ohne Test

---

## Eskalation

Bei Unklarheiten:
1. **NICHT** raten oder annehmen
2. Explizit beim User nachfragen
3. Optionen präsentieren (mit Vor-/Nachteilen)
4. User entscheiden lassen

---

Letzte Aktualisierung: 2026-01-10
