import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\danie\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('example.png')


img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
pytesseract
##############################################
##### Image to String   ######
##############################################
print(pytesseract.image_to_string(img))
cv2.imshow('img', img)
cv2.waitKey(0)