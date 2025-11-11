import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def train_iris_model():
    """
    Loads the Iris dataset, trains a KNN classifier, and evaluates it.
    """
    
    # 1. Load the dataset
    iris = load_iris()
    X = iris.data
    y = iris.target
    feature_names = iris.feature_names
    target_names = iris.target_names

    # Optional: Print dataset information
    print("--- Iris Dataset Information ---")
    print(f"Features: {feature_names}")
    print(f"Targets: {target_names}")
    print(f"Shape of data (X): {X.shape}")
    print(f"Shape of target (y): {y.shape}")
    print("-" * 30 + "\n")

    # 2. Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, 
        test_size=0.3, 
        random_state=42, 
        stratify=y
    )

    print("--- Data Split ---")
    print(f"Training samples: {X_train.shape[0]}")
    print(f"Testing samples: {X_test.shape[0]}")
    print("-" * 30 + "\n")

    # 3. Initialize and Train the Model (K-Nearest Neighbors)
    # We'll use n_neighbors=3 as a common starting point
    print("Training a K-Nearest Neighbors (KNN) model with k=3...")
    model = KNeighborsClassifier(n_neighbors=3)
    
    # Train the model on the training data
    model.fit(X_train, y_train)
    print("Model training complete.")
    print("-" * 30 + "\n")

    # 4. Evaluate the Model
    
    # Make predictions on the unseen test data
    y_pred = model.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    # Generate a detailed classification report
    report = classification_report(
        y_test, 
        y_pred, 
        target_names=target_names
    )
    
    # Generate a confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    
    print("--- Model Evaluation Results ---")
    print(f"Accuracy: {accuracy:.4f} (or {accuracy*100:.2f}%)")
    print("\nClassification Report:")
    print(report)
    
    print("\nConfusion Matrix:")
    # Pretty print the confusion matrix
    print(f"{'':<10} | {'Predicted ' + target_names[0]:<15} | {'Predicted ' + target_names[1]:<15} | {'Predicted ' + target_names[2]:<15}")
    print("-" * 65)
    for i, row in enumerate(cm):
        print(f"Actual {target_names[i]:<7} | {row[0]:<15} | {row[1]:<15} | {row[2]:<15}")
    
    print("\n--- Example Prediction ---")
    # Take the first sample from the test set for a demo
    sample = X_test[0]
    sample_target = y_test[0]
    
    # model.predict expects a 2D array
    sample_pred = model.predict([sample]) 
    
    predicted_class = target_names[sample_pred[0]]
    actual_class = target_names[sample_target]
    
    print(f"Sample Features: {sample}")
    print(f"Actual Class: {actual_class}")
    print(f"Predicted Class: {predicted_class}")


# --- Main execution ---
if __name__ == "__main__":
    train_iris_model()