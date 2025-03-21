from django.urls import path
from .views import AadhaarOCRAPIView  # Change this from upload_aadhaar_image to upload_image

urlpatterns = [
    path('aadhar_extract/', AadhaarOCRAPIView.as_view(), name='upload_image'),  # Ensure this matches your API route
]
 