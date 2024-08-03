import base64
import json
import uuid
import io
import os

from PIL import Image


class ImageEncoder:
    def __init__(self, filename, image_data):
        self.filename = filename + '-' + uuid.uuid4().hex
        self.image_data = image_data
        current_dir = os.path.abspath('.')
        self.path = os.path.join(current_dir,'images', 'igen', self.filename + '.png')        

    def encode_image(self):
        decoded_data = base64.b64decode(self.image_data)
        image_json = {
            "image": decoded_data.decode("utf-8")
        }
        return image_json

    def write_to_file(self):
        # RAW Base64
        image_json = self.encode_image()
        with open(self.path, "w") as f:
            json.dump(image_json, f)

    def convert_to_png(self):
        decoded_data = base64.b64decode(self.image_data)
        image = Image.open(io.BytesIO(decoded_data))
        image.save(self.path, "PNG")