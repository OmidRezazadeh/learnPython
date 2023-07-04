import seaborn
import matplotlib
import scipy

data = scipy.stats.norm(0, 1).rvs(10000)
matplotlib.figure.Figure(figsize=(200, 7))
seaborn.displot(data)
matplotlib.pyplot.show()
