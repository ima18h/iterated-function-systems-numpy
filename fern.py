import numpy as np
import matplotlib.pyplot as plt
import pathlib


class AffineTransform:
    def __init__(self, a=0., b=0., c=0., d=0., e=0., f=0.):
        self._abcd = self._ef = np.asarray([[a, b], [c, d]])
        self._ef = np.asarray([[e], [f]])

    def __call__(self, x, y):
        # np.dot maybe introducing overhead?
        return np.dot(self._abcd, [[x], [y]]) + self._ef


f1 = AffineTransform(0,0,0,0.16,0,0)
f2 = AffineTransform(0.85, 0.04, -0.04, 0.85, 0, 1.60)
f3 = AffineTransform(0.20, -0.26, 0.23, 0.22, 0, 1.6)
f4 = AffineTransform(-0.15, 0.28, 0.26, 0.24, 0, 0.44)

functions = [f1, f2, f3, f4]
p_cumulative = [0.01, 0.86, 0.92, 1.00]
def select(funcs, probcum):
    r = np.random.random()
    for j, p in enumerate(probcum):
        if r < p:
            return funcs[j]


plt.axis("equal")
plt.axis('off')
x = [[0], [0]]
plt.scatter(0, 0)
# TODO: optimize
for i in range(5000):
    x = select(functions, p_cumulative)(x[0][0], x[1][0])
    plt.scatter(x[0], x[1])

plt.savefig(pathlib.Path(__file__).parent.resolve().__str__() + '\\figures\\' + "barnsley_fern",
            dpi=400, s=0.1)

