from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
import base64
from sklearn.externals import joblib
import numpy as np
import json

app = Flask(__name__)
model = joblib.load('model/classifier.pkl')
preds_info = {
    0: 'adil',
    1: 'rohan',
    3: 'christian',
    4: 'rui'
}
IMG_SIZE = 128

def img_to_vec(img):    
    return np.array(img).ravel()


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/classify', methods=['POST'])
def classify():
    json_data = request.get_json(force=True)
    image = json_data['photo']
    decoded_image = base64.b64decode(image)
    bytes_image = BytesIO(decoded_image)
    pil_image = Image.open(bytes_image)
    left = int(json_data['x'])
    upper = int(json_data['y'])
    right = int(json_data['width']) + left
    lower = int(json_data['height']) + upper 
    pil_image = pil_image.crop((left, upper, right, lower))
    pil_image = pil_image.resize((IMG_SIZE, IMG_SIZE))
    img_vec = img_to_vec(pil_image)
    prediction = model.predict([img_vec])[0]
    name = preds_info[prediction]
    return jsonify({"name": name})


if __name__ == '__main__':
    app.run(debug=True, use_debugger=True, use_reloader=True, passthrough_errors=True)
