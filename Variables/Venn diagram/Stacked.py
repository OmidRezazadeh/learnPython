import pandas
import matplotlib
import seaborn

matplotlib.figure.Figure(figsize=(200, 7))
df = pandas.DataFrame({
    "Name": ["Ali", "Sadegh", "Mohamad"],
    "Apple": [60, 20, 30],
    "Banana": [20, 40, 30]
})
seaborn.barplot(y="Name", x="Apple", data=df, label="Apple", color="red", alpha=.5, orient="h")
seaborn.barplot(y="Name", x="Banana", left=[60, 20, 30], data=df, label="Banana", color="blue", alpha=.5, orient="h")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
