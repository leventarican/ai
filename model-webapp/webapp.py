import pickle
import flask
from flask import request
import numpy as np

app = flask.Flask(__name__)

#loading my model
model = pickle.load(open("model.pkl","rb"))

# curl -i -H "Content-Type: application/json" -X POST -d '{"feature_array":[[0.55298, -3.4619, 1.7048, 1.1008]]}' http://127.0.0.1:5000/predict
# HTTP/1.0 200 OK
# Content-Type: application/json
# Content-Length: 32
# Server: Werkzeug/0.15.4 Python/3.5.3
# Date: Sat, 13 Jul 2019 21:42:13 GMT
#
# {
#   "prediction": [
#     1
#   ]
# }
@app.route('/predict', methods=['POST'])
def dev():
    # force json=true. we dont need to sent application/json mimetype then.
    feature_array = request.get_json(force=True)['feature_array']
    print(feature_array)
    print(type(feature_array))
    print('prediction')
    response = {}
    response['prediction'] = model.predict(feature_array).tolist()
    print(response['prediction'])

    return flask.jsonify(response)

@app.route('/ping')
def ping():
    return '<code>pong</code>'

if __name__ == '__main__':
    app.run(debug=True)
