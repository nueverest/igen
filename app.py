from urllib.parse import urljoin

from flask import Flask, render_template, request, redirect, flash, url_for
import os
import random
from image_gen_togetherai import AiImage


app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/', methods=['GET', 'POST'])
def index():
    # if request.method == 'POST':
    #     return redirect(url_for('upload_form'))
    # else:
    #     return render_template('index.html')
    return redirect(url_for('upload_form'))

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the post request has the file part
    print("here is request files ", request.files)
    # if 'file' not in request.files:
    #     flash('No file part')
    #     return redirect(url_for('upload_form'))

    file = request.files['file']
    print("here is file name ", file.filename, file.name)

    # # If the user does not select a file, the browser submits an empty file without a filename
    # if file.filename == '':
    #     flash('No selected file')
    #     return redirect(url_for('upload_form'))
    current_dir = os.path.abspath('.')
    upload_path = os.path.join(current_dir, 'static', 'upload')
    try:
        if not os.path.exists(upload_path):
            os.makedirs(upload_path)
    except Exception as e:
        print(f"An error occurred: {e}")
    file_path = os.path.join(upload_path, file.name)
    print("here is file path ", file_path)
    file.save(file_path + '.png')
    ai_image = AiImage()

    path = "static/upload/" + file.name
    generate_file_path = urljoin("http://127.0.0.1:5000/", path)
    print("here is generate file path ", generate_file_path)
    images = ai_image.generate(generate_file_path)

    flash('File successfully uploaded')
    return render_template('index.html', images=images)

@app.route('/upload_form')
def upload_form():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)