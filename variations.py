#import chaos_game as cg
import numpy as np


class Variations:
    def __init__(self, x, y, name: str):
        self._x = x
        self._y = y
        self._variation = name
        self._func = getattr(Variations, name)

    def transform(self):
        return self._func(self._x, self._y)

    @staticmethod
    def linear(x, y):
        return x, y

    @staticmethod
    def handkerchief(x, y):
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(x, y)
        return r * np.sin(theta + r), r * np.cos(theta - r)

    @staticmethod
    def swirl(x, y):
        r = np.sqrt(x ** 2 + y ** 2)
        return x * np.sin(r**2) - y * np.cos(r**2), x * np.cos(r**2) + y * np.sin(r**2)

    @staticmethod
    def disc(x, y):
        r = np.sqrt(x ** 2 + y ** 2)
        theta = np.arctan2(x, y)
        c = theta / np.pi
        return c * np.sin(np.pi * r), c * np.cos(np.pi * r)

    @staticmethod
    def eyefish(x, y):
        r = np.sqrt(x ** 2 + y ** 2)
        c = 2 / (r + 1)
        return c * x, c * y

    @staticmethod
    def horseshoe(x, y):
        r = np.sqrt(x ** 2 + y ** 2)
        c = 1 / r
        return c * ((x-y) * (x+y)), c * 2 * x*y

