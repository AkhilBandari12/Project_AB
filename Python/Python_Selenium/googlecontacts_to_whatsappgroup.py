import time
# import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def whatsapp_groupmaker():

    driver = webdriver.Chrome()  
    driver.get("https://web.whatsapp.com")  
    driver.maximize_window()
    time.sleep(30)

    # search_box = driver.find_element(By.XPATH, "//input[@type='text']")
    # search_box.send_keys("CKR")
    # time.sleep(3)
    # contacts = driver.find_elements(By.XPATH, "//span[contains(text(), 'CKR')]")

    # for contact in contacts:
    #     contact.click()
    #     time.sleep(1)  
    try:
        contacts = driver.find_elements(By.XPATH, "//span[contains(text(), 'CKR')]")
        # print(contacts)
        for i in range(len(contacts)):
            contacts = driver.find_elements(By.XPATH, "//span[contains(text(), 'CKR')]")  # Re-fetch elements
            contacts[i].click()
            time.sleep(1)  # Add slight delay for stability
        # break  
    except Exception as e:
        print(f"Error encountered: {e}. Retrying...")

    time.sleep(300)

whatsapp_groupmaker()