count_fizzbuzz = 0
count_fizz = 0
count_buzz = 0

# Geht durch die Schleife 
for i in range(1, 51):
    # Fragt ob die Zahl durch 3 oder durch 5 Teilbar ist. 
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        count_fizzbuzz += 1
        # elif = else if
    elif i % 3 == 0:        
        print("Fizz")
        count_fizz +=1
    elif i % 5 == 0:
        print("Buzz")
        count_buzz +=1
    else:
        print(i)

print("Häufigkeiten:") 
print("FizzBuzz:", count_fizzbuzz)
print("Fizz:", count_fizz)
print("Buzz:", count_buzz)


# Berechne die Summe aller Zahlen von 1 bis 1000, die durch 3 oder 5 restlos teilbar sind.


summe = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        summe += i
print("Die Summe aller Zahlen von 1 bis 1000, die durch 3 oder 5 teilbar sind:", summe)
print(sum([i for i in range(1,1000) if i % 3 == 0 or i % 5 == 0]))
print(sum(filter(lambda i: i % 3 == 0 or i % 5 == 0, range(1,1000))))