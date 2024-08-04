from flask import Flask, render_template, request,jsonify
import os
import random
from image_gen_togetherai import AiImage


app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         user_input = request.form.get('user_input', '')  # 安全获取 user_input
#         if user_input:
#             ai_image = AiImage()
#             images = ai_image.generate(user_input)  # 生成基于用户输入的图像链接
#             return jsonify({'images': images})  # 返回图像链接的 JSON
#         else:
#             return jsonify({'error': 'No input provided'}), 400  # 没有输入时返回错误
#     else:
#         # 对于 GET 请求，渲染并返回初始 HTML 页面
#         return render_template('index.html')

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
