import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Define vertices for the triangle (x, y coordinates)
vertices = [(0.2, 0.2), (0.8, 0.2), (0.5, 0.8)]

# Create a triangle
triangle = patches.Polygon(vertices, edgecolor='orange', facecolor='yellow')

# Plot the triangle
fig, ax = plt.subplots()
ax.add_patch(triangle)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Triangle')
plt.show()
