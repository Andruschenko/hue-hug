import base64
import cStringIO

import numpy as np
from flask import Flask, jsonify, make_response, request
from PIL import Image

from src.processor.cutter import ClairesCutter

app = Flask(__name__)

# Routes


@app.route('/api/v1/', methods=['GET'])
def hello_world():
    print 'Hello World!'
    return jsonify({'hello': 'world'})

@app.route('/api/v1/echo', methods=['POST'])
def echo():
    jsonData = request.get_json(force=True)
    return jsonify(jsonData)

@app.route('/api/v1/submit', methods=['POST'])
def process_image():
    jsonData = request.get_json(force=True)

    if len(jsonData['image']) < 20:
        return jsonify({'error': 'image is too short'})

    cutter = ClairesCutter(jsonData['image'], 'base64')
    positions = cutter.getPositions()
    pieces = {'red': [], 'green': [], 'blue': []}
    for color in positions:
        for position in positions[color]:
            imagePart = Image.fromarray(cutter.crop(position))
            buffer = cStringIO.StringIO()
            imagePart.save(buffer, format="JPEG")
            imageAsBase64 = base64.b64encode(buffer.getvalue())
            pieces[color].append(imageAsBase64)
    return jsonify({'pieces': pieces})


# Pretty error handling
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request. Please check your request syntax.'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Nothing found at this route.'}), 404)


@app.errorhandler(405)
def not_found(error):
    return make_response(jsonify({'error': 'Request method not allowed.'}), 405)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
