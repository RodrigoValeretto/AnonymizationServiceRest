from flask import request, jsonify
from flask_restful import Resource
from PIL import Image
from deepface import DeepFace
import io
import logging
import base64

logger = logging.getLogger(__name__)


class Anonymizer(Resource):
    def post(self):
        try:
            rq = request.json

            print("Request received: ", rq)

            image_bytes = rq.get("Image")

            image = Image.open(io.BytesIO(base64.b64decode(image_bytes)))

            embeddings = DeepFace.represent(image, model_name="Facenet")

            logger.info("Embeddings returned")

            result = jsonify({"anonymizedImage": embeddings})

            logger.debug("Result", result)

            return result, 200
        except Exception as ex:
            logger.error("An error ocurred: %s", ex)
            return "Error", 500
