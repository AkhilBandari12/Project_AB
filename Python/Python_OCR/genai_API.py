import textwrap
import PIL.Image
import google.generativeai as genai
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


def text_extract(img_path):
    GOOGLE_API_KEY = "AIzaSyC6s22hTuVbbw-1yUEaoAYMWVBKfQDFEEA"
    genai.configure(api_key=GOOGLE_API_KEY)

    # Use a method available in the API
    img = PIL.Image.open(img_path)
    print("Extracting text...")

    # Assuming 'generate_text' is the correct method to interact with the model
    response = genai.generate_text(
        prompt="You are an OCR expert specializing in extracting text from scanned images. Read the image carefully and return only the extracted text without any additional information.",
        images=[img],
        stream=True
    )
    
    response.resolve()

    lis = to_markdown(response.text)
    print(lis)


path = "/home/buzzadmin/Documents/Desktop/Click_On_This/upload/Project-B/Python/Python_OCR/sample_pan.png"
text_extract(path)
