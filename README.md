# artificial intelligence

# AI

model checkpoint
----------------
in machine learning, a model checkpoint is a file containing the weights (i.e., the parameters) of a trained model at a particular point during training.

model card
----------
a model card is a document that provides information about a machine learning model. I.e.: 
* https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md
* https://github.com/tatsu-lab/stanford_alpaca/blob/main/model_card.md

# pytorch
a ML framework. See example `pytorch/`

# flask
* for deploying the model i use flask
* `model-webapp/helloflask.py` is sample hello world flask app.

option 0
--------
* run it with:
```bash
export FLASK_APP=helloflask.py
python -m flask run
```
* open browser (or curl -i) http://127.0.0.1:5000/
* debug mode can be activated by
```bash
export FLASK_ENV=development
```

option 1
--------
* call app.run function in main
```python
if __name__ == '__main__':
    app.run(debug=True)
```

# links
famous ml dataset: fisher's iris data set (iris.data)
https://archive.ics.uci.edu/ml/datasets/iris
