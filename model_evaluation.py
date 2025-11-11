# ---------Regression: R², RMSE, MAE (and optional MAPE)---------------
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
 
y_true = np.array([3.0, 2.5, 4.2, 5.0, 6.1])
y_pred = np.array([2.8, 2.7, 4.0, 5.3, 5.9])

r2   = r2_score(y_true, y_pred)
rmse = mean_squared_error(y_true, y_pred, squared=False)   
mae  = mean_absolute_error(y_true, y_pred)
 
mape = np.mean(np.abs((y_true - y_pred) / np.clip(np.abs(y_true), 1e-12, None))) * 100

print(f"R^2 : {r2:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"MAE : {mae:.4f}")
print(f"MAPE: {mape:.2f}%")


# ------------------Classification: Accuracy, Precision, Recall, F1, Confusion Matrix-------------
# ------------------A) Binary classification (with probabilities → threshold 0.5)--------------

import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
 
y_true = np.array([0, 1, 1, 0, 1, 0, 1])
y_proba = np.array([0.2, 0.9, 0.7, 0.4, 0.8, 0.3, 0.65])
 
thr = 0.5
y_pred = (y_proba >= thr).astype(int)

acc  = accuracy_score(y_true, y_pred)
prec = precision_score(y_true, y_pred, zero_division=0)
rec  = recall_score(y_true, y_pred, zero_division=0)
f1   = f1_score(y_true, y_pred, zero_division=0)
cm   = confusion_matrix(y_true, y_pred)

print(f"Accuracy : {acc:.4f}")
print(f"Precision: {prec:.4f}")
print(f"Recall   : {rec:.4f}")
print(f"F1-score : {f1:.4f}")
print("Confusion matrix:\n", cm)
 
print("\nClassification report:\n", classification_report(y_true, y_pred, zero_division=0))


# -------------------B) Multiclass classification------------------

import numpy as np
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix, classification_report
 
y_true = np.array([0,1,2,1,0,2,1,2,0])
y_pred = np.array([0,2,2,1,0,1,1,2,0])

acc = accuracy_score(y_true, y_pred)
 
prec_macro, rec_macro, f1_macro, _ = precision_recall_fscore_support(y_true, y_pred, average='macro', zero_division=0)
prec_weighted, rec_weighted, f1_weighted, _ = precision_recall_fscore_support(y_true, y_pred, average='weighted', zero_division=0)

cm = confusion_matrix(y_true, y_pred)

print(f"Accuracy        : {acc:.4f}")
print(f"Precision (macro): {prec_macro:.4f} | (weighted): {prec_weighted:.4f}")
print(f"Recall    (macro): {rec_macro:.4f} | (weighted): {rec_weighted:.4f}")
print(f"F1        (macro): {f1_macro:.4f} | (weighted): {f1_weighted:.4f}")
print("Confusion matrix:\n", cm)
 
print("\nPer-class report:\n", classification_report(y_true, y_pred, zero_division=0))


# ---------------------Tiny “no-sklearn” versions (pure NumPy)-------------------------

import numpy as np

def r2_np(y, yhat):
    ss_res = np.sum((y - yhat)**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    return 1 - ss_res / ss_tot

def rmse_np(y, yhat):
    return np.sqrt(np.mean((y - yhat)**2))

def mae_np(y, yhat):
    return np.mean(np.abs(y - yhat))

def conf_mat_np(y_true, y_pred, labels=None):
    if labels is None:
        labels = np.unique(np.concatenate([y_true, y_pred]))
    L = len(labels)
    idx = {lab:i for i,lab in enumerate(labels)}
    cm = np.zeros((L, L), dtype=int)
    for t,p in zip(y_true, y_pred):
        cm[idx[t], idx[p]] += 1
    return cm, labels


# -----------------EDA-----------------------


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
data = {
    'Age': np.random.randint(18, 60, 50),
    'Experience': np.random.randint(0, 40, 50),
    'Salary': np.random.randint(30000, 150000, 50),
    'Department': np.random.choice(['HR', 'Tech', 'Sales', 'Finance'], 50),
    'Gender': np.random.choice(['Male', 'Female'], 50)
}

df = pd.DataFrame(data)
 
df.to_csv('employee_data.csv', index=False)
print("Dataset created and saved as 'employee_data.csv'\n")
 
print("--- Basic Information ---")  
print(df.info())

print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Summary Statistics ---")
print(df.describe())

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Unique Values per Column ---")
print(df.nunique())
 
plt.figure(figsize=(6,4))
df['Department'].value_counts().plot(kind='bar', title='Department Distribution')
plt.xlabel('Department')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(6,4))
plt.scatter(df['Experience'], df['Salary'])
plt.title('Experience vs Salary')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary')
plt.show()

plt.figure(figsize=(6,4))
plt.hist(df['Age'], bins=10, edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()