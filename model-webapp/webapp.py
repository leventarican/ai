import pickle
import flask
from flask import request

app = flask.Flask(__name__)

#loading my model
model = pickle.load(open("model.pkl","rb"))

# 2d array
# curl localhost:5000/ -d '{"feature_array":"[[0.1, 0.2, 0.3], [1.0, 2.0, 3.0]]"}'
array2d = [[0.1, 0.2, 0.3], [1.0, 2.0, 3.0]]

# access with
# curl localhost:5000/ -d '{"feature_array": "bar"}'
@app.route('/', methods=['POST'])
def index():

    print('predictions...')

    #getting an array of features from the post request's body
    # force json=true. we dont need to sent application/json mimetype then.
    # # curl localhost:5000/ -d '{"feature_array": "bar"}' -H 'Content-Type: application/json'
    feature_array = request.get_json(force=True)['feature_array']

    print(feature_array)

    #creating a response object
    #storing the model's prediction in the object
    response = {}
    response['predictions'] = model.predict([feature_array]).tolist()

    print(response)

    #returning the response object as json
    return flask.jsonify(response)

@app.route('/dev', methods=['POST'])
def dev():
    print('dev...')
    feature_array = request.get_json(force=True)['feature_array']
    print(feature_array)

    print('predictions...')
    response = {}
    response['predictions'] = model.predict([feature_array]).tolist()

    return '<code>dev</code>'

@app.route('/ping')
def ping():
    return '<code>ping</code>'
