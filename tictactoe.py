x_choice = "X"
o_choice = "O"
count = 2
board_ind = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def board():
    print("-" * 9)
    print("| " + board_ind[0], board_ind[1], board_ind[2] + " |")
    print("| " + board_ind[3], board_ind[4], board_ind[5] + " |")
    print("| " + board_ind[6], board_ind[7], board_ind[8] + " |")
    print("-" * 9)


def out_of_range(coordinate):  # Returns True if user coordinates
    for n in list(coordinate.split()):  # are out of the board range
        if n.isnumeric() is False:
            return False
        elif int(n) > 3:
            return True
    return False


coordinates = {"1 3": 0, "2 3": 1, "3 3": 2,
               "1 2": 3, "2 2": 4, "3 2": 5,
               "1 1": 6, "2 1": 7, "3 1": 8}

column1 = [0, 3, 6]  # Combos
column2 = [1, 4, 7]
column3 = [2, 5, 8]
row1 = [0, 1, 2]
row2 = [3, 4, 5]
row3 = [6, 7, 8]
obl1 = [0, 4, 8]
obl2 = [2, 4, 6]

wins = [column1, column2, column3,
        row1, row2, row3,
        obl1, obl2]


def winning(list1, list2=None):
    if list2 is None:
        list2 = wins
    for combo in list2:
        if all(numbers in list1 for numbers in combo):
            return True


def o_x_alternation():  # Selecting X or O to input in the board list
    global count
    if count % 2 == 0:
        board_ind[coordinates[user_coor]] = x_choice
        count += 1
    else:
        board_ind[coordinates[user_coor]] = o_choice
        count += 1


board()

while True:
    user_coor = input("Enter the coordinates: > ")

    if out_of_range(user_coor):  # user coordinates execution
        print("Coordinates should be from 1 to 3!")
    elif user_coor not in coordinates:
        print("You should enter numbers!")
    elif board_ind[coordinates[user_coor]] == (x_choice or o_choice):
        print("This cell is occupied! Choose another one!")
    elif board_ind[coordinates[user_coor]] == " ":
        o_x_alternation()

    board()

    o_indices = [i for i, x in enumerate(board_ind) if x == o_choice]
    x_indices = [i for i, x in enumerate(board_ind) if x == x_choice]

    if winning(o_indices):  # win, lose or draw execution
        print("O wins")
        break
    elif winning(x_indices):
        print("X wins")
        break
    elif " " not in board_ind:
        print("Draw")
        break
