import matplotlib.pyplot as plt
import numpy as np

points = np.loadtxt('points.csv', delimiter=',')
distances = np.loadtxt('distances.csv', delimiter=',')

x = points[:,0]
y = points[:,1]

plt.scatter(x, y, c=distances, cmap='viridis', s=50)
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Scatter Plot of Points Colored by Distance')
plt.grid(True)
plt.legend()

cbar = plt.colorbar()
cbar.set_label('Distance')

plt.show()



