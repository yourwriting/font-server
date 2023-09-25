from flask import Flask, request, send_file
import io
from werkzeug.utils import secure_filename
import os
import concatImg
import prepare
import jamo1
import jamo2
import jamo3
import pngtottf

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('files')
    for f in files:
        f.save('./images/' + secure_filename(f.filename))
    return 'upload success!'

@app.route('/create', methods=['POST'])
def create():
    # prepare.run() # 이미지 전처리
    # jamo1.run() # 조합
    # jamo2.run()
    # input_folder = './crops'
    # output_folder = './combinations'
    # jamo3.combine_letters3(input_folder, output_folder)
    folder = './combinations'

    image_paths = [os.path.join(folder, f)
                for f in os.listdir(folder) if f.endswith('.PNG')]
    image_paths = sorted(image_paths)

    # # Create and save image grid
    image = concatImg.concat_images(image_paths, (50, 50), (84, 133))
    # fontforge
    pngtottf.makefont(50, 50)
    return 'create success!'
    # with open('font.ttf', 'rb') as font_file:
        # font_binary = io.BytesIO(font_file.read())
    # return send_file(font_binary, mimetype='application/font-sfnt')

if __name__ == '__main__':
    app.run()
