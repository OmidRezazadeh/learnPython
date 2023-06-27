from random import sample
import numpy as np

pop = list(range(1, 11))
print(sample(pop, 5))
np.random.choice(pop, 4, replace=True)
