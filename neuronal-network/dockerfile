FROM tensorflow/tensorflow:latest-py3
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./basic_classification.py
