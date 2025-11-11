import numpy as np
import matplotlib.pyplot as plt

# Generate data
data_uniform = np.random.rand(1000)
data_normal = np.random.normal(0, 1, 1000)

# Plot histograms
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.hist(data_uniform, bins=30, color='skyblue', edgecolor='black')
plt.title('Uniform Distribution (rand)')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.subplot(1,2,2)
plt.hist(data_normal, bins=30, color='salmon', edgecolor='black')
plt.title('Normal Distribution (normal)')
plt.xlabel('Value')

plt.tight_layout()
plt.show()
