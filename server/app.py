from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
import base64
from sklearn.externals import joblib
import numpy as np
import os
import requests
import json
import cv2
import face_recognition
import time
from multiprocessing import Process



app = Flask(__name__)
model = joblib.load('model/classifier.pkl')
# preds_info = {
#     0: 'Adil',
#     1: 'Rohan',
#     2: 'Rui'
# }

email_info = {
    'Adil': 'adil99@gmail.com',
    'Rui': 'raguiar@gmail.com',
    'Rohan': 'rohan@gmail.com',
    'Christian': 'christian@gmail.com'
}

hometown_info = {
    'Rui': "Palo Alto, CA",
    'Adil': "Vancouver, Canada",
    'Rohan': 'San Francisco, CA',
    'Christian': 'Beijing, China'
}

likes_info = {
    'Rui': "Running, Swimming",
    'Adil': "Biking, Hiking",
    'Rohan': 'Hackathons, Movies, Running',
    'Christian': 'Making Videos, Soccer'
}

fb_links = {
    "Rui": "https://www.facebook.com/rui.aguiar.125",
    "Adil": "https://www.facebook.com/4d117",
    "Rohan": "https://www.facebook.com/profile.php?id=100015096588541",
    "Christian": "https://www.facebook.com/profile.php?id=100009333463110"
}


IMG_SIZE = 128
SCALE_FACTOR = 5.5
data_dir = 'model/data/rohan/'
img_num = 1

picture_of_rui = face_recognition.load_image_file("picture_of_rui.jpg")
rui_face_encoding = face_recognition.face_encodings(picture_of_rui)[0]
picture_of_adil = face_recognition.load_image_file("picture_of_adil.jpg")
adil_face_encoding = face_recognition.face_encodings(picture_of_adil)[0]
picture_of_rohan = face_recognition.load_image_file("picture_of_rohan.jpg")
rohan_face_encoding = face_recognition.face_encodings(picture_of_rohan)[0]
picture_of_christian = face_recognition.load_image_file("picture_of_christian.jpg")
christian_face_encoding = face_recognition.face_encodings(picture_of_christian)[0]


@app.route('/')
def hello_world():
    return "Hello, world"
    # return _get_graph_api_details('rui')


def get_access_token(name):
    if name == 'Rui':
        access_token = os.environ['RUI_ACCESS_TOKEN']
    elif name == 'Adil':
        access_token = os.environ['ADIL_ACCESS_TOKEN']
    elif name == 'Rohan':
        access_token = os.environ['ROHAN_ACCESS_TOKEN']
    elif name == 'Christian':
        access_token = os.environ['CHRISTIAN_ACCESS_TOKEN']
    return access_token

def _get_graph_api_details(name):
    access_token = get_access_token(name)
    r = requests.get("https://graph.facebook.com/me?fields=hometown,likes,email&access_token=" + access_token)
    content = json.loads(r.content)
    if 'likes' in content:
        likes = content['likes']['data'][-2]['name']
        likes += ", " + content['likes']['data'][-5]['name']
    else:
        likes = likes_info[name]
    if 'email' in content:
        email = content['email']
    else:
        email = email_info[name]
    link = fb_links[name]
    if 'hometown' in content:
        hometown = content['hometown']['name'],
    else:
        hometown = hometown_info[name]
    return jsonify({"name": name, "email": email, "hometown": hometown, "likes": likes, "link": link})

def get_face_class(face_encoding):
    results = face_recognition.face_distance([rui_face_encoding, adil_face_encoding, rohan_face_encoding, christian_face_encoding], face_encoding)
    if results[0] == min(results):
        return 'Rui'
    if results[1] == min(results):
        return 'Adil'
    if results[2] == min(results):
        return 'Rohan'
    if results[3] == min(results):
        return 'Christian'
    return 'Rui'

def _get_prediction(json_data):
    global img_num
    
    image = json_data['photo']
    decoded_image = base64.b64decode(image)
    bytes_image = BytesIO(decoded_image)
    pil_image = Image.open(bytes_image)
#     pil_image.save('phone_img_before_crop.jpg')
    picture = np.array(pil_image)
#     picture = face_recognition.load_image_file("phone_img_before_crop.jpg")
    face_encoding = face_recognition.face_encodings(picture)[0]
    prediction = get_face_class(face_encoding)
    return prediction


@app.route('/classify', methods=['POST'])
def classify():
    json_data = request.get_json(force=True)
    print("going to get preds")
    name = _get_prediction(json_data)
    return _get_graph_api_details(name)
    return jsonify({"name": name, "email": email_info[name], "hometown": hometown_info[name], "likes": likes_info[name], "link": fb_links[name]})


if __name__ == '__main__':
    app.run(debug=False, use_debugger=True, use_reloader=True, passthrough_errors=True)
