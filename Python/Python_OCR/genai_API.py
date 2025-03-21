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

    # Load the Gemini Pro Vision model
    model = genai.GenerativeModel("gemini-pro-vision")

    # Open the image
    img = PIL.Image.open(img_path)
    print("Extracting text...")

    # Call the correct method for image processing
    response = model.generate_content(
        [img, "Extract the text from this image and return only the extracted text."]
    )

    # Extract the text and print
    extracted_text = response.text
    lis = to_markdown(extracted_text)
    print(lis)


# Define the image path
path = "/home/buzzadmin/Documents/Desktop/PAN/179765-199554-PanCard-202502130956281739420788.jpg"
text_extract(path)
