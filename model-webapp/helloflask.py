from flask import Flask
app = Flask(__name__)

# run with:
# export FLASK_APP=helloflask.py
# python -m flask run

@app.route('/')
def hello_world():
    return 'hello world'
