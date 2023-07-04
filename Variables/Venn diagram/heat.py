import numpy
import seaborn
import matplotlib.pyplot as plt

data = numpy.array([
    [1, 2, 3, 4, 5],
    [2, 3, 5, 1, 4],
    [3, 4, 1, 2, 5]
])
plt.figure(figsize=(5, 7))
seaborn.heatmap(numpy.corrcoef(data), cmap='mako', annot=True)
plt.show()