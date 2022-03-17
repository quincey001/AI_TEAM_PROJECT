from copy import deepcopy

class Sudoku():
 
    def __init__(self, table, rows=9, columns=9):
        self.table = table
        self.rows = rows
        self.columns = columns

    def inspectColumn(self, column, digit):

        for row in range(self.rows):
            if digit == self.table[row][column]:
                return False
        return True
  
    def inspectRow(self, row, digit):

        for column in range(self.columns):
            if digit == self.table[row][column]:
                return False
        return True
  
    def inspectSqaure(self, row, column, digit):

        squareColumnIndex = (column // 3) * 3
        squareRowIndex = (row // 3) * 3

        for row in range(squareRowIndex, squareRowIndex + 3):
            for column in range(squareColumnIndex, squareColumnIndex + 3):
                if self.table[row][column] == digit:
                    return False
        return True
  
    def getNextEmptyCell(self):
    
        for row in range(self.rows):
            for column in range(self.columns):
                if self.table[row][column] == 0:
                    return row, column

    def getSuccessors(self):

        row, column = self.getNextEmptyCell()
        newTables = []
        for number in range(1, 9+1):
            if self.inspectRow(row, number) and self.inspectColumn(column, number) and self.inspectSqaure(row, column, number):
                newTable = deepcopy(self.table)
                newTable[row][column] = number
                newTables.append(Sudoku(newTable))
        return newTables

    def isGoalState(self):

        for row in range(self.rows):
            for column in range(self.columns):
                if self.table[row][column] == 0:
                    return False
        return True

    def __str__(self):
        sudoku = ""
        for row in range(self.rows):
            for column in range(self.columns):
                sudoku += f"{self.table[row][column]} "
            sudoku += "\n"
        return sudoku



  
