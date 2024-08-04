from flask import Flask, render_template, request
import os
import random
from image_gen_togetherai import AiImage


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = ''
    images = []
    if request.method == 'POST':
        user_input = request.form['user_input']

        ai_image = AiImage()
        ai_image.generate(prompt=user_input)

        # Get 4 random images from the static/img directory
        image_files = os.listdir('static/img')
        images = random.sample(image_files, min(4, len(image_files)))
    return render_template('index.html', user_input=user_input, images=images)

if __name__ == '__main__':
    app.run(debug=True)