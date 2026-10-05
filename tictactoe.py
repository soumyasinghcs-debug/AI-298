import random

board = [' '] * 9

def show_board():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()

def win(player):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] == player:
            return True
    return False

print("Tic-Tac-Toe")
print("You are X. Computer is O.")

while True:
    show_board()

    # Player's turn
    position = int(input("Choose a position (0-8): "))

    if board[position] != ' ':
        print("That position is already taken!")
        continue

    board[position] = 'X'

    if win('X'):
        show_board()
        print("You win!")
        break

    if ' ' not in board:
        show_board()
        print("It's a draw!")
        break

    # Computer's turn
    empty = [i for i in range(9) if board[i] == ' ']
    computer_move = random.choice(empty)
    board[computer_move] = 'O'

    print("Computer chose:", computer_move)

    if win('O'):
        show_board()
        print("Computer wins!")
        break