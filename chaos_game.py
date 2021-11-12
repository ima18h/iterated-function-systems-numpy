import numpy as np
import matplotlib.pyplot as plt
import pathlib


class ChaosGame:
    def __init__(self, n: int = 3, r: float = 0.5):
        """Need to make sure input is of right type, and 0 < r < 1, n > 2.
        This checks first, then sets the attributes after. sets to default if not possible.
        _corners are 2d arrays of floats, so are _points. """
        self._n: int
        self._r: float
        self._solved = False
        # not sure how to type corners and points,
        # which are lists of tuples then converted to np arrays
        self._corners: list
        self._points = np.asarray([(0., 0., 0)])

        # better way to handle all situations? this looks a bit ugly to me in constructor
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
        """Generates and saves the corner points of the ngon.
        saved as 2d array of floats"""
        theta = 2 * np.pi / self._n
        corners = [(np.sin(theta), np.cos(theta))] * self._n
        for i in range(self._n):
            corners[i] = (np.sin(theta * i), np.cos(theta * i))
        self._corners = np.asarray(corners)

    def plot_ngon(self):
        plt.plot(self._corners[:, 0], self._corners[:, 1])

    def _starting_point(self):
        """Randomly selects a starting point inside the ngon
        :return: python list with 2 elements of float type
        """
        spoint = [0, 0]
        w = [0.] * self._n
        for i in range(self._n):
            w[i] = np.random.random()
        wsum = sum(w)
        for i in range(self._n):
            w[i] = w[i] / wsum
            spoint[0] += w[i] * self._corners[i][0]
            spoint[1] += w[i] * self._corners[i][1]
        return spoint

    def iterate(self, steps: int = 10, discard: int = 5):
        """Discards the first discard points.
        The third element in each tuple is the random chosen corner index
        be aware that, currently, index is a float"""
        current_point = np.asarray(self._starting_point())

        self._points = [(0., 0., 0)] * (steps - discard)
        self._points = np.asarray(self._points)
        for i in range(discard):
            c = self._corners[np.random.randint(0, self._n)]
            current_point = self._r * current_point + (1 - self._r) * c

        for i in range(steps - discard):
            cind = np.random.randint(0, self._n)
            current_point = self._r * current_point + (1 - self._r) * self._corners[cind]
            self._points[i] = *current_point, cind
        self._solved = True

    def plot(self, color: bool, cmap: str):
        """Colors is a tuple of the corner indices, when color=True. """
        colors = "black"
        if color:
            colors = self.gradient_color
        if self._solved:
            plt.scatter(self._points[:, 0], self._points[:, 1], c=colors,
                        cmap=cmap, s=0.1)
        else:
            raise Exception("Need to iterate() before plotting")

    def show(self, color=False, cmap="rainbow"):
        plt.axis("Equal")
        plt.axis('off')
        self.plot(color, cmap)
        plt.show()

    def savepng(self, outfile: str, color=False, cmap="rainbow"):
        plt.axis("Equal")
        plt.axis('off')
        self.plot(color, cmap)
        plt.savefig(pathlib.Path(__file__).parent.resolve().__str__() + '\\figures\\' + outfile,
                    dpi=400)

    @property
    def gradient_color(self):
        """Returns an array with each points rgb colors calculated based on
        the selected corner and the previous points color
        gc = gradiant colors, cc = corner colors

        :return: array of shape (x, 3). x depends on how many iterated points
        """
        if self._solved:
            colors = iter([plt.cm.tab20(i) for i in range(20)])
            cc = []
            i = 0
            # TODO: this can only create a limited number of colors then repeat
            while len(cc) < self._corners.shape[0]:
                cc.append(next(colors))
                i += 1
                if i == 20:
                    colors = iter([plt.cm.tab20b(i) for i in range(20)])
                    i = 0
            cc = np.delete(np.asarray(cc), 3, 1)
            # probably exists better way to initialize gc than converting back to list
            gc = np.asarray([cc[int(self._points[0][2])]] * self._points.shape[0])
            # i need an arbitrary amount of chosen colors for the corners
            for i in range(1, self._points.shape[0]):
                gc[i] = (gc[i - 1] + cc[int(self._points[i][2])]) / 2
            return gc
        else:
            raise Exception("Need to iterate() before creating colors")

# testing stuff
# game = ChaosGame(6, 1/3)

# game.iterate(20000, 100)

# game.show(True)
# game.savepng("stonks", True)
