from PIL import Image

class Model:
    def predict(self, img: Image):
        return {
            'name': 'Bob',
            'age': 20
        }
