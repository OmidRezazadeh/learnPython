import matplotlib.pyplot as plt
import seaborn
import numpy

x1 = numpy.random.uniform(-1, 1, 1000)
x2 = x1 ** 2 + numpy.random.normal(0, 1, 1000) / 10
seaborn.jointplot(x=x1, y=x2, kind='scatter')
plt.show()
