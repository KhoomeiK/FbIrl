from flask import Flask, request
from PIL import Image
from sklearn.externals import joblib
import numpy as np
import json

app = Flask(__name__)
model = joblib.load('model/classifier.pkl')


def img_to_vec(img):
    return np.array(img).ravel()


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/classify', methods=['POST'])
def classify():
    image = request.files['image']
    pil_image = Image.open(image)
    img_vec = img_to_vec(pil_image)
    prediction = model.predict([img_vec])[0]
    return {"prediction": prediction}


if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)
