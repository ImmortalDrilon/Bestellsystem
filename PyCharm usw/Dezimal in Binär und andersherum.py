def dezimal_in_binaer(zahl):
    binaer = ""
    while zahl > 0:
        rest = zahl % 2 
        binaer = str(rest) + binaer
        zahl = zahl // 2 
    return binaer


# 01001100 als Ergebnis. 128 64 32 16 8 4 2 1 
print(dezimal_in_binaer(77))



def binär_zu_dezimal(binärzahl):
  dezimalzahl = 0
  for zahl in binärzahl:
    # Hier wird mal 2 gerechnet, weil der bisherige Wert verdoppelt werden muss.
    dezimalzahl = dezimalzahl * 2 + int(zahl)
  return dezimalzahl

# Beispiel:
binärzahl = "11111111"
dezimalzahl = binär_zu_dezimal(binärzahl)
print(f"Die Dezimalzahl zu {binärzahl} ist: {dezimalzahl}")



def dezimal_in_binaer_mit_bin(x):
    binaer = bin(x)
    # Entferne die ersten beiden Zeichen '0b'
    binaer = binaer[2:]
    return binaer

# Beispielaufruf:
print(dezimal_in_binaer_mit_bin(255))  # Ausgabe: 1101


