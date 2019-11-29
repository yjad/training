game = [[' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']]
coordinates = [[1,2,3],
        [4,5,6],
        [7,8,9]]


def check_tic_tac_toe_winner(player):
    p = player_symbol(player)
      # check rows
    for i in range(3):
        if game[i][0] == p and game[i][1] == p and game[i][2] == p:
            print (f'player # {player} Won, row {i+1} ***')
            return 0
      # check columns
    for i in range(3):
        if game[0][i] == p and game[1][i] == p and game[2][i] == p:
            print (f'player # {player} Won, col {i+1} ***')
            return 0
        # \ diagonal
    if game[0][0] == p and game[1][1] == p and game[2][2] == p:
            print (f'player # {player} Won, \\ diagonal ***')
            return 0
      # / diagonal

    if game[0][2] == p and game[1][1] == p and game[2][0] == p:
        print (f'player # {player} Won, / diagonal ***')
        return 0
    return -1   # no winner yet

def print_game():
    for j in range(3):
        print(game[j])


def player_symbol(player):
    if player == 1:
        return 'X'
    else:
        return 'O'


def get_player_input(player: int):

    while True:
        x = input(f"Player {player}, '{player_symbol(player)}': enter 1 to 9 or q tp quit: ")
        if x == 'q':
            return -1
        elif x < '1' or x > '9':
            print("Invalid input")
            continue
        else:
            i,j = get_coordinate(int(x))
            if game[i][j] == ' ':
                game[i][j] = player_symbol(player)
                return 0
            if game[i][j] == player_symbol(player):
                print (f' Invalid move, you')
                print_game()
                continue
            else:
                print(f' Invalid move, your opponent')
                print_game()
                continue


def get_coordinate(one_coord:int):
    for i in range(3):
        for j in range(3):
            if coordinates[i][j] == one_coord:
                return i,j


# -----------------------------------------------------
#  Execute
# -----------------------------------------------------

while True:
    print_game()
    status = get_player_input(1)
    if status == -1: # quit
        break
    elif check_tic_tac_toe_winner(1) == 0:     # player 1 wins
        break

    print_game()
    get_player_input(2)

    if status == -1:  # quit
        break
    elif check_tic_tac_toe_winner(2) == 0:     # player 2 wins
        break

