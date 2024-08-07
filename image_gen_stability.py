from io import BytesIO
import json
import os
# from PIL import Image
from datetime import datetime
import requests
import time
from keys import STABLE_API_KEY


class StableImage:
    def __init__(self):
        self.api_key = STABLE_API_KEY

    def send_generation_request(
        self,
        host,
        params
    ):
        headers = {
            "Accept": "image/*",
            "Authorization": f"Bearer {self.api_key}"
        }

        # Encode parameters
        files = {}
        image = params.pop("image", None)
        mask = params.pop("mask", None)
        if image is not None and image != '':
            files["image"] = open(image, 'rb')
        if mask is not None and mask != '':
            files["mask"] = open(mask, 'rb')
        if len(files)==0:
            files["none"] = ''

        # Send request
        print(f"Sending REST request to {host}...")
        response = requests.post(
            host,
            headers=headers,
            files=files,
            data=params
        )
        if not response.ok:
            raise Exception(f"HTTP {response.status_code}: {response.text}")

        return response

    def image_control(
            self,
            image_path,
            prompt,
            output_path,
            negative_prompt="",
            control_strength=0.65,
            seed=42,
            output_format="png"
    ):
        if not os.path.exists(image_path):
            Warning(f"{image_path} not exits")
            return {"status_code": 404, "error": f"{image_path} does not exists."}
        if not prompt.strip():
            Warning("prompt can not be empty")
            return {"status_code": 400, "error": "empty prompt"}
        
        #print(image_path, prompt)
        #return {"status_code": 200, "image": ""}
    
        host = f"https://api.stability.ai/v2beta/stable-image/control/structure"
        params = {
            "control_strength" : control_strength,
            "image" : image_path,
            "seed" : seed,
            "output_format": output_format,
            "prompt" : prompt,
            "negative_prompt" : negative_prompt
        }

        response = self.send_generation_request(
            host,
            params
        )

        # Decode response
        output_image = response.content
        finish_reason = response.headers.get("finish-reason")
        seed = response.headers.get("seed")

        # Check for NSFW classification
        if finish_reason == 'CONTENT_FILTERED':
            raise Warning("Generation failed NSFW classifier")

        # Save result
        # filename, _ = os.path.splitext(os.path.basename(image_path))
        # output_path = f"/tmp/{filename}_{seed}.{output_format}"
        print(f"Saved image {output_path}")
        with open(output_path, "wb") as f:
            f.write(output_image)

        return {
            "status_code": 200,
            "image_path": output_path
        }
    