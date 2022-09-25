from imageai.Detection import ObjectDetection

def init_detector():
    obj_detect = ObjectDetection()
    obj_detect.setModelTypeAsYOLOv3()
    obj_detect.setModelPath("/Users/adriencastelbou/Downloads/yolo.h5")
    obj_detect.loadModel()
    return obj_detect