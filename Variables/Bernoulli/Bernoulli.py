import numpy


def prob(p):
    return p


def generate(size, p):
    data = []
    for _ in range(size):
        prob = numpy.random.rand()
        if prob < p:
            data.append(1)
        else:
            data.append(0)
        return data


data = generate(20000, 0.6)
print(data.count(1))
print(data.count(0))
