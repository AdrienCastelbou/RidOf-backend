from flask import Flask, request
from PIL import Image
from itemsDetections import init_detector
import json 
import io
import base64

app = Flask(__name__)
items_detector = init_detector()

@app.route('/detect_items', methods=['POST'])
def detect_items():
    print(request.data)
    file = request.files['image']
    file.save("target.jpeg")
    img = Image.open("target.jpeg")
    detected_obj = items_detector.detectObjectsFromImage(input_image="target.jpeg", output_image_path="target_output.jpeg", minimum_percentage_probability = 80)
    items_list = []
    for obj in detected_obj:
        byteIO = io.BytesIO()
        resized_img = img.crop(box=obj["box_points"])
        resized_img.save(byteIO, format='JPEG')
        byteArr = byteIO.getvalue()
        items_list.append({'name': obj["name"], 'img': base64.encodebytes(byteArr).decode()})
    json_dump = json.dumps({"items": items_list})
    return json_dump


@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)