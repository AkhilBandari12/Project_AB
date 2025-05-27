*** Settings ***
# Library    RPA.Browser.Selenium    #auto_close=${False}
Library    SeleniumLibrary
Library    Collections
Library    OperatingSystem
Library    String
Library    Process
Library    excel.py
Library    DateTime
Library    RPA.Email.ImapSmtp
Library    captcha_text.py

# Test Teardown    Teardown Test
# Suite Teardown    Run Keywords    Check If Test Failed And Send Email
# Suite Setup    Initialize Suite Variables
# Suite Teardown    Check If Test Failed And Send Email
# Test Teardown    Capture Test Status



*** Variables ***
${username}                              
${password}
${process_type}                   
${year}   
${month}                                          
${salary dispursal date}      
${remarks}                    
${Test}   
${Total_EDLI_Contribution(ER Share A/C 21)}     
${EPF_Inspection_Charges}                       
${EDLI_Administration_Charges}                  
${EDLI_Inspection_Charges}                      
${input_file_path}        
${Total_Number_Of_Employees_In_Month}           
${Total_Number_Of_Excluded_Employees_In_Month}  
${Total_Gross_Wages_Of_Excluded_Employees_In_Month}  
${SCREENSHOT_FILE}          /app/epfo_api/captcha_screenshot.png
# compliance_scripts/epfo_captcha_20240819_123422.png

${download_directory}    /home/ubuntu/compliance_bot/test_data
${EMAIL_SERVER}                 smtp.gmail.com
${EMAIL_PORT}                   587
${TAGGED_EMAIL}                 lakshmi.l@buzzworks.com                                                                         #bandari.akhil@buzzworks.com, shashwat.b@buzzworks.com           
${BOT_START_SUBJECT}            EPFO AUTOMATION 
${EMAIL_USERNAME}       bandari.akhil@buzzworks.com                                # lakshmi.l@buzzworks.com
${EMAIL_SENDER}         ${EMAIL_USERNAME}
# ${TAGGED_EMAIL}         lakshmi.l@buzzworks.com
${SUBJECT}              Failed_User.
${EMAIL_PASSWORD}       zhcn mmym kllb mhuq                                        #dwbr qelg rjom phdf
# ${TEST_FAILED}                  
${VERIFY_BUTTON_LOCATOR}    //*[@id="tbClaimList"]/tbody/tr/td[12]/a[contains(text(), 'Verify')]
${TIMEOUT}            60s


*** Keywords ***

Send Failure Email
    [Arguments]    ${task_error}    
    ${subject}=    Set Variable    EPFO BOT Failure Notification
    ${body}=    Set Variable    Hi Compliance Team,\n\nThe BOT has failed during the execution of EPFO Remittance.\nError occurred while ${task_error}. \n\nThis is an automated email, please do not reply.\n\nThanks & Regards,\nAutomation Team.
    Authorize SMTP    ${EMAIL_USERNAME}    ${EMAIL_PASSWORD}    ${EMAIL_SERVER}    ${EMAIL_PORT}
    Send Message    ${EMAIL_SENDER}    ${TAGGED_EMAIL}    ${subject}    ${body}

Send_Start_email
    ${email_body}=    Set Variable     Hi Compliance Team,\n\nThe BOT has started the execution of EPFO Remittance\n\nThis is an automated email, please do not reply.\n\nThanks & Regards,\nAutomation Team.
    Authorize SMTP    ${EMAIL_USERNAME}   ${EMAIL_PASSWORD}    ${EMAIL_SERVER}    ${EMAIL_PORT}
    Send Message     ${EMAIL_SENDER}    ${TAGGED_EMAIL}    ${BOT_START_SUBJECT}    ${email_body}    


Send_Success_email

    ${email_body}=    Set Variable     Hi Compliance Team,\n\nThe BOT has Successfully executed the EPFO Remittance\n\nThis is an automated email, please do not reply.\n\nThanks & Regards,\nAutomation Team.
    Authorize SMTP    ${EMAIL_USERNAME}   ${EMAIL_PASSWORD}    ${EMAIL_SERVER}    ${EMAIL_PORT}
    Send Message     ${EMAIL_SENDER}    ${TAGGED_EMAIL}    ${BOT_START_SUBJECT}    ${email_body}

# Teardown Test
#     Run Keyword If    '${TEST FAILED}' == 'True'    Send Failure Email
Login Process
    Sleep    2s
    Click Button    xpath://*[@id="btnCloseModal"]  
    Log    Opened EPFO login page   

    Wait Until Element Is Visible    id=username1    timeout=90s     
    Input Text    xpath://*[@id="username1"]     ${username}       
    Sleep    1s
    Log    ${username}
    Wait Until Element Is Visible    id=password    timeout=90s    
    Input Text    xpath://*[@id="password"]     ${password}                
    Sleep    1s
    Log    ${password} 
    
    Wait Until Element Is Visible    xpath=//div[@id='toggleCaptcha']//div[contains(@class, 'mb-3')]//img   timeout=90s

    Capture Element Screenshot    xpath=//div[@id='toggleCaptcha']//div[contains(@class, 'mb-3')]//img    ${SCREENSHOT_FILE}
    ${result}=    Run Keyword    captcha_text.captcha_ectract    ${SCREENSHOT_FILE}
    Log    ${result}
    Input Text    xpath=//*[@id="captcha"]    ${result}
    # Sleep    12s

    Wait Until Element Is Visible     //button[@value="Submit"]  timeout=30s 
    Click Button        //button[@value="Submit"]

    ${payment}=    Run Keyword And Return Status    Element should be Visible     //*[contains(@class, 'dropdown-toggle') and contains(text(), 'Payment')]
    Log    ${payment}
    [Return]    ${payment}
# Login Process
#     Sleep    2s
#     Click Button    xpath://*[@id="btnCloseModal"]  
#     Log    Opened EPFO login page   

#     Wait Until Element Is Visible    id=username1    timeout=90s     
#     Input Text    xpath://*[@id="username1"]     ${username}       
#     Sleep    1s
#     Log    ${username}
#     Wait Until Element Is Visible    id=password    timeout=90s    
#     Input Text    xpath://*[@id="password"]     ${password}                
#     Sleep    1s
#     Log    ${password} 
    
#     Wait Until Element Is Visible    xpath=//div[@id='toggleCaptcha']//div[contains(@class, 'col-sm-7')]//img    timeout=90s

#     Capture Element Screenshot    xpath=//div[@id='toggleCaptcha']//div[contains(@class, 'col-sm-7')]//img    ${SCREENSHOT_FILE}
#     ${result}=    Run Keyword    captcha_text.captcha_ectract    ${SCREENSHOT_FILE}
#     Log    ${result}
#     Input Text    xpath=//*[@id="captcha"]    ${result}
#     # Sleep    12s

#     Wait Until Element Is Visible     //button[@value="Submit"]  timeout=30s
#     Click Button        //button[@value="Submit"]

#     # Sleep    2s
#     # Click Button    xpath://*[@id="btnCloseModal"]  

#     # ${current_url}=    Get Location
#     # Log    Current URL: ${current_url}
#     # [Return]    ${current_url}

#     # Sleep    2s
#     # ${element_exists}    Run Keyword And Return Status    Element Should Be Visible      //*[@id="divMenuBar"]        timeout=15s
#     # Log    ${element_exists} 
#     # [Return]    ${element_exists}
#     ${payment}=    Run Keyword And Return Status    Element should be Visible     //*[contains(@class, 'dropdown-toggle') and contains(text(), 'Payment')]
#     Log    ${payment}
#     [Return]    ${payment}

Switch To Original Window
    ${window_handles}=    Get Window Handles
    ${original_window_index}=    Evaluate    len(${window_handles}) - 2
    Switch Window    ${window_handles}[${original_window_index}]

Click Element When Visible
    [Arguments]    ${PreLocator}    ${Elementtype}    ${PostLocator}
    Wait Until Element Is Visible     ${PreLocator}   timeout=120    error=${Elementtype} not visible within 2m
    Click Element     ${PreLocator}
    Wait Until Element Is Visible    ${PostLocator}    timeout=30    error= unable to navigate to next page
    Log    Successfully Clicked on ${Elementtype}

Open EPF India Website
    # Open Browser    https://www.epfindia.gov.in/site_en/index.php#    firefox     remote_url=http://10.1.20.101:3000/wd/hub        options=add_experimental_option("detach", True)        options=add_argument("--enable-remote-debugging")    ff_profile_dir=set_preference("browser.download.folderList", 2);set_preference("browser.download.dir", r"/home/ubuntu/compliance_bot/test_data");set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")    
    # Open Browser    https://www.epfindia.gov.in/site_en/index.php#  firefox     remote_url=http://172.31.44.225:3001/wd/hub         options=add_experimental_option("detach", True)        options=add_argument("--enable-remote-debugging") 
    # Wait Until Element Is Visible    xpath://*[@id="ecr_panel_1"]    timeout=30     error=Unbale to launch EPF website..  


    Open Browser    https://unifiedportal-emp.epfindia.gov.in/epfo/     firefox                #remote_url=http://172.31.44.225:3001/wd/hub        options=add_experimental_option("detach", True)        options=add_argument("--enable-remote-debugging") 
    Maximize Browser Window
    Wait Until Element Is Visible   //button[@id="btnCloseModal"]     timeout=30s     error= Unable to find Alert Popup..  
Click ECR/Returns/Payment Button
    Click Element     xpath://*[@id="ecr_panel_1"]
    Switch Window        EPFO: Home     timeout=30s
    Maximize Browser Window
    Wait Until Element Is Visible    xpath://*[@id="btnCloseModal"]    timeout=30s     error= Unable to find Alert Popup..
    Sleep    3s
# Accept Popup
#     Sleep    2s
#     Click Button    xpath://*[@id="btnCloseModal"]  
#     Log    Opened EPFO login page   
# Enter Username and Password
#     Wait Until Element Is Visible   xpath://*[@id="username1"]    timeout=30s     error=Unable to find username input
#     Input Text    xpath://*[@id="username1"]     ${username}       
#     Input Text    xpath://*[@id="password"]     ${password}                
#     Log    Entered username and password   
# Login Process
#     Sleep    2s
#     Click Button    xpath://*[@id="btnCloseModal"]  
#     Log    Opened EPFO login page   
#     Wait Until Element Is Visible    id=username1    timeout=90s     
#     Input Text    xpath://*[@id="username1"]     ${username}       
#     Sleep    1s
#     Log    ${username}
#     Wait Until Element Is Visible    id=password    timeout=90s    
#     Input Text    xpath://*[@id="password"]     ${password}                
#     Sleep    1s
#     Log    ${password} 
#     Wait Until Element Is Visible    xpath=//div[@id='toggleCaptcha']//div[contains(@class, 'col-sm-7')]//img    timeout=90s

#     Capture Element Screenshot    xpath=//div[@id='toggleCaptcha']//div[contains(@class, 'col-sm-7')]//img    ${SCREENSHOT_FILE}
#     ${result}=    Run Keyword    captcha_text.captcha_ectract    ${SCREENSHOT_FILE}
#     Log    ${result}

#     Input Text    xpath=//*[@id="captcha"]    ${result}
#     Sleep    2s

#     Wait Until Element Is Visible     //button[@value="Submit"]  timeout=30s
#     Click Button        //button[@value="Submit"]
#     ${current_url}=    Get Location
#     Log    Current URL: ${current_url}
#     [Return]    ${current_url}

# Click Payment Menu Button
#     # Wait Until Element Is Visible     //button[@value="Submit"]  timeout=30s
#     # Click Button        //button[@value="Submit"]
#     TRY
#         Wait Until Element Is Visible       //*[contains(@class, 'dropdown-toggle') and contains(text(), 'Payment')]    timeout=30s    error=Unable to login EPFO
#     EXCEPT    message 
#         Click Element    //*[@id="digitalJeevanAlertBox"]//*[@id="alertButtton"]/a
#         Wait Until Element Is Visible       //*[contains(@class, 'dropdown-toggle') and contains(text(), 'Payment')]    timeout=30s    error=Unable to login EPFO
#     END    
# #     ${current_url}=    Get Location
#     Log    Current URL: ${current_url}
#     [Return]    ${current_url}
    # Log    Successfully logging EPFO
Click Payments Menu
    Click Element When Visible    //*[contains(@class, 'dropdown-toggle') and contains(text(), 'Payment')]    Payment Menu    //ul[@class='dropdown-menu m1']//a[text()='ECR/RETURN FILING']     # payment
# Click ECR/RETURN FILE Menu Item  
#     Click Element When Visible    //ul[contains(@class, 'dropdown-menu') and contains(@class, 'show')]//a[text()='ECR/RETURN FILING']
Click ECR Upload Hyperlink
    Click Element When Visible    //tr[@class='row1 trs']//a[text()='ECR Upload']    ECR Upload Hyperlink      //*[@id="ui-id-3"]      # ECR Upload     
Click ECR file upload Button    
    Click Element When Visible    //*[@id="ui-id-3"]     ECR file upload Button    //*[@id="salaryDate"]     # ECR file upload
Click WageMonth Button 
    #print(input_file_path,"input_file_pathinput_file_path")
    ${original_date}    Set Variable    ${salary dispursal date}
    ${Salary_date}    Convert Date    ${original_date}    result_format=%d/%m/%Y
    # Log    Formatted Date: ${Salary_date}
    Wait Until Element Is Visible    //*[@id="salaryDate"]    timeout=30s
    Input Text    //*[@id="salaryDate"]    ${Salary_date}                   #salary disbursal date
    # Sleep    3s
    Wait Until Element Is Visible    //a[@title="Calendar" and @data-target="wageMonth"]    timeout=30s
    Click Element When Visible     //a[@title="Calendar" and @data-target="wageMonth"]    wagemonth     //select[@class="ui-datepicker-year"]/option[text()='${year}']   
    Click Element When Visible      //select[@class="ui-datepicker-year"]/option[text()='${year}']      wage year       //select[@class="ui-datepicker-month"]/option[text()='${month}']
    Click Element When Visible     //select[@class="ui-datepicker-month"]/option[text()='${month}']      Month Button      //button[text()="Done"]
    Click Element When Visible    //button[text()="Done"]      Done     ecrFileType    
    Wait Until Element Is Visible    ecrFileType    timeout=30s                  
    Select Radio Button    ecrFileType    ${process_type}
    Wait Until Element Is Visible    xpath://*[@id="ecrFileUploadRemarks"]     timeout= 30s
    Input Text       xpath://*[@id="ecrFileUploadRemarks"]    ${remarks}                 #remarksUpload Textfile       
    Sleep    2s
    Log    ${input_file_path}            
    ${result}    Run Keyword    excel.excel_to_text    ${input_file_path}
    # ${result}=    Run Process    python3    excel.py    ${input_file_path}
    Log    ${result} 
    Sleep    10s                          
    Choose File    //*[@id="multiFile"]    ${result}
    # Sleep    3s                          
    Wait Until Element Is Visible    //*[@id="btnUploadECRFile"]    timeout=50s    error=unable to find Upload button
    Click Element    //*[@id="btnUploadECRFile"]
    # Sleep    5s
Download ECR File and ECR Statement  
    Sleep    10s
    Wait Until Element Is Visible    //*[@id="tbClaimList"]/tbody/tr/td[9]/a[@title="Click to download ECR file."]       timeout=30s 
    Click Element  //*[@id="tbClaimList"]/tbody/tr/td[9]/a[@title="Click to download ECR file."]
    Wait Until Element Is Visible    //*[@id="tbClaimList"]/tbody/tr/td[10]/a/span    timeout=30s 

    Click Element    //*[@id="tbClaimList"]/tbody/tr/td[10]/a/span 

# Download ECR Statement
#     Click Element    //*[@id="tbClaimList"]/tbody/tr/td[10]/a/span 
Click Verify Button
    Click Element    //*[@id="tbClaimList"]/tbody/tr/td[12]/a[contains(text(), 'Verify')]
    Handle Alert

Click Other Elements
    Sleep    3s
    Wait Until Element Is Visible    //li//a[text()='ECR Home Page']    timeout=30s
    Click Element    //li//a[text()='ECR Home Page']
    Wait Until Element Is Visible    //a[text()='ECR Upload']    timeout=30s
    Click Element    //a[text()='ECR Upload']
    # Sleep    10s
    # Click Element    //*[@id="tbClaimList"]/tbody/tr/td[12]/a[contains(text(), 'Verify')]
    # Handle Alert
    

Generate TRRN Number and Click Prepare Challan Button
    # Wait Until Element Is Visible    xpath=//div[@class="alert alert-success"]     timeout=30s
    # # ${text}=    Get Element Attribute    xpath=//div[@class="alert alert-success"]    innerText
    # ${text}=    Get Element Attribute    xpath=//div[@class="alert alert-success"]    textContent
    Sleep    4s
    Wait Until Element Is Visible     xpath://div[@role="alert"]       timeout=30s
    ${text}=    Get Text    xpath://div[@role="alert"]
    Log    Extracted Text: ${text}

    # ${transid}    Get Regexp Matches    ${text}    (?sim)(?<=TRRN is\\s)\\d+         
    # Log  NewText: ${transid[0]} 
    ${first_split}=    Split String    ${text}    .
    Log    ${first_split}
    ${Second_split}=    Split String    ${first_split}[1]    is 
    Log    ${Second_split}
    ${TRRN_No}=    Set Variable    ${Second_split}[1]
    # Log    ${transid[0]}
    # ${transid[0]}=    Set Variable    ${TRRN_No.strip()}
    ${transid[0]}=    Get Substring    ${TRRN_No}    1
    Sleep    3s

    ${link_element}    Get web Element    xpath=//tr[td[text()='${transid[0]}']]//a[contains(text(), 'Prepare Challan')]
    Click Element    ${link_element}
    Wait Until Element Is Visible    //input[@id="edliContributionRemitted"]      timeout= 30    error= unable to find EPF_Inspection_charges element    
    Input Text    //input[@id="edliContributionRemitted"]                         ${Total_EDLI_Contribution(ER Share A/C 21)}    
    Input Text    //input[@id='epfInspectionCharges']                             ${EPF_Inspection_Charges}
    Input Text    //input[@id="edliAdministrationCharges"]                        ${EDLI_Administration_Charges}
    Input Text    //input[@id="edliInspectionCharges"]                            ${EDLI_Inspection_Charges}
    # Input Text    //input[@id='totalNumberOfEmployeesInMonth']                    ${Total_Number_Of_Employees_In_Month}
    # Input Text    //input[@id="totalNumberOfExcludedEmployeesInMonth"]            ${Total_Number_Of_Excluded_Employees_In_Month}
    # Input Text    //input[@id="totalGrossWagesOfExcludedEmployeesInMonth"]        ${Total_Gross_Wages_Of_Excluded_Employees_In_Month}
    Wait Until Element Is Visible    //button[@id='submitEcr']    timeout= 30    error= unable to submit button    
    Click Element  //button[@id='submitEcr']
    Handle Alert
    Wait Until Element Is Visible    //tr[td[text()='${transid[0]}']]//a[contains(@title, 'Click to finalize challan')]    timeout= 30    error= unable to find finalize element         
    Click Element   //tr[td[text()='${transid[0]}']]//a[contains(@title, 'Click to finalize challan')]
    Handle Alert        
    Click Element When Visible      //tr[td[text()='${transid[0]}']]//a[@title='Click to download challan receipt file.']          DOwnload receipt file    //tr[td[text()='${transid[0]}']]//a[contains(text(), 'Pay')]
    Wait Until Element Is Visible   //tr[td[text()='${transid[0]}']]//a[contains(text(), 'Pay')]    timeout= 30    error= unable to find pay button 
    Click Element                   //tr[td[text()='${transid[0]}']]//a[contains(text(), 'Pay')]    


*** Test Cases ***

# Sending Bot Status Email
# ...    Send_Start_email

Launch EPFO website
    # TRY
    #     Open EPF India Website
    #     Sleep     3s
    #     Click ECR/Returns/Payment Button
    # EXCEPT    
    #     Close Browser
    #     Log    Failed to open the website Retrying again
    #     Open EPF India Website  
    #     ${task_error}=    Set Variable    Launching the EPFO Website
    #     # Send Failure Email    ${task_error}
    # FINALLY
    #     Log    Retried twice and Failed 
    # END

     Open EPF India Website
    # Click ECR/Returns/Payment Button
    Sleep    2s
    ${payment}=    Set Variable    False
    WHILE    '${payment}' == 'False'   
        ${payment}=    Login Process
        Sleep    1s
    END
Login EPFO Application 
    # Sleep    2s
    # ${current_url}=    Set Variable    https://www.epfindia.gov.in/site_en/index.php#
    # WHILE    '${current_url}' == 'https://www.epfindia.gov.in/site_en/index.php#'
    #     ${current_url}=    Login Process  
    #     Run Keyword If    '${current_url}' == 'https://www.epfindia.gov.in/site_en/index.php#'    Log    Login attempt failed. Retrying...
    #     Log    Login successful. Exiting the loop.
    # END
    # Click Payment Menu Button   
    # Click Signin Button
    ${payment}=    Set Variable    False
        WHILE    '${payment}' == 'False'   
            ${payment}=    Login Process
            Sleep    1s
        END
Navigate to ECR upload page
    TRY
        Click Payments Menu
        Click ECR/RETURN FILE Menu Item 
        Click ECR Upload Hyperlink
    EXCEPT    
        Log    Failed to Navigate to ECR upload Page
        ${task_error}=    Set Variable    Navigating to ECR upload page
        # Send Failure Email    ${task_error}
    FINALLY
        Log    ECR PAge Loaded
    END
ECR Fileupload
    TRY
    Click ECR file upload Button 
    Click WageMonth Button    
    Sleep    10s
    EXCEPT    
        Log    Failed while uploading the file
        ${task_error}=    Set Variable    uploading the file to ECR upload page
        # Send Failure Email    ${task_error}
    FINALLY
        Log    Uploaded
    END

ECR File Verification  
    TRY
        Sleep    3s
        ${visible}=    Run Keyword And Return Status    Element should be Visible     //*[@id="tbClaimList"]/tbody/tr/td[12]/a[contains(text(), 'Verify')] 
        Log    ${visible}
        WHILE    ${visible} == False
            Click Other Elements    
            Sleep    20s
            ${visible}=    Run Keyword And Return Status    Element Should Be Visible    //*[@id="tbClaimList"]/tbody/tr/td[12]/a[contains(text(), 'Verify')]
            Log    ${visible}
            Sleep    25s
        END
        Sleep    5s
        Download ECR File and ECR Statement  
        Switch To Original Window
        Click Element    //*[@id="tbClaimList"]/tbody/tr/td[12]/a[contains(text(), 'Verify')]
        Handle Alert
        Sleep    2s
        Generate TRRN Number and Click Prepare Challan Button
        Switch To Original Window
        # Send_Success_email
    EXCEPT    
        Log    Failed while verifying uploaded the file
        ${task_error}=    Set Variable    verifying the uploaded file
        # Send Failure Email    ${task_error}
    FINALLY
        Log    Verified

    END


