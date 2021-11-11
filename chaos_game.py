import numpy as np
import matplotlib.pyplot as plt



class ChaosGame:
    def __init__(self, n: int = 3, r: float = 0.5):
        """Need to make sure input is of right type, and 0 < r < 1, n > 2.
        This checks first, then sets the attributes after. sets to default if not possible. """
        self._n: int
        self._r: float
        self._corners: list

        try:
            if not isinstance(n, int):
                raise TypeError("n should be an int")
        except TypeError as terr:
            print(terr.args)
            print("trying to convert")
            n = int(n)
        if n < -2:
            print("n need to be int > 2, converting to positive int")
            self._n = self._n * -1
        elif -2 <= n <= 2:
            print("n has to be int > 2")
            print("using default n = 3")
            self._n = 3
        else:
            self._n = n

        try:
            if not isinstance(r, float):
                raise TypeError("TypeError: r should be a float 0 < r < 1")
        except TypeError as terr:
            print(terr.args)
            print("trying to convert")
            r = float(r)
        if not (0 < r < 1):
            print("r should be a float 0 < r < 1")
            print("using default r = 0.5")
            self._r = 0.5
        else:
            self._r = r

        self._generate_ngon()

    def _generate_ngon(self):
        theta = 2*np.pi / self._n
        corners = [None] * self._n
        for i in range(self._n):
            corners[i] = (np.sin(theta*i), np.cos(theta*i))
        self._corners = corners


game = ChaosGame(5, 0.6)
print(game._corners[3])
