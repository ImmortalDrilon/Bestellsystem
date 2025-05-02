# adventure

def adventure(): 
    print("Du befindest dich in einem düsteren Raum.")
    while True:
        aktion = input("Was möchtest du tun? (weitergehen und dinge suchen, hier bleiben und auf Hilfe warten...): ")
        if aktion == "gehen":
            print("Du gehst durch die Tür und findest einen Schatz")
            break
        elif aktion == "suchen":
            print("Du hast hier nichts gefunden. Du musst weitergehen...")
        else:
            print("Unbekannter Befehl.")

adventure()