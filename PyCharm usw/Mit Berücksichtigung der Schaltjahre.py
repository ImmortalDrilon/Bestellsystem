from datetime import datetime

# Geburtsdatum vom Benutzer abfragen
while True:
    try:
        tag = int(input("An welchem Tag sind Sie geboren? (TT) "))
        monat = int(input("In welchem Monat sind Sie geboren? (MM) "))
        jahr = int(input("In welchem Jahr sind Sie geboren? (JJJJ) "))
        geburtsdatum = datetime(jahr, monat, tag)
        break
    except ValueError:
        print("Bitte geben Sie ein gültiges Datum ein.")

# Geburtsdatum vom Benutzer abfragen
try:
    # Heutiges Datum
    heute = datetime.now()
    # Differenz in Tagen berechnen
    differenz = (heute - geburtsdatum).days
    print(f"Sie sind {differenz} Tage alt.")
except ValueError:
    print("Das eingegebene Datum entspricht nicht dem Format TT.MM.JJJJ. Bitte versuchen Sie es erneut.")

# Die datetime.strptime berücksichtigt automatisch die korrekte Anzahl von Tagen in jedem Jahr, einschließlich der zusätzlichen Tage in Schaltjahren. 


# Aktuelles Datum und Uhrzeit abrufen
heute = datetime.now()

# Ausgabe des aktuellen Datums und der aktuellen Uhrzeit
print(f"Das aktuelle Datum und die aktuelle Uhrzeit sind: {heute}")


