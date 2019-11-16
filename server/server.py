from flask import Flask, request
from PIL import Image
from .model.dummy_model import Model
app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/classify', methods=['POST'])
def classify():
    image = request.files['file']
    pil_image = Image.open(image)

    model = Model()
    return model.predict(pil_image)


