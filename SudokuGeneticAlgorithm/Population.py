import itertools
import numpy
import random
import Chromosome
NumDigits = 9
class Population(object):
    """
       generate a collection of chromosomes as a population, which are possible solutions for sudoku
    """
    def __init__(self):
        self.chromosomes = []
        return

    def isRowDuplicate(self, row, value, given):
        """ Check whether there is a duplicate of a fixed/given value in a row. """
        for column in range(0, NumDigits):
            if (given.values[row][column] == value):
                return True
        return False

    def isColumnDuplicate(self, column, value, given):
        """ Check whether there is a duplicate of a fixed/given value in a column. """
        for row in range(0, NumDigits):
            if (given.values[row][column] == value):
                return True
        return False

    def isBlockDuplicate(self, row, column, value, given):
        """ Check whether there is a duplicate of a fixed/given value in a 3 x 3 block. """
        i = 3 * (int(row / 3))
        j = 3 * (int(column / 3))

        if ((given.values[i][j] == value)
                or (given.values[i][j + 1] == value)
                or (given.values[i][j + 2] == value)
                or (given.values[i + 1][j] == value)
                or (given.values[i + 1][j + 1] == value)
                or (given.values[i + 1][j + 2] == value)
                or (given.values[i + 2][j] == value)
                or (given.values[i + 2][j + 1] == value)
                or (given.values[i + 2][j + 2] == value)):
            return True
        else:
            return False

    def generatePopulation(self, chromosomeNumber, given):
        self.chromosomes = []
        avElement = Chromosome.Chromosome()
        avElement.values = [[[] for j in range(0, NumDigits)] for i in range(0, NumDigits)]

        for row, column in itertools.product(range(0,9),range(0,9)):
            for value in range(1, 10):
                """
                get every possible elements in one [] element in 9X9 [] avElement
                if the element in given puzzle is 0, then put every possible elements in this position
                if the element in given puzzle is not 0, put the give value in one [] element with the position[row, column]
                """
                if ((given.values[row][column] == 0)
                    and not (self.isColumnDuplicate(column, value,given)
                            or self.isBlockDuplicate(row, column, value, given)
                            or self.isRowDuplicate(row, value, given)
                            )):
                    #put possible values in []
                    avElement.values[row][column].append(value)
                elif (given.values[row][column] != 0):
                    #put the given value in []
                    avElement.values[row][column].append(given.values[row][column])
                    break
        #generate chromosomeNumber chromosomes for this generation as a population
        for polulation in range(0, chromosomeNumber):
            g = Chromosome.Chromosome()
            for i in range(0, NumDigits):
                #generate a new row[9 * 0]
                row = numpy.zeros(NumDigits, dtype=int)
                for j in range(0, NumDigits):
                    #if the given value is not 0, put it in row[j]
                    if (given.values[i][j] != 0):
                        row[j] = given.values[i][j]
                    # if the given values is 0, randomly put the possible value to row[j]
                    elif (given.values[i][j] == 0):
                        row[j] = avElement.values[i][j][random.randint(0, len(avElement.values[i][j]) - 1)]

                # if the possible values and given values in row are not 9, then put possible values in the row again
                while (len(list(set(row))) != NumDigits):
                    for j in range(0, NumDigits):
                        if (given.values[i][j] == 0):
                            row[j] = avElement.values[i][j][random.randint(0, len(avElement.values[i][j]) - 1)]
                # put 9 rows into generation g
                g.values[i] = row
            self.chromosomes.append(g)
        # Compute the fitness of all chromosomes in the population.
        self.updateFitness()
        print("Population Generation is complete.")
        return

    def updateFitness(self):
        """ get update fitness score for every chromosome"""
        for candidate in self.chromosomes:
            candidate.getFitnessScore()
        return

    def sort(self):
        """ sort the chromosomes' fitness score. """
        for i in range(len(self.chromosomes) - 1):
            max = i
            for j in range(i + 1, len(self.chromosomes)):
                if self.chromosomes[max].fitness < self.chromosomes[j].fitness:
                    max = j
            temp = self.chromosomes[i]
            self.chromosomes[i] = self.chromosomes[max]
            self.chromosomes[max] = temp
        return
