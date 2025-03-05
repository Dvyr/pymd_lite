
class Units:
    """
    A class for reducing physical quantities to their dimensionless form.

    Parameters
    ----------
    sigma : float, optional
        The base length. Default is 1.0.
    epsilon : float, optional
        The base energy. Default is 1.0.
    mass : float, optional
        The base mass. Default is 1.0.

    """

    def __init__(self, sigma: float = 1.0, epsilon: float = 1.0,
                 mass: float = 1.0) -> None:
        """
        Initialize the Units class.

        Parameters
        ----------
        sigma : float, optional
            The base length. Default is 1.0.
        epsilon : float, optional
            The base energy. Default is 1.0.
        mass : float, optional
            The base mass. Default is 1.0.
        """
        self.sigma = sigma    # Base length
        self.epsilon = epsilon # Base energy
        self.mass = mass      # Base mass

    def reduce_length(self, r):
        "Reduce a length to its dimensionless form."
        return r / self.sigma

    def reduce_energy(self, E):
        "Reduce an energy to its dimensionless form."
        return E / self.epsilon

    def reduce_time(self, t):
        "Reduce a time to its dimensionless form."
        return t * (self.epsilon / (self.mass * self.sigma**2))**0.5
