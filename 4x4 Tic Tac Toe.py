import random
from colorama import Fore, Style, init
init(autoreset=True)

# 4x4 grid tick tac toe game 
def print_board(board):
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.GREEN + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
    # Print the board in a 4x4 format
    print()
    print('  ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]) + ' | ' + colored(board[3]))
    print('  ' + '-' * 21)
    print('  ' + colored(board[4]) + ' | ' + colored(board[5]) + ' | ' + colored(board[6]) + ' | ' + colored(board[7]))
    print('  ' + '-' * 21)
    print('  ' + colored(board[8]) + ' | ' + colored(board[9]) + ' | ' + colored(board[10]) + ' | ' + colored(board[11]))
    print('  ' + '-' * 21)
    print('  ' + colored(board[12]) + ' | ' + colored(board[13]) + ' | ' + colored(board[14]) + ' | ' + colored(board[15]))
    print()

def player_choice():
    symbol = '' # Initialize symbol variable
    while symbol not in ['X', 'O']: # Loop until a valid symbol is chosen
        symbol = input(Fore.BLUE + "Do you want to be X or O? " + Style.RESET_ALL).upper()
    if symbol == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def player_move(board, symbol):
    move = -1
    while move not in range(1, 17) or not board[move - 1].isdigit():
        try:
            move = int(input("Enter your move (1-16): "))
            if move not in range(1, 17) or not board[move - 1].isdigit():
                print("Invalid move. Please try again.")
        except ValueError:
            print("Please enter a number between 1 and 16.")
    board[move - 1] = symbol

def ai_move(board, ai_symbol, player_symbol):
    for ai in range(16):
        if board[ai].isdigit():
            board_copy = board.copy()
            board_copy[ai] = ai_symbol
            if check_win(board_copy, ai_symbol):
                board[ai] = ai_symbol
                return
            
    for player in range(16):
        if board[player].isdigit():
            board_copy = board.copy()
            board_copy[player] = player_symbol
            if check_win(board_copy, player_symbol):
                board[player] = ai_symbol
                return
            
    possible_moves = [i for i in range(16) if board[i].isdigit()]
    move = random.choice(possible_moves)  # Randomly select a move
    board[move] = ai_symbol

def check_win(board, symbol):
    win_conditions = [
        
        (0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15), # Horizontal
        (0, 4, 8, 12), (1, 5, 9, 13), (2, 6, 10, 14), (3, 7, 11, 15), # Vertical
        (0, 5, 10, 15), (3, 6, 9, 12)                                 # Diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == board[condition[3]] == symbol:
            return True
    return False

def check_full(board):
    return all(not spot.isdigit() for spot in board)

def tic_tac_toe():
    print(Fore.CYAN + "Welcome to 4x4 Tic Tac Toe!" + Style.RESET_ALL)
    player_name =   input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)
    while True:
        board = [str(i + 1) for i in range(16)] # Initialize the board with numbers 1-16
        player_symbol, ai_symbol = player_choice()
        turn= 'Player'
        game_on = True

        while game_on:
            print_board(board)
            if turn == 'Player':
                player_move(board, player_symbol)
                if check_win(board, player_symbol):
                    print_board(board)
                    print(Fore.GREEN + f"{player_name} wins!" + Style.RESET_ALL)
                    game_on = False
                else:
                    if check_full(board):
                        print_board(board)
                        print(Fore.YELLOW + "It's a draw!" + Style.RESET_ALL)
                        break
                    else:
                        turn = 'AI'
            else:
                ai_move(board, ai_symbol, player_symbol)
                if check_win(board, ai_symbol):
                    print_board(board)
                    print(Fore.RED + "AI wins!" + Style.RESET_ALL)
                    game_on = False
                else:
                    if check_full(board):
                        print_board(board)
                        print(Fore.YELLOW + "It's a draw!" + Style.RESET_ALL)
                        break
                    else:
                        turn = 'Player'

        play_again = input(Fore.MAGENTA + "Do you want to play again? (yes/no): " + Style.RESET_ALL).lower()
        if play_again != 'yes':
            print(Fore.CYAN + "Thank you for playing!" + Style.RESET_ALL)
            break

if __name__ == "__main__": #main function 
    tic_tac_toe()