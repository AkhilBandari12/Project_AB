import os
import pytesseract
import pdfplumber
import cv2
import numpy as np
from pdf2image import convert_from_path
from PIL import Image
import re
import easyocr

def preprocess_image(img):
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    gray = cv2.bilateralFilter(gray, 9, 75, 75)
    gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                 cv2.THRESH_BINARY, 31, 2)
    kernel = np.ones((1, 1), np.uint8)
    gray = cv2.dilate(gray, kernel, iterations=1)
    gray = cv2.erode(gray, kernel, iterations=1)
    return gray

def correct_skew(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 200, minLineLength=100, maxLineGap=5)
    
    if lines is not None:
        angles = [np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi for line in lines for x1, y1, x2, y2 in line]
        if angles:
            median_angle = np.median(angles)
            (h, w) = image.shape[:2]
            center = (w // 2, h // 2)
            M = cv2.getRotationMatrix2D(center, median_angle, 1.0)
            image = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    
    return image

def extract_pan(text):
    pan_regex = r"[A-Z]{5}[0-9]{4}[A-Z]{1}"
    matches = re.findall(pan_regex, text)
    return matches if matches else None

def extract_text_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file not found at {pdf_path}")
        return None
    
    extracted_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        extracted_text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    
    if extracted_text.strip():
        print("Selectable text found. Extracting text without OCR...")
        return extracted_text
    
    print("No selectable text found. Performing OCR on scanned PDF...")
    images = convert_from_path(pdf_path)
    
    for i, img in enumerate(images):
        img = np.array(img)
        img = correct_skew(img)
        img = preprocess_image(img)
        processed_image_path = f"processed_page_{i+1}.png"
        Image.fromarray(img).save(processed_image_path)
        
        custom_config = "--oem 3 --psm 6"
        extracted_text += pytesseract.image_to_string(img, lang="eng", config=custom_config) + "\n"
    
    return extracted_text

def main():
    # pdf_path = '/home/buzzadmin/Documents/Desktop/Click_On_This/upload/Project-B/Python/Python_OCR/PAN.pdf'
    pdf_path = '/home/buzzadmin/Documents/Desktop/Click_On_This/upload/Project-B/Python/Python_OCR/pan_data.pdf'
    print("Starting OCR script...")
    
    text = extract_text_from_pdf(pdf_path)
    if text:
        with open("extracted_text.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("OCR extraction completed! Text saved to 'extracted_text.txt'.")
        
        pan_numbers = extract_pan(text)
        if pan_numbers:
            print("Extracted PAN Numbers:", pan_numbers)
        else:
            print("No PAN numbers found.")
    else:
        print("Failed to extract text from the document.")

if __name__ == "__main__":
    main()
