%matplotlib kitcat

1+3

print("cool")


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1, 1, 0.1)
two_x_exp = np.exp(2.0 * x)
tanh = (two_x_exp - 1.0) / (two_x_exp + 1.0)


plt.gca().clear()
plt.plot(x, tanh)
plt.show()
