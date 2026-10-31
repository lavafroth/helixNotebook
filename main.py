import matplotlib
matplotlib.use('kitcat')

7*7

print("cool")


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.1)
two_x_exp = np.exp(2.0 * x)
tanh = (two_x_exp - 1.0) / (two_x_exp + 1.0)


plt.plot(x, tanh)
plt.show()

plt.plot(x, 1/(1+np.exp(-x)))
plt.show()
