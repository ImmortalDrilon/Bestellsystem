import random

def number_guessing_game():
    random_number = random.randint(1, 100)
    trys = 0
    highscore = 1000  # Setze einen hohen Anfangswert für den Highscore

    while trys < 10:
        guess = int(input("Guess a number between 1 and 100: "))
        trys += 1

        if guess < random_number:
            print("The number is bigger.")
        elif guess > random_number:
            print("The number is lower.")
        else:
            print(f"Congratulations! You guessed the number in {trys} trys!!")
            if trys < highscore:
                highscore = trys
            break

    print(f"Du hast leider alle Versuche verbraucht. Die Zahl war: {random_number}")
    print(f"Dein Highscore an trys ist: {highscore}")

number_guessing_game()
#Todo Nach 3 Versuchen spiel beenden. => Eigentlich done
# Neues Programm mit Zufallszahlen von 1-100 oder 1-1000. => Mögliche Funktionen: Highscore, Mehrere Schwierigkeitsstufen oder auch Mathematische Rätseln. => In progress