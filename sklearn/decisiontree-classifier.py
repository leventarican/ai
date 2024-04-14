from sklearn import datasets
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd

# Assuming iris.csv is structured similarly to the sklearn iris dataset
path = "iris.csv"
data = pd.read_csv(path, delimiter=",")

col_name = 'species'
# Extract the species column
col = data[col_name]
# Drop the species column from the data
data = data.drop([col_name], axis=1)

# Split the data into training and testing sets
train_data, test_data, train_col, test_col = train_test_split(data, col, test_size=0.03, random_state=42)

# Create the model
model = tree.DecisionTreeClassifier()

# Train the model
model.fit(train_data, train_col)

# Predict with the model
predicted_col = model.predict(test_data)

# If you want to compare predictions with the actual species names
print("\nComparing predictions with actual species names:")
actual_vs_predicted = pd.DataFrame({'Actual': test_col, 'Predicted': predicted_col})
print(actual_vs_predicted.reset_index(drop=True))

score = metrics.accuracy_score(test_col, predicted_col)
print(f"accuracy score: {score}")
