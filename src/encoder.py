import cv2
import pickle

from settings import Settings

def encode(frame):
    settings = Settings()
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), settings.get_jpg_quality()]
    result, image = cv2.imencode('.jpg', frame, encode_param)
    if result: 
        # pickle representation of the object obj as a bytes object, instead of writting it to a file
        return pickle.dumps(image, 0)