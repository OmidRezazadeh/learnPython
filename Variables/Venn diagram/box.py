import matplotlib.pyplot as plt
import seaborn

data = [1, 2, 3, 4, 5]
plt.figure(figsize=(5, 7))
seaborn.boxplot(data, color='blue')
plt.show()
