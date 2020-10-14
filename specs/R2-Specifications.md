# R2 Specifications
## R2 /register [GET]
### 1) Test Case R2.1  - If the user has logged in, redirect back to the user profile page /
#### Actions:
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /login again
- validate that current page contains `#welcome-header` element

<br />

### 2) Test Case R2.2  - otherwise, show the user registration page
#### Actions:
- open /register
- validate that current page contains `#register` element
- if fields exist, do nothing

<br />

#### 3) Test Case R2.3  - 	the registration page shows a registration form requesting: email, user name, password, password2
##### Mocking: 
- Mock backend.get_user to return to test_user instance
##### Actions:
- open /register
- validate that current page contains the following elements
    - `#email`
    - `#name`
    - `#password`
    - `#password2`

<br />

## R2 /register [POST]
### 4) Test Case R2.4  - The registration form can be submitted as a [POST] request to the current URL (/register)
#### Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password='Password123!'
    password2='Password123!'
)
```
#### Actions:
**Positive**
- open /register
- fill out input elements:
    - `#email` with the email from test_user instance
    - `#name` with the name from test_user instance
    - `#password` with the password from test_user instance
    - `#password2` with the password2 from test_user instance
- click element `input[type="submit"]`
- validate that current page element `#registration-fail` has style `visibility: hidden`
- validate that current page element `#registration-success` has style `visibility: visible`
- validate that current page element `#registration-success` has innerHTML *"Registration Successful"*

**Negative**
- open /register
- click element `input[type="submit"]`
- validate that current page element `#registration-fail` has style `visibility: visible`
- validate that current page element `#registration-fail` has innerHTML *"Registration Error: Please try again"*
- validate that current page element `#registration-success` has style `visibility: hidden`

<br />

### 5) Test Case R2.5  - Email, password, password2 all have to satisfy the same required as defined in R1
#### Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password='Password123!'
    password2='Password123!'
)

test_user_bad_email = User(
    email=['', 'test_frontendtest.com', 'test_frontend@testcom', '.test_frontend@test.com']
)

test_user_bad_password = User(
    password=['', 'Pass!', 'password123!', 'PASSWORD123!', 'Password123']
)

test_user_bad_password2 = User(
    password2=['', 'Pass!', 'password123!', 'PASSWORD123!', 'Password123']
)
```
#### Actions:
**Positive**
- open /register
- fill out input elements:
    - `#email` with the email from test_user instance
    - `#name` with the name from test_user instance
    - `#password` with the password from test_user instance
    - `#password2` with the password2 from test_user instance
- click element `input[type="submit"]`
- validate that current page element `#registration-fail` has style `visibility: hidden`
- validate that current page element `#registration-success` has innerHTML *"Registration Successful"*
- validate that current page element `#registration-success` has style `visibility: visible`

**Negative - Email**
- open /register
- fill out input elements:
    - `#name` with the name from test_user instance
    - `#password` with the password from test_user instance
    - `#password2` with the password2 from test_user instance
- iterate over email array in test_user_bad_email, for every email in the array:
    - enter the email in input element with id `#email`
    - click element `input[type="submit"]`
    - validate that current page element `#registration-fail` has style `visibility: visible`
    - validate that current page element `#registration-fail` has innerHTML *"Registration Error: Invalid email address"*
    - validate that current page element `#registration-success` has style `visibility: hidden`

**Negative - Password**
- open /register
- fill out input elements:
    - `#email` with the email from test_user instance
    - `#name` with the name from test_user instance
    - `#password2` with the password2 from test_user instance
- iterate over password array in test_user_bad_password, for every password in the array:
    - enter the password in input element with id `#password`
    - click element `input[type="submit"]`
    - validate that current page element `#registration-fail` has style `visibility: visible`
    - validate that current page element `#registration-fail` has innerHTML *"Registration Error: Invalid password, ensure it is minimum length 6, at least one upper case, at least one lower case, and at least one special character"*
    - validate that current page element `#registration-success` has style `visibility: hidden`

**Negative - Password2**
- open /register
- fill out input elements:
    - `#email` with the email from test_user instance
    - `#name` with the name from test_user instance
    - `#password` with the password2 from test_user instance
- iterate over password2 array in test_user_bad_password2, for every password in the array:
    - enter the password in input element with id `#password2`
    - click element `input[type="submit"]`
    - validate that current page element `#registration-fail` has style `visibility: visible`
    - validate that current page element `#registration-fail` has innerHTML *"Registration Error: Entered passwords are not identical"*
    - validate that current page element `#registration-success` has style `visibility: hidden`

<br />

### 6) Test Case R2.6  - Password and password2 have to be exactly the same
#### Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password='Password123!'
    password2='Password123!'
)

test_user_bad_password2 = User(
    password2='Password123! '
)
```
#### Actions:
**Positive**
- open /register
- fill out input elements:
    - `#email` with the email from test_user instance
    - `#name` with the name from test_user instance
    - `#password` with the password from test_user instance
    - `#password2` with the password2 from test_user instance
- click element `input[type="submit"]`
- validate that current page element `#registration-fail` has style `visibility: hidden`
- validate that current page element `#registration-success` has innerHTML *"Registration Successful"*
- validate that current page element `#registration-success` has style `visibility: visible`

**Negative**
- open /register
- fill out input elements:
    - `#email` with the email from test_user instance
    - `#name` with the name from test_user instance
    - `#password` with the password from test_user instance
    - `#password2` with the password2 from test_user_bad_password instance
- click element `input[type="submit"]`
- validate that current page element `#registration-fail` has style `visibility: visible`
- validate that current page element `#registration-fail` has innerHTML *"Registration Error:  Entered passwords are not identical"*
- validate that current page element `#registration-success` has style `visibility: hidden`

<br />


### 7) Test Case R2.7  - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character.
#### Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password='Password123!'
    password2='Password123!'
)

test_user_bad_name= User(
    name=['', 'test_frontend123!', ' test_frontend123', 'test_frontend123 ']
)
```
#### Actions:
**Positive**
- open /register
- fill out input elements:
    - `#email` with the email from test_user instance
    - `#name` with the name from test_user instance
    - `#password` with the password from test_user instance
    - `#password2` with the password2 from test_user instance
- click element `input[type="submit"]`
- validate that current page element `#registration-fail` has style `visibility: hidden`
- validate that current page element `#registration-success` has innerHTML *"Registration Successful"*
- validate that current page element `#registration-success` has style `visibility: visible`

**Negative**
- open /register
- fill out input elements:
    - `#email` with the email from test_user instance
    - `#password` with the password from test_user instance
    - `#password2` with the password2 from test_user instance
- iterate over name array in test_user_bad_name, for every name in the array:
    - enter the name in input element with id `#name`
    - click element `input[type="submit"]`
    - validate that current page element `#registration-fail` has style `visibility: visible`
    - validate that current page element `#registration-fail` has innerHTML *"Registration Error: Invalid name, ensure it is non-empty, alphanumeric, and doesn't have a space as the first or last character."*
    - validate that current page element `#registration-success` has style `visibility: hidden`

<br />


### 8) Test Case R2.8  - User name has to be longer than 2 characters and less than 20 characters.
#### Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password='Password123!'
    password2='Password123!'
)

test_user_bad_name= User(
    name=['te', 'test_frontend1234567890']
)
```
#### Actions:
**Positive**
- open /register
- fill out input elements:
    - `#email` with the email from test_user instance
    - `#name` with the name from test_user instance
    - `#password` with the password from test_user instance
    - `#password2` with the password2 from test_user instance
- click element `input[type="submit"]`
- validate that current page element `#registration-fail` has style `visibility: hidden`
- validate that current page element `#registration-success` has innerHTML *"Registration Successful"*
- validate that current page element `#registration-success` has style `visibility: visible`

**Negative**
- open /register
- fill out input elements:
    - `#email` with the email from test_user instance
    - `#password` with the password from test_user instance
    - `#password2` with the password2 from test_user instance
- iterate over name array in test_user_bad_name, for every name in the array:
    - enter the name in input element with id `#name`
    - click element `input[type="submit"]`
    - validate that current page element `#registration-fail` has style `visibility: visible`
    - validate that current page element `#registration-fail` has innerHTML *"Registration Error: Invalid name, ensure it is at least 3 characters, but no longer than 20"*
    - validate that current page element `#registration-success` has style `visibility: hidden`

<br />


#### 9) Test Case R2.9  - For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute)'
##### Actions:
- open /register
- click element `input[type="submit"]`
- validate that current page element `#registration-fail` has style `visibility: visible`
- validate that current page element `#registration-fail` has innerHTML *"Registration Error: Please try again"*
- validate that current page element `#registration-success` has style `visibility: hidden`
- open /login
- validate that current page has element `message` has style `visibility: visible`
- validate that current page element `message` has innerHTML *"email, name, password, password2 format s incorrect"*

<br />

### 10) Test Case R2.10  - If the email already exists, show message 'this email has been ALREADY used'
#### Mocking: 
- Mock backend.get_user to return a test_user instance
#### Actions:
- open /register
- fill out input elements:
    - `#email` with the email from test_user instance
    - `#name` with the name from test_user instance
    - `#password` with the password from test_user instance
    - `#password2` with the password2 from test_user instance
- click element `input[type="submit"]`
- validate that current page element `#registration-fail` has style `visibility: visible`
- validate that current page element `#registration-success` has innerHTML *"Registration Error: Entered email is already in use"*
- validate that current page element `#registration-success` has style `visibility: hidden`


<br />


### 11) Test Case R2.11  - If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page
#### Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password='Password123!'
    password2='Password123!'
)
```
#### Actions:
- open /logout
- open /register
- fill out input elements:
    - `#email` with the email from test_user instance
    - `#name` with the name from test_user instance
    - `#password` with the password from test_user instance
    - `#password2` with the password2 from test_user instance
- click element `input[type="submit"]`
- validate that current page element `#registration-fail` has style `visibility: hidden`
- validate that current page element `#registration-success` has innerHTML *"Registration Successful"*
- validate that current page element `#registration-success` has style `visibility: visible`
- open /login
- fill out input elements:
    - `#email` with the email from test_user instance
    - `#name` with the name from test_user instance
- open /
- validate that current page contains `#welcome-header` element
- validate current page element `#balance` has value *5000*