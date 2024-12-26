import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the range of x and y values
x = np.linspace(-5, 5, 50)  # Extending the range for more variation
y = np.linspace(-5, 5, 50)

# Create meshgrid for X and Y
X, Y = np.meshgrid(x, y)

# Calculate Z values for each combination of X and Y
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface with color map
surface = ax.plot_surface(X, Y, Z, cmap='viridis')

# Add a colorbar with correct normalization
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5)

# Set axis labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Display the plot
plt.show()

# Author - Mmabiaa
