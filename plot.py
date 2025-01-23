import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x*np.sin(2*x)

x = np.linspace(-100, 100, 1000)
plt.plot(f(x), color='orange', marker='o', markersize=1, linestyle='dashed')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = x*sin(2x)')
plt.grid(True)
plt.legend()
plt.show()


