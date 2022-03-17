import os
from search import DFS, BFS
from sudoku import Sudoku
import sys

def read_data(filename):
  try:
    abs_path = os.path.abspath(f"samples/{filename}")
    with open(abs_path, "r") as f:
      contents = f.readlines()
    table = []
    for row in contents:
      new_row = [int(number.strip()) for number in row if number != '\n' and number != ' ']
      table.append(new_row)
    return table

  except FileNotFoundError:
     return None

def main():
  filename = sys.argv[2]
  filename += ".txt"
  data = read_data(filename)

  if data is not None:

    sudoku = Sudoku(data)

    if (sys.argv[1]) == 'dfs':
      print("Depth First Search")
      dfs = DFS(sudoku)
      dfs.search()

    elif (sys.argv[1]) == 'bfs':
      print("Breadth First Search")
      bfs = BFS(sudoku)
      bfs.search()

    else:
      print(f"Agent {sys.argv[1]} does not exist.")
      print("try:\n  - dfs\n  - bfs")

  else:
    print("This file does not exit. Please enter another file name")

if __name__ == '__main__':
  main()