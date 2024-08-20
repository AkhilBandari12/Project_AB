*** Settings ***
Library           RPA.HTTP

*** Variables ***
${API_URL}        https://app.hoppr.in
${ENDPOINT}       /api/uan-generation-linking-process
${USERNAME}       adminapi
${KEY}            eshyosdmtoopcfrgxthftnfwthdicxmmioxedozotygbztmzfecjmxznzersteiketxusgydkpcqcljeptabzxthzmuvpyrfvjgdcwlytxpdvcfwmhytzvkzvrqammra
${DATA_COUNT}     5

*** Tasks ***
GET API
    ${params}=    Create Dictionary    username=${USERNAME}    key=${KEY}    data_count=${DATA_COUNT}
    RPA.HTTP.Create Session    apisession    ${API_URL}
    ${response}=    Get Request    apisession    ${ENDPOINT}    params=${params}
    Log    ${response.status_code}
    Log    ${response.json()}

POST API
    ${headers}=  create dictionary   Content-Type=application/json
    ${params}=    Create Dictionary    username=${USERNAME}    key=${KEY}
    # ${data}=    Create Dictionary    employee_id=100     aadhaar_number=007    name=abc   uan_status=NA    uan_num=000    remarks=NA     entity_status=NA    user_uuid=1111    time=30
    ${data} = {'employee_id': 168663, 'aadhaar_number': '469500867395', 'name': 'J PRATHIPAN', 'uan_status': 'Newly created', 'uan_num': '101221665846', 'remarks': 'sucess', 'entity_status': 'approval pending','user_uuid':'1111','time':30}
    RPA.HTTP.Create Session    apisession    ${API_URL}
    ${response}=    Post Request    apisession    ${ENDPOINT}    params=${params}    data=${data}   headers=${headers}

   


    