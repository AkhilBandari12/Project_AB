from PIL import Image, ImageDraw, ImageFont

def generate_second_page(self):
    second_page = Image.new('RGB', (self.width, self.height), color='white')
    draw = ImageDraw.Draw(second_page)
    # Card dimensions in pixels for 300 DPI (5.3 cm x 8.4 cm)
    # width, height = 625, 992  # Convert cm to pixels (5.3 x 8.4 cm at 300 DPI)
    # card = Image.new('RGB', (width, height), color='white')
    # draw = ImageDraw.Draw(card)

    # Define fonts (adjust font paths and sizes as per your setup)
    font_bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
    font_normal = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)

    # Add the Buzzworks logo
    try:
        logo_path = "buzz_logo.png"  # Replace with the actual logo path
        logo = Image.open(logo_path)
        logo_width, logo_height = int(self.width * 0.5), int(self.height * 0.1)  # Resize logo
        logo = logo.resize((logo_width, logo_height))
        second_page.paste(logo, ((self.width - logo_width) // 2, int(self.height * 0.05)), logo.convert("RGBA"))
    except Exception as e:
        print(f"Error loading logo: {e}")

    # Add "Conditions For Use"
    draw.text(
        (self.width // 2, int(self.height * 0.2)), 
        "Conditions For Use", 
        font=font_bold, 
        fill="black", 
        anchor="mm"
    )

    # Add the conditions text
    conditions_text = (
        "This Card remains the property of\n"
        "Buzzworks Business Services Pvt. Ltd.\n"
        "and is non-transferable. The bearer of\n"
        "this ID card is not authorised to collect\n"
        "cash. This card must be surrendered\n"
        "when employment with Buzzworks\n"
        "Business Services Pvt. Ltd. ceases. Loss\n"
        "must be reported to the issuing authority."
    )
    draw.multiline_text(
        (10, int(self.height * 0.3)), 
        conditions_text, 
        font=font_normal, 
        fill="black", 
        align="center", 
        anchor="mm"
    )

    # Add the "If Found" text
    if_found_text = (
        "If Found Kindly return to\n"
        "Buzzworks Business Services Pvt. Ltd."
    )
    draw.multiline_text(
        (self.width // 2, int(self.height * 0.55)), 
        if_found_text, 
        font=font_bold, 
        fill="black", 
        align="center", 
        anchor="mm"
    )

    # Add the address
    address_text = (
        "502-503 Shreya House,\n"
        "Pereira Hill Road,\n"
        "Off. Andheri-Kurla Road,\n"
        "Andheri (East), Mumbai-400 099"
    )
    draw.multiline_text(
        (self.width // 2, int(self.height * 0.65)), 
        address_text, 
        font=font_normal, 
        fill="black", 
        align="center", 
        anchor="mm"
    )

    # Add the website URL
    website_text = "www.buzzworks.com"
    blue_strip_height = int(self.height * 0.1)  # 10% of the card height
    draw.rectangle(
        [(0, self.height - blue_strip_height), (self.width, self.height)], 
        fill=(30, 36, 78)  # Matte blue color
    )
    draw.text(
        (self.width // 2, self.height - blue_strip_height // 2), 
        website_text, 
        font=font_bold, 
        fill="white", 
        anchor="mm"
    )

    second_page_path = f"{self.user_data['name'].replace(' ', '_')}_second_page.png"
    second_page.save(second_page_path)
    print(f"Second page saved as: {second_page_path}")
    return second_page_path
