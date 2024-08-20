*** Settings ***
Library    RPA.HTTP 


*** Variables ***
#API Setup
${BASE_URL}        https://app.hoppr.in
${ENDPOINT}       /api/uan-generation-linking-process
${USERNAME}       adminapi
${KEY}            eshyosdmtoopcfrgxthftnfwthdicxmmioxedozotygbztmzfecjmxznzersteiketxusgydkpcqcljeptabzxthzmuvpyrfvjgdcwlytxpdvcfwmhytzvkzvrqammra
${DATA_COUNT}     5


${employee_id}    170585
${aadhaar_number}    690706280007
${name}   Akash
${uan_status}    None
${uan_num}    None
${remarks}    Error:Aadhaar authentication failed. Demographic information such as Name, Date of Birth, Gender or any combination of the same available with the UIDAI/AADHAAR system do not match with details available with EPFO. Kindly get it corrected at UIDAI or in the EPFO records through Basic details change functionality.
${entity_status}    creation pending
${uuid}    130c60e2-4221-4179-a294-e1e4c5f2784c
${time}    56



*** Keywords ***

RunAPI
    ${data}=    Create Dictionary    employee_id=${employee_id}     aadhaar_number=${aadhaar_number}    name=${name}   uan_status=${uan_status}    uan_num=${uan_num}    remarks=${remarks}     entity_status=${entity_status}    user_uuid=${uuid}    time=${time}
    ${headers}=  create dictionary   Content-Type=application/json
    ${params}=    Create Dictionary    username=${USERNAME}    key=${KEY}
    RPA.HTTP.Create Session    apisession    ${BASE_URL}    verify=False
    ${response}=    Post Request    apisession    ${ENDPOINT}    params=${params}    data=${data}    headers=${headers}
    Log    ${response}

*** Test Cases ***
runAAAA
    RunAPI