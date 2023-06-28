import numpy
from scipy import stats

data = [12, 3, 4, 5, 6, 7, 89, 53, 32, 4]

data1 = [3, 4, 4, 5, 6, 7, 8, 9, 0]
sorted(data)

median = numpy.median(data)
print(median)

x = stats.mode(data1)
print(x)