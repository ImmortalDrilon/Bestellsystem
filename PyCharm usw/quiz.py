quiz = {
    "Frage 1: Wie lautet die Hauptstadt von Deutschland?": {
        "Antwortmöglichkeiten": ["A: Bonn", "B: München", "C: Berlin"],
        "RichtigeAntwort": "C"
    },
    "Frage 2: Wie lange dauerte der 30-Jährige Krieg?": {
        "Antwortmöglichkeiten": ["A: 50 Jahre", "B: 30 Jahre", "C: 20 Jahre"],
        "RichtigeAntwort": "B"
    },
    "Frage 3: Wann war der zweite Weltkrieg?": {
        "Antwortmöglichkeiten": ["A: 1910-1922", "B: 1939-1945", "C: 2019-2024" ],
        "RichtigeAntwort": "B"
    }
}

punkte = 0

for frage, details in quiz.items():
    print(frage)
    for i, antwort in enumerate(details["Antwortmöglichkeiten"]): 
        print(f"{i+1}. {antwort}")
    
    user_antwort = input("Deine Antwort: ").upper()
    
    if user_antwort == details["RichtigeAntwort"]:
        print("Richtig!")
        punkte += 1
    else:
        print("Leider falsch.")

print(f"Du hast {punkte} von {len(quiz)} Punkten erreicht.")  # len gibt im Quiz nur die Anzahl der Fragen zurück. 