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

    regex_DOB = re.compile(r'\d{2}[-/]\d{2}[-/]\d{4}')
    regex_num = re.compile(r'[A-Z]{5}[0-9]{4}[A-Z]{1}')

    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    plt.axis("off")
    
    if regex_num.findall(text):
        print("Pan Card Number:", regex_num.findall(text)[0])
    else:
        print("Blurry Image! No PAN Number detected!")

    print('=================================')

    if regex_DOB.findall(text):
        print("DATE OF BIRTH:", regex_DOB.findall(text)[0])
    else:
        print("Blurry Image! No DATE OF BIRTH detected!")

    print('=================================')

# Run the function

path = "/home/buzzadmin/Documents/Desktop/AADHAR/142599-200636-AadharCard-202502210200051740126605.jpg"

# path = "/home/buzzadmin/Documents/Desktop/Click_On_This/upload/Project-B/Python/Python_OCR/sample_pan_data.png"        #Done
# path = "/home/buzzadmin/Documents/Desktop/Click_On_This/upload/Project-B/Python/Python_OCR/sample_pan.png"               #Blurry Image! No DATE OF BIRTH detected!
# path = "/home/buzzadmin/Documents/Desktop/PAN/142599-200636-PanCard-202502210200041740126604.jpg"  # Blurry Image! No DATE OF BIRTH detected!
# path = "/home/buzzadmin/Documents/Desktop/PAN/179684-199466-PanCard-202502120221131739350273.jpg"  # Done
# path = "/home/buzzadmin/Documents/Desktop/PAN/179765-199554-PanCard-202502130956281739420788.jpg"  #Blurry Image! No PAN Number No DATE OF BIRTH detected!
# path = "/home/buzzadmin/Documents/Desktop/PAN/180068-199887-PanCard-202502150318161739612896.jpg"  #Blurry Image! No PAN Number detected!
# path = "/home/buzzadmin/Documents/Desktop/PAN/180931-200833-PanCard-202502241133461740377026.jpg"  #Blurry Image! No PAN Number No DATE OF BIRTH detected!
# path = "/home/buzzadmin/Documents/Desktop/PAN/181760-201722-PanCard-202503010248451740820725.jpg"  #Blurry Image! No PAN Number No DATE OF BIRTH detected!
# path = "/home/buzzadmin/Documents/Desktop/PAN/181866-201841-PanCard-202503031202451740983565.jpg"    ##Blurry Image! No PAN Number No DATE OF BIRTH detected!



ExtractDetails(path)













































# import numpy as np # linear algebra
# import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# import re
# #Tesseract Library
# import pytesseract

# import cv2
# import matplotlib.pyplot as plt
# from PIL import Image
# import os

# ### Make prettier the prints ###
# from colorama import Fore, Style
# c_ = Fore.CYAN
# m_ = Fore.MAGENTA
# r_ = Fore.RED
# b_ = Fore.BLUE
# y_ = Fore.YELLOW
# g_ = Fore.GREEN
# w_ = Fore.WHITE

# import warnings
# warnings.filterwarnings(action='ignore')




# def ExtractDetails(image_path):
#     text = pytesseract.image_to_string(Image.open(image_path), lang = 'eng')
#     print(text)
#     text = text.replace("\n", " ")
#     text = text.replace("  ", " ")
#     regex_DOB = re.compile('\d{2}[-/]\d{2}[-/]\d{4}')
#     regex_num = re.compile('[A-Z]{5}[0-9]{4}[A-Z]{1}')
    
#     image = cv2.imread(os.path.join(image_path))
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     plt.imshow(image)
#     plt.axis("off")  
    
#     if len(regex_num.findall(text)) == 0:
#         print(f'{y_}Blurry Image for tesseract. Input new clear image for viewing pan card number !!!')
#         print(Style.RESET_ALL)
#     else:
#         print("Pan Card Number : ", regex_num.findall(text)[0])
        
#     print('=================================')
    
#     if len(regex_DOB.findall(text)) == 0:
#         print(f'{y_}Blurry Image for tesseract. Input new clear image for viewing DATE OF BIRTH !!!')
#         print(Style.RESET_ALL)
#     else:
#         print("DATE OF BIRTH :   ", regex_DOB.findall(text)[0])
        
#     print('=================================')




#     ExtractDetails('/home/buzzadmin/Documents/Desktop/Click_On_This/upload/Project-B/Python/Python_OCR/sample_pan_data.png')
