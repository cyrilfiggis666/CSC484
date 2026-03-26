"""
Start program

Load the Iris dataset from scikit-learn

Store the feature data in X
Store the target data in y

Split the dataset into training data and testing data
    Use 80% for training
    Use 20% for testing

Create an empty list to store accuracy scores

Create a range of k values from 1 through 20

For each k value in the range
    Create a KNeighborsClassifier model using the current k value
    Train the model using the training data
    Use the model to predict the test data
    Calculate the accuracy of the predictions
    Store the accuracy score in the list

Find the highest accuracy score in the list
Find the k value that matches the highest accuracy score

Display all k values and their accuracy scores
Display the optimal k value and its accuracy score

End program
"""


"""
This program uses the Iris dataset from scikit-learn to determine the
optimal k value for a KNeighborsClassifier model. The program loads the
dataset, separates the features and target values, splits the data into
training and testing sets, and then trains multiple KNN models using
different k values.

For each k value tested, the program evaluates the model's accuracy on
the testing data and stores the result. After all k values have been
evaluated, the program identifies the k value with the highest accuracy
and displays the results.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target # type: ignore

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Store accuracy results
accuracies = []
k_values = range(1, 21)

# Train and evaluate models for different k values
for k in k_values:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    accuracies.append(accuracy)

# Determine the best k value
best_accuracy = max(accuracies)
best_k = accuracies.index(best_accuracy) + 1

# Display results
print("K Value vs Accuracy:")
for i, accuracy in enumerate(accuracies, start=1):
    print(f"k = {i}: Accuracy = {accuracy:.4f}")

print("\nOptimal k value:")
print(f"Best k = {best_k} with accuracy = {best_accuracy:.4f}")