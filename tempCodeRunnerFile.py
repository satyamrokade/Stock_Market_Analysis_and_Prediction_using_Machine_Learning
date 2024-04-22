import cv2
import pytesseract

# Path to your image file
image_path = ".\gpay.jpg"

# Read the image using OpenCV
img = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Use Tesseract to extract text from the image
extracted_text = pytesseract.image_to_string(gray)

# Print the extracted text
print(extracted_text)
