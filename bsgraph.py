import numpy as np
import matplotlib.pyplot as plt

x = [i for i in np.arange(0, 5, 0.1)]
y = [i * i for i in x]
plt.plot(x, y)
plt.show()