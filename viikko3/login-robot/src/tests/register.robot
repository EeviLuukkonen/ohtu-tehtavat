*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  eevi  eevi1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle1234
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  e  jaakko1234
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  eevi  q
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  eevi  eevijakalle
    Output Should Contain  Password must contain something other that letters a-z

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123