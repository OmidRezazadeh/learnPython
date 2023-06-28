import scipy

data = scipy.stats.binom(10, 0.5).pmf(3)
print(data)

data1 = scipy.stats.binom(10, 0.5).rvs(size=10000)
print(data1)