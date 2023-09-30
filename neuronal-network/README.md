# neuronal network, basic classification
* tech stack: tensorflow (keras), python, docker
* based on: <https://www.tensorflow.org/tutorials/keras/basic_classification>
__run__
```
docker build --tag basic_classification .
docker run basic_classification
```
__result__
```
Epoch 1/2
60000/60000 [==============================] - 11s 176us/sample - loss: 0.4996 - acc: 0.8243
Epoch 2/2
60000/60000 [==============================] - 10s 161us/sample - loss: 0.3733 - acc: 0.8649
actual: ankle boot; prediction: ankle boot
actual: pullover; prediction: pullover
actual: trouser; prediction: trouser
actual: trouser; prediction: trouser
actual: shirt; prediction: shirt
actual: trouser; prediction: trouser
actual: coat; prediction: coat
actual: shirt; prediction: shirt
actual: sandal; prediction: sandal
actual: sneaker; prediction: sneaker
```
