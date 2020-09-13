import itertools

def win():

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # horizontally
    for row in game:
        print(row)
        if all_same(row):
            print(f"player {row[0]} is the Winner!!! horizontally (-)")
            return True


     # vertically

    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"player {check[0]} is the Winner!!! vertically (|)")
            return True

    # diagonal win
    # left to right

    diag = []
    for ix in range(len(game)):
        diag.append(game[ix][ix])

    if all_same(diag):
        print(f"player {diag[0]} is the Winner!!! diagonally (\\)")
        return True

    # right to left

    diag = []
    for col, row in zip(reversed(range(len(game))), range(len(game))):
        diag.append(game[row][col])

    if all_same(diag):
        print(f"player {diag[0]} is the Winner!!! diagonally (/)")
        return True
    return False






def game_board(game_map, player = 0, row = 0 , column = 0, just_display = False):
    try:
        if game_map[row][column] != 0:
            print("This place is already taken. Please choose next")
            return game_map, False
        # print("   0, 1, 2")
        print("   "+"  ".join([str(i) for i in range(3)]))  #same as print("   0  1  2"))

        if not just_display:
            game_map[row][column] = player

        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True

       
    except IndexError as e:
        print("Error: did you enter either 0 1 or 2? ", e)
        return game_map, False
    except Exception as e:
        print("Error: Something went wrong ", e)
        return game_map, False



# game_board(game, player= 1, row= 1, column= 2)
# game_board(game, just_display= True)

play = True
player = [1,2]
while play:
    # game = [[0, 0, 0],
    #         [0, 0, 0],
    #         [0, 0, 0]]

    game_size = int(input("Enter the size of the game \n"))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f" Current Player :{current_player} ")
        played = False

        while not played:
            col_choice = int(input("Enter the column you want to select (0, 1, 2) "))
            row_choice = int(input("Enter the row you want to select (0, 1, 2)"))
            game, played = game_board(game, current_player, row_choice, col_choice)

        if win():
            game_won = True
            again = input("Game Over! \n Would you like to play again? (y/n)")
            if again.lower() == "y":
                print("New Game")
            elif again.lower() == "n":
                print("Bye!")
                play = False
            else:
                print("Not a valid answer. Bye!")
                play = False





# #diagonal win
# #left to right
#
# diag = [}
# for ix in range(len(game)):
#         diag.append(game[ix][ix])
# if diag.count(diag[0]) == len(diag) and diag != 0:
#         print(f"player {diag[0]} is the Winner!!! diagonally (\)")
#
# #right to left
#
# diag = []
# for col, row in zip(reversed(range(len(game))), range(len(game))):
#         diag.append(game[row][col])
# if diag.count(diag[0]) == len(diag) and diag != 0:
#         print(f"player {diag[0]} is the Winner!!! diagonally (/)")


# vertical win

# def verWin():
#     x = -1
#     for run in range(3):
#
#         check = []
#         x += 1
#         # print(x)
#         for row in game:
#             check.append(row[x])
#         if check.count(check[0]) == len(check) and check != 0:
#             print("Winner")
#
# verWin()
#



# # horizontal win
# def horiWin():
#     for row in game:
#         print(row)
#         if row.count(row[0]) == len(row) and row[0] != 0:
#             print("Winner!!!")
# horiWin()













