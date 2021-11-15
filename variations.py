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

