import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Create random 5x5 data
data = np.random.rand(5, 5)

# Create heatmap
sns.heatmap(data, annot=True, cmap='coolwarm')

plt.title("Random Heatmap Example")
plt.show()
