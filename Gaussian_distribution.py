import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random points from a normal (Gaussian) distribution
data = np.random.normal(loc=0, scale=1, size=1000)  # mean=0, std=1

# Plot histogram
plt.hist(data, bins=30, density=True, alpha=0.6, edgecolor='black')

# Overlay the theoretical Gaussian curve
x = np.linspace(-4, 4, 1000)
y = (1 / (np.sqrt(2 * np.pi))) * np.exp(-0.5 * x**2)
plt.plot(x, y, 'r', linewidth=2)

plt.title("Gaussian (Normal) Distribution")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.show()
