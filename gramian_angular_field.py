# Math
import math
import numpy as np
import matplotlib
from tools import *

class gramian_angular_field():

    def __init__(self, serie):
        pass
        self.serie = serie
    def transform(self):
        """Compute the Gramian Angular Field of an image"""
        # Min-Max scaling
        min_ = np.amin(self.serie)
        max_ = np.amax(self.serie)
        scaled_serie = (2*self.serie - max_ - min_)/(max_ - min_)

        # Floating point inaccuracy!
        scaled_serie = np.where(scaled_serie >= 1., 1., scaled_serie)
        scaled_serie = np.where(scaled_serie <= -1., -1., scaled_serie)

        # Polar encoding
        phi = np.arccos(scaled_serie)
        # Note! The computation of r is not necessary
        r = np.linspace(0, 1, len(scaled_serie))

        # GAF Computation (every term of the matrix)
        gaf = tabulate(phi, phi, cos_sum)

        return(gaf, phi, r, scaled_serie)