# sudoku_board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
#                 [5, 2, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 8, 7, 0, 0, 0, 0, 3, 1],
#                 [0, 0, 3, 0, 1, 0, 0, 8, 0],
#                 [9, 0, 0, 8, 6, 3, 0, 0, 5],
#                 [0, 5, 0, 0, 9, 0, 6, 0, 0],
#                 [1, 3, 0, 0, 0, 0, 2, 5, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 7, 4],
#                 [0, 0, 5, 2, 0, 6, 3, 0, 0]]


def backtrack(sudoku_board):
    # IF NO EMPTY POSITION FOUND, IT INDICATES THAT THE SOLUTION IS FOUND
    row_column = empty_positions(sudoku_board)
    if not row_column:
        return True
    else:
        row, column = row_column

    # CHECK IF THE NUMBER (1-9) FITS IN THE ROW, COLUMN AND SUB-GRID
    for i in range(1, 10):
        if check_number(sudoku_board, i, (row, column)):
            sudoku_board[row][column] = i

            # HERE I CALL backtrack FUNCTION RECURSIVELY,
            if backtrack(sudoku_board):
                return True

            # IF backtrack IS NOT TRUE, BACKTRACK AND RESET THE LAST ELEMENT WHICH WAS ADDED
            sudoku_board[row][column] = 0

    return False


# TO FIND EMPTY SQUARE AND RETURN THE POSITION OF THAT
def empty_positions(sudoku_board):
    for i in range(len(sudoku_board)):
        for j in range(len(sudoku_board[0])):
            if sudoku_board[i][j] == 0:
                return i, j  # RETURN THE ROW AND COLUMN POSITION OF THE SQUARE IF IT HAS A VALUE OF 0

    return None


# TO SEPARATE THE BOARD INTO DIFFERENT SECTIONS
def solution(sudoku_board):
    for i in range(len(sudoku_board)):
        # DRAW A HORIZONTAL LINE AFTER EVERY 3 ROWS
        if i % 3 == 0 and i != 0:
            # PRINT THIS LINE WHEN i IS DIVISIBLE BY 3
            print("--------------------------")

        # DRAW A PIPE SYMBOL AFTER EVERY 3 COLUMN (WHEN j IS DIVISIBLE BY 3)
        for j in range(len(sudoku_board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            # IF WE ARE AT THE LAST POSITION, WE ADD GO TO THE NEXT LINE
            if j == 8:
                print(sudoku_board[i][j])
            else:
                print(str(sudoku_board[i][j]) + " ", end="")


def check_number(sudoku_board, number, square_position):
    # CHECK IF A NUMBER (1-9) FITS IN THE ROW
    # IF ANY SQUARE IN THE ROW HAS BEEN INSERTED WITH THE NUMBER, THEN WE IGNORE IT
    for i in range(len(sudoku_board[0])):
        if sudoku_board[square_position[0]][i] == number and square_position[1] != i:
            return False

    # CHECK IF A NUMBER (1-9) FITS IN THE COLUMN
    # IF ANY SQUARE IN THE COLUMN HAS BEEN INSERTED WITH THE NUMBER, THEN WE IGNORE IT
    for i in range(len(sudoku_board)):
        if sudoku_board[i][square_position[1]] == number and square_position[0] != i:
            return False

    # I CHECK IN WHICH SUB-GRID I AM IN USING FLOOR DIVISION
    sub_grid_x = square_position[1] // 3
    sub_grid_y = square_position[0] // 3

    # CHECK IF THE NUMBER (1-9) FITS IN THE SUB-GRID
    for i in range(sub_grid_y * 3, sub_grid_y * 3 + 3):
        for j in range(sub_grid_x * 3, sub_grid_x * 3 + 3):
            if sudoku_board[i][j] == number and (i, j) != square_position:
                return False

    # RETURN TRUE IF THE NUMBER FITS ROW, COLUMN AND SUB-GRID
    return True


# backtrack(sudoku_board)
# solution(sudoku_board)

# DONEE
