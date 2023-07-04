import matplotlib.pyplot as plt

plt.figure(figsize=(9, 10))

plt.pie([40, 10, 15],
        labels=['python', 'scala', 'php'],
        colors=['yellow', 'red', 'blue'],
        explode=[0.1, 0.0, 0.0],
        autopct='%1.2f%%', pctdistance=0.65)

plt.show()
