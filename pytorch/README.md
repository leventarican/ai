PyTorch examples

# GAN

The MNIST dataset is a well-known dataset of handwritten digits, consisting of 60,000 training images and 10,000 test images. Each image is a grayscale image of size 28x28 pixels.

A common PyTorch convention is to save models using either a .pt or .pth file extension.
* https://pytorch.org/tutorials/beginner/saving_loading_models.html

# run
```bash
# train model, download data
python gan.py

# time for create models
# real	6m54.486s
# user	17m30.973s

# generate image
python gan-run.py
```

# install
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```