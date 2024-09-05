from selenium.webdriver.common.by import By
from selenium import webdriver 
import time
import psycopg2
from psycopg2 import sql


def db_connection():
    db_config = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': 'newpassword',
        'host': 'localhost',  # or your database host
        'port': '5432'  # default PostgreSQL port
    }

    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    return conn,cursor

def eportal_db_input(input,aadhar_num):
    # Database connection parameters

    if input == 1 and aadhar_num == 0:
        try:
            conn,cursor = db_connection()
            query = sql.SQL('SELECT * FROM e_portal WHERE "Status" IS NULL;')
            cursor.execute(query)
            results = cursor.fetchall()
            return results
        except Exception as e:
            print(f"An error occurred: {e}")
    if input == 2:
        try:
            conn,cursor = db_connection()
            # query_data_before = "UPDATE e_portal SET 'Status' = '$$STATUS','Remarks' = '$$REMARKS' WHERE 'Aadhar_Number' = '$$AadharNumber';"
            # with open("/home/buzzadmin/Desktop/E-Portal/sql_query.txt","r") as file:
            # #     query_data_before = file.read()
            # query_data = query_data_before.replace('$$AadharNumber',aadhar_num)
            # query_data = query_data_before.replace('$$STATUS','Success')
            # query_data = query_data_before.replace('$$REMARKS','PAN is already linked with AADHAR')

            query_data = 'UPDATE e_portal SET "Status" = '+"'Success'"+','+'"Remarks" ='+"'PAN is already linked with AADHAR'"+' WHERE "Aadhar_Number" =' +"'"+aadhar_num+"'"+';'
            print(query_data)
            cursor.execute(sql.SQL(query_data))
            conn.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
    if input == 3:
        try:
            conn,cursor = db_connection()
            # with open("/home/buzzadmin/Desktop/E-Portal/sql_query.txt","r") as file:
            #     query_data_before = file.read()
            #     query_data = query_data_before.replace('$$AadharNumber',aadhar_num)
            #     query_data = query_data_before.replace('$$STATUS','Fail')
            #     query_data = query_data_before.replace('$$REMARKS','Incorrect PAN details')
            query_data = 'UPDATE e_portal SET "Status" = '+"'Fail'"+','+'"Remarks" ='+"'Incorrect PAN details'"+' WHERE "Aadhar_Number" =' +"'"+aadhar_num+"'"+';'

            print(query_data)
            cursor.execute(sql.SQL(query_data))
            conn.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
    if input == 4:
        try:
            conn,cursor = db_connection()
            # with open("/home/buzzadmin/Desktop/E-Portal/sql_query.txt","r") as file:
            #     query_data_before = file.read()
            #     query_data = query_data_before.replace('$$AadharNumber',aadhar_num)
            #     query_data = query_data_before.replace('$$STATUS','Fail')
            #     query_data = query_data_before.replace('$$REMARKS','Incorrect AADHAR number')
            
            query_data = 'UPDATE e_portal SET "Status" = '+"'Fail'"+','+'"Remarks" ='+"'Incorrect AADHAR number'"+' WHERE "Aadhar_Number" =' +"'"+aadhar_num+"'"+';'
            print(query_data)
            cursor.execute(sql.SQL(query_data))
            conn.commit()
        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            cursor.close()
            conn.close()


def e_portal_validation():
    # Source -- https://www.zenrows.com/blog/selenium-avoid-bot-detection#disable-automation-indicator-webdriver-flags
    
    #Xpaths
    pan_input_xpath = '//*[@id="mat-input-0"]'
    aadhar_input_xpath = '//*[@id="mat-input-1"]'
    button_xpath = "//button[contains(text(), 'View Link Aadhaar Status')]"
    close_button_xpath = '//*[@id="linkAadhaarFailureClose"]'

    success = 'is already linked to given Aadhaar'
    pan_error = 'PAN does not exist.'
    aadhar_error = 'Please enter a valid Aadhaar Number.'

    #disable of automation flag
    options = webdriver.ChromeOptions() 
    options.add_argument("--disable-blink-features=AutomationControlled") 
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    options.add_experimental_option("useAutomationExtension", False) 
    driver = webdriver.Chrome(options=options) 
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 

    #Navigating to the url


    input_data_db = eportal_db_input(input=1,aadhar_num=0)
    if input_data_db:
        for each_row in input_data_db:
            driver.get("https://eportal.incometax.gov.in/iec/foservices/#/pre-login/link-aadhaar-status")
            driver.maximize_window()
            time.sleep(5)
            print(each_row)
            #variables
            pan = str(each_row[1])
            aadhar = str(each_row[0])
            #Enter the details into the required feilds
            pan_input_element = driver.find_element(By.XPATH, pan_input_xpath)
            pan_input_element.send_keys(pan)
            aadhar_input_element = driver.find_element(By.XPATH, aadhar_input_xpath)
            aadhar_input_element.send_keys(aadhar)
            view_status_element = driver.find_element(By.XPATH,button_xpath)
            view_status_element.click()
            time.sleep(5)
            popup_text_element = driver.find_element(By.CSS_SELECTOR, "#linkAadhaarFailure_desc .ng-star-inserted")
            popup_text = popup_text_element.text
            if popup_text.__contains__(success):
                print("Successfully Validated and the given person's PAN is already linked with AADHAR")
                eportal_db_input(input=2,aadhar_num=aadhar)
                close_button_element = driver.find_element(By.XPATH,close_button_xpath)
                close_button_element.click()
            elif popup_text.__contains__(pan_error):
                print("Given an incorrect PAN Details")
                eportal_db_input(input=3,aadhar_num=aadhar)
                close_button_element = driver.find_element(By.XPATH,close_button_xpath)
                close_button_element.click()
            elif popup_text.__contains__(aadhar_error):
                print("Given an incorrect AADHAR Number")
                eportal_db_input(input=4,aadhar_num=aadhar)
                close_button_element = driver.find_element(By.XPATH,close_button_xpath)
                close_button_element.click()
            time.sleep(5)
    else:
        print("No DATA to Process")
# eportal_db_input()
e_portal_validation()
