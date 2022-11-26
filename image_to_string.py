from PIL import Image
import pytesseract
import cv2
import os

# download Tesseract-OCR and install
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess(image):
	# load the example image and convert it to grayscale
	# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	filename = "{}.jpg".format(os.getpid())
	cv2.imwrite(filename, image)

	# return gray
	return filename

def ocr(filename):
	path = os.getcwd()
	im = Image.open(path+"\\"+filename)
	text = pytesseract.image_to_string(im)
	os.remove(filename)
	return text

def enter_image(input):
	# im = cv2.imread(input)  # rasm kirgizamiz
	x = preprocess(input)
	return ocr(x)
