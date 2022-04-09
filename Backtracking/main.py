from Backtracking import backtrack
from Backtracking import solution
from datetime import datetime
import pandas as pd
from matplotlib import pyplot as plt


def get_board():
    board_list = []
    board = []
    with open('puzzles.txt', 'r') as file:
        for line in file:
            if line == "\n":
                board_list.append(board)
                board = []
            else:
                board.append(list(map(int, line.strip())))
        board_list.append(board)

    return board_list


# PLOT THE GRAPH
def plot_time(easy, medium, hard):
    plt.plot(range(1, 11), easy['time'], label="Easy Puzzle")
    plt.plot(range(1, 11), medium['time'], label="Medium Puzzle")
    plt.plot(range(1, 11), hard['time'], label="Hard Puzzle")

    plt.xlabel('puzzle number')
    plt.ylabel('Time took (s)')
    plt.title("Comparison of times taken to solve puzzles - Backtracking")
    plt.legend()

    plt.show()


def main():
    boards = get_board()

    # CREATE DATAFRAME
    time_taken = {
        'board_number': [],
        'time': [],
    }
    df = pd.DataFrame(time_taken)

    for i in range(len(boards)):
        board = []
        print("")
        print("STARTING SUDOKU BOARD NUMBER: ", i+1)
        for row in boards[i]:
            str1 = " ".join(str(number) for number in row)
            row2 = [int(number.strip()) for number in str1 if number != '\n' and number != ' ']
            print(row2)
            board.append(row2)

        # GET TTME TAKEN TO SOLVE EACH BOARD
        start_time = datetime.now()
        backtrack(board)
        solution(board)
        end_time = datetime.now()

        time_in_second = (end_time - start_time).total_seconds()  # CONVERT TIME TO ONLY SECOND
        print('Puzzle {} solved in {} second'.format(i+1, time_in_second))

        result = [i+1, time_in_second]
        df.loc[len(df)] = result

    df['board_number'] = df['board_number'].astype(int)  # REMOVE INTEGER FROM BOARD_NUMBER
    df.set_index('board_number', inplace=True)  # SET BOARD_NUMBER AS INDEX

    easy = df.iloc[:10]
    medium = df.iloc[10:20]
    hard = df.iloc[20:30]
    print(easy)
    print(medium)
    print(hard)
    print('Easy puzzles total taken: ', easy['time'].sum())
    print('Medium puzzles total taken: ', medium['time'].sum())
    print('Hard puzzles total taken: ', hard['time'].sum())
    
    plot_time(easy, medium, hard)


if __name__ == '__main__':
    main()


# DONE