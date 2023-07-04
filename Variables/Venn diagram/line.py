import seaborn
import matplotlib

x = ["far", 'ord', 'tir', 'mor', 'sha']
y = [20, 10, 23, 40, 50]

matplotlib.pyplot.figure(figsize=(5, 7))
seaborn.lineplot(x=x, y=y, color="red", alpha=0.8)

matplotlib.pyplot.show()
