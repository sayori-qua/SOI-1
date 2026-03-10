import numpy as np
import matplotlib.pyplot as plt

data = [
4520.03,179.34,5486.32,46070.31,24674.96,4754.77,8908.38,6907.32,
4142.84,3083.64,45409.92,2422.23,25035.76,7557.07,15869.8,7777.68,
10475.32,9751,71332.02,37872.33,22370.58,7891.34,32188.59,14000.91,
7556.19,56017.72,38340.36,14860.46,30694.14,20828.36,6742.38,9118.41,
15030,27538.17,92144.28,20517.37,29665.42,50063,73509.47,189891
]

plt.figure(figsize=(8,6))
plt.boxplot(data)
plt.ylim(0, 100000)
plt.title("Boxplot распределения Inbound Tourism Expenditure")
plt.ylabel("million USD")

plt.grid(True)

plt.savefig("boxplot.png", dpi=300)
plt.show()