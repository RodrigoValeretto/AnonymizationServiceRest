from flask import Flask
from flask_restful import Api
from anonymizer import Anonymizer

app = Flask(__name__)
api = Api(app)

api.add_resource(Anonymizer, "/anonymize")

if __name__ == "__main__":
    app.run(debug=True)
