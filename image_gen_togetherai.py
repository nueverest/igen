from together import Together

from keys import TOGETHER_API_KEY
from image_encoder import ImageEncoder


class AiImage:
    def __init__(self):
        self.client = Together(api_key=TOGETHER_API_KEY)

    def generate(self, prompt):
        qualifiers = {
            'harrypotter': 'with a harry potter newpaper theme',
            '2dcartoon': 'as a two dimensional cartoon',
            '3dcartoon': 'as a three dimensional cartoon',
            'monalisa': 'as the mona lisa',
            'lion': 'as a lion',
            'starwars': 'with a star wars theme'
        }

        models = {
            # 'stable-diffusion-2_1': 'stabilityai/stable-diffusion-2-1',               # $0.01 (n=4)
            # 'stable-diffusion-1_5-runwayml': 'runwayml/stable-diffusion-v1-5',        # $0.01 (n=4) did not handle URL properly
            'stable-diffusion-xl': 'stabilityai/stable-diffusion-xl-base-1.0',  # $0.01 (n=4)
            # 'realistic-vision': 'SG161222/Realistic_Vision_V3.0_VAE',                 # $0.01 (n=4)
            # 'analog-diffusion': 'wavymulder/Analog-Diffusion',                        # $0.01 (n=4)
            # 'open-journey-4': 'prompthero/openjourney',                               # $0.01 (n=4)
            # 'dragonfly': 'togethercomputer/Llama-3-8B-Dragonfly-v1',
            # 'dragonfly-med': 'togethercomputer/Llama-3-8B-Dragonfly-Med-v1',
        }

        imageFileNames = []
        for key, value in models.items():
            response = self.client.images.generate(
                prompt=prompt,
                model=value,
                steps=10,
                n=4  # Number of images to generate.
            )

            filename = prompt.replace(' ', '-')
            filename += '-' + key

            # Save all 'n' images where 'n' is the number of images to generate
            for n in range(len(response.data)):
                img = ImageEncoder(filename, response.data[n].b64_json)
                img.convert_to_png()
                imageFileNames.append(img.filename)
        return imageFileNames
