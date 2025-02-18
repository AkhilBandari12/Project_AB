import os
from google.cloud import vision
from google.cloud.vision import types
import io

def text_extract(img_path):
    # Set Google Cloud API credentials
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/your/service-account-file.json"

    # Initialize the Vision client
    client = vision.ImageAnnotatorClient()

    # Open the image file
    with io.open(img_path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Perform text detection
    response = client.text_detection(image=image)
    texts = response.text_annotations

    # Extract the detected text
    if texts:
        print("Detected text:")
        print(texts[0].description)
    else:
        print("No text detected.")

# Path to the image file
path = "/home/buzzadmin/Documents/Desktop/Click_On_This/upload/Project-B/Python/Python_OCR/sample_pan.png"
text_extract(path)
