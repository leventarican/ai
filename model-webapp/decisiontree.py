import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

dataset = pd.read_csv('testbench.csv')
#print(dataset.shape)
#print(dataset.head())

X = dataset.drop('result', axis=1)
y = dataset['result']
#print(X)
#print(y)

# leave 20% of data for test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
#print(X_train)

classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

pickle.dump(classifier,open("model.pkl","wb"))

#y_pred = classifier.predict(X_test)
#y_pred = classifier.predict([[0.32924,-4.4552,4.5718,-0.9888]])
y_pred = classifier.predict([[0.55298,-3.4619,1.7048,1.1008]])
print(y_pred)
