from sklearn import datasets
import matplotlib.pyplot as plt
from collections import Counter

# Load the Iris dataset
iris = datasets.load_iris()

# Extract the data and target values
data = iris.data
target = iris.target

# Define the feature names
feature_names = iris.feature_names
print(f"feature: {feature_names}")

# Define the target names
target_names = iris.target_names

# Define pastel colors for each species
colors = ['#FF9999', '#99FF99', '#9999FF']  # Pastel red, green, blue

# Count the number of samples for each species
species_count = Counter(target)

# Print the count for each species
for i, name in enumerate(target_names):
    print(f"{name}: {species_count[i]} samples")

# Create a scatter plot for the first two features with pastel colors
plt.figure(figsize=(6, 4))
for i in range(len(target_names)):
    plt.scatter(data[target == i, 0], data[target == i, 1], c=colors[i], label=target_names[i], edgecolor='k')

# Add a legend, labels, and title
plt.legend(loc='upper right')
plt.xlabel(feature_names[0])
plt.ylabel(feature_names[1])
plt.title('Iris Dataset: Sepal Length vs Sepal Width')
plt.show()
