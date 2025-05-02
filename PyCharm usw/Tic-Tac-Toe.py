def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
        # Druckt das aktuelle Spielfeld

def check_winner(board, player):
     # Zweck: Überprüft, ob der Spieler eine vollständige Zeile besetzt hat.  
    return any(all(s == player for s in row) for row in board) or \
           any(all(row[i] == player for row in board) for i in range(3)) or \
           all(board[i][2-i] == player for i in range(3))
           # Prüft ob der Spieler gewonnen hat. 

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0        # Zugzähler wurde auf 0 gesetzt. 
   

    while turn < 9: # Hauptschleife, < 9 Züge läuft das Spiel. Andernfalls 9 > => Spiel beendet. 
        print_board(board)
        row, col = map(int, input(f"Player {players[turn % 2]}, enter row and column (0, 1, 2): ").split())
        
        if board[row][col] == " ":
            board[row][col] = players[turn % 2]
            if check_winner(board, players[turn % 2]):
                print_board(board)
                print(f"Player {players[turn % 2]} wins!")
                return # Das Spiel endet. 
            turn += 1
        else:
            print("This spot is already taken. Try again.")
    
    print_board(board)
    print("It's a tie!")

     # Steuert das gesamte Tic-Tac-Toe-Spiel. 

tic_tac_toe()
