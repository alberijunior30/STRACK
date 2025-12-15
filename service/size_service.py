import cv2
import os
from model.model_size import model_size

def size(directory):
    image = cv2.imread(directory)
    
    if image is not None:
        
        h, w, *_ = image.shape

        os.remove(directory)

    return model_size(height=h, width=w)