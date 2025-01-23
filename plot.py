import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x*np.sin(2*x)

x = np.linspace(-100, 100, 1000)
plt.plot(f(x), color='red', marker='o', markersize=1)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()


