# PrimzahlAufgabe

def ist_primzahl(zahl): # Funktion definiert
  for i in range(2, zahl):
    print(f'{zahl} % {i} = {zahl / i}')
    if zahl % i == 0:
      return False
  return True 
      

# zahl_zu_pruefen = int(input("Gib eine Zahl ein: "))
zahl_zu_pruefen = 0

# Ruft die Funktion auf. 
if ist_primzahl(zahl_zu_pruefen):
  print(zahl_zu_pruefen, "ist eine Primzahl.")
else:
  print(zahl_zu_pruefen, "ist keine Primzahl.")

# Finde die 10001. Primzahl: Die 6. Primzahl ist 13.





def is_prime(zahl):
    if zahl <= 1: return False
    if zahl <= 3: return True
    if zahl % 2 == 0 or zahl % 3 == 0: return False
    i = 2
    while i*i <= zahl:
        if zahl % i == 0 or zahl % i+2 == 0: return False
        i += 1 # Überspringt alle Zahlen die 2 oder 3 teilbar sind. 
    return True

def find_nth_prime(zahl):
    count, num = 0, 2
    while count < zahl:
        if is_prime(num): count += 1
        num += 1
    return num - 1

if __name__ == '__main__':
  nth = 10001 #nth repräsentiert die Position der Primzahl die gesucht wird
  result = find_nth_prime(nth)    # nth = natürliche zahl, th = die ...te Zahl
  print(f"Die {nth}. Primzahl ist: {result}")
