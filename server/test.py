import os
import requests

url = 'http://127.0.0.1:5000/' + 'classify'
sample_img_path = 'model/data/pins_Aaron Paul/Aaron Paul0_262.jpg'

with open(sample_img_path, 'rb') as img:
    name_img = os.path.basename(sample_img_path)
    files = {'image': (name_img, img, 'multipart/form-data', {'Expires': '0'})}
    with requests.Session() as s:
        r = s.post(url, files=files)
        print(r.status_code)
        print(r.content)
