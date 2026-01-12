import cv2
import numpy as np

#lower_hsv = np.array([171, 140, 100])
#upper_hsv = np.array([179, 200, 255])
#lower_hsv = np.array([0, 40, 60])
#upper_hsv = np.array([25, 180, 255])

#lower_hsv = np.array([0, 0, 0])
#upper_hsv = np.array([100, 255, 255])
#lower_hsv = np.array([15, 100, 100])  
#upper_hsv = np.array([35, 255, 255])

lower_hsv = np.array([10, 80, 80])    
upper_hsv = np.array([40, 255, 255])

def preprocess(image_rgb: np.ndarray) -> np.ndarray:
    """Returns a 2D array"""
    hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    return mask
