import cv2
import pytesseract
import utils as utils


pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\danie\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

utils.remove_blue_borders('plates/plate3.jpg', 'plates/borderless.png')
img = cv2.imread('plates/borderless.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
pytesseract
##############################################
##### Image to String   ######
##############################################
print(pytesseract.image_to_string(img))
cv2.imshow('img', img)
cv2.waitKey(0)