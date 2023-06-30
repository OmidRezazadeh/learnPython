import scipy

data = scipy.stats.poisson.pmf(5, 10)

uniform = scipy.stats.uniform(10, 20)
print(uniform.pdf(21))
print(uniform.cdf(21))
