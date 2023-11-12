from flask import Flask, request, Response
import io
from werkzeug.utils import secure_filename
import os
import prepare
import jamo1
import jamo2
import jamo3
import concatImg
import pngtottf

app = Flask(__name__)
imageSize = 25

@app.route('/', methods=['GET'])
def home():
    return 'your-writing-flask-server'


@app.route('/font/upload', methods=['POST'])
def upload():
    files = request.files.getlist('files')
    for f in files:
        f.save('./images/' + secure_filename(f.filename))
    return 'upload success!'


@app.route('/font/combine', methods=['GET'])
def combine():
    # 이미지 전처리
    prepare.run() 
    # 조합
    jamo1.run()
    jamo2.run()
    input_folder = './crops'
    output_folder = './combinations'
    jamo3.combine_letters3(input_folder, output_folder)
    # resize
    prepare.transletters()
    return 'combine success!'


@app.route('/font/concat', methods=['GET'])
def concat():
    folder = './letters2'
    image_paths = [os.path.join(folder, f)
                for f in os.listdir(folder) if f.endswith('.PNG')]
    image_paths = sorted(image_paths)

    concatImg.concat_images(image_paths, (imageSize, imageSize), (84, 133))
    return 'concat success!'


@app.route('/font/create', methods=['GET'])
def create():
    pngtottf.makefont(imageSize, imageSize)
    
    with open('font.ttf', 'rb') as font_file:
        font_binary = io.BytesIO(font_file.read())
    response = Response(font_binary, content_type='application/x-font-ttf')
    response.headers['Content-Disposition'] = 'inline; filename=font.ttf'
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')