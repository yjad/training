# %matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

fig = plt.figure()
ax = plt.axes()

# x = np.linspace(0, 10, 1000)
# print (x)
# ax.plot(x,np.sin(x))

# ax.plot(x, x + 0, linestyle='-')
# ax.plot(x, x + 1, linestyle='-.')
# ax.plot(x, x + 2, linestyle='--')
# ax.plot(x, x + 3, linestyle=':')

x = np.linspace(0, 10, 30)
y = np.sin(x)

plt.plot(x, np.sin(x), '-ok', color='black');

plt.show()