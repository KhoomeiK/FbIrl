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

fb_links = {
    "Rui": "https://www.facebook.com/rui.aguiar.125",
    "Adil": "https://www.facebook.com/4d117",
    "Rohan": "https://www.facebook.com/profile.php?id=100015096588541"
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


# def img_to_vec(img):
#     return np.array(img).ravel()

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
    link = fb_links['name']
    if 'hometown' in content:
        hometown = content['hometown']['name'],
    else:
        hometown = "Cupertino, CA"
    return jsonify({"name": name, "email": email, "hometown": hometown, "likes": likes, "link": link})

def get_face_class(face_encoding):
    print(len(face_encoding))
    print(len(rui_face_encoding))
    try:
        is_rui = face_recognition.compare_faces([rui_face_encoding], face_encoding)
        if is_rui:
            return 'Rui'
        is_adil = face_recognition.compare_faces([adil_face_encoding], face_encoding)
        if is_adil:
            return 'Adil'
        is_rohan = face_recognition.compare_faces([rohan_face_encoding], face_encoding)
        if is_rohan:
            return 'Rohan'
    except Exception:
        return 'Rui'
    return 'Rui'

def _get_prediction(json_data):
    global img_num
    image = json_data['photo']
    decoded_image = base64.b64decode(image)
    bytes_image = BytesIO(decoded_image)
    pil_image = Image.open(bytes_image)
    
    pil_image.save('phone_img_before_crop.jpg')
#     face_locations = face_recognition.face_locations(img_arr)
#     top, right, bottom, left = face_locations[0]
#     pil_image = pil_image.crop((left, top, right, bottom))
#     pil_image.save('phone_img_after_crop.jpg')


#     pil_image = pil_image.resize((IMG_SIZE, IMG_SIZE))
#     img_arr = np.array(pil_image)
    face_recognition.load_image_file("phone_img_before_crop.jpg")
    try:
        face_encoding = face_recognition.face_encodings(img_arr)[0]
    except Exception as e:
        return 'Rui'
#     print("face_recognition.face_encodings")
#     img_vec = np.array(pil_image).ravel()
#     img_num += 1
    prediction = get_face_class(face_encoding)
    return prediction


@app.route('/classify', methods=['POST'])
def classify():
    json_data = request.get_json(force=True)
    name = _get_prediction(json_data)
#     name = preds_info[prediction]
    # return _get_graph_api_details(name)
    return jsonify({"name": name, "email": email_info[name], "hometown": hometown_info[name], "likes": likes_info[name], "link": fb_links[name]})


if __name__ == '__main__':
    app.run(debug=False, use_debugger=True, use_reloader=True, passthrough_errors=True)
