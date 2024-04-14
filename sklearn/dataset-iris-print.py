import pandas as pd

# Load the Iris dataset from the CSV file
iris_data = pd.read_csv("iris.csv")

# Print the head of the DataFrame (the first 5 rows)
print(iris_data.head())

#    sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm) species
# 0                5.1               3.5                1.4               0.2  setosa
# 1                4.9               3.0                1.4               0.2  setosa
# 2                4.7               3.2                1.3               0.2  setosa
# 3                4.6               3.1                1.5               0.2  setosa
# 4                5.0               3.6                1.4               0.2  setosa
