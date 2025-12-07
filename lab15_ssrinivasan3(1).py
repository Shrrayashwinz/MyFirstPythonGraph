"""
Program Name: "lab15_ssrinivasan3.py"

Author: Shrrayash Srinivasan

Purpose of this program: I will be using trig functions to plot at least three circles on one graph using matplotlib. Enjoy!
I finally got it to plot four circles!

Date: December 2, 2025

"""
import math
import matplotlib.pyplot as plt

# Prepare angle values in radians
angles = [math.radians(deg) for deg in range(360)]

# Circle 1: Centered at origin (0, 0)
x1 = [math.cos(a) for a in angles]
y1 = [math.sin(a) for a in angles]

# Circle 2: Centered at (4, 5)
x2 = [4 + math.cos(a) for a in angles]
y2 = [5 + math.sin(a) for a in angles]

# Circle 3: Centered at (-2, 8)
x3 = [-2 + math.cos(a) for a in angles]
y3 = [8 + math.sin(a) for a in angles]

# Circle 4: Centered at (10, -5)
x4 = [10 + math.cos(a) for a in angles]
y4 = [-5 + math.sin(a) for a in angles]


# Plotting
plt.figure(figsize=(12, 12))
plt.plot(x1, y1, label='Circle at (0,0)', color='green', linewidth=2)
plt.plot(x2, y2, label='Circle at (4,5)', color='orange', linestyle='-', linewidth=4)
plt.plot(x3, y3, label='Circle at (-3,8)', color='red', linestyle=':', linewidth=5)
plt.plot(x4, y4, label='Circle at (10,-5)', color='blue', linestyle='=', linewidth=4)


plt.title('Four Circles , One Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()

