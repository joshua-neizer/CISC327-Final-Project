## R2 Specifications
### R2 /register [GET]

#### 1) Test Case R2.1  - If the user has logged in, redirect back to the user profile page /
##### Mocking: 
- Mock backend.get_user to return a test_user instance
##### Actions:
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element submit
- open /login again
- validate that current page contains `#welcome-header` element

<br />

#### 2) Test Case R2.2  - otherwise, show the user registration page
##### Mocking: 
- Mock backend.get_user to return to test_user instance
##### Actions:
- open /register
- validate that current page contains `#password2` element
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
- if fields exist, do nothing
- if fields do not exist reopen /register

<br />

### R2 /register [POST]
#### 4) Test Case R2.4  - The registration form can be submitted as a [POST] request to the current URL (/register)
##### Mocking: 
- Mock backend.get_user to return to test_user instance
##### Actions:
- open /register
- fill registration form with test data
- click submit
- if form cannot be submitted, redirect to / code 303
    - assert [POST] response to /register with required message

<br />

#### 5) Test Case R2.5  - Email, password, password2 all have to satisfy the same required as defined in R1
##### Mocking: 
- Mock backend.get_user to return to test_user instance
##### Actions:
- open /register
- fill registration with test data
- Check email, password and password2
    - request.form.get('email')
    - validate email follows all RFC 5322 spec (e.g. local part of address can contain A to Z, 0 to 9, !#$&'*+-/=?^_`{|}~
    - request.form.get('password')
    - validate email follows required complexity (i.e. min length 6, at least one upper case, at least one one lower case, at least one special character)
    - request.form.get('password2')
    - validate email follows required complexity (i.e. min length 6, at least one upper case, at least one one lower case, at least one special character)
- if any of these validations fail
    - assert [POST] response to /register with required message

<br />

#### 6) Test Case R2.6  - Password and password2 have to be exactly the same
##### Mocking: 
- Mock backend.get_user to return to test_user instance
##### Actions:
- open /register
- enter user password in `#password`
- enter user password2 in `#password2`
- click submit
- if #password and #password2 are not the exact same
    - assert [POST] request to /register with error message 'registration failed'

<br />


#### 7) Test Case R2.7  - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character.
##### Mocking: 
- Mock backend.get_user to return to test_user instance
##### Actions:
- open /register
- enter name in `#name`
- request.form.get('name')
- validate name follows the follow conditions
    - checks if empty
    - checks if alphanumeric-only
    - checks if there is any space that is not the first or last character
- if any of these tests fail
    - asset [POST] request to \register with error message 'registration failed'

<br />


#### 8) Test Case R2.8  - User name has to be longer than 2 characters and less than 20 characters.
##### Mocking: 
- Template Mock
##### Actions:
- open /register
- enter name in `#name`
- click submit
- if `#name` is less than three characters or more than nineteen characters
    - asset [POST] request to \register with error message 'registration failed'

<br />


#### 9) Test Case R2.9  - For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute)
##### Mocking: 
- Mock backend.get_user to return to test_user instance
##### Actions:
- open /register
- enter data in input fields
- click submit
- if formatting errors exist
    - assert [POST] request to /register with error message 'registration failed'
    - open /login
    - display message "{} format is incorrect.'.format(the_corresponding_attribute)"

<br />


#### 10) Test Case R2.10  - If the email already exists, show message 'this email has been ALREADY used'
##### Mocking: 
- Mock backend.get_user to return to test_user instance
##### Actions:
- open /register
- fill out registration form
- click submit
- backend calls register_user(email, password, password, password2)
- if `#email` exists, return with error "email already exists"
    - assert [POST] request to /register with error message 'registration failed'


<br />


#### 11) Test Case R2.11  - If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page
##### Mocking: 
- Mock backend.get_user to return to test_user instance
##### Actions:
- open /register
- enter data into input fields
- click submit
- backend calls register_user(email, name, password, password2)
    - assert [POST] request to /register success
    - backend calls create_user(email, name, password)
    - backend calls set_balance(email, password, 5000)
- open /register
