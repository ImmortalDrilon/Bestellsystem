
# Aufgabe: Bestellmanagement-System für ein Café oder Restaurant

In dieser Aufgabe soll ein Bestellmanagement-System für ein Café oder Restaurant entwickelt werden. Das Programm soll die Verwaltung von Bestellungen ermöglichen, Artikel und ihre Preise speichern, Rabatte und Steuern berechnen und eine detaillierte Zusammenfassung der Bestellungen anzeigen.

## Anforderungen:

### 1. Menüsystem:
- Erstelle ein Menü mit verschiedenen Artikeln (z.B. Kaffee, Tee, Snacks) und deren Preise.
- Das Menü sollte als Dictionary oder Liste von Tuples gespeichert werden, wobei der Artikelname der Schlüssel ist und der Preis der Wert.
- Beispiel: 
    ```python
    menu = {
      'Kaffee': 2.5,
      'Tee': 2.0,
      'Kuchen': 3.0
    }
    ```

### 2. Bestellverwaltung:
- Implementiere eine Funktion, die es ermöglicht, eine Bestellung aufzugeben.
- Der Benutzer soll Artikel aus dem Menü auswählen und die Menge angeben können.
- Speichere jede Bestellung in einer Liste von Dictionaries, wobei jedes Dictionary die bestellten Artikel und die dazugehörigen Mengen enthält.
- Beispiel:
    ```python
    bestellungen = [
        {'Kaffee': 2, 'Tee': 1},
        {'Kuchen': 3}
    ]
    ```

### 3. Preisberechnung:
- Erstelle eine Funktion, die den Gesamtpreis einer Bestellung basierend auf den Preisen im Menü und den bestellten Mengen berechnet.
- Implementiere zusätzlich eine Möglichkeit, Rabatte anzuwenden (z.B. 10% Rabatt für Bestellungen über 20 Euro).
- Berechne die Mehrwertsteuer (19%) auf den Gesamtpreis.

### 4. Zusammenfassung der Bestellung:
- Entwickle eine Funktion, die eine detaillierte Zusammenfassung einer Bestellung ausgibt:
    - Auflistung der bestellten Artikel und Mengen
    - Einzelpreise der Artikel
    - Gesamtsumme vor und nach Anwendung des Rabatts
    - Endpreis inklusive Steuern

### 5. Fehlerbehandlung:
- Implementiere eine einfache Fehlerbehandlung für folgende Fälle:
    - Auswahl eines nicht existierenden Artikels
    - Eingabe einer ungültigen Menge (z.B. negative Zahlen oder nicht numerische Eingaben)

### 6. Hauptmenü erstellen
- Erstelle ein Hauptmenü zur Auswahl der Aktionen:
  - Neue Bestellung aufgeben
  - Bestehende Bestellungen anzeigen
  - Bestehende Bestellung anpassen
  - Beenden

### 7. Bestellhistorie
- Füge die Möglichkeit hinzu, mehrere Bestellungen zu verwalten und eine Bestellhistorie zu führen.
- Die Bestellhistorie sollte als Liste von Tuples oder Dictionaries gespeichert werden, wobei jede Bestellung mit einem Zeitstempel versehen ist.

### 8. Statistiken (zurückgestellt)
- Implementiere eine Funktion, die Statistiken zu den Bestellungen liefert:
    - Häufig bestellte Artikel
    - Durchschnittlicher Bestellwert
    - Gesamtumsatz des Cafés / Restaurants

### 9. Kundenverwaltung (zurückgestellt)
- Erweitere das System, um auch Kunden zu verwalten. Jeder Kunde kann mehrere Bestellungen haben.
- Speichere Kunden in einem Dictionary, wobei der Kunde als Schlüssel und seine Bestellungen als Liste von Dictionaries gespeichert werden.

---

## Beispielausgabe:

```
Willkommen im Bestellsystem!
1. Bestellen
2. Bestellungen anzeigen
3. Bestellung anpassen
4. Statistiken anzeigen
5. Beenden

Bitte wählen Sie eine Option: 1

Menü:
1. Kaffee - 2.50 Euro
2. Tee - 2.00 Euro
3. Kuchen - 3.00 Euro

Was möchten Sie bestellen? Kaffee
Wie viele möchten Sie bestellen? 2

Möchten Sie noch etwas bestellen? (ja/nein) ja

Was möchten Sie bestellen? Kuchen
Wie viele möchten Sie bestellen? 1

Möchten Sie noch etwas bestellen? (ja/nein) nein

Ihre Bestellung:
Kaffee x 2: 5.00 Euro
Kuchen x 1: 3.00 Euro

Gesamtpreis vor Rabatt: 8.00 Euro
Endpreis nach Steuern: 9.52 Euro
```

---

## Lernziele:

1. **Grundlegende Programmierkonzepte:**
    - Variablen, Funktionen und Kontrollstrukturen (if/else)

2. **Handhabung verschiedener Datentypen:**
    - Zahlen (float/int) für Preise und Mengen
    - Strings für Artikelbezeichnungen
    - Listen, Dictionaries und Tuples für Bestellungen und Menüverwaltung

3. **Schleifen:**
    - For- und While-Schleifen zur Menüanzeige und Bestellungserfassung

4. **Fehlerbehandlung:**
    - Umgang mit ungültigen Benutzereingaben (try/except)

5. **Strukturierung eines komplexeren Programms:**
    - Durch die verschiedenen Anforderungen wird die Aufgabe in kleinere, handhabbare Teile unterteilt, die eine Strukturierung und Modularisierung des Codes erfordern.
