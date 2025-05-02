# Irgendwas mit Tupel

#Verschiedene Index[0]   [1]      [2]
person = ("Drilon Gashi", 19 , "Essen")


personen = [
    ("Drilon Gashi", 1999999),
    ("Drilon Gashi", 1999999),
    ("Drilon Gashi", 1999999),
    ("Drilon Gashi", 1999999),
    ("Drilon Gashi", 1999999),
    ("Drilon Gashi", 1999999),
    ("Drilon Gashi", 1999999)
]

name = person [0]
alter = person [1] 
stadt = person [2]

print(name)
print(alter)
print(stadt)



# Globale Variablen

x = "Toll" 

def myfunc():
    print("Pyhton ist " +  x)

myfunc()



# Gerade Zahlen / ungerade Zahlen
zahl = int(input("Gib eine Zahl ein: "))

if zahl % 2 == 0:
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")


    
# Addition, Subtraktion, Multiplikation, Division
ergebnis = 5 + 3 * 2 - 4 / 2
print(ergebnis)  # Ausgabe: 9

# Potenzieren
quadrat = 4 ** 2
print(quadrat)  # Ausgabe: 16

# Modulo (Rest bei Division)
rest = 17 % 5
print(rest)  # Ausgabe: 2

radius = 5
pi = 3.14159
flaeche = pi * radius ** 2
umfang = 2 * pi * radius
print("Fläche:", flaeche)
print("Umfang:", umfang)