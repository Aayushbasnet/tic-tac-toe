import itertools

def win(current_game):

    def checker(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
#     horizontally
    for row in current_game:
        print(row)
        if checker(row):
            print(f"Winner!!! Player {row[0]} Horizontally (-) ")
            return True
# vertically
    for ver in range(len(current_game)):
        col = []
        for row in current_game:
            col.append(row[ver])
        if checker(col):
            print(f"Winner!!!Player {col[0]} Vertically (|) ")
            return True

#diagonally
    #left to right
    diag = []
    for ix in range(len(current_game)):
        diag.append(current_game[ix][ix])

    if checker(diag):
        print(f"Winner!!! Player {diag[0]} diagonally (\\)")
        return True

    #right to left
    diag = []
    for col, row in zip(reversed(range(len(current_game))), range(len(current_game))):
        diag.append(current_game[row][col])
    if checker(diag):
        print(f"Winner!!! Player {diag[0]} diagonally (/)")
        return True

    return False


def game_board(game_map, player = 0, row = 0, column = 0, just_display = False):
    try:
        if game_map[row][column] != 0:
            print("This place is occupied")
            return game_map, False

        print("   "+"  ".join([str(i) for i in range(game_size)]))
        if not just_display:
            game_map[row][column] = player

        for count, row in enumerate(game_map):
            print(count, row)
        return game_map,True
    except IndexError as e:
        print("Error: Choose between 0 1 or 2", e)
        return game_map, False
    except Exception as e:
        print("Error: Something went wrong", e)
        return game_map, False






play = True
players = [1,2]
while play:
    game_size = int(input("Enter the size of the game \n"))
    game = [[0 for i in range(game_size)]for i in range(game_size)]
    game, _ = game_board(game, just_display=True)
    player_sel = itertools.cycle(players)
    game_won = False
    while not game_won:
        current_player = next(player_sel)
        print(f"Current Player: {current_player}")
        played = False
        while not played:

            row_sel = int(input("Enter the row (0 1 2) "))
            col_sel = int(input("Enter the col (0 1 2) "))

            game, played = game_board(game, current_player, row_sel, col_sel)
        if win(game):
                game_won = True
                play = False




