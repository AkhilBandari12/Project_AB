import os
import cv2
import pytesseract
import re
# import numpy as np
from PIL import Image
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

class AadhaarOCRAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    
    def preprocess_image(self, image_path):
        """Preprocess the image to improve OCR accuracy"""
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        return Image.fromarray(image)
    
    def extract_details(self, image_path):
        """Extract Aadhaar details from the image"""
        preprocessed_image = self.preprocess_image(image_path)
        text = pytesseract.image_to_string(preprocessed_image, lang='eng')
        text = text.replace("\n", " ").replace("  ", " ")
        
        # Extract Name (Assuming it's in Title Case)
        name_match = re.search(r'([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)', text)
        name = name_match.group(1) if name_match else "Name not found"

        # Extract Aadhaar Number (4-4-4 format)
        aadhaar_match = re.search(r'\b\d{4}\s\d{4}\s\d{4}\b', text)
        aadhaar_number = aadhaar_match.group(0) if aadhaar_match else "Aadhaar not found"

        # Extract DOB (Format: DD/MM/YYYY)
        dob_match = re.search(r'\b\d{2}/\d{2}/\d{4}\b', text)
        dob = dob_match.group(0) if dob_match else "DOB not found"
        
        return {"name": name, "aadhaar_number": aadhaar_number, "dob": dob}
    
    def post(self, request, *args, **kwargs):
        """Handle Aadhaar image upload and extract details"""
        if not request.FILES.get('image'):
            return Response({"status": "error", "message": "No image uploaded"}, status=400)
        
        image_file = request.FILES['image']
        file_path = default_storage.save('aadhaar_images/' + image_file.name, ContentFile(image_file.read()))
        full_path = os.path.join(default_storage.location, file_path)
        
        extracted_data = self.extract_details(full_path)
        
        return Response({"status": "success", "data": extracted_data}, status=200)
