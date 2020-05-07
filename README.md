# artificial intelligence

TODO: move repositories
* https://github.com/leventarican/ml
* https://github.com/leventarican/neuronal-network

# sample flask app
* for deploying the model i use flask
* helloflask.py is sample hello world flask app.

## run option 0
* run it with:
```
export FLASK_APP=helloflask.py
python -m flask run
```
* open browser (or curl -i) http://127.0.0.1:5000/
* debug mode can be activated by
```
export FLASK_ENV=development
```

## run option 1
* call app.run function in main
```
if __name__ == '__main__':
    app.run(debug=True)
```

# ML
* Machine learning is rapidly moving closer to where data is collected — edge devices.

# links
famous ml dataset: fisher's iris data set (iris.data)
https://archive.ics.uci.edu/ml/datasets/iris
