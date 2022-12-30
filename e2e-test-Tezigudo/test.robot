*** Settings ***
Documentation    This is a test that create bill with 1 user are header of bills
...              and it will cant create.
Library     SeleniumLibrary
# Resource           ${CURDIR}/cloud.txt
Resource           ${CURDIR}/local.txt

*** Variables ***
${BROWSER}         Chrome

*** Test Cases ***
Login test
    Open WePay
    Login
    # Reload Page
    Wait Until Page Contains    //div[@class='sweet-alert']    timeout=10s
    Wait Until Page Contains Element    id=plus-btn
    Click Plus Button
    Wait Until Page Contains Element    name=create_title
    Insert Demo Bill and Create it

    # wait until page contains element    class=swal2-confirm swal2-styled
    # Click Button    class=swal2-confirm swal2-styled



*** Keywords ***
Open WePay
    Open Browser   ${SITE_URL}    ${BROWSER}



Insert user and password
    Input Text   name=login   ${USERNAME}
    Input Text   name=password   ${PASSWORD}

Login
    Insert user and password
    Click Button   id=id_submit

Click Plus Button
    Click Button   id=plus-btn

    # Wait Until Page Contains Button   class=swal2-confirm swal2-styled  20s

Insert Demo Bill and Create it
    Input Text   name=title   demo bill
    Input Text   name=topic_name   demo topic
    Input Text   name=topic_price   200
    Input Text   id=username-ts-control   demo
    Press Keys   id=username-ts-control    ENTER
    Click Button  name=create_title