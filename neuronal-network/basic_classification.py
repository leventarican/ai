import tensorflow as tf
from tensorflow import keras
import numpy as np
#import matplotlib.pyplot as plt

# data
(train_images, train_labels), (test_images, test_labels) = keras.datasets.fashion_mnist.load_data()
class_names = ['tshirt', 'trouser', 'pullover', 'dress', 'coat', 'sandal', 'shirt', 'sneaker', 'bag', 'ankle boot']
train_images = train_images / 255.0
test_images = test_images / 255.0

# create model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),  # 28x28 pixel images
    keras.layers.Dense(128, activation="relu"),   # activation function = rectify linear unit
    keras.layers.Dense(10, activation="softmax")
])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# train model
model.fit(train_images, train_labels, epochs=2)

# variable name says everything
prediction = model.predict(test_images)

# show result
for i in range(10):
    act = "actual: " + class_names[test_labels[i]]
    pre = "prediction: " + class_names[np.argmax(prediction[i])]
    print(act + "; " + pre)
    #plt.grid(False)
    #plt.imshow(test_images[i], cmap=plt.cm.binary)
    #plt.xlabel(act)
    #plt.title(pre)
    #plt.show()
