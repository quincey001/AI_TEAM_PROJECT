from pulp import *
import time
from profile import profile

class CSP():

    def __init__(self, table):
        self.Sequence = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        # The Vals, Rows and Cols sequences all follow this form
        self.values = self.Sequence
        self.row = self.Sequence
        self.column = self.Sequence

        # The boxes list is created, with the row and column index of each square in each box
        self.Boxes =[]
        # The prob variable is created to contain the problem data        
        self.constraint = LpProblem("Sudoku Problem",LpMinimize)

        # The problem variables are created
        self.choices = LpVariable.dicts("Choice",(self.values,self.row,self.column),0,1,LpInteger)
        # A list of strings from "1" to "9" is created
        self.table = table


    def create_box_list(self):
        for i in range(3):
            for j in range(3):
                self.Boxes += [[(self.row[3*i+k], self.column[3*j+l]) for k in range(3) for l in range(3)]]

   # A constraint ensuring that only one value can be in each square is created 
    def one_value_in_cell(self):
        for r in self.row:
            for c in self.column:
                new_constraint = []
                for v in self.values:
                    new_constraint.append(self.choices[v][r][c])
                self.constraint += lpSum(new_constraint) == 1, ""
    
    def row_constraint(self):
        self.constraint += 0, "Arbitrary Objective Function"
        # The row, column and box constraints are added for each value
        for v in self.values:
            for r in self.row:
                new_constraint = []
                for c in self.column:
                    new_constraint.append(self.choices[v][r][c])
                self.constraint += lpSum(new_constraint) == 1,""
        
            for c in self.column:
                new_constraint = []
                for r in self.row:
                    new_constraint.append(self.choices[v][r][c])
                self.constraint += lpSum(new_constraint) == 1,""

            for b in self.Boxes:
                new_constraint = []
                for (r,c) in b:
                    new_constraint.append(self.choices[v][r][c])
                self.constraint += lpSum(new_constraint) == 1,""
  
    def extisting_constraint(self):
        for row in range(9):
            for col in range(9):
                if self.table[row][col] != 0:
                    self.constraint += self.choices[str(self.table[row][col])][str(row+1)][str(col+1)] == 1,""
    
    def writeLP(self):
        # The problem data is written to an .lp file
        self.constraint.writeLP("Sudoku.lp")

    @profile
    def solve(self):
        # The problem is solved using PuLP's choice of Solver
        start = time.time()
        self.create_box_list()
        self.one_value_in_cell()
        self.row_constraint()
        self.extisting_constraint()
        self.writeLP()
        self.constraint.solve()
        end = time.time()
        print(end - start)
        self.printStatus()
        self.print_and_write()

    def printStatus(self):
        #The status of the solution is printed to the screen
        print("Status:", LpStatus[self.constraint.status])

    def print_and_write(self):
        sudokuout = ""
        # The solution is written to the sudokuout.txt file 
        for r in self.row:
            for c in self.column:
                for v in self.values:
                    if value(self.choices[v][r][c])==1:             
                        sudokuout = sudokuout + (str(v) + " ")   
                        if c == "9":
                            sudokuout = sudokuout + '\n'                
        print(sudokuout)

