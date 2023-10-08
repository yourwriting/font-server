from flask import Flask, request, send_file
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

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('files')
    for f in files:
        f.save('./images/' + secure_filename(f.filename))
    return 'upload success!'


@app.route('/combine', methods=['GET'])
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


@app.route('/concat', methods=['GET'])
def concat():
    folder = './letters2'
    image_paths = [os.path.join(folder, f)
                for f in os.listdir(folder) if f.endswith('.PNG')]
    image_paths = sorted(image_paths)

    image = concatImg.concat_images(image_paths, (33, 33), (84, 133))
    return 'concat success!'


@app.route('/create', methods=['GET'])
def create():
    pngtottf.makefont(33, 33)

    with open('font.ttf', 'rb') as font_file:
        font_binary = io.BytesIO(font_file.read())
    return send_file(font_binary, mimetype='application/font-sfnt')

if __name__ == '__main__':
    app.run()
