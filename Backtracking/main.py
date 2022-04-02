from Backtracking import backtrack
from Backtracking import solution

board = []


def get_board():
    with open('board.txt', 'r') as file:
        for line in file:
            row = [int(number.strip()) for number in line if number != '\n' and number != ' ']
            board.append(row)

    return board


def main():
    sudoku_board = get_board()

    if sudoku_board is not None:
        backtrack(sudoku_board)
        solution(sudoku_board)


if __name__ == '__main__':
    main()


# DONEE