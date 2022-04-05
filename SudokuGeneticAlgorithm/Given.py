import numpy as np
from Chromosome import Chromosome
class Given(Chromosome):
    """ this object contains the given/known values. """

    def __init__(self, values):
        self.values = values
        return
