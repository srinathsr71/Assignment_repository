*** Settings ***
Library    Collections
Library    RequestsLibrary

*** Variables ***
${listu} =    https://reqres.in/api/users?page=2
${createu} =    https://reqres.in/api/users
${updateu} =    https://reqres.in/api/users/2
${deleteu} =    https://reqres.in/api/users/2
*** Keywords ***
List users
    [Documentation]      Test Get a list of all users
    ${response}=    GET    ${listu}    expected_status=200
    Should Be Equal As Strings    ${response.status_code}    200
    Log    ${response.json()}
Create User
    [Arguments]    ${name}    ${job}
    [Documentation]  Test Create a new user with  valid data   
    ${request}=    Create Dictionary    name=${name}    job=${job}
    ${response}=    POST    ${createu}    json=${request}    expected_status=201
    Should Contain    ${response.text}    ${name}
    Should Be Equal As Strings    ${response.status_code}    201
    Log    ${response.json()}

Create User With Invalid data
    [Documentation]   Test create a new user with invalid data
    ${request}=    Create Dictionary    name=" "     job=" "
    ${response}=    POST    ${createu}    json=${request}    expected_status=201   
    Should Be Equal As Strings    ${response.status_code}    201
Update User
    [Arguments]    ${name}    ${job}
    [Documentation]    Test Update the data of an existing user
    ${request}=    Create Dictionary    name=${name}    job=${job}
    ${response}=    PATCH    ${updateu}    json=${request}    expected_status=200
    Should Contain    ${response.text}    ${name}
    Should Be Equal As Strings    ${response.status_code}    200
    Log    ${response.json()}
Delete User
    [Documentation]    Test Delete a created user
    ${response}=    DELETE    ${deleteu}    expected_status=204
    Should Be Equal As Strings    ${response.status_code}    204
*** Test Cases ***
Executing tests
    List users
    Create User    saikiran    tester
    Create User    snathosh    Manual Tester
    Create User With Invalid data    
    Update User    kiransai    SDET
    Delete User        
