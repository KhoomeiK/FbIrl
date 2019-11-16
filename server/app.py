from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
import base64
from sklearn.externals import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model/classifier.pkl')
preds_info = {
    0: 'adil',
    1: 'rohan',
    3: 'christian',
    4: 'rui'
}

email_info = {
    'adil': 'adil99@gmail.com',
    'rui': 'raguiar@gmail.com',
    'christian': 'christian@gmail.com',
    'rohan': 'rohan@gmail.com'
}

hometown_info = {
    'rui': "Palo Alto, CA",
    'adil': "Vancouver, Canada",
    'christian': 'San Mateo, CA',
    'rohan': 'San Francisco, CA'
}

likes_info = {
    'rui': "Running, Swimming",
    'adil': "Biking, Hiking",
    'christian': 'Books, Tennis',
    'rohan': 'Hackathons, Movies, Running'
}


IMG_SIZE = 128
SCALE_FACTOR = 6

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
    pil_image.save('phone_img_before_crop.jpg')
    # pil_image = pil_image.crop((left, upper, right, lower))
    pil_image = pil_image.resize((IMG_SIZE, IMG_SIZE))
    pil_image.save('phone_img_after_crop.jpg')
    img_vec = img_to_vec(pil_image)
    prediction = model.predict([img_vec])[0]
    name = preds_info[prediction]
    # fake data for now
    return jsonify({"name": name, "email": email_info[name], "hometown": hometown_info[name], "likes": likes_info[name]})


if __name__ == '__main__':
    app.run(debug=True, use_debugger=True, use_reloader=True, passthrough_errors=True)
