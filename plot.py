import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def plot_2d_function(func, x_range, y_range, title):
    x = np.linspace(x_range[0], x_range[1], 100)
    y = np.linspace(y_range[0], y_range[1], 100)
    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    ax.set_title(title)
    
if __name__ == "__main__":
    def f1(x, y):
        return x * y

    def f2(x, y):
        return x**2 + y**2

    def f3(x, y):
        return np.sin(3 * x) * y
    
    #plot 2d functions
    x_range = [-3,3]
    y_range = [-3,3]
    plot_2d_function(f1, x_range, y_range, "f(x, y) = x * y")
    plot_2d_function(f2, x_range, y_range, "f(x, y) = x^2 + y^2")
    plot_2d_function(f3, x_range, y_range, "f(x, y) = sin(3x) * y")
    
    #Bar plot
    values_for_bars = np.loadtxt('values_for_bars.csv', delimiter=',')

    counts = Counter(values_for_bars)
    values = sorted(counts.keys())
    frequencies = [counts[val] for val in values]
    
    plt.figure()
    plt.bar(values, frequencies, color='skyblue')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Bar Plot of Values')
    plt.grid(axis='y', alpha=0.75)
    
    #Histograms
    values_for_hist = np.loadtxt('values_for_hist.csv', delimiter=',')
    
    plt.figure()
    plt.hist(values_for_hist, bins=20, edgecolor = 'black', color = 'lightcoral')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Values')
    plt.grid(axis='y', alpha=0.75)

    plt.show()

