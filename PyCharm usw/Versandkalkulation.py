# Toni Pohnke, Drilon Gashi

def calculate_total_price(preis, anzahl):
    return preis * anzahl

def calculate_brutto_price(netto_preis):
    return netto_preis * 1.19

#TODO: Eingabenüberprüfung
wein_name = input("Weinname: ")
preis_pro_flasche = float(input("Preis pro Flasche: ").replace(",", "."))
anzahl = int(input("Anzahl der bestellten Flaschen: "))

gesamtpreis_netto = calculate_total_price(preis_pro_flasche, anzahl)
gesamtpreis_brutto = calculate_brutto_price(gesamtpreis_netto)

anzahl_kartons = anzahl // 6

# schauen, ob Flaschen übrig bleiben
if anzahl % 6 == 0:
    anzahl_freie_plaetze = 0
else:
    # falls Flaschen übrig bleiben, + 1 Karton und freie Plätze berechnen
    anzahl_freie_plaetze = 6 - (anzahl % 6)
    anzahl_kartons += 1

print("\nIhre Angaben:")
print(f"Weinname: {wein_name}")
print(f"Preis pro Flasche: {preis_pro_flasche}")
print(f"Anzahl an Flaschen: {anzahl}")

print("---------------------------------")

print(f"Brutto Preis: {gesamtpreis_brutto:.2f}€")
print(f"Netto Preis: {gesamtpreis_netto:.2f}€")
print(f"Kartons benötigt: {anzahl_kartons}")
print(f"Freie Plätze im letzten Karton: {anzahl_freie_plaetze}")