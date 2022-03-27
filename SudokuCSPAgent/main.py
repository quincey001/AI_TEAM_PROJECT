import os
import sys
from cspAgent import CSP

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
  filename = sys.argv[1]
  filename += ".txt"
  data = read_data(filename)

  if data is not None:

    csp = CSP(data)
    csp.solve()
 
  else:
    print("This file does not exit. Please enter another file name")

if __name__ == '__main__':
  main()