"""
chromosome is a possible solution for sudoku puzzle
"""
import itertools

import numpy
import random
from Population import Population
class Chromosome(object):
    """
      A candidate solutions to the Sudoku puzzle.
      it has every elements and fitness score
    """
    def __init__(self):

        self.values = numpy.zeros((9, 9), dtype=int)
        self.fitness = None
        return
    def sumDuplcateColumn(self):
        # put duplicate column number in 1X9 columnCount
        columnCount = numpy.zeros(9, dtype=int)
        columnSum = 0
        # traverse each column
        for i in range(0, 9):
            nonzero = 0
            # traverse each element in this column
            for j in range(0, 9):
                # record every elements in [1X9] columnCount, and mark their times
                columnCount[self.values[j][i] - 1] += 1
            # if the element in this column is not 0, them get 1 mark
            for k in range(0, 9):
                if columnCount[k] != 0:
                    nonzero += 1
            # if there is no zero in this column, nonzero is 1
            nonzero = nonzero / 9
            columnSum = (columnSum + nonzero)
            columnCount = numpy.zeros(9, dtype=int)
        columnSum = columnSum / 9
        return columnSum

    def sumDuplicateBlock(self):
        # put duplicate block number in blockCount
        blockCount = numpy.zeros(9, dtype=int)
        blockSum = 0
        # traverse every elements in block
        for row, column in itertools.product(range(0, 9, 3), range(0, 9, 3)):
            blockCount[self.values[row][column] - 1] += 1
            blockCount[self.values[row][column + 1] - 1] += 1
            blockCount[self.values[row][column + 2] - 1] += 1

            blockCount[self.values[row + 1][column] - 1] += 1
            blockCount[self.values[row + 1][column + 1] - 1] += 1
            blockCount[self.values[row + 1][column + 2] - 1] += 1

            blockCount[self.values[row + 2][column] - 1] += 1
            blockCount[self.values[row + 2][column + 1] - 1] += 1
            blockCount[self.values[row + 2][column + 2] - 1] += 1
            nonzero = 0
            for k in range(0, 9):
                if blockCount[k] != 0:
                    nonzero += 1
            nonzero = nonzero / 9
            blockSum = blockSum + nonzero
            blockCount = numpy.zeros(9, dtype=int)
        blockSum = blockSum / 9
        return blockSum

    def getFitnessScore(self):
        """ a method evalute the chromosome """
        columnSum = self.sumDuplcateColumn()
        blockSum = self.sumDuplicateBlock()
        if (int(columnSum) == 1 and int(blockSum) == 1):
            fitness = 1.0
        else:
            fitness = columnSum * blockSum
        self.fitness = fitness
        return

    def mutate(self, mutationRate, given):
        """ swap two values in a row """

        r = random.uniform(0, 1.1)
        while (r > 1):  # make sure the random number is less than 1
            r = random.uniform(0, 1.1)
        mute_success = False
        # if random number < mutate rate 0.5, then mutate
        if (r < mutationRate):
            while (not mute_success):
                #generate random row1[0-8]
                row1 = random.randint(0, 8)
                row2 = row1
                fromColumn = random.randint(0, 8)
                toColumn = random.randint(0, 8)
                while (fromColumn == toColumn):
                    fromColumn = random.randint(0, 8)
                    toColumn = random.randint(0, 8)
                if (given.values[row1][fromColumn] == 0 and given.values[row1][toColumn] == 0):
                    # if the column is not duplicate and row is not duplicate, block is not duplicate, then swap
                    if (not Population.isColumnDuplicate(self,toColumn, given.values[row1][fromColumn], given)
                            and not Population.isColumnDuplicate(self,fromColumn, given.values[row2][toColumn], given)
                            and not Population.isBlockDuplicate(self,row2, toColumn, given.values[row1][fromColumn], given)
                            and not Population.isBlockDuplicate(self,row1, fromColumn, given.values[row2][toColumn]), given):
                        # Swap two values.
                        temp = self.values[row2][toColumn]
                        self.values[row2][toColumn] = self.values[row1][fromColumn]
                        self.values[row1][fromColumn] = temp
                        mute_success = True

        return mute_success


