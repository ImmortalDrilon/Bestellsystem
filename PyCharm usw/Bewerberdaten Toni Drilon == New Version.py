# Drilon Gashi, Toni Pohnke


from decimal import *


while True:

    try:

        bewerbernummer = int(input("Wie lautet Ihre Bewerbernummer? "))

        break

    except ValueError:

        print("Bitte geben Sie eine gültige Bewerbernummer an!")


name = input("Wie lautet Ihr Name? ")

vorname = input("Wie lautet Ihr Vorname? ")

geschlecht = input("Wie lautet ihr Geschlecht? ") 

strasse = input("Wie lautet Ihre Adresse (Straße)? ")


while True:

    try:

        hausnummer = int(input("Wie lautet Ihre Adresse (Hausnummer)? "))

        break

    except ValueError:

        print("Bitte geben Sie eine gültige Hausnummer an!")


while True:

    try:

        postleitzahl = int(input("Wie lautet Ihre Adresse (Postleitzahl)? "))

        break

    except ValueError:

                print("Bitte geben Sie eine gültige Postleitzahl an!")


from datetime import datetime


# Geburtsdatum vom Benutzer abfragen

geburtsdatum = input("Wie lautet Ihr Geburtsdatum? (im Format TT.MM.JJJJ) ")


try:
 

    geburtsdatum = datetime.strptime(geburtsdatum, "%d.%m.%Y") # Konvertiert einen String das ein Datum/Uhrzeit enthält in einem Objekt. str = string

    # Heutiges Datum

    heute = datetime.now()

    if geburtsdatum > heute:
        print("Das Geburtsdatum liegt in der Zukunft! Bitte geben Sie ein gültiges Datum ein.")
    else: 
    # Berechnet das Alter in Jahren
        alter = heute.year - geburtsdatum.year
        

        if ( heute.month < geburtsdatum.month ):
            alter -=1

        if( heute.month == geburtsdatum.month and heute.day < geburtsdatum.day):
            alter -=1

        if (heute.month, heute.day) < (geburtsdatum.month, geburtsdatum.day):
            alter -= 1

    print(f"Sie sind {alter} Jahre alt.")

except ValueError:
    print("Bitte geben Sie das Datum im richtigen Format TT.MM.JJJJ ein.")
 
    # heute in alter in jahren sagt 

except ValueError:

    print("Das eingegebene Datum entspricht nicht dem Format TT.MM.JJJJ. Bitte versuchen Sie es erneut.")

# Aus Geb berechnen. Geburtsdatum bis zum jetzigen Tag ausrechnen.

while True:

    try:

        wunschgehalt = Decimal(input("Was für einen Gehalt wünschen Sie sich? "))
        if 32000 <= wunschgehalt <= 100000:
            break
        else: 
            print("Bitte geben Sie ein Wunschgehalt zwischen 32.000€ und 100.000€ ein.")
    except InvalidOperation:

        print("Bitte geben Sie ein gültiges Wunschgehalt an!")


vorstrafen = input("Haben Sie Vorstrafen? (ja/nein) ").lower() == "ja"


print(f"Bewerber: {bewerbernummer}, Name: {name}, Vorname: {vorname}, Alter: {alter} "

      f"Geschlecht: {geschlecht}, Straße: {strasse}, Hausnummer: {hausnummer}, "

      f"Postleitzahl: {postleitzahl}, Geburtsdatum: {geburtsdatum}, "

      f"Wunschgehalt: {wunschgehalt} €, Vorstrafen: {vorstrafen}, ") 
