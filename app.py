from flask import Flask, render_template, request,jsonify
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
        images = ai_image.generate(user_input)
    return render_template('index.html', user_input=user_input, images=images)

if __name__ == '__main__':
    app.run(debug=True)
