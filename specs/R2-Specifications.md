## R2 Specifications
### R2 /register [GET]

#### #) Test Case R2.#  - Template
##### Mocking: 
- Template Mock
##### Actions:
- Template Action

<br />

#### 1) Test Case R2.1  - If the user has logged in, redirect back to the user profile page /
##### Mocking: 
- Mock backend.get_user to return a test_user instance
##### Actions:
- open /logout (to invalid any logged-in sessions that may exist)
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /login again
- validate that current page contains `#welcome-header` element

<br />

#### 2) Test Case R2.2  - otherwise, show the user registration page
##### Mocking: 
- Mock backend.get_user to return to test_user instance
##### Actions:
- open /register
- validate that current page contains `#password2` 

<br />

#### 2) Test Case R2.3  - 	the registration page shows a registration form requesting: email, user name, password, password2
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

### R2 /register [POST]
#### #) Test Case R2.#  - Template
##### Mocking: 
- Template Mock
##### Actions:
- Template Action