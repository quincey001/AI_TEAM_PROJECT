from pulp import *

class CSP():

    def __init__(self, table):
        self.Sequence = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        # The Vals, Rows and Cols sequences all follow this form
        self.Vals = self.Sequence
        self.Rows = self.Sequence
        self.Cols = self.Sequence

        # The boxes list is created, with the row and column index of each square in each box
        self.Boxes =[]
        # The prob variable is created to contain the problem data        
        self.prob = LpProblem("Sudoku Problem",LpMinimize)

        # The problem variables are created
        self.choices = LpVariable.dicts("Choice",(self.Vals,self.Rows,self.Cols),0,1,LpInteger)
        # A list of strings from "1" to "9" is created

        self.table = table


    def create_box_list(self):
        for i in range(3):
            for j in range(3):
                self.Boxes += [[(self.Rows[3*i+k], self.Cols[3*j+l]) for k in range(3) for l in range(3)]]

   # A constraint ensuring that only one value can be in each square is created 
    def one_value_in_cell(self):
        for r in self.Rows:
            for c in self.Cols:
                self.prob += lpSum([self.choices[v][r][c] for v in self.Vals]) == 1, ""
    
    def row_constraint(self):
        self.prob += 0, "Arbitrary Objective Function"
        # The row, column and box constraints are added for each value
        for v in self.Vals:
            for r in self.Rows:
                self.prob += lpSum([self.choices[v][r][c] for c in self.Cols]) == 1,""
        
            for c in self.Cols:
                self.prob += lpSum([self.choices[v][r][c] for r in self.Rows]) == 1,""

            for b in self.Boxes:
                self.prob += lpSum([self.choices[v][r][c] for (r,c) in b]) == 1,""
  
    def extisting_constraint(self):
        for row in range(9):
            for col in range(9):
                if self.table[row][col] != 0:
                    self.prob += self.choices[str(self.table[row][col])][str(row+1)][str(col+1)] == 1,""
    
    def writeLP(self):
        # The problem data is written to an .lp file
        self.prob.writeLP("Sudoku.lp")

    def solve(self):
        # The problem is solved using PuLP's choice of Solver
        self.create_box_list()
        self.one_value_in_cell()
        self.row_constraint()
        self.extisting_constraint()
        self.writeLP()
        self.prob.solve()
        self.printStatus()
        self.print_and_write()
        #print(self.__str__())

    def printStatus(self):
        #The status of the solution is printed to the screen
        print("Status:", LpStatus[self.prob.status])

    def print_and_write(self):
        sudokuout = ""
        # The solution is written to the sudokuout.txt file 
        for r in self.Rows:
            for c in self.Cols:
                for v in self.Vals:
                    if value(self.choices[v][r][c])==1:             
                        sudokuout = sudokuout + (str(v) + " ")   
                        if c == "9":
                            sudokuout = sudokuout + '\n'                
        print(sudokuout)

