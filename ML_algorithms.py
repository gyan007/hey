from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1],[2],[3],[4],[5]])
y = np.array([2,4,6,8,10])

model = LinearRegression()
model.fit(X, y)
print("Prediction for 6:", model.predict([[6]])[0])


# --------------------------------


from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.array([[1],[2],[3],[4],[5]])
y = np.array([0,0,0,1,1])

model = LogisticRegression()
model.fit(X, y)
print("Prediction for 3.5:", model.predict([[3.5]])[0])


# -----------------------------------


from sklearn.neighbors import KNeighborsClassifier
import numpy as np

X = np.array([[1],[2],[3],[6],[7],[8]])
y = np.array([0,0,0,1,1,1])

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)
print("Prediction for 4:", model.predict([[4]])[0])



# -----------------------------------


from sklearn.svm import SVC
import numpy as np

X = np.array([[1],[2],[3],[6],[7],[8]])
y = np.array([0,0,0,1,1,1])

model = SVC(kernel='linear')
model.fit(X, y)
print("Prediction for 4:", model.predict([[4]])[0])



# -----------------------------------


from sklearn.tree import DecisionTreeClassifier
import numpy as np

X = np.array([[1],[2],[3],[6],[7],[8]])
y = np.array([0,0,0,1,1,1])

model = DecisionTreeClassifier()
model.fit(X, y)
print("Prediction for 5:", model.predict([[5]])[0])



# -----------------------------------



from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1],[2],[3],[10],[11],[12]])

model = KMeans(n_clusters=2, n_init=10)
model.fit(X)

print("Cluster Centers:", model.cluster_centers_)
print("Labels:", model.labels_)



# -----------------------------------



import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Age':[22,25,29,35,40,41,50],
    'Salary':[25000,30000,40000,50000,60000,65000,70000]
}
df = pd.DataFrame(data)

print(df.describe())      
print(df.corr())           
df.plot(x='Age', y='Salary', kind='scatter')  
plt.show()
