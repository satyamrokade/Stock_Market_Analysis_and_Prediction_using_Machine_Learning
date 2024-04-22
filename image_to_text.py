import cv2
import easyocr

# Path to your image file
image_path = "D:\Algo\gpay1.jpg"

# Read the image using OpenCV
img = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Initialize the OCR reader
reader = easyocr.Reader(['en', 'hi'])

# Use OCR to extract text from the image
results = reader.readtext(gray)

# Extracted text
extracted_text = ' '.join([result[1] for result in results])

# Print the extracted text
print(extracted_text)

import re

# Extracted text from the transaction screenshot
# extracted_text = "A र 3,000 Received from ANUPAM KUMARI Freshers party Received र ३,००० Today २:०7 AM UPI Transaction ID 925412455928 Toः MAHESH KUMAR SAINI SO RAM PRATAPSAINI haryanvivideostatus@okaxis From: ANUPAM KUMARI (Bank of Baroda) anupamkumari1 २०४1 9९8@okicici Google Transaction ID CICAgKCGhI62Pg Payments may take up to 3 working days to be reflected in your account G Pay"

# Regular expressions for extracting amount, sender, receiver, and date
amount_pattern = re.compile(r'र\s*([\d,]+)')
sender_receiver_pattern = re.compile(r'from \s*(.*?)\s*To:\s*(.*?)\s*')
date_pattern = re.compile(r'Today\s*([\d:]+)\s*(AM|PM)')

# Extract amount
amount_match = amount_pattern.search(extracted_text)
amount = amount_match.group(1).replace(',', '') if amount_match else None

# Extract sender and receiver
sender_receiver_match = sender_receiver_pattern.search(extracted_text)
sender = sender_receiver_match.group(1).strip() if sender_receiver_match else None
receiver = sender_receiver_match.group(2).strip() if sender_receiver_match else None

# Extract date
date_match = date_pattern.search(extracted_text)
date = date_match.group(1) + ' ' + date_match.group(2) if date_match else None

# Print extracted details
print("Amount:", amount)
print("Sender:", sender)
print("Receiver:", receiver)
print("Date:", date)
