from keras.models import load_model
import matplotlib.pyplot as plt
from profile import profile
import numpy as np
import time

filepath = "best_weights.hdf5"

model = load_model(filepath)


def normalize(a):
    return (a / 9) - .5


def denormalize(a):
    return (a + .5) * 9


def fill_sudoku_with_trained_model(problem):
    feat = problem

    while True:
        out = model.predict(feat.reshape((1, 9, 9, 1)))
        out = out.squeeze()

        pred = np.argmax(out, axis=1).reshape((9, 9)) + 1
        prob = np.around(np.max(out, axis=1).reshape((9, 9)), 2)

        feat = denormalize(feat).reshape((9, 9))
        mask = (feat == 0)

        if mask.sum() == 0:
            break

        prob_new = prob * mask
        ind = np.argmax(prob_new)
        x, y = (ind // 9), (ind % 9)
        val = pred[x][y]
        feat[x][y] = val
        feat = normalize(feat)
    return pred


def test_accuracy(feats, labels):
    correct = 0
    for i, feat in enumerate(feats):
        pred = fill_sudoku_with_trained_model(feat)
        true = labels[i].reshape((9, 9)) + 1
        if abs(true - pred).sum() == 0:
            correct += 1
    print(correct / feats.shape[0])


def solve_sudoku(game):
    game = game.replace('\n', '')
    game = game.replace(' ', '')
    game = np.array([int(j) for j in game]).reshape((9, 9, 1))
    game = normalize(game)
    game = fill_sudoku_with_trained_model(game)
    return game


@profile
def analyse_time(puzzle_file):
    init_time = time.time()
    simple_puzzles = open(puzzle_file, 'r').readlines()
    time_for_each_puzzle = []
    for puzzle in simple_puzzles:
        print(f"solving {puzzle}")
        st_time = time.time()
        solution = solve_sudoku(puzzle)
        ed_time = time.time()
        exc_time = ed_time - st_time
        time_for_each_puzzle.append(exc_time)
        print("exec time : ", exc_time)
        print(f"solved\n{solution}\n")
    end_time = time.time()
    exec_time = end_time - init_time
    print("Time took to solve {} - {}s".format(len(simple_puzzles), exec_time))
    return time_for_each_puzzle, exec_time


exc_time_foreach_simple_puzzle, total_exc_time_simple = analyse_time('sudoku_dataset/simple_puzzle.txt')
exc_time_foreach_medium_puzzle, total_exc_time_medium = analyse_time('sudoku_dataset/medium_puzzle.txt')
exc_time_foreach_hard_puzzle, total_exc_time_hard = analyse_time('sudoku_dataset/hard_puzzle.txt')

print(exc_time_foreach_simple_puzzle, total_exc_time_simple)
print(exc_time_foreach_medium_puzzle, total_exc_time_medium)
print(exc_time_foreach_hard_puzzle, total_exc_time_hard)

fig, (ax1, ax2) = plt.subplots(1,2)
index_time = list(range(0,len(exc_time_foreach_simple_puzzle)))
ax1.plot(index_time, exc_time_foreach_simple_puzzle, label="Easy Puzzle")
ax1.plot(index_time, exc_time_foreach_medium_puzzle, label="Medium Puzzle")
ax1.plot(index_time, exc_time_foreach_hard_puzzle, label="Hard Puzzle")
ax1.set_xlabel('puzzle number')
ax1.set_ylabel('Time took (s)')
ax1.set_xticks(np.arange(len(index_time)))
ax1.set_title("Comparison of times for puzzles of various difficulty levels.")
ax1.legend()
# plt.show()

all_puzzle_time_took = {'Easy': total_exc_time_simple,'Medium': total_exc_time_medium, 'Hard':total_exc_time_hard}
puzzle_type = list(all_puzzle_time_took.keys())
values = list(all_puzzle_time_took.values())
# fig = plt.figure(figsize=(10, 5))
# creating the bar plot
ax2.bar(puzzle_type, values, color='maroon',
        width=0.4)
ax2.set_xlabel("Puzzle Categories")
ax2.set_ylabel("Time took in Second(s)")
ax2.set_title("Time took to solve 10 each categories of the puzzles")
ax2.legend()

plt.show()