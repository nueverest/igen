from flask import Flask, render_template, request
import os
import random
from image_gen_togetherai import AiImage
from image_gen_stability import StableImage


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


@app.route('/image2image', methods=['GET', 'POST'])
def image2image():
    images = []
    output_format = "png"
    if request.method == 'POST':
        # upload file
        theme = request.form['theme']
        if theme == "star_war":
            file = request.files['file']
            prompt = "render the person in a star wars setting hold random colored light saber"
            print(prompt)
            current_dir = os.path.abspath('.')
            basename, _ = os.path.splitext(file.filename)
            image_path = os.path.join(current_dir, "static", "img", file.filename)
            output_path = os.path.join(current_dir, "static", "img", f"{theme}_{basename}.{output_format}")
            print("input image", file.filename, image_path, output_path)
            if not os.path.exists(output_path):
                print("invoking AI model...")
                ai_image = StableImage()
                response = ai_image.image_control(image_path, prompt, output_path=output_path, output_format=output_format)
                print(response)
            images = [os.path.basename(image_path), os.path.basename(output_path)]
        
        if theme == "disney":
            file = request.files['file']
            prompt = "render the picture in disney land play with cartoon style"
            print(prompt)
            current_dir = os.path.abspath('.')
            basename, _ = os.path.splitext(file.filename)
            image_path = os.path.join(current_dir, "static", "img", file.filename)
            output_path = os.path.join(current_dir, "static", "img", f"{theme}_{basename}.{output_format}")
            if not os.path.exists(output_path):
                print("invoking AI model...")
                ai_image = StableImage()
                response = ai_image.image_control(image_path, prompt, output_path=output_path, output_format=output_format)
                print(response)
            images = [os.path.basename(image_path), os.path.basename(output_path)]

    return render_template('image2image.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)