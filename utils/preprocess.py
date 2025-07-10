import cv2
import numpy as np

def preprocess_frame(frame_bytes):
    arr = np.frombuffer(frame_bytes, np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (84, 84))
    return img
