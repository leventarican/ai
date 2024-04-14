import pandas as pd
from sklearn import datasets

# Load the Iris dataset
iris = datasets.load_iris()

# Create a DataFrame with the data and the feature names as columns
df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)

# Optionally, if you want to include the target (species) in the CSV
df_iris['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Export the DataFrame to a CSV file
df_iris.to_csv('iris.csv', index=False)
