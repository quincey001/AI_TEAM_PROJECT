import numpy
import psutil
from Given import Given
from Population import Population
from Crossover import CycleCrossover
from Chromosome import Chromosome
from SudokuGeneticAlgorithm import profile
from Tournament import Tournament
class Sudoku(object):
    def __init__(self, chromosomeNumber, eliteNumber, generationNumber):
        self.chromosomeNumber = chromosomeNumber
        self.eliteNumber = eliteNumber
        self.generationNumber = generationNumber
        self.given = None
        return

    def load(self, path):
        # Load a file containing SUDOKU to solve.
        with open(path, "r") as f:
            values = numpy.loadtxt(f).astype(int)
            self.given = Given(values)
        print("INPUT\n", values)
        return

    def solve(self):
        mutateNumber = 0  # mutation number
        staleCount = 0  # number of staling generation
        prevFitness = 0  # previous fitness

        # variables for mutation
        phi = 0  # number of tiems, child is better than parents
        sigma = 1  # update mutation rate
        mutationRate = 0.5 #initial mutation rate

        # Generating initial population.
        self.population = Population()
        self.population.generatePopulation(self.chromosomeNumber, self.given)

        # Start solving.
        for generation in range(0, self.generationNumber):
            print("Generation %d" % generation)

            # Check for a solution.
            bestFitness = 0.0
            bestSolution = self.given
            # check every chromosome in population
            #if the fitness == 1, then the chromosome is a solution
            #if the fitness > bestFitness 0,
            for c in range(0, self.chromosomeNumber):
                fitness = self.population.chromosomes[c].fitness
                if (float(fitness) > 0.95):
                    print("Solution found at generation %d!" % generation)
                    print(self.population.chromosomes[c].values)
                    return self.population.chromosomes[c]

                # Find the best fitness.
                if (fitness > bestFitness):
                    bestFitness = fitness
                    bestSolution = self.population.chromosomes[c].values

            print("Best fitness: %f" % bestFitness)

            #next generation
            nextPopulation = []

            #preserve the best fittest chromosmos for next generation
            # 0.6*200=120 elites in new generation
            self.population.sort()
            elites = []
            for e in range(0, self.eliteNumber):
                elite = Chromosome()
                elite.values = numpy.copy(self.population.chromosomes[e].values)
                elites.append(elite)

            for count in range(self.eliteNumber, self.chromosomeNumber, 2):
                # Select parents from population via a tournament.
                t = Tournament()
                parent1 = t.compete(self.population.chromosomes)
                parent2 = t.compete(self.population.chromosomes)

                ## Cross-over.
                cc = CycleCrossover()
                child1, child2 = cc.crossover(parent1, parent2, crossoverRate=1.0)

                # Mutate child1.
                child1.getFitnessScore()
                oldFitness = child1.fitness
                muate_success = child1.mutate(mutationRate, self.given)
                child1.getFitnessScore()
                if (muate_success):
                    mutateNumber += 1
                    if (child1.fitness > oldFitness):  # Used to calculate the relative success rate of mutations.
                        phi = phi + 1

                # Mutate child2.
                child2.getFitnessScore()
                oldFitness = child2.fitness
                muate_success = child2.mutate(mutationRate, self.given)
                child2.getFitnessScore()
                if (muate_success):
                    mutateNumber += 1
                    if (child2.fitness > oldFitness):  # Used to calculate the relative success rate of mutations.
                        phi = phi + 1

                # Add children to new population.
                nextPopulation.append(child1)
                nextPopulation.append(child2)

            # Append elites onto the end of the population. These will not have been affected by crossover or mutation.
            for e in range(0, self.eliteNumber):
                nextPopulation.append(elites[e])

            # Select next generation.
            self.population.chromosomes = nextPopulation
            self.population.updateFitness()

            # Calculate  mutation rate
            # (based on Rechenberg's 1/5 success rule).
            # This is to stop too much mutation as the fitness progresses towards unity.
            if (mutateNumber == 0):
                phi = 0  # Avoid divide by zero.
            else:
                phi = phi / mutateNumber

            if (phi > 0.2):
                sigma = sigma * 0.998  # sigma higher, less mutationRate
            if (phi < 0.2):
                sigma = sigma / 0.998  # sigma lower, more mutationRate

            mutationRate = abs(numpy.random.normal(loc=0.0, scale=sigma, size=None))
            while mutationRate > 1:
                mutationRate = abs(numpy.random.normal(loc=0.0, scale=sigma, size=None))

            # Check for stale population.
            self.population.sort()

            if generation == 0:
                prevFitness = bestFitness
                staleCount = 1

            elif prevFitness == bestFitness:
                staleCount += 1

            elif prevFitness != bestFitness:
                staleCount = 0
                prevFitness = bestFitness

            # Re-generatePopulation the population if 100 generations have passed with the
            # fittest two chromosomes always having the same fitness.
            if (staleCount >= 150):
                print("The population has gone stale. Re-generatePopulationing...")
                self.population.generatePopulation(self.chromosomeNumber, self.given)
                staleCount = 0
                sigma = 1
                phi = 0
                mutations = 0
                mutationRate = 0.5

        print("No solution found.", bestSolution)
        return None

# puzzle = "/Users/congqinyan/TCD LECTURES/semester two/AI/team-project/AI_TEAM_PROJECT/SudokuGeneticAlgorithm/simple/2.txt"
# s = Sudoku(200, 140, 1500)
# s.load(puzzle)
# solution = s.solve()
