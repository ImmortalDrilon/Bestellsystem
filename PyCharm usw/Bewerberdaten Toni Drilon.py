# Toni Pohnke, Drilon Gashi

# Decimal statt float, da float nicht akkurat ist
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

hausnummer = input("Wie lautet Ihre Adresse (Hausnummer)? ")

postleitzahl = input("Wie lautet Ihre Adresse (Postleitzahl)? ")

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

print(f"Bewerber: {bewerbernummer}, " \
f"Name: {name}, Vorname: {vorname}, " \
f"Geschlecht: {geschlecht}, " \
f"Straße: {strasse}, " \
f"Hausnummer: {hausnummer}, " \
f"Postleitzahl: {postleitzahl}, " \
f"Geburtsdatum: {geburtsdatum}, " \
f"Wunschgehalt: {wunschgehalt}, " \
f"Vorstrafen: {vorstrafen}")