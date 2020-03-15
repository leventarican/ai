# object detection with OpenCV - DNN

* dev environment: linux (= ubuntu)

__build OpenCV from source__
* https://docs.opencv.org/4.2.0/d9/d52/tutorial_java_dev_intro.html
```
git clone git://github.com/opencv/opencv.git
cd opencv
git checkout 2.4
mkdir build
cd build
```
* generate Makefile: `cmake -DBUILD_SHARED_LIBS=OFF ..`
* build: `make -j8`. this could take some time (~ minutes)

# object detection with YOLO (you only look once)
__TODO__ not finished yet
* http://origamidocs.hellonico.info/#/?id=origami-computer-vision-made-simple
