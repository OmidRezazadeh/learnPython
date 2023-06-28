import numpy

data = [12, 3, 4, 5, 6, 7, 89, 53, 32, 4]
total = 0
for x in data:
    total += x
print(total / len(data))

print(numpy.mean(data))
