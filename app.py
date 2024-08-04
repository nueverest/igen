import requests

from flask import Flask, render_template, request

from image_gen_togetherai import AiImage
from options import Options


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    options = Options()
    grid = options.grid

    user_input = ''
    images = []    
    if request.method == 'POST':
        topics = [
            'Man', 'Woman', 'Animal', 'Plant', 'Vehicle',
            'Star Wars', 'Barbie', 'Anime', 'Matrix', 'Avengers', 
            'Photo', 'Sculpture', 'Painting', 'Sketch', 'Carving',
            'Minecraft', 'GTA', 'Fornite', 'League of Legends', 'World of Warcraft', 
            'Funny', 'Somber', 'Still', 'Happy', 'Relaxed',
        ]

        user_inputs = []
        for topic in topics:
            # print(request.form[topic])
            user_inputs.append(request.form[topic])
        
        user_input = options.generate_prompt(user_request_form=user_inputs)
        # ai_image = AiImage()
        # images = ai_image.generate(user_input)
    return render_template('index.html', grid=grid, user_input=user_input, images=images)


@app.route('/text', methods=['GET', 'POST'])
def text():
    user_input = ''
    images = []
    if request.method == 'POST':
        user_input = request.form['user_input']

        ai_image = AiImage()
        images = ai_image.generate(user_input)
    return render_template('text_prompt.html', user_input=user_input, images=images)


if __name__ == '__main__':
    app.run(debug=True)