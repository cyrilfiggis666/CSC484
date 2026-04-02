"""
Pseudocode: Diabetes Prediction Model

BEGIN

    IMPORT required libraries

    LOAD dataset from OpenML
    CONVERT to DataFrame

    DISPLAY sample data and structure

    SET X = features
    SET y = target column

    CONVERT y values:
        negative -> 0
        positive -> 1

    SPLIT data into training and testing sets (80/20)

    INITIALIZE scaler
    SCALE training data
    SCALE testing data

    INITIALIZE Logistic Regression model
    TRAIN model
    PREDICT on test data
    CALCULATE accuracy

    INITIALIZE KNN model (k = 7)
    TRAIN model
    PREDICT on test data
    CALCULATE accuracy

    DISPLAY model comparison

    GENERATE sample predictions (first 5 rows) for both models
    DISPLAY predictions and actual values

END
"""


"""
CSC484 Portfolio Project
Diabetes Prediction Model using Logistic Regression and K-Nearest Neighbors.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import fetch_openml

# Load dataset from OpenML
diabetes = fetch_openml(name='diabetes', version=1, as_frame=True)

# Convert to pandas DataFrame
df = diabetes.frame

# Inspect the data
print(df.head())
print(df.info())

# Separate features and target
X = df.drop('class', axis=1)
y = df['class']

# Convert target labels to numeric
y = y.map({'tested_negative': 0, 'tested_positive': 1})
print(y.unique())

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.shape, X_test.shape)

# Scale the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(X_train_scaled[:5])



# Logistic Regression model
log_model = LogisticRegression()
log_model.fit(X_train_scaled, y_train)

# Logistic Regression predictions
log_predictions = log_model.predict(X_test_scaled)

# Logistic Regression accuracy
print("Logistic Regression Accuracy:", accuracy_score(y_test, log_predictions))



# KNN model
# Initialize the K-Nearest Neighbors model with k = 7
knn_model = KNeighborsClassifier(n_neighbors=7)

# Train the KNN model using the scaled training data
knn_model.fit(X_train_scaled, y_train)

# Generate predictions using the KNN model on the test data
knn_predictions = knn_model.predict(X_test_scaled)

# Evaluate the KNN model by calculating accuracy
print("KNN Accuracy:", accuracy_score(y_test, knn_predictions))
print("\nModel Comparison Complete.")



# Generate sample predictions using Logistic Regression
sample_prediction_log = log_model.predict(X_test_scaled[:5])
print("Logistic Regression Sample Predictions:", sample_prediction_log)

# Generate sample predictions using KNN
sample_prediction_knn = knn_model.predict(X_test_scaled[:5])
print("KNN Sample Predictions:", sample_prediction_knn)

# Display the actual values for comparison
print("Actual Values:", y_test.iloc[:5].to_numpy())

print("\nProgram Complete.")