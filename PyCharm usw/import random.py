import random

def number_guessing_game():
    highscores = {}  # Ein leeres Wörterbuch für die Highscores

    try:
        # Versuche, die Highscores aus einer Datei zu laden
        with open('highscores.txt', 'r') as file:
            for line in file:
                # strip entfernt Leerzeichen, Tabulatoren oder Zeilenumbrüche am Anfang und Ende der Zeile

                name, score = line.strip().split(':') # split teilt die Zeile an jedem ':' und gibt eine Liste zurück
                try:
                    highscores[name] = int(score)  # Konvertiert den Score in eine Ganzzahl
                except ValueError:
                    print(f"Ungültiger Eintrag in der Highscore-Datei: {line.strip()}")
    except FileNotFoundError:
        pass  # Die Datei existiert noch nicht

    name = input("Wie heißt du? ") 
    random_number = random.randint(1, 50) # Generiert eine zufällige Zahl zwischen 1 und 50
    tries = 0 # Zählt die Anzahl der Versuche 

    while tries < 10:
        guess = int(input("Rate eine Zahl zwischen 1 und 50: "))
        tries += 1 # Erhöht die Anzahl der Versuche

        if guess < random_number:
            print("Die Zahl ist größer.")  # Gibt aus, dass die gesuchte Zahl größer ist
        elif guess > random_number:
            print("Die Zahl ist kleiner.")  # Gibt aus, dass die gesuchte Zahl kleiner ist 
        else:
            print(f"Herzlichen Glückwunsch, {name}! Du hast die Zahl in {tries} Versuchen erraten!!")
            highscores[name] = tries # Speichert den Score des Spielers 
            break

    # Speichere die Highscores in einer Datei
    with open('highscores.txt', 'w') as file: # w = write
        for name, score in highscores.items(): # Tupel
            file.write(f"{name}:{score}\n")

    # Zeige die Top 5 Highscores an
    print("\nTop 5 Highscores:")
    # lambda sagt nach welchem Wert jedes Element sortiert werden soll. Lambda legt das Sortierkriterium fest.
    for i, (name, score) in enumerate(sorted(highscores.items(), key=lambda x: x[1])[:5], start=1): # i = index 
        print(f"{i}. {name}: {score} Versuche")

number_guessing_game()