import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
 
mean = float(input("Enter mean: "))
std_dev = float(input("Enter standard deviation: "))
size = int(input("Enter sample size: "))

# Generate random data from a Gaussian distribution
sns.histplot(data, kde=True, bins=30, color="skyblue", edgecolor="black")


# Plot histogram with KDE
sns.histplot(data, kde=True)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Gaussian (Normal) Distribution")
plt.show()
