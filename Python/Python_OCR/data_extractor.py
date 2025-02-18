# import os
# import pytesseract
# import pdfplumber
# import cv2
# import numpy as np
# from pdf2image import convert_from_path
# from PIL import Image

# # Path to your scanned PDF file
# pdf_path = "/home/buzzadmin/Documents/Desktop/Click_On_This/upload/Project-B/Python/Python_OCR/pan_data.pdf"

# print("Starting OCR script...")

# if not os.path.exists(pdf_path):
#     print(f"❌ Error: PDF file not found at {pdf_path}")
#     exit()

# print("✅ PDF file exists. Proceeding with extraction...")

# # 🟢 **Step 1: Check if PDF has selectable text**
# extracted_text = ""
# with pdfplumber.open(pdf_path) as pdf:
#     extracted_text = "\n".join(
#         page.extract_text() for page in pdf.pages if page.extract_text()
#     )

# if extracted_text.strip():
#     print("🔹 Selectable text found. Extracting text without OCR...")
# else:
#     print("🔹 No selectable text found. Performing OCR on scanned PDF...")

#     # 🟢 **Step 2: Convert PDF pages to images**
#     images = convert_from_path(pdf_path)

#     # 🟢 **Step 3: Apply Enhanced Preprocessing for OCR**
#     def preprocess_image(img):
#         """Preprocess image to enhance OCR readability"""
#         img = np.array(img)

#         # Convert to grayscale
#         gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#         # Apply Adaptive Thresholding (Better than simple thresholding)
#         adaptive = cv2.adaptiveThreshold(
#             gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2
#         )

#         # Denoise (Remove small dots and background noise)
#         denoised = cv2.fastNlMeansDenoising(adaptive, None, 30, 7, 21)

#         # Sharpen image
#         kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
#         sharpened = cv2.filter2D(denoised, -1, kernel)

#         return sharpened

#     extracted_text = ""
#     for i, img in enumerate(images):
#         processed_img = preprocess_image(img)

#         # Save processed image for debugging
#         processed_image_path = f"processed_page_{i+1}.png"
#         Image.fromarray(processed_img).save(processed_image_path)
#         print(f"🖼️ Saved processed image: {processed_image_path}")

#         # Perform OCR with custom configurations
#         custom_config = r'--oem 3 --psm 6'  # OCR Engine Mode 3, Page Segmentation 6 (Assumes blocks of text)
#         extracted_text += pytesseract.image_to_string(processed_img, lang="eng", config=custom_config) + "\n"

# # 🟢 **Step 4: Save Extracted Text to File**
# output_text_file = "extracted_text.txt"
# with open(output_text_file, "w", encoding="utf-8") as f:
#     f.write(extracted_text)

# print(f"✅ OCR extraction completed! Text saved to '{output_text_file}'.")

# # 🟢 **Step 5: Print Extracted Text (For Debugging)**
# print("\n🔍 Extracted Text Preview:\n")
# print(extracted_text[:1000])  # Show only first 1000 characters































import os
import pytesseract
import pdfplumber
import cv2
import numpy as np
from pdf2image import convert_from_path
from PIL import Image

# Path to your scanned PDF file
# pdf_path = "/home/buzzadmin/Documents/Desktop/Click_On_This/upload/Project-B/Python/Python_OCR/pan_data.pdf"
pdf_path = '/home/buzzadmin/Documents/Desktop/Click_On_This/upload/Project-B/Python/Python_OCR/PAN.pdf'

print("Starting OCR script...")

if not os.path.exists(pdf_path):
    print(f"❌ Error: PDF file not found at {pdf_path}")
    exit()

print("✅ PDF file exists. Proceeding with extraction...")

# 🟢 **Step 1: Check if PDF has selectable text (Avoid OCR if possible)**
extracted_text = ""
with pdfplumber.open(pdf_path) as pdf:
    extracted_text = "\n".join(
        page.extract_text() for page in pdf.pages if page.extract_text()
    )

if extracted_text.strip():
    print("🔹 Selectable text found. Extracting text without OCR...")
else:
    print("🔹 No selectable text found. Performing OCR on scanned PDF...")

    # 🟢 **Step 2: Convert PDF pages to images**
    images = convert_from_path(pdf_path)

    # 🟢 **Step 3: Apply Preprocessing for OCR**
    for i, img in enumerate(images):
        # Convert to grayscale
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)

        # Increase contrast (Thresholding)
        _, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

        # Save the preprocessed image for debugging
        processed_image_path = f"processed_page_{i+1}.png"
        Image.fromarray(img).save(processed_image_path)
        print(f"🖼️ Saved processed image: {processed_image_path}")

        # Perform OCR
        extracted_text += pytesseract.image_to_string(img, lang="eng") + "\n"

# 🟢 **Step 4: Save Extracted Text to File**
output_text_file = "extracted_text.txt"
with open(output_text_file, "w", encoding="utf-8") as f:
    f.write(extracted_text)

print(f"✅ OCR extraction completed! Text saved to '{output_text_file}'.")

# 🟢 **Step 5: Print Extracted Text (For Debugging)**
print("\n🔍 Extracted Text Preview:\n")
print(extracted_text[:1000])  # Show only first 1000 characters
