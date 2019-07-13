from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/ping')
def ping():
    return '<code>pong</code>'

# run with if you dont call app.run
# export FLASK_APP=helloflask.py
# python -m flask run
if __name__ == '__main__':
    app.run(debug=True)
