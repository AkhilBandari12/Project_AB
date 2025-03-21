import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to format phone numbers
def format_phone_numbers(numbers):
    return [f"+91 {num[:5]} {num[5:]}" for num in numbers]

# Function to read phone numbers from an Excel file
def read_phone_numbers_from_excel(file_path):
    df = pd.read_excel(file_path)
    phone_numbers = df['MOBILE NO'].astype(str).tolist()  # Ensure numbers are strings
    return format_phone_numbers(phone_numbers)

# WhatsApp Automation Function
def whatsapp_groupmaker(excel_file):
    phone_numbers = read_phone_numbers_from_excel(excel_file)

    driver = webdriver.Chrome()  
    driver.get("https://web.whatsapp.com")  
    driver.maximize_window()

    # Wait for QR code scan
    # WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//canvas")))

    try:
        # Click on the menu and create a new group
        menu_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Menu'])[1]")))
        menu_button.click()

        new_group_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='New group']")))
        new_group_option.click()

        input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search name or number']")))

        # Loop through numbers and add them to the group
        for number in phone_numbers:
            print(f"Adding {number}...")
            input_field.clear()
            input_field.send_keys(number)
            time.sleep(2)

            try:
                # print(f"(//span[text()='{number}'])[2]")
                # phone_number_span = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, f"//span[text()='{number}']")))
                # print(phone_number_span)
                phone_number_span = driver.find_element(By.XPATH, f"(//span[text()='{number}'])[2]")
                phone_number_span.click()
                # time.sleep(300)
                # phone_number_span.click()
                time.sleep(1)
            except Exception:
                print(f"Number {number} not found or not on WhatsApp.")

        # Click Next (Arrow)
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='arrow-forward']")))
        next_button.click()

        # Enter Group Name
        group_name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//p[contains(@class, 'selectable-text')])[2]")))
        group_name_field.send_keys("Beerpur")

        # # Click Create (Checkmark)
        # create_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='checkmark-medium']")))
        # create_button.click()

        # print("Group Created Successfully!")
        # time.sleep(5)

    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        driver.quit()  

# Run the bot with an Excel file input
file_path = "/home/buzzadmin/Documents/Desktop/Click_On_This/upload/Project-B/Python/Output_Excels/Beerpur.xlsx"
whatsapp_groupmaker(file_path)
































# import time
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Function to format phone numbers
# def format_phone_numbers(numbers):
#     return [f"+91 {num[:5]} {num[5:]}" for num in numbers]

# # Function to read and update phone numbers from an Excel file
# def read_phone_numbers_from_excel(file_path):
#     df = pd.read_excel(file_path)
    
#     if 'STATUS' not in df.columns:
#         df['STATUS'] = 'Pending'  # Default status
    
#     pending_numbers = df[df['STATUS'] == 'Pending']['MOBILE NO'].astype(str).tolist()
#     return df, format_phone_numbers(pending_numbers)

# # Function to update Excel with status
# def update_excel_status(file_path, df):
#     df.to_excel(file_path, index=False)

# # WhatsApp Automation Function
# def whatsapp_groupmaker(excel_file):
#     df, phone_numbers = read_phone_numbers_from_excel(excel_file)
    
#     if not phone_numbers:
#         print("All numbers have been processed. Exiting...")
#         return
    
#     driver = webdriver.Chrome()
#     driver.get("https://web.whatsapp.com")
#     driver.maximize_window()

#     # Wait for QR code scan
#     WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//canvas")))

#     try:
#         # Click on the menu and create a new group
#         menu_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Menu'])[1]")))
#         menu_button.click()
        
#         new_group_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='New group']")))
#         new_group_option.click()

#         input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search name or number']")))

#         # Loop through numbers and add them to the group
#         for index, number in enumerate(phone_numbers):
#             print(f"Processing {number}...")
#             input_field.clear()
#             input_field.send_keys(number)
#             time.sleep(2)
            
#             try:
#                 phone_number_span = driver.find_element(By.XPATH, f"(//span[text()='{number}'])[2]")
#                 phone_number_span.click()
#                 time.sleep(1)
#                 df.loc[df['MOBILE NO'].astype(str) == number.replace('+91 ', '').replace(' ', ''), 'STATUS'] = 'Done'
#             except Exception:
#                 print(f"Number {number} not found or not on WhatsApp.")
#                 df.loc[df['MOBILE NO'].astype(str) == number.replace('+91 ', '').replace(' ', ''), 'STATUS'] = 'Failed'
            
#             update_excel_status(excel_file, df)  # Save progress after each number

#         # Click Next (Arrow)
#         next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='arrow-forward']")))
#         next_button.click()

#         # Enter Group Name
#         group_name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//p[contains(@class, 'selectable-text')])[2]")))
#         group_name_field.send_keys("Beerpur")
        
#         # Click Create (Checkmark)
#         create_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='checkmark-medium']")))
#         create_button.click()
#         print("Group Created Successfully!")
#         time.sleep(5)
        
#     except Exception as e:
#         print(f"Error: {e}")
    
#     finally:
#         driver.quit()

# # Run the bot with an Excel file input
# file_path = "/home/buzzadmin/Documents/Desktop/Click_On_This/upload/Project-B/Python/Output_Excels/Beerpur.xlsx"
# whatsapp_groupmaker(file_path)



















# import time
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# # Function to format phone numbers
# def format_phone_numbers(numbers):
#     return [f"+91 {num[:5]} {num[5:]}" for num in numbers]

# # Function to read phone numbers from an Excel file
# def read_phone_numbers_from_excel(file_path):
#     df = pd.read_excel(file_path)
#     phone_numbers = df['MOBILE NO'].astype(str).tolist()  # Ensure numbers are strings
#     return format_phone_numbers(phone_numbers)

# # WhatsApp Automation Function
# def whatsapp_groupmaker(excel_file):
#     phone_numbers = read_phone_numbers_from_excel(excel_file)

#     driver = webdriver.Chrome()  # You can use Edge or Firefox if needed
#     driver.get("https://web.whatsapp.com")  # Open WhatsApp Web
#     driver.maximize_window()
#     time.sleep(30)  # Wait for QR code scan

#     # Click on the menu and create a new group
#     driver.find_element(By.XPATH, "(//button[@aria-label='Menu'])[1]").click()  
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//*[text()='New group']").click()
#     time.sleep(2)

#     input_field = driver.find_element(By.XPATH, "//input[@placeholder='Search name or number']")

#     # Loop through numbers and add them to the group
#     for number in phone_numbers:
#         print(f"Adding {number}...")
#         input_field.clear()
#         input_field.send_keys(number)
#         time.sleep(2)
#         try:
#             time.sleep(2)
#             phone_number_span = driver.find_element(By.XPATH, f"//span[text()='{number}']")
#             time.sleep(2)
#             phone_number_span.click()
#             time.sleep(2)
#         except Exception as e:
#             print(e)
#             print(f"Number {number} not found or not on WhatsApp.")
    
#     # Click Next (Arrow)
#     driver.find_element(By.XPATH, "//span[@data-icon='arrow-forward']").click()
#     time.sleep(2)

#     # Enter Group Name
#     group_name_field = driver.find_element(By.XPATH, "(//p[contains(@class, 'selectable-text')])[2]")
#     group_name_field.send_keys("Beerpur")

#     # # Click Create (Checkmark)
#     # driver.find_element(By.XPATH, "//span[@data-icon='checkmark-medium']").click()

#     # print("Group Created Successfully!")
#     # time.sleep(10)
#     # driver.quit()  # Close browser

# # Run the bot with an Excel file input
# # file_path = input("Enter the path of the Excel file: ")
# file_path = "/home/buzzadmin/Documents/Desktop/Click_On_This/upload/Project-B/Python/Output_Excels/Beerpur.xlsx"
# whatsapp_groupmaker(file_path)
