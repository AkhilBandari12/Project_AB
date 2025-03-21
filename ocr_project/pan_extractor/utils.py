import cv2
import pytesseract
import re
import numpy as np
from PIL import Image
import io

def preprocess_image(image: np.ndarray):
    """Preprocess the image to improve OCR accuracy"""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    resized = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)  # Upscale for better clarity
    _, thresh = cv2.threshold(resized, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # Apply thresholding
    return thresh

def extract_details(image: np.ndarray):
    """Extract PAN details from an image"""
    processed_image = preprocess_image(image)
    pil_image = Image.fromarray(processed_image)
    text = pytesseract.image_to_string(pil_image, lang='eng')

    text = text.replace("\n", " ").replace("  ", " ")

    regex_DOB = re.compile(r'\d{2}[-/]\d{2}[-/]\d{4}')
    regex_pan = re.compile(r'[A-Z]{5}[0-9]{4}[A-Z]{1}')

    pan_number = regex_pan.findall(text)
    dob = regex_DOB.findall(text)

    return {
        "pan_number": pan_number[0] if pan_number else "Not Detected",
        "date_of_birth": dob[0] if dob else "Not Detected"
        # "extracted_text": text
    }
