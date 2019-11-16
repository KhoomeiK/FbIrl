from flask import Flask, request
from PIL import Image
from server.model.dummy_model import Model
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/classify', methods=['POST'])
def classify():
    image = request.files['image']
    pil_image = Image.open(image)

    model = Model()
    return json.dumps(model.predict(pil_image))


if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)
