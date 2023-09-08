from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('files')
    for f in files:
        f.save('./images/' + secure_filename(f.filename))
    return 'done!'

if __name__ == '__main__':
    app.run()
