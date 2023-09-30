import numpy

print('perception')

inputs = numpy.array([
[1,0,0],
[1,0,1],
[1,1,0],
[1,1,1]
])

expected = numpy.array([0, 1, 1, 1])

def heaviside(sum):
    if sum >= 0:
        return 1
    else:
        return 0

def perception_eval(inputs, expected, w):
    result = []
    for index, input in enumerate(inputs):
        sum = numpy.dot(w, input) # dot product
        result.append(heaviside(sum))
    return result

w = numpy.array([[1,1,1], [-1,1,1]])

result = perception_eval(inputs, expected, w[0])
result = perception_eval(inputs, expected, w[1])
print('expected: {}; result: {}; with weights: {}'.format(expected, result, w[0]))
print('expected: {}; result: {}; with weights: {}'.format(expected, result, w[1]))
