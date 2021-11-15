from __future__ import annotations
#import chaos_game as cg
import numpy as np
import matplotlib.pyplot as plt


class Variations:
    def __init__(self, x, y, name: str):
        self._x = x
        self._y = y
        self._variation = name
        _implemented = ["linear", "handkerchief", "swirl",
                             "disc", "eyefish", "horseshoe"]
        if name.lower() in _implemented:
            self._func: callable = getattr(Variations, name)
        else:
            raise Exception("variation not implemented")

    def transform(self):
        return self._func(self._x, self._y)

    @classmethod
    def from_chaos_game(cls, game, variation):
        # TODO: this if should probably be handled by ChaosGame class, not here
        if not game._solved:
            raise Exception("game not solved. use iterate method first.")
        return Variations(game._points[:, 0], game._points[:, 1], variation)

    @classmethod
    def linear_combination_wrap(cls, var1: Variations, var2: Variations):
        # TODO: sanitize. x,y should be same for vars. are vars transformed yet?
        def linear_combination(w):
            if not (0 <= w <= 1):
                raise Exception("w should be between 0 and 1")
            # assuming not transformed yet
            u1, v1 = var1.transform()
            u2, v2 = var2.transform()
            return w * u1 + (1-w) * u2, w * v1 + (1-w) * v2
        return linear_combination

    @staticmethod
    def linear(x, y) -> tuple[list, list]:
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


"""
N = 70
grid_values = np.linspace(-1, 1, N)
x, y = np.meshgrid(grid_values, grid_values)
x_values = x.flatten()
y_values = y.flatten()

transformations = ["linear", "handkerchief", "swirl", "eyefish"]
variations = [Variations(x_values, y_values, version) for version in transformations]

fig, axs = plt.subplots(2, 2, figsize=(9, 9))
for i, (ax, variation) in enumerate(zip(axs.flatten(), variations)):
    u, v = variation.transform()

    ax.plot(u, -v, markersize=1, marker=".", linestyle="", color="black")
    # ax.scatter(u, -v, s=0.2, marker=".", color="black")
    ax.set_title(variation._variation)
    ax.axis("off")

fig.savefig("figures/variations_4b.png")
plt.show()
"""

# plot variations of chaos game
# TODO: after iterating, game object becomes NoneType. wtf? importing variations into chaos_game works fine
#game = cg.ChaosGame().iterate(20000, 100)
#print(type(game))
#colors = game.gradient_color
#variation = Variations.from_chaos_game(game, "horseshoe").transform()


#plt.scatter(variation[:,0], -variation[:,1], s=0.2, marker=".", c=colors)
