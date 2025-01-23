import random

def names_and_symbols():
    print("Player 1 - Please enter your name")
    first_name = input()
    print(f"Hi {first_name}, Please select a symbol - X or O. if you want me to choose for you press any another button")
    first_player_symbol=input()
    if first_player_symbol in ['x','o']:
        first_player_symbol=first_player_symbol.upper()
    second_player_symbol=''
    if first_player_symbol not in['X','O']:
        first_player_symbol=random.choice(['X', 'O'])
    if first_player_symbol == 'X':
        second_player_symbol='O'
    if first_player_symbol == 'O':
        second_player_symbol = 'X'
    print("Player 2 - Please enter your name")
    second_name = input()
    print(
        f"{first_name} your symbol is {first_player_symbol}, {second_name} your symbol is {second_player_symbol}. Good Luck!")
    print(f"\n{first_name} and {second_name}, please enter the name of the starting player")
    while True:
        try:
            starting_player=input()
            if starting_player not in (first_name,second_name):
                raise Exception("Invalid name")
            else:
                if starting_player == first_name:
                    return first_player_symbol, second_player_symbol
                else:
                    return second_player_symbol, first_player_symbol
        except Exception as e:
            print("\nInvalid name! Please enter one of the names exactly like you entered before ")



def create_board():
    board = [' ', ' ',' ',' ',' ',' ',' ',' ',' ']
    return board


def print_board(board,chosen_places):
    print("\nBoard:")
    for i,symbol in enumerate (board):
        if i in chosen_places:
            print(f"[{symbol}]", end=" ")
        else:
            print(f"[ ]", end=" ")
        if(i + 1) % 3 == 0:
            print()



def play_game():
    board = create_board()
    chosen_places = []
    symbols = names_and_symbols()
    turn = 0
    print_board(board, chosen_places)
    while len(chosen_places)<9:
        symbol = symbols[turn]
        try:
                choose_place = input("\nEnter the index of the place where you want to put your symbol (0-8)")
                choose_place = int(choose_place)
                if choose_place < 0 or choose_place > 8 or choose_place in chosen_places:
                    raise Exception("Invalid index")
                else:
                    board[choose_place]=symbol
                    chosen_places.append(choose_place)
                    print_board(board, chosen_places)
                    if is_win(board):
                        play_again()
                        break
                    turn = 1-turn
                    if len(chosen_places) == 9:
                        print("It is a draw!")
                        play_again()
        except Exception as e:
                print("\nOops! Invalid index. Try again...")




def is_win(board):
    winning_symbol=' '
    i=0
    win = False
    while i<=6:
        if board[i] == board[i+1] == board[i+2] and board[i] in ['X', 'O']:
            win = True
            winning_symbol = board[i]
        i=i+3

    i = 0
    while i<=2:
        if board[i] == board[i+3] == board[i+6] and board[i] in ['X', 'O']:
            win = True
            winning_symbol = board[i]
        i=i+1


    if board[0] == board[4] == board[8] and board[0] in ['X', 'O']:
        win = True
        winning_symbol = board[0]

    if board[2] == board[4] == board[6] and board[2] in ['X', 'O']:
        win = True
        winning_symbol = board[2]

    if win:
        print (f"Congratulation! {winning_symbol} is the Winner!")
        return True


def play_again():
    print("Do you want to play again? if so, please press 'Y'. Else, please press any another button.")
    additional_game = input()
    if additional_game in ['Y','y']:
        play_game()









if __name__ == '__main__':
    play_game()


