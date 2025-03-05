import numpy as np

class Mol:
    def __init__(self, dim=3, r=None, rv=None, ra=None):
        self.dim = dim
        self.r = r if r is not None else np.zeros(dim)
        self.rv = rv if rv is not None else np.zeros(dim)
        self.ra = ra if ra is not None else np.zeros(dim)
        
