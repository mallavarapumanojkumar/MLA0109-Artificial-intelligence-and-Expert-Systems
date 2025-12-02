import random

board = [" "] * 9

def print_board():
    print("\n")
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print("\n")

def check_winner(p):
    win = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),
           (1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(board[a] == board[b] == board[c] == p for a,b,c in win)

def human_move():
    while True:
        move = int(input("Enter position (1-9): ")) - 1
        if 0 <= move < 9 and board[move] == " ":
            board[move] = "X"
            break
        else:
            print("Invalid move, try again.")

def ai_move():
    free = [i for i in range(9) if board[i] == " "]
    move = random.choice(free)
    board[move] = "O"

def is_full():
    return " " not in board

print("Tic Tac Toe Game (You = X, AI = O)")
print_board()

while True:
    human_move()
    print_board()
    if check_winner("X"):
        print("You win!")
        break
    if is_full():
        print("It's a draw!")
        break

    ai_move()
    print("AI played:")
    print_board()
    if check_winner("O"):
        print("AI wins!")
        break
    if is_full():
        print("It's a draw!")
        break
