# Galgenmännchen 

import random

def hangman():
    wort = random.choice(["Apfel", "Birne", "Orange"])
    buchstaben = set(wort)
    geratene_buchstaben = set()

    leben = 6

    while len(buchstaben) > 0 and leben > 0:
        print('Dein Wort:', ' '.join('_' if buchstabe not in geratene_buchstaben else buchstabe for buchstabe in wort))
        buchstabe = input('Rate einen Buchstaben: ').lower()

        if buchstabe in wort:
            geratene_buchstaben.add(buchstabe)
            print('Richtig!')
        else:
            leben -= 1
            print('Falsch!')

    if leben == 0:
        print('Du hast verloren. Das Wort war:', wort)
    else:
        print('Gratulation! Du hast gewonnen!')

hangman()