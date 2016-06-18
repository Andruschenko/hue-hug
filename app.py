## External imports
from flask import Flask, make_response, request, jsonify
import json

## Local imports
from src.processor.crop import getImagesAsJson

app = Flask(__name__)

## Routes

@app.route('/api/v1/', methods=['GET'])
def hello_world():
    return jsonify({ 'hello': 'world' })

@app.route('/api/v1/submit', methods=['POST'])
def process_image():
    image = request.form['image']

    # ## Debugging
    # with open('images/imageTropical.json') as dataFile:
    #     data = json.load(dataFile)
    #     imageAsJson = getImagesAsJson(data['src'])

    imageAsJson = getImagesAsJson(image)
    return jsonify({ 'colors': imageAsJson })


## Pretty error handling

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Nothing found at this route.'}), 404)

@app.errorhandler(405)
def not_found(error):
    return make_response(jsonify({'error': 'Request method not allowed.'}), 405)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')