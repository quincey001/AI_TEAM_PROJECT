from Chromosome import Chromosome
import numpy
import random
class CycleCrossover(object):
    """ Crossover relates to the analogy of genes within each parent candidate mixing together
    in the hopes of creating a fitter child candidate.
    Cycle crossover is used here"""

    def __init__(self):
        return

    def crossover(self, parent1, parent2, crossoverRate):
        """ Create two new child chromosomes by crossing over parent genes. """
        child1 = Chromosome()
        child2 = Chromosome()

        # Make a copy of the parent genes.
        child1.values = numpy.copy(parent1.values)
        child1.fitness = parent1.fitness
        child2.values = numpy.copy(parent2.values)
        child2.fitness = parent2.fitness

        r = random.uniform(0, 1.1)
        while (r > 1):  # Outside [0, 1] boundary. Choose another.
            r = random.uniform(0, 1.1)

        # Perform crossover.
        if (r < crossoverRate):
            # Pick a crossover point. Crossover must have at least 1 row (and at most Nd-1) rows.
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

        while ((0 in childRow1) and (0 in childRow2)):  # While child rows not complete...
            if (cycle % 2 == 0):  # Even cycles.
                # Assign next unused value.
                index = self.findUnused(row1, remaining)
                start = row1[index]
                remaining.remove(row1[index])
                childRow1[index] = row1[index]
                childRow2[index] = row2[index]
                next = row2[index]

                while (next != start):  # While cycle not done...
                    index = self.findValue(row1, next)
                    childRow1[index] = row1[index]
                    remaining.remove(row1[index])
                    childRow2[index] = row2[index]
                    next = row2[index]

                cycle += 1

            else:  # Odd cycle - flip values.
                index = self.findUnused(row1, remaining)
                start = row1[index]
                remaining.remove(row1[index])
                childRow1[index] = row2[index]
                childRow2[index] = row1[index]
                next = row2[index]

                while (next != start):  # While cycle not done...
                    index = self.findValue(row1, next)
                    childRow1[index] = row2[index]
                    remaining.remove(row1[index])
                    childRow2[index] = row1[index]
                    next = row2[index]

                cycle += 1

        return childRow1, childRow2

    def findUnused(self, parent_row, remaining):
        for i in range(0, len(parent_row)):
            if (parent_row[i] in remaining):
                return i

    def findValue(self, parent_row, value):
        for i in range(0, len(parent_row)):
            if (parent_row[i] == value):
                return i