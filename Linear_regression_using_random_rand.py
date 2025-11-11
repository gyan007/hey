import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate random x values (uniformly distributed between 0 and 10)
x = 10 * np.random.rand(100)

# Step 2: Create linear relationship y = 3x + 4 + noise
noise = np.random.randn(100)  # Gaussian noise
y = 3 * x + 4 + noise

# Step 3: Fit a linear regression using the least squares method
# np.polyfit returns slope (m) and intercept (b) for degree=1 (linear)
m, b = np.polyfit(x, y, 1)

# Step 4: Predict y values using regression line
y_pred = m * x + b

# Step 5: Plot the data and regression line
plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, y_pred, color='red', linewidth=2, label=f'Regression line: y={m:.2f}x+{b:.2f}')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression using NumPy")
plt.legend()
plt.grid(True)
plt.show()
