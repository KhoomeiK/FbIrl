from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
import base64
from sklearn.externals import joblib
import numpy as np
import os
import requests
import json

app = Flask(__name__)
model = joblib.load('model/classifier.pkl')
preds_info = {
    0: 'Adil',
    1: 'Rohan',
    2: 'Rui'
}

email_info = {
    'Adil': 'adil99@gmail.com',
    'Rui': 'raguiar@gmail.com',
    'Rohan': 'rohan@gmail.com'
}

hometown_info = {
    'Rui': "Palo Alto, CA",
    'Adil': "Vancouver, Canada",
    'Rohan': 'San Francisco, CA'
}

likes_info = {
    'Rui': "Running, Swimming",
    'Adil': "Biking, Hiking",
    'Rohan': 'Hackathons, Movies, Running'
}


IMG_SIZE = 128
SCALE_FACTOR = 5.5
data_dir = 'model/data/rohan/'
img_num = 1

def img_to_vec(img):
    return np.array(img).ravel()


@app.route('/')
def hello_world():
    return "Hello, world"
    # return _get_graph_api_details('rui')


def get_access_token(name):
    if name == 'Rui':
        access_token = os.environ['RUI_ACCESS_TOKEN']
    elif name == 'Adil':
        access_token = os.environ['ADIL_ACCESS_TOKEN']
    else:
        access_token = os.environ['ROHAN_ACCESS_TOKEN']
    return access_token

def _get_graph_api_details(name):
    access_token = get_access_token(name)
    r = requests.get("https://graph.facebook.com/me?fields=hometown,likes,email&access_token=" + access_token)
    content = json.loads(r.content)
    likes = content['likes']['data'][-2]['name']
    likes += ", " + content['likes']['data'][-5]['name']
    email = content['email']
    if 'hometown' in content:
        hometown = content['hometown']['name'],
    else:
        hometown = "Cupertino, CA"
    return jsonify({"name": name, "email": email, "hometown": hometown, "likes": likes})
    

def _get_prediction(json_data):
    global img_num
    image = json_data['photo']
    decoded_image = base64.b64decode(image)
    bytes_image = BytesIO(decoded_image)
    pil_image = Image.open(bytes_image)
    pil_image.save('phone_img_before_crop.jpg')
    left = int(json_data['x']) * SCALE_FACTOR
    upper = int(json_data['y']) * SCALE_FACTOR
    right = int(json_data['width']) * SCALE_FACTOR + left
    lower = int(json_data['height']) * SCALE_FACTOR + upper
    print(left, upper, right, lower)
    pil_image = pil_image.crop((left, upper, right, lower))
    pil_image = pil_image.resize((IMG_SIZE, IMG_SIZE))
    pil_image.save('phone_img_after_crop.jpg')
    # pil_image.save(data_dir + str(img_num) + '.jpg')
    img_num += 1
    img_vec = img_to_vec(pil_image)
    prediction = model.predict([img_vec])[0]
    return prediction


@app.route('/classify', methods=['POST'])
def classify():
    json_data = request.get_json(force=True)
    prediction = _get_prediction(json_data)
    name = preds_info[prediction]
    # return _get_graph_api_details(name)
    return jsonify({"name": name, "email": email_info[name], "hometown": hometown_info[name], "likes": likes_info[name]})


if __name__ == '__main__':
    app.run(debug=True, use_debugger=True, use_reloader=True, passthrough_errors=True)
