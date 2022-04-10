from Chromosome import Chromosome
import numpy
import random
class CycleCrossover(object):
    """ crossover is to mix parent chromosomes to create new child chromosomes """

    def __init__(self):
        return

    def crossover(self, parent1, parent2, crossoverRate):
        """ Create two new child chromosomes from two parent chromosomes """
        child1 = Chromosome()
        child2 = Chromosome()

        # Make a copy of the parent genes.
        child1.values = numpy.copy(parent1.values)
        child1.fitness = parent1.fitness
        child2.values = numpy.copy(parent2.values)
        child2.fitness = parent2.fitness


        r = random.uniform(0, 1.1)
        while (r > 1):
            r = random.uniform(0, 1.1)

        # Perform crossover.
        if (r < crossoverRate):
            # Choose a random crossover point.
            crossoverPoint1 = random.randint(0, 8)
            crossoverPoint2 = random.randint(1, 9)
            while (crossoverPoint1 == crossoverPoint2):
                crossoverPoint1 = random.randint(0, 8)
                crossoverPoint2 = random.randint(1, 9)

            if (crossoverPoint1 > crossoverPoint2):
                temp = crossoverPoint1
                crossoverPoint1 = crossoverPoint2
                crossoverPoint2 = temp

            for i in range(crossoverPoint1, crossoverPoint2):
                child1.values[i], child2.values[i] = self.crossoverRows(child1.values[i], child2.values[i])

        return child1, child2

    def crossoverRows(self, row1, row2):
        childRow1 = numpy.zeros(9)
        childRow2 = numpy.zeros(9)

        remaining = [i for i in range(1, 9 + 1)]
        cycle = 0
        # while the row1 and row2 are not swaped completely
        while ((0 in childRow1) and (0 in childRow2)):
            #if cyle is even, swap row1 and row2
            if (cycle % 2 == 0):
                # set unused values as start
                index = self.findUnusedValue(row1, remaining)
                start = row1[index]
                remaining.remove(row1[index])
                childRow1[index] = row1[index]
                childRow2[index] = row2[index]
                next = row2[index]
                # find the next value in row1
                while (next != start):
                    index = self.findValue(row1, next)
                    childRow1[index] = row1[index]
                    remaining.remove(row1[index])
                    childRow2[index] = row2[index]
                    next = row2[index]
                cycle += 1

            else:
                #if cycle is odd, swap row2 and row1
                index = self.findUnusedValue(row1, remaining)
                start = row1[index]
                remaining.remove(row1[index])
                childRow1[index] = row2[index]
                childRow2[index] = row1[index]
                next = row2[index]
                while (next != start):
                    index = self.findValue(row1, next)
                    childRow1[index] = row2[index]
                    remaining.remove(row1[index])
                    childRow2[index] = row1[index]
                    next = row2[index]
                cycle += 1

        return childRow1, childRow2

    def findUnusedValue(self, parent_row, remaining):
        for i in range(0, len(parent_row)):
            if (parent_row[i] in remaining):
                return i

    def findValue(self, parent_row, value):
        for i in range(0, len(parent_row)):
            if (parent_row[i] == value):
                return i