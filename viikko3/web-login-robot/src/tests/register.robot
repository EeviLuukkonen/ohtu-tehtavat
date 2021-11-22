*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

***Test Cases***
Register With Valid Username And Password
    Set Username  moikka
    Set Password  moikka1234
    Set Password Confirmation  moikka1234
    Submit Registration Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  mo
    Set Password  moikka12345
    Set Password Confirmation  moikka12345
    Submit Registration Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  moikkaa
    Set Password  mo1
    Set Password Confirmation  mo1
    Submit Registration Credentials
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  moikkaa
    Set Password  moikkaa1234
    Set Password Confirmation  moikkaa12345
    Submit Registration Credentials
    Register Should Fail With Message  Password and password confirmation don't match

Login After Successful Registration
    Create User And Go To Login Page 
    Login As Kalle
    Main Page Should Be Open

Login After Failed Registration
    Set Username  moikkaa
    Set Password  mo1
    Set Password Confirmation  mo1
    Submit Registration Credentials
    Go To Login Page
    Set Username  moikkaa
    Set Password  mo1
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password


***Keywords***
Go To Register Page
    Go To  ${REGISTER URL}

Submit Registration Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open

Login As Kalle
    Set Username  kalle
    Set Password  kalle123
    Submit Login Credentials

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}