# LAB 2 - TIC-TAC-TOE
# HUMAN = X
# AI = O

board = [" "] * 9


def display_board():

    print("\n-------------")

    for i in range(0, 9, 3):

        print(
            "|", board[i],
            "|", board[i + 1],
            "|", board[i + 2], "|"
        )

        print("-------------")


def check_winner(player):

    winning_patterns = [

        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
      
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),

        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_patterns:

        if board[a] == board[b] == board[c] == player:
            return True

    return False


def empty_cells():

    return [
        i for i in range(9)
        if board[i] == " "
    ]


def count_winning_moves(player):

    count = 0

    for cell in empty_cells():

        board[cell] = player

        if check_winner(player):
            count += 1

        board[cell] = " "

    return count


def creates_double_threat(cell, player):

    board[cell] = player

    threats = count_winning_moves(player)

    board[cell] = " "

    return threats >= 2


def strategic_score(cell):

    score = 0


    # -----------------------------------
    # 1. IMMEDIATE WIN
    # -----------------------------------

    board[cell] = "O"

    if check_winner("O"):

        board[cell] = " "

        return 10000

    board[cell] = " "


    # -----------------------------------
    # 2. BLOCK OPPONENT
    # -----------------------------------

    board[cell] = "X"

    if check_winner("X"):

        score += 9000

    board[cell] = " "


    # -----------------------------------
    # 3. CREATE DOUBLE THREAT
    # -----------------------------------

    if creates_double_threat(cell, "O"):

        score += 5000


    # -----------------------------------
    # 4. PREVENT DOUBLE THREAT
    # -----------------------------------

    if creates_double_threat(cell, "X"):

        score += 4500


    # -----------------------------------
    # 5. CENTER PREFERENCE
    # -----------------------------------

    if cell == 4:

        score += 100


    # -----------------------------------
    # 6. CORNER PREFERENCE
    # -----------------------------------

    if cell in [0, 2, 6, 8]:

        score += 70


    # -----------------------------------
    # 7. EDGE PREFERENCE
    # -----------------------------------

    if cell in [1, 3, 5, 7]:

        score += 30


    # -----------------------------------
    # 8. OPPOSITE CORNER STRATEGY
    # -----------------------------------

    opposite = {
        0: 8,
        2: 6,
        6: 2,
        8: 0
    }

    for corner in opposite:

        if (
            board[corner] == "X"
            and cell == opposite[corner]
        ):

            score += 150


    # -----------------------------------
    # 9. FUTURE WINNING OPPORTUNITIES
    # -----------------------------------

    board[cell] = "O"

    future_opportunities = count_winning_moves("O")

    board[cell] = " "

    score += future_opportunities * 200


    return score


def choose_ai_move():

    best_score = -float("inf")
    best_move = None

    for cell in empty_cells():

        score = strategic_score(cell)

        if score > best_score:

            best_score = score
            best_move = cell

    return best_move


print("\n======================")
print(" TIC-TAC-TOE")
print("======================")

print("You = X")
print("AI = O")

# Initial board
display_board()

total_moves = 0
while True:

    # -----------------------------------
    # HUMAN MOVE
    # -----------------------------------

    try:
        move = int(input("\nEnter your move (0-8): "))

    except ValueError:

        print("Please enter a number between 0 and 8.")
        continue


    if move < 0 or move > 8:

        print("Invalid position.")
        continue


    if board[move] != " ":

        print("Position already occupied.")
        continue


    board[move] = "X"
    total_moves+=1

    # Show board after human move
    display_board()


    # Check human victory
    if check_winner("X"):

        print("\nYou win!")
        break


    # Check draw
    if not empty_cells():

        print("\nDraw!")
        break


    # -----------------------------------
    # AI MOVE
    # -----------------------------------

    ai_move = choose_ai_move()

    board[ai_move] = "O"
    total_moves+=1

    # Show board after AI move
    display_board()


    # Check AI victory
    if check_winner("O"):

        print("\nAI wins!")
        break


    # Check draw
    if not empty_cells():

        print("\nDraw!")
        break

print("\nTotal moves: ", total_moves)