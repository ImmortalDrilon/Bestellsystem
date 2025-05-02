# Toni Pohnke, Drilon Gashi
from decimal import *

while(True):
    try:
        bewerbernummer = int(input("Wie lautet Ihre Bewerbernummer? "))
        break
    except:
        print("Bitte geben Sie eine gültige Bewerbernummer an!")

name = input("Wie lautet Ihr Name? ")

vorname = input("Wie lautet Ihr Vorname? ")

geschlecht = input("Als welches Geschlecht identifizieren Sie sich? ")

strasse = input("Wie lautet Ihre Adresse (Straße)? ")

while(True):
    try:
        hausnummer = int(input("Wie lautet Ihre Adresse (Hausnummer)? "))
        break
    except:
        print("Bitte geben Sie eine gültige Hausnummer an!")

while(True):
    try:
        postleitzahl = int(input("Wie lautet Ihre Adresse (Postleitzahl)? "))
        break
    except:
        print("Bitte geben Sie eine gültige Postleitzahl an!")

geburtsdatum = input("Wie lautet Ihr Geburtsdatum? ")

while(True):
    try:
        wunschgehalt = Decimal((input("Was für einen Gehalt wünschen Sie sich? ")))
        break
    except:
        print("Bitte geben Sie ein gültiges Wunschgehalt an!")

vorstrafen = input("Haben Sie Vorstrafen? (ja/nein) ")

# bei Eingabe von "ja" (case-insensitive) wird Vorstrafen auf True gesetzt,
# in allen anderen Fällen wird Vorstrafen auf False gesetzt
vorstrafen = (vorstrafen.lower() == "ja")

print(f"Bewerber: {bewerbernummer}, Name: {name}, Vorname: {vorname}, "
      f"Geschlecht: {geschlecht}, Straße: {strasse}, Hausnummer: {hausnummer}, "
      f"Postleitzahl: {postleitzahl}, Geburtsdatum: {geburtsdatum}, "
      f"Wunschgehalt: {wunschgehalt}, Vorstrafen: {vorstrafen}")


  