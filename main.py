import numpy as np


class ParticleSwarm:
    """
    Class for holding the swarm of electrical charges.
    """

    def __init__(self,
                 cube_shape: tuple = (10., 10., 10.),
                 charge_mean=0.,
                 charge_var=1.,
                 number_of_charges=100):
        """
        Generates number_of_charges charges within the cube_shape of random
        charge with the magnitude mean=charge_mean and var=charge_var.
        """
        self.cube_shape = cube_shape
        self.charge_mean = charge_mean
        self.charge_var = charge_var
        self.number_of_charges = number_of_charges
        # create an array of 0-1 numbers:
        self.coords = np.random.uniform(low=-1., high=1.,
                                        size=(number_of_charges,
                                              len(cube_shape)))
        # scale each dimension according to the cube_shape
        # WARNING: this will cause the space of charges to be "stretched" in
        # some directions, items won't be uniformly spaced across dimensions
        for dim in range(len(cube_shape)):
            self.coords[dim, :] *= cube_shape[dim] / 2
        # drawing magnitudes from a normal distribution
        self.magnitudes = np.random.normal(charge_mean, charge_var,
                                           size=number_of_charges)

    def get_matrix(self):
        """
        Returns an array of shape (number_of_charges, len(cube_shape) +
        + 1) with the magnitude stored in the last column.
        """
        return np.append(self.coords,
                         np.expand_dims(self.magnitudes, 1),
                         axis=1)


if __name__ == '__main__':
    charges = ParticleSwarm()
    print(charges.get_matrix())
