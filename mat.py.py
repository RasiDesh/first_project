#Using Matplotlib to create line plots

import matplotlib.pyplot as plt

# 1. Prepare Data
x_values = [-1, 2, -3, 4, -5]
y_values = [-2, 5, -3, 6, 4]

# 2. Create a Plot
plt.plot(x_values, y_values, label="My Data")

# 3. Customize the Plot
plt.title("Simple Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True) # Add a grid for better readability

# 4. Display the Plot
plt.show()