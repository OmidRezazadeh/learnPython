import numpy

data = [1, 2, 3, 4, 5, 6, 90, 12, 5, 4]

# print(max(data) - min(data))

Q1, Q2, Q3 = numpy.quantile(data, [0.25, 0.5, 0.75])
data_qr = Q3 - Q2

print(data_qr)

# varians
print(numpy.var(data))
print(numpy.std(data))
