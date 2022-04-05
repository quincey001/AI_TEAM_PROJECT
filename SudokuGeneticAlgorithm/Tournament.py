import random
class Tournament(object):
    """ best two parents election to crossover

    Two individuals are selected from the population pool and a random number in [0, 1] is chosen.
    If this number is less than the 'selection rate' (e.g. 0.85), then the fitter individual is selected;
    otherwise, the weaker one is selected.
    """

    def __init__(self):
        return

    def compete(self, chromosomes):
        """ Pick 2 random chromosomes from the population and get them to compete against each other. """
        c1 = chromosomes[random.randint(0, len(chromosomes) - 1)]
        c2 = chromosomes[random.randint(0, len(chromosomes) - 1)]
        f1 = c1.fitness
        f2 = c2.fitness

        # Find the fittest and the weakest.
        if (f1 > f2):
            fittest = c1
            weakest = c2
        else:
            fittest = c2
            weakest = c1

        selection_rate = 0.85
        r = random.uniform(0, 1.1)
        while (r > 1):  # Outside [0, 1] boundary. Choose another.
            r = random.uniform(0, 1.1)
        if (r < selection_rate):
            return fittest
        else:
            return weakest
