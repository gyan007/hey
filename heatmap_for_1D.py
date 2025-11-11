import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1D data
data = np.array([1, 3, 2, 5, 4])

# Convert to 2D (1 row, 5 columns)
data_2d = data.reshape(1, -1)

# Plot heatmap
sns.heatmap(data_2d, annot=True, cmap='coolwarm', cbar=True)
plt.title("Heatmap of 1D Data (as Single Row)")
plt.xlabel("Index")
plt.ylabel("")
plt.show()
