import cv2
import pytesseract
import re
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def preprocess_image(image_path):
    """Preprocess the image to improve OCR accuracy"""
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale
    image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)  # Upscale for better clarity
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]  # Apply thresholding
    return Image.fromarray(image)

def ExtractDetails(image_path):
    print(f"Processing: {image_path}")  

    # Extract text with preprocessing
    preprocessed_image = preprocess_image(image_path)
    text = pytesseract.image_to_string(preprocessed_image, lang='eng')
    print("\nExtracted Text:\n", text)  
    text = text.replace("\n", " ").replace("  ", " ")
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    plt.axis("off")
    
    # Extract Name (Assuming it's in Title Case)
    name_match = re.search(r'([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)', text)
    name = name_match.group(1) if name_match else "Name not found"


    # Extract Aadhaar Number (4-4-4 format)
    aadhaar_match = re.search(r'\b\d{4}\s\d{4}\s\d{4}\b', text)
    aadhaar_number = aadhaar_match.group(0) if aadhaar_match else "Aadhaar not found"

    # Extract DOB (Format: DD/MM/YYYY)
    dob_match = re.search(r'\b\d{2}/\d{2}/\d{4}\b', text)
    dob = dob_match.group(0) if dob_match else "DOB not found"

    print("Name:", name)
    print("Aadhaar Number:", aadhaar_number)
    print("DOB:", dob)


# Run the function

# path = "/home/buzzadmin/Documents/Desktop/AADHAR/142599-200636-AadharCard-202502210200051740126605.jpg"       #Done
# path = "/home/buzzadmin/Documents/Desktop/AADHAR/179684-199466-AadharCard-202502120221131739350273.jpg"     #Done
# path = "/home/buzzadmin/Documents/Desktop/AADHAR/180931-200833-AadharCard-202502241133461740377026.jpg"       #Error
# path = "/home/buzzadmin/Documents/Desktop/AADHAR/181760-201722-AadharCard-202503010248451740820725.jpg"
path = "/home/buzzadmin/Documents/Desktop/AADHAR/181866-201841-AadharCard-202503031202451740983565.jpg"
ExtractDetails(path)

























#import cv2
# import pytesseract
# import re
# import numpy as np
# from PIL import Image
# import matplotlib.pyplot as plt

# def preprocess_image(image_path):
#     """Preprocess the image to improve OCR accuracy"""
#     image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale
#     image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)  # Upscale for better clarity
#     image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]  # Apply thresholding
#     return Image.fromarray(image)

# def clean_text(text):
#     """Remove unwanted OCR artifacts"""
#     text = text.replace("\n", " ").replace("  ", " ")
#     text = re.sub(r'[^A-Za-z0-9/\s]', '', text)  # Remove special characters except "/"
#     return text

# def extract_details(image_path):
#     print(f"Processing: {image_path}")  

#     # Extract text with preprocessing
#     preprocessed_image = preprocess_image(image_path)
#     raw_text = pytesseract.image_to_string(preprocessed_image, lang='eng')

#     cleaned_text = clean_text(raw_text)  # Remove noise
#     print("\nExtracted Text:\n", cleaned_text)  

#     # Extract Aadhaar Number (4-4-4 format)
#     aadhaar_match = re.search(r'\b\d{4}\s\d{4}\s\d{4}\b', cleaned_text)
#     aadhaar_number = aadhaar_match.group(0) if aadhaar_match else "Aadhaar not found"

#     # Extract DOB (Format: DD/MM/YYYY or DD-MM-YYYY)
#     dob_match = re.search(r'\b\d{2}[/\-]\d{2}[/\-]\d{4}\b', cleaned_text)
#     dob = dob_match.group(0) if dob_match else "DOB not found"

#     # Extract Name with better filtering
#     words = cleaned_text.split()
#     possible_names = []
#     skip_keywords = {"government", "india", "authority", "unique", "identification", "male", "female"}

#     for i in range(len(words) - 1):
#         if words[i].istitle() and words[i].lower() not in skip_keywords:
#             possible_names.append(words[i])

#         # Ensure at least two consecutive words form a valid name
#         if len(possible_names) > 1:
#             break  

#     name = " ".join(possible_names) if possible_names else "Name not found"

#     print("\n✅ Extracted Details:")
#     print("Name:", name)
#     print("Aadhaar Number:", aadhaar_number)
#     print("DOB:", dob)

#     # Display Image (Optional)
#     image = cv2.imread(image_path)
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     plt.imshow(image)
#     plt.axis("off")
#     plt.show()


# # Run the function
# # path = "/home/buzzadmin/Documents/Desktop/AADHAR/181760-201722-AadharCard-202503010248451740820725.jpg"
# path = "/home/buzzadmin/Documents/Desktop/AADHAR/181866-201841-AadharCard-202503031202451740983565.jpg"
# extract_details(path)



# Run the function

# path = "/home/buzzadmin/Documents/Desktop/AADHAR/142599-200636-AadharCard-202502210200051740126605.jpg"       #Done
# path = "/home/buzzadmin/Documents/Desktop/AADHAR/179684-199466-AadharCard-202502120221131739350273.jpg"     #Done
# # path = "/home/buzzadmin/Documents/Desktop/AADHAR/180931-200833-AadharCard-202502241133461740377026.jpg"       #Error
# path = "/home/buzzadmin/Documents/Desktop/AADHAR/181760-201722-AadharCard-202503010248451740820725.jpg"
# ExtractDetails(path)