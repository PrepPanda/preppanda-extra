from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from encrypt import encrypt_string
from extract_data import extract_data
from save_to_json import save_to_json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'Files/data/'
JSON_FOLDER = 'Files/json/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSON_FOLDER'] = JSON_FOLDER

Allowed_Extensions = set(['docx', 'pdf'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Allowed_Extensions


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_name = filename.split('.')[0]
        file_extension = filename.split('.')[1]
        filename = encrypt_string(file_name) + '.' + file_extension
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        data = extract_data(filepath)
        print(data)

        json_filename = filename.split('.')[0] + '.json'
        json_filepath = os.path.join(app.config['JSON_FOLDER'], json_filename)
        save_to_json(data, json_filepath)

        return jsonify({'data': data, 'message': 'File successfully uploaded'}), 200
    return jsonify({'error': 'Invalid file'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
