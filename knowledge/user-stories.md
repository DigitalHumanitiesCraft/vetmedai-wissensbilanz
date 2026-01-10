# User Stories: VetMedAI Wissensbilanz

> **Status**: Hypothesen zur Validierung im Workshop (11.02.2026)
> **Quelle**: Webrecherche zu österreichischem Hochschulrecht, WBV 2016, unidata-Dokumentation
> **Methodik**: Diese Stories sind keine bestätigten Anforderungen, sondern forschungsbasierte Annahmen. Der Workshop dient der Validierung, Korrektur und Priorisierung.

---

## Machbarkeitsanalyse gegen tatsächliche Daten

**Vollständige Reports:**
- [User Story Feasibility](../outputs/reports/user_story_feasibility.md) - Allgemeine Machbarkeit
- [Epic VetMedUni Feasibility](../outputs/reports/epic_vetmeduni_feasibility.md) - VetMedUni-spezifische Validierung

**Zusammenfassung:**

| Story | Machbarkeit | Kritischer Befund |
|-------|-------------|-------------------|
| D-01 Zeitreihen | OK Umsetzbar | Warnung: Erhebungsmethoden geändert (12/21 Kennzahlen mit 2022-2024) |
| D-02 Uni-Vergleich | OK Umsetzbar | 4 MedUnis verfügbar, Durchschnitt bei Prozent eingeschränkt |
| D-03 Betreuungsrelation | KRITISCH | Formel nicht verifizierbar (Abweichung 6.5 zwischen Berechnung und Epic-Angabe) |
| D-04 Abweichungen | OK Umsetzbar | - |
| D-05 Datenqualität | OK Umsetzbar | - |
| B-01 bis B-04 Text | OK Umsetzbar | LLM-basiert, keine Daten-Blocker |

**Legende:** OK = Vollständig umsetzbar, KRITISCH = Daten-Validierung erforderlich

**Kritische Erkenntnisse:**
1. **Betreuungsrelation (D-03):** Berechnet 1:11.1, Epic gibt 1:17.6 an (Abweichung 6.5). Entweder andere Formel oder andere Datenquelle.
2. **Prüfungsaktive Quote:** Berechnet 73.7%, Epic gibt >90% an. Definition unklar (Diplomstudium vs. alle Studien?).
3. **Personalkategorien fehlen:** Professor/Dozent/Assoziierte Prof. nicht differenziert in UniData.

---

## Persona

**Michael Forster** – Fachverantwortlicher für Wissensbilanz und Berichtswesen an der VetMedUni Wien.

Arbeitet mit UniData-Kennzahlen, erstellt den jährlichen Leistungsbericht (Kurz- oder Langfassung), kommentiert Kennzahlenentwicklungen und bereitet Daten für das Leistungsvereinbarungs-Monitoring vor. Berichtet an Rektorat und Universitätsrat. Muss bis 30. April die Wissensbilanz einreichen.

---

## Use Case 1: Dashboard (Datenexploration)

### D-01: Zeitreihenvergleich einer Kennzahl

> Als Berichtersteller will ich die Entwicklung einer Kennzahl über mehrere Jahre sehen, um Trends zu beschreiben und Veränderungen zu kommentieren.

**Begründung**: Die WBV 2016 schreibt einen Dreijahresvergleich vor. Kennzahlen werden "jährlich erhoben und im Vergleich von drei Jahren dargestellt" (Akademie der bildenden Künste).

**Akzeptanzkriterien**:
- Auswahl einer Kennzahl (z.B. 1-A-1 Personal)
- Filterung nach Dimensionen (Geschlecht, Verwendung, Kopf/VZÄ)
- Visualisierung als Linien- oder Balkendiagramm
- Export der Daten für Weiterverarbeitung

**Priorität (Hypothese)**: Hoch

---

### D-02: Vergleich mit anderen Universitäten

> Als Berichtersteller will ich die VetMedUni mit anderen Medizinischen Universitäten vergleichen, um die relative Position einzuordnen.

**Begründung**: unidata dient dem "effizienten Benchmarking" (TU Wien). Der Vergleich mit Universitäten gleichen Typs ist für die Einordnung der eigenen Leistung relevant.

**Akzeptanzkriterien**:
- Auswahl von Vergleichsuniversitäten (MedUni Wien, MedUni Graz, MedUni Innsbruck)
- Nebeneinanderstellung derselben Kennzahl
- Optional: Durchschnittsberechnung der Vergleichsgruppe

**Priorität (Hypothese)**: Mittel

**Offene Frage**: Welche Vergleichsgruppe ist relevant? Nur Medizin-Unis oder auch andere Spezialuniversitäten?

---

### D-03: Betreuungsrelation berechnen

> Als Berichtersteller will ich die Betreuungsrelation für die VetMedUni berechnen, um sie mit den Zielwerten der Leistungsvereinbarung zu vergleichen.

**Begründung**: Die Betreuungsrelation ist ein "wesentlicher Indikator für die Universitätsfinanzierung" (BMBWF). Der Hochschulplan 2030 definiert Zielwerte (1:35). Die Berechnung erfordert die Kombination von Personal- und Studierendendaten.

**Akzeptanzkriterien (ANGEPASST nach Datenvalidierung)**:
- Berechnung möglich: Prüfungsaktive Studien (2-A-6 Gesamt) / ProfessorInnen & Äquivalente (2-A-1)
- Vergleich mit Zielwert aus Leistungsvereinbarung
- Zeitreihe der Betreuungsrelation

**Priorität (Hypothese)**: Hoch (finanzierungsrelevant)

**KRITISCHER VALIDIERUNGSBEFUND:**
- **Original-Formel (aus Recherche):** Prüfungsaktive / VZÄ (Professoren + Dozenten + Assoz. Prof.)
- **Problem:** Personalkategorien (Prof/Dozent/Assoz.Prof) NICHT in UniData differenziert
- **Mögliche Formel:** Prüfungsaktive (2-A-6) / ProfessorInnen & Äquivalente (2-A-1)
- **Berechnet für VetMedUni 2024:** 1:11.1
- **Epic-Angabe VetMedUni:** 1:17.6
- **Abweichung:** 6.5 (sehr hoch!)

**Workshop-Klärung ZWINGEND erforderlich:**
1. Welche exakte Formel nutzt VetMedUni für Betreuungsrelation 1:17.6?
2. Nutzt VetMedUni interne Datenquellen (nicht aus UniData)?
3. Ist "Diplomstudium" eine Teilmenge von "Prüfungsaktive Studien"?
4. Sind "Professoren + Dozenten + Assoz.Prof" identisch mit "ProfessorInnen & Äquivalente"?

**Ohne Klärung:** Feature nur mit Disclaimer "Vereinfachte Berechnung, Abweichung zur offiziellen Zahl möglich" umsetzbar.

---

### D-04: Abweichungen identifizieren

> Als Berichtersteller will ich schnell erkennen, wo Kennzahlen von Erwartungen oder Vorjahreswerten abweichen, um diese Stellen gezielt zu kommentieren.

**Begründung**: Der Leistungsbericht muss "wesentliche Ereignisse und Entwicklungen" darstellen (WBV 2016). Signifikante Veränderungen erfordern Erklärungen.

**Akzeptanzkriterien**:
- Automatische Markierung von Veränderungen >10% zum Vorjahr
- Filterung nach Richtung (Anstieg/Rückgang)
- Sortierung nach Größe der Abweichung

**Priorität (Hypothese)**: Mittel

---

### D-05: Datenqualität prüfen

> Als Berichtersteller will ich Datenqualitätsprobleme erkennen, bevor ich Zahlen in den Bericht übernehme.

**Begründung**: Das Datenclearing zwischen Unis und BMBWF umfasst "Plausibilitätsprüfungen" (WBV-Arbeitsbehelf). Fehlerhafte Daten führen zu Rückfragen.

**Akzeptanzkriterien**:
- Summenvalidierung (Frauen + Männer = Gesamt)
- Markierung von Null-Werten und fehlenden Daten
- Hinweis auf bekannte Ausnahmen (z.B. UR hat keine ordentlichen Studierenden)

**Priorität (Hypothese)**: Hoch (Voraussetzung für alles andere)

---

## Use Case 2: Berichterstellung (Textgenerierung)

### B-01: Kennzahlenkommentierung generieren

> Als Berichtersteller will ich einen Textentwurf für die Interpretation einer Kennzahl generieren, um den Schreibprozess zu beschleunigen.

**Begründung**: Kennzahlen werden laut WBV 2016 "mit Interpretationstexten ergänzt". Diese Texte folgen einem wiederkehrenden Muster: Beschreibung des Wertes, Vergleich mit Vorjahr, Einordnung der Entwicklung.

**Akzeptanzkriterien**:
- Input: Kennzahl, Zeitraum, ggf. Vergleichsuniversitäten
- Output: Sachlicher Fließtext (2-4 Sätze) ohne Wertung
- Korrekte Zahlenwerte aus den Daten
- Editierbar durch Nutzer

**Priorität (Hypothese)**: Hoch

**Offene Frage**: Gibt es Vorlagen oder Beispieltexte aus früheren Wissensbilanzen der VetMedUni?

---

### B-02: Vorjahresvergleich formulieren

> Als Berichtersteller will ich automatisch generierte Vergleichssätze zum Vorjahr, um repetitive Formulierungen nicht selbst schreiben zu müssen.

**Begründung**: Der Dreijahresvergleich ist vorgeschrieben. Typische Formulierungen wie "Im Vergleich zum Vorjahr steigt die Anzahl der Studienabschlüsse um 5%" (Uni Graz Wissensbilanz 2023) wiederholen sich.

**Akzeptanzkriterien**:
- Automatische Berechnung der prozentualen Veränderung
- Sprachliche Variation (nicht immer "steigt um X%")
- Kontextsensitiv: Absolute Zahlen bei kleinen Werten, Prozent bei großen

**Priorität (Hypothese)**: Mittel

---

### B-03: Ampelstatus-Begründung erstellen

> Als Berichtersteller will ich eine Begründung für den Ampelstatus eines Vorhabens entwerfen lassen, um das Leistungsvereinbarungs-Monitoring effizienter zu erstellen.

**Begründung**: Teil 3 der Wissensbilanz dokumentiert den "Stand der Umsetzung jener Ziele und Vorhaben, die in der Leistungsvereinbarung festgelegt sind" (Akademie der bildenden Künste). Jedes Vorhaben erhält einen Ampelstatus (grün/gelb/rot) mit Begründung.

**Akzeptanzkriterien**:
- Input: Vorhaben-Beschreibung, aktueller Status, relevante Kennzahlen
- Output: Kurze Begründung (3-5 Sätze) für gewählten Ampelstatus
- Sachlich, ohne Beschönigung

**Priorität (Hypothese)**: Mittel

**Offene Frage**: Wie viele Vorhaben umfasst die aktuelle Leistungsvereinbarung der VetMedUni?

---

### B-04: Abschnitt für Leistungsbericht entwerfen

> Als Berichtersteller will ich einen Textentwurf für einen thematischen Abschnitt des Leistungsberichts generieren, der mehrere Kennzahlen integriert.

**Begründung**: Der Leistungsbericht umfasst Bereiche wie "Forschung und Entwicklung", "Lehre", "gesellschaftliche Zielsetzungen" (WBV 2016 § 4). Jeder Abschnitt integriert narrative Beschreibung mit Kennzahlenverweisen.

**Akzeptanzkriterien**:
- Input: Themenbereich, relevante Kennzahlen, Highlights/Ereignisse
- Output: Strukturierter Fließtext (1-2 Seiten)
- Verweise auf konkrete Kennzahlen mit korrekten Werten
- Keine Erfindung von Fakten

**Priorität (Hypothese)**: Niedrig (komplexer, für späteren Sprint)

**Offene Frage**: Welche Informationsquellen neben UniData fließen in den Leistungsbericht ein?

---

## Nicht in Scope (Hypothese)

Folgende Funktionen sind vermutlich außerhalb des Promptotype-Umfangs:

- **Dateneingabe**: Der Promptotype liest UniData-Exporte, erstellt keine neuen Daten
- **BMBWF-Schnittstelle**: Keine direkte Übermittlung ans Ministerium
- **Rechnungsabschluss**: Finanzdaten sind nicht Teil von UniData
- **Vollständige Wissensbilanz**: Der Promptotype unterstützt Teilaufgaben, ersetzt nicht den gesamten Prozess