from flask import Flask, request, jsonify
from PIL import Image
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
    image = request.files['photo']
    pil_image = Image.open(image)
    print(request)
    left = int(request.form.get('x'))
    upper = int(request.form.get('y'))
    right = int(request.form.get('width')) + left
    lower = int(request.form.get('height')) + upper 
    pil_image = pil_image.crop((left, upper, right, lower))
    pil_image = pil_image.resize((IMG_SIZE, IMG_SIZE))
    img_vec = img_to_vec(pil_image)
    prediction = model.predict([img_vec])[0]
    name = preds_info[prediction]
    return jsonify({"name": name})


if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)
