"""
Program Name: "lab15_ssrinivasan3.py"

Author: Shrrayash Srinivasan

Purpose of this program: I will be using trig functions to plot a circle using matplotlib. Will make more circle graphs later.

Date: December 2, 2025

"""
import math
import matplotlib.pyplot as plt

# Generate angle values from 0 to 359 degrees
angles_deg = range(360)
angles_rad = [math.radians(deg) for deg in angles_deg]

# Create x and y lists using cosine and sine
x_vals = [math.cos(rad) for rad in angles_rad]
y_vals = [math.sin(rad) for rad in angles_rad]

# Plotting the unit circle with style experimentation
plt.figure(figsize=(6, 6))
plt.plot(
    x_vals,
    y_vals,
    linestyle='--',
    linewidth=3,
    color='green',
    marker='o',
    markersize=2,
    label='Unit Circle (cos θ, sin θ)'
)

# Add labels, title, grid, and legend
plt.title("Circumference of Circle")
plt.xlabel("Cosine")
plt.ylabel("Sine")
plt.grid(True, linestyle=':', linewidth=0.8)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()  
