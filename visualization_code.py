# 1️ Heatmap
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(5, 5)
sns.heatmap(data, annot=True)
plt.show()

#  2️ Line Chart
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 7]

plt.plot(x, y)
plt.show()

#  3️ Bar Chart
import matplotlib.pyplot as plt

x = ['A', 'B', 'C', 'D']
y = [10, 20, 15, 25]

plt.bar(x, y)
plt.show()

#  4️ Pie Chart
import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
sizes = [40, 30, 20, 10]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()

#  5️ Histogram
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)
plt.hist(data, bins=20)
plt.show()

#  6 Scatter
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)
plt.scatter(x, y, color='red', label='Scatter plot')
plt.show()