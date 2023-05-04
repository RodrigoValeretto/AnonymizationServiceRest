# Anonymization Service Rest

A python anonymization server that connects via rest with comparison service, another repository from this github profile. This service uses DeepFace python library to return embeddings from an image that ComparisonService sends via rest.

## Configuration

To run this server it is important to have python installed on your machine. It can be obtained in https://www.python.org/downloads/

After that, using pip, install all the dependencies.

```shell
pip install pillow deepface numpy flask flask-restful
```

To run the app
```shell
python3 app.py
```

