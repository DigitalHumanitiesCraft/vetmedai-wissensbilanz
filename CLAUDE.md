# Claude Collaboration Rules

Regeln für die Zusammenarbeit zwischen Mensch und Claude in diesem Projekt.

## Kommunikation

Sachlich, direkt, fachterminologisch korrekt. Keine Emojis, keine Superlative, keine emotionale Validierung. Konstruktive Kritik ohne Beschönigung. Probleme direkt benennen statt abschwächen.

## Promptotyping-Methodik

Phasen sequentiell durchlaufen, keine überspringen.

1. **Preparation** Rohmaterial sammeln
2. **Exploration** Sondieren, negative Erkenntnisse dokumentieren
3. **Destillation** Context Compression
4. **Implementation** Iterativ mit LLM

Exploration muss vor Design-Entscheidungen abgeschlossen sein.

## Daten und Code

Nur verifizierte Daten aus tatsächlichen Dateien, keine Hypothesen oder Platzhalter. Bei Unsicherheit explizit als unklar markieren.

| Aspekt | Regel |
|--------|-------|
| Pfade | Relativ, nie hardcoded absolut |
| Inputs | `data/json/` |
| Outputs | `outputs/{tables\|figures\|reports}/`, nie Root |
| Scripts | Ein Script pro Forschungsfrage, mit Docstring |
| Python | Error-Handling für File I/O, Type Hints |

## Dokumentation

**Markdown** Klare Hierarchie, keine Emojis, Code-Blöcke mit Sprachbezeichnung, Tabellen für strukturierte Daten.

**Commits** Conventional Commits (`feat:`, `fix:`, `docs:`, `refactor:`), erste Zeile max 72 Zeichen, Body erklärt Was und Warum.

**Code-Kommentare** Docstrings nach Template, Inline nur bei komplexer Logik, keine TODO-Kommentare (stattdessen Issues oder `knowledge/*`).

## Knowledge Vault

`knowledge/` als Obsidian-kompatibler Vault. Promptotyping-Documents für LLM-Kontext, `journal.md` für Prozess-Chronologie.

## Session-Protokoll

**Start** `journal.md` und `INDEX.md` lesen, Git Status prüfen, TODOs aus letzter Session aufnehmen.

**Ende** Offene TODOs dokumentieren, `journal.md` aktualisieren, Git committen oder stashen, nächste Schritte definieren.

## Bei Unklarheit

Nicht raten oder annehmen. Explizit nachfragen, Optionen mit Vor- und Nachteilen präsentieren, User entscheiden lassen.