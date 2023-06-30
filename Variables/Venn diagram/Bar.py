import seaborn
import matplotlib

fig = matplotlib.figure.Figure(figsize=(200, 7))
seaborn.barplot(x=[100, 180, 50, 20, 120], y=['c#', 'Python', 'R', 'Matlab', 'js'], orient='h')

print(matplotlib.pyplot.show())
