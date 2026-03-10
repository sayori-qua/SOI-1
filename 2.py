import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data = np.array([
4520.03,179.34,5486.32,46070.31,24674.96,4754.77,8908.38,6907.32,
4142.84,3083.64,45409.92,2422.23,25035.76,7557.07,15869.8,7777.68,
10475.32,9751.0,71332.02,37872.33,22370.58,7891.34,32188.59,14000.91,
7556.19,56017.72,38340.36,14860.46,30694.14,20828.36,6742.38,9118.41,
15030.0,27538.17,92144.28,20517.37,29665.42,50063.0,73509.47,189891.0
])

bins = [0, 5350, 11074, 20720, 42884, 200000]

shape, loc, scale = stats.lognorm.fit(data, floc=0)

x = np.linspace(min(data), max(data), 1000)
pdf = stats.lognorm.pdf(x, shape, loc=loc, scale=scale)

plt.figure(figsize=(10,6))

plt.hist(data,
         bins=bins,
         density=True,
         alpha=0.6,
         edgecolor='black',
         label='Гистограмма')

plt.plot(x,
         pdf,
         color='red',
         linewidth=3,
         label='Логнормальная плотность')

plt.xlim(0,80000)

plt.title('Гистограмма и оценка плотности распределения')
plt.xlabel('Inbound Tourism Expenditure, million USD')
plt.ylabel('Плотность')

plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.tight_layout()

plt.savefig("histogram_density.png", dpi=300)

plt.show()