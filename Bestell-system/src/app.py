# Definiere die Funktion app(), die ausgeführt werden soll, wenn die Datei als Python-Skript ausgeführt wird.
import datetime  # Importiert das Modul zur Arbeit mit Datum und Uhrzeit
import sqlite3  # Importiert das Modul zur Arbeit mit SQLite-Datenbanken
from src.artikel import read_all_artikel, read_artikel_by_name  # Importiert Funktionen zum Lesen von
# Artikeln aus der Datenbank
from src.bestellung import read_all_bestellungen, create_bestellung, update_bestellung, read_bestellung
# Importiert Funktionen zum Arbeiten mit Bestellungen
from src.bestellung_artikel import add_bestellung_artikel, read_all_bestellung_artikel, update_bestellung_artikel
# Importiert Funktionen zum Arbeiten mit den Artikeln einer Bestellung

__CONN: sqlite3.Connection  # Definiert eine Variable für die Datenbankverbindung

def zeige_menu(artikel_preise):
    """
    Zeigt das Menü mit den zur Verfügung stehenden Produkten für die Bestellung an.

    :param artikel_preise: Enthält Artikelname und Preis
    :return: None
    """
    print("Willkommen! Das ist unser Menü!\n")
    print("Menü:")
    # Iteriert über alle Artikel und deren Preise und zeigt sie an
    for index, (artikel, preis) in enumerate(artikel_preise.items(), start=1): # 'enumerate' fügt jedem Artikel eine
        # Nummer hinzu, die bei 1 beginnt, 'index' ist diese Nummer (1, 2, 3 usw.), und 'artikel' ist der Name des
        # Artikels, während 'preis' der Preis ist.
        gerundeter_preis = round(preis, 2)  # Preis auf zwei Dezimalstellen runden
        print(f"{index}. {artikel} - {gerundeter_preis} Euro")  # Anzeige des Artikelnamens und Preises

def aufgabe_bestellungen(_CONN, artikel_preise):
    """
    Erfasst Bestellungen basierend auf den verfügbaren Artikeln und deren Preisen.

    :param _CONN: Die Datenbankverbindung
    :param artikel_preise: Artikelname und Preis
    :return: Artikelnamen und bestellte Mengen
    """
    bestellungs_id = create_bestellung(_CONN, "Drilon")  # Erstellt eine neue Bestellung in der Datenbank
    bestellungen = {}  # Dictionary zum Speichern der bestellten Artikel und deren Mengen
    while True:
        input_artikel = input("Bitte wählen Sie einen Artikel aus dem Menü (oder 'fertig'): ").strip()
        if input_artikel.lower() == 'fertig':
            break  # Beendet die Eingabe, wenn der Benutzer 'fertig' eingibt
        if input_artikel not in artikel_preise:
            print("Artikel nicht gefunden. Bitte versuchen Sie es erneut.")
            continue  # Wiederholt die Schleife, wenn der Artikel nicht existiert
        while True:
            try:
                artikel_menge = int(input(f"Wie viele {input_artikel} möchten Sie bestellen? ").strip())
                # Benutzer wird gefragt, wie viele Stücke von dem gewählten Artikel er bestellen möchte.
                if artikel_menge <= 0: # 'input' ist eine Eingabeaufforderung.
                    print("Die Menge muss positiv sein. Bitte geben Sie eine gültige Menge ein.")
                    continue  # Fordert den Benutzer auf, eine gültige Menge einzugeben
                break  # Verlassen der Schleife, wenn die Eingabe gültig ist
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")  # Fehlerbehandlung für ungültige Eingaben

        # Artikel-ID aus der Datenbank abrufen
        artikel_id = read_artikel_by_name(_CONN, input_artikel)[0]  # Ruft die ID des ausgewählten Artikels ab
        # Artikel zur Bestellung in der Datenbank hinzufügen
        add_bestellung_artikel(_CONN, bestellungs_id, artikel_id, artikel_menge)  # Fügt den Artikel mit der Menge zur Bestellung hinzu
        # Menge aktualisieren
        bestellungen[input_artikel] = artikel_menge  # Speichert die bestellte Menge für den Artikel

    return bestellungen  # Gibt die gesammelten Bestellungen zurück

def berechne_bruttopreis(netto_preis):
    """
    Berechnet den Bruttopreis basierend auf dem Nettopreis.

    :param netto_preis: Nettopreis des Artikels
    :return: Bruttopreis des Artikels
    """
    return round(netto_preis * 1.19, 2)  # Berechnung mit 19% Mehrwertsteuer, Rundung nach 2 Kommastellen

def berechne_gesamtpreis(bestellungen, artikel_preise):
    """
    Berechnet den Gesamt-Netto- und -Bruttopreis basierend auf den bestellten Artikeln und deren Preisen.

    :param bestellungen: Enthält die bestellten Artikel und die Mengen.
    :param artikel_preise: Enthält die Artikelnamen und Preise.
    :return: tuple, enthält den Gesamt-Netto- und -Bruttopreis
    """
    # Berechnet den Gesamt-Netto-Preis durch Summierung der Einzelpreise
    gesamt_netto = sum(artikel_preise[artikel] * menge for artikel, menge in bestellungen.items())
    gesamt_netto = wende_rabatt_an(gesamt_netto)  # Wendet den Rabatt auf den Gesamtpreis an
    gesamt_brutto = berechne_bruttopreis(gesamt_netto)  # Berechnung des Gesamt-Bruttopreises
    return round(gesamt_netto, 2), gesamt_brutto  # Gibt beide Preise zurück

def neue_bestellung_hinzufuegen(_CONN, bestellungen):
    """
    Erstellt eine neue Bestellung mit einem Zeitstempel, den bestellten Artikeln,
    dem Nettopreis und dem Bruttopreis und fügt diese zur Bestellhistorie hinzu.

    :param _CONN: Die Datenbankverbindung
    :param bestellungen: Enthält bestellte Artikel und deren Menge.
    :return: None
    """
    timestamp = datetime.datetime.now().isoformat()  # Aktuellen Zeitstempel erstellen
    # Bestellung in der Datenbank erstellen und die ID erhalten
    bestellungs_id = create_bestellung(_CONN, timestamp)  # Erstellt die Bestellung mit dem Zeitstempel
    for artikel, menge in bestellungen.items():  # Iteriert über alle bestellten Artikel und deren Mengen
        artikel_id = read_artikel_by_name(_CONN, artikel)[0]  # Artikel-ID abrufen
        # Artikel zur Bestellung in der Datenbank hinzufügen
        add_bestellung_artikel(_CONN, bestellungs_id, artikel_id, menge)  # Fügt jeden Artikel zur Bestellung hinzu

def bestellhistorie_anzeigen(_CONN):
    """
    Gibt die Bestellhistorie auf der Konsole aus. Wenn keine Bestellungen vorhanden sind,
    wird eine entsprechende Nachricht angezeigt.

    :param _CONN: Die Datenbankverbindung
    :return: None
    """
    print("\nBestellhistorie:")
    bestellungen = read_all_bestellungen(_CONN)  # Alle Bestellungen aus der Datenbank abrufen
    if not bestellungen:
        print("Keine Bestellungen gefunden.")  # Ausgabe, wenn keine Bestellungen existieren
        return

    # Diese Schleife geht durch jede Bestellung in der Liste 'bestellungen'.
    for bestellung in bestellungen:
        # 'bestellung' enthält Informationen über die Bestellung.
        # Hier wird die Bestell-ID und der Zeitstempel extrahiert (das Datum und die Uhrzeit der Bestellung).
        bestellungs_id, timestamp = bestellung[:2]  # Bestell-ID und Zeitstempel extrahieren

        # Wir rufen die Artikel ab, die zu dieser Bestellung gehören, indem wir die Bestell-ID verwenden.
        artikel_daten = read_all_bestellung_artikel(_CONN, bestellungs_id)  # Artikel zur Bestellung abrufen

        # Hier geben wir die Bestell-ID und das Datum der Bestellung aus.
        print(f"Bestellung ID {bestellungs_id} vom {timestamp}")  # Ausgabe der Bestell-ID und des Zeitstempels

        # Diese innere Schleife geht durch die Artikel, die in dieser Bestellung enthalten sind.
        for menge, artikel_name, preis, mwst in artikel_daten:
            # Hier geben wir die Menge, den Namen des Artikels und den Preis aus.
            print(f"{menge}x {artikel_name} (Preis: {preis} Euro)")  # Ausgabe der Artikel und deren Preise
        print("----------------------------------------")

def wende_rabatt_an(preis):
    """
    Überprüft, ob der Preis über einer definierten Schwelle liegt und wendet einen Rabatt an.

    :param preis: Der ursprüngliche Preis
    :return: Preis nach Anwendung des Rabatts
    """
    rabatt_schwelle = 20.00  # Preisgrenze für Rabatt
    rabatt_prozentsatz = 0.10  # Rabattprozentsatz
    if preis > rabatt_schwelle:  # Überprüfen, ob der Preis die Schwelle überschreitet
        rabatt = preis * rabatt_prozentsatz  # Rabatt berechnen
        preis -= rabatt  # Rabatt vom Preis abziehen
        print(f"Ein Rabatt von {round(rabatt, 2)} Euro wurde angewendet.\n")  # Rabatt anzeigen
    return preis  # Preis nach Anwendung des Rabatts zurückgeben

def bestellung_zusammenfassen(_CONN, bestell_id):
    """
    Zeigt die Zusammenfassung einer Bestellung an.

    :param _CONN: Die Datenbankverbindung
    :param bestell_id: Die ID der Bestellung, die zusammengefasst werden soll
    :return: None
    """
    bestellung = read_bestellung(_CONN, bestell_id)  # Bestellung wird aus der Datenbank abgerufen
    if not bestellung:
        print("Bestellung nicht gefunden.")  # Fehlermeldung, wenn die Bestellung nicht gefunden wurde
        return

    artikel_daten = read_all_bestellung_artikel(_CONN, bestell_id)  # Alle Artikel der Bestellung werden abgerufen

    print(f"Zusammenfassung der Bestellung ID {bestell_id} vom {bestellung[1]}:\n")  # Ausgabe der Bestell-ID und des Zeitstempels
    # f-string ist ein Formatierter String, um Variablen in einen Text einzufügen.
    # '\n' erzeugt einen Zeilenumbruch, sodass der folgende Text auf einer neuen Zeile beginnt.

    gesamt_netto = 0  # Initialisiert den Gesamt-Netto-Preis
    for menge, artikel_name, preis, _ in artikel_daten:  # Iteriert über die Artikel der Bestellung
        gesamtpreis_artikel = menge * preis  # Gesamtpreis für jeden Artikel berechnen
        gesamt_netto += gesamtpreis_artikel  # Gesamtpreis summieren
        print(f"{menge}x {artikel_name} (Einzelpreis: {preis} Euro, Gesamtpreis: {gesamtpreis_artikel} Euro)")  # Ausgabe der Artikel

    gesamt_netto = round(gesamt_netto, 2)  # Gesamtpreis auf zwei Dezimalstellen runden
    gesamt_netto_mit_rabatt = wende_rabatt_an(gesamt_netto)  # Rabatt anwenden
    gesamt_brutto = berechne_bruttopreis(gesamt_netto_mit_rabatt)  # Brutto-Gesamtpreis berechnen

    print("\nGesamtsumme ohne Rabatt: {:.2f} Euro".format(gesamt_netto))  # Gesamtsumme ohne Rabatt anzeigen
    if gesamt_netto != gesamt_netto_mit_rabatt:
        print("Gesamtsumme nach Rabatt: {:.2f} Euro".format(gesamt_netto_mit_rabatt))  # Gesamtsumme nach Rabatt anzeigen, falls Rabatt angewendet wurde
    print("Endpreis inklusive Steuern: {:.2f} Euro".format(gesamt_brutto))  # Endpreis inklusive Steuern anzeigen
    # {:.2f} bedeutet, dass die Zahl als Fließkommazahl mit zwei Dezimalstellen formatiert wird.
    print("----------------------------------------")

def bestellung_anpassen(_CONN, artikel_preise):
    """
    Zeigt die aktuelle Bestellhistorie an und ermöglicht es dem Benutzer, eine
    bestehende Bestellung anzupassen.
    """
    bestellhistorie_anzeigen(_CONN)  # Zeige die Bestellhistorie an
    bestellungen = read_all_bestellungen(_CONN)  # Hole alle Bestellungen aus der Datenbank
    if not bestellungen:
        return  # Wenn keine Bestellungen vorhanden sind, wird die Funktion beendet

    while True:
        try:
            # Benutzer zur Eingabe der Bestell-ID auffordern
            auswahl = int(input("Bitte wählen Sie die Bestell-ID, die Sie anpassen möchten: ").strip())
            # Ein 'strip' entfernt alle führenden und nachfolgenden Leerzeichen (oder andere angegebene Zeichen) von einem String.
            # Zur Info: String speichert Text, int speichert Ganzzahlen.
            if auswahl not in [bestellung[0] for bestellung in bestellungen]: # Diese Bedingung überprüft,
                # ob die eingegebene Auswahl (Bestell-ID) nicht in einer Liste von bestehenden Bestell-IDs ist.
                print("Ungültige Auswahl. Bitte wählen Sie eine gültige Bestell-ID.")
                continue  # Wiederholen, wenn die Auswahl ungültig ist
            break
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")  # Fehlermeldung bei ungültiger Eingabe

    bestellung = read_bestellung(_CONN, auswahl)  # Bestellinformationen abrufen
    if not bestellung:
        print("Bestellung nicht gefunden.")  # Fehlermeldung, wenn Bestellung nicht gefunden wurde
        return

    print(f"\nSie bearbeiten die Bestellung vom {bestellung[1]}:")  # Zugriff auf das zweite Element der tuple (Zeitstempel)
    # Ein tuple ist ein Datentyp, die eine geordnete Sammlung von Elementen oder 'Dingen' enthält.
    aktuelle_artikel = read_all_bestellung_artikel(_CONN, auswahl)  # Artikel zur Bestellung abrufen
    bestellungen_dict = {artikel[1]: artikel[0] for artikel in aktuelle_artikel}  # Artikel in ein Dictionary umwandeln

    while True:
        # Zeige aktuelle Bestellartikel an
        for artikel, menge in bestellungen_dict.items():
            print(f"{menge}x {artikel}")

        artikelname = input(
            "\nGeben Sie den Namen des Artikels ein, den Sie ändern oder hinzufügen möchten (oder 'fertig', um zu speichern): ").strip()
        if artikelname.lower() == 'fertig':
            break  # Beendet die Eingabe, wenn der Benutzer 'fertig' eingibt

        artikel_id = read_artikel_by_name(_CONN, artikelname)[0]  # Artikel-ID wird abgerufen

        while True:
            try:
                menge = int(input(
                    f"Neue Menge für {artikelname} (aktueller Bestand: {bestellungen_dict.get(artikelname, 0)}): "))  # Fordert neue Menge an
                if menge < 0:
                    print("Die Menge darf nicht negativ sein. Bitte geben Sie eine gültige Menge ein.")
                    continue  # Schleife erneut durchlaufen, wenn die Menge negativ ist
                break  # Schleife verlassen, wenn die Eingabe gültig ist
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")  # Fehlermeldung bei ungültiger Eingabe

        if menge == 0:
            delete_bestellung_artikel(_CONN, auswahl, artikel_id)  # Artikel wird entfernt, wenn die Menge 0 ist
            del bestellungen_dict[artikelname]  # Entfernt den Artikel aus dem Dictionary
            print(f"{artikelname} wurde entfernt.")
        else:
            bestellungen_dict[artikelname] = menge  # Aktualisiert die Menge im Dictionary
            update_bestellung_artikel(_CONN, auswahl, artikel_id, menge)  # Die Menge wird aktualisiert
            print(f"{menge} Stück von {artikelname} wurden hinzugefügt oder aktualisiert.")

    print("Bestellung erfolgreich aktualisiert.")  # Bestätigung der Aktualisierung

    # Nach der Anpassung die Zusammenfassung der Bestellung anzeigen
    bestellung_zusammenfassen(_CONN, auswahl)

def hauptmenu(_CONN):
    """
    Hauptmenü der Anwendung, das verschiedene Optionen für den Benutzer bereitstellt.
    """
    artikel_preise = {artikel[1]: artikel[2] for artikel in read_all_artikel(_CONN)}  # Artikel und Preise abrufen

    while True:
        print("\nHauptmenü:")
        print("1. Neue Bestellung aufgeben")
        print("2. Bestehende Bestellungen anzeigen")
        print("3. Bestehende Bestellung anpassen")
        print("4. Zusammenfassung einer Bestellung anzeigen")
        print("5. Beenden")

        auswahl = input("Bitte wählen Sie eine Option (1-5): ").strip()

        if auswahl == '1':
            zeige_menu(artikel_preise)  # Menü der Artikel wird angezeigt
            neue_bestellungen = aufgabe_bestellungen(_CONN, artikel_preise)  # Aufgeben einer neuen Bestellung
            if neue_bestellungen:  # Überprüfen, ob neue Bestellungen vorhanden sind
                gesamt_netto, gesamt_brutto = berechne_gesamtpreis(neue_bestellungen, artikel_preise)  # Berechnung der Gesamtpreise
                neue_bestellung_hinzufuegen(_CONN, neue_bestellungen)  # Neue Bestellung in der Datenbank speichern

        elif auswahl == '2':
            bestellhistorie_anzeigen(_CONN)  # Anzeige der Bestellhistorie

        elif auswahl == '3':
            bestellung_anpassen(_CONN, artikel_preise)  # Anpassung einer bestehenden Bestellung

        elif auswahl == '4':
            try:
                # Zusammenfassung einer Bestellung anzeigen
                bestell_id = int(input(
                    "Bitte geben Sie die Bestell-ID ein, für die Sie eine Zusammenfassung anzeigen möchten: ").strip())
                bestellung_zusammenfassen(_CONN, bestell_id)  # Zeigt die Zusammenfassung der angegebenen Bestellung
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")  # Fehlermeldung bei ungültiger Eingabe

        elif auswahl == '5':
            print("Programm wird beendet.")  # Programm beenden
            break  # Schleife beenden

        else:
            print(
                "Ungültige Auswahl. Bitte wählen Sie eine Option zwischen 1 und 5.")  # Fehlerausgabe bei ungültiger Eingabe

# Dieser Block wird nur ausgeführt, wenn das Skript direkt ausgeführt wird.
if __name__ == '__main__':
    _CONN = sqlite3.connect("../db.sqlite3")  # Verbindung zur Datenbank wird hergestellt
    hauptmenu(_CONN)  # Hauptmenü wird aufgerufen
    _CONN.close()  # Datenbankverbindung wird geschlossen
