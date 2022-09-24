from imageai.Detection import ObjectDetection

obj_detect = ObjectDetection()
obj_detect.setModelTypeAsYOLOv3()
obj_detect.setModelPath("/Users/adriencastelbou/Downloads/yolo.h5")
obj_detect.loadModel()
detected_obj = obj_detect.detectObjectsFromImage(
    input_image="./test_image.jpeg",
    output_image_path="./test_image_output.jpg"
)

for obj in detected_obj:
    print(obj["name"] + "-"
          +str(obj["percentage_probability"]),
          obj["box_points"])