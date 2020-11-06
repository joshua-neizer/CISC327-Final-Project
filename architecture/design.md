# Design

## Structure

For the most part, the structure of this software
will match the template.
However,
logic that can be easily separated,
such as login / register validation,
should be refactored into other files.
Applying this pattern enforces 
the Single Responsibility Principle,
which minimizes convolution of concerns.
In addition,
to achieve the simplest possible implementation,
small, pure functions are preferred to
implicit object state.
This also makes testing easier,
as the outputs of each function are
designed to be consistent.

The front end of the program has the responsibilities of being the interface with the user. 
Here, the user is able to enter their information into forms to login and register as a new user, in `/login` and `/register` respectively. The frontend has the responsibility to ensure validity and correct formatting
in all of the submitted information, as outlined in the requirements. This will maintain consistent data storage. The front end does not interact with the database, but requests
information through the backend and uses POST methods to enter new information.

The backend of the program has the responsibility of writing and reading 
information to and from the database. The backend starts new sessions, saves new
users, updates user information and will retrieve user information. Moreover, the
backend is responsible for database security as no information can be accessed without 
appropriate permissions such as valid passwords.

## Function Descriptions

| File Name | Method | Intention |
|--|--|--|
| `frontend.py` | | |
| | **register_get** |  If a user is logged in redirect to the home page, otherwise redirect to register <br> :return: home page if logged in, register page if not logged in  |
| | **register_post** |  Intake register form information and validate that all entered information follows requirements R1 (login) and R2 (register).<br>:return: if requirement not met, error page with specific error message<br>:return: if requirements met, redirect to login page  |
| | **login_get** |  If user is logged in, redirect to home page, otherwise redirect to login  |
| | **login_post** |  Intake all login form information and validate using login_user then redirect to home  |
| | **logout** |  When user logs out, remove logged in user and redirect to home page<br>:return: redirect to home page  |
| | **authenticate** |  param inner_function: any python function that accepts a user object<br>Wrap any python function and check the current session to see if the user has logged in. If login, it will call the inner_function with the logged in user object. |
| | **profile** |  authentication is done in the wrapper function see above  |
| | **page_not_found** |  Handle 404 errors<br>:param error: error message<br>:return: display a 404 error page  |
| `backend.py` | | |
| | **get_user** | Get a user by a given email<br>:param email: the email of the user<br>:return: a user that has the matched email address |
| | **login_user** | Check user authentication by comparing the password<br>:param email: the email of the user<br>:param password: the password input<br>:return: the user if login succeeds |
| | **register_user** | Register the user to the database<br>:param email: the email of the user<br>:param name: the name of the user<br>:param password: the password of user<br>:param password2: another password input to make sure the input is correct<br>:return: an error message if there is any, or None if register succeeds |
| `login_format.py` | | |
| | **is_valid_password()** | Returns boolean indicating whether a password is valid, according to R1 and R2 password definitions |
| | **is_valid_email()** | Returns a boolean indicating whether an email is valid, according to RFC 5322 requirements, using the `validate_email` library  |
| | **is_valid_username()** | Returns boolean indicating whether a username is valid, according to R1 and R2 username definitions |

## Program Diagram
![User](qa327.png "User Diagaram")
![Relationships](qa327_packages.png "Relationships Diagram")

### Description

The **diagram to the left** details the attributes of the user model. This has the attributes balance, email, id, name and password. These attributes contain the user's account balance, the email for their account, the user id name, the name of the individual associated with that account, and their account password, respectively. 

The **diagram to the right** shows the relationships between packages in the program. The main program `qa327`, inherits methods and functions, from almost all other programs. The outlier is `login_format`, as it is used to validate inputted user information within the `frontend` program.

As a whole, the `__main__.py` program will instantiate the website by running the server. When the user interacts with the website, `frontend.py` will handle the various http requests from the client by redirecting the user to the appropriate page and posting requests for them. Whenever the user enters information into the client, `frontend.py` uses functions defined in `login_format.py` to ensure correct formatting and validity of information as outlined in the requirements. `frontend.py` intakes information and passes it to `backend.py` to perform any database operations (eg. reading, writing, updating etc.) with `models.py`.

## Code Style

To establish a consistent and clear coding style,
the team has decided to follow some of the
[PEP-8](https://www.python.org/dev/peps/pep-0008/)
conventions.
To guarantee that the team adheres to these guidelines,
the PyLint tool will be used.
A custom linter configuration will also be created from
the default template,
such that style rules can be adjusted to
the team's preference and application. PyLint's scoring system will be used to ensure code meets clarity objectives as only code with a score of **9/10 or higher** is acceptable. 

### Code Style Examples
* Snake case for variable names
* Using four spaces for indentation
* All constant variables have format `CONSTANT_NAME`
* All boolean values have format `is_NAME`
* All lists variables are plural, .i.e `users`

# Test Design

## Test strategy
The levels of testing will be unit testing and integration testing. Unit testing will be done indiviudally by each group member who is implementing a given specification (R1,R2, etc.). The unit testing will be done using pytest and will take place before merging into main. Individuals should ensure that respective unit tests pass, but in some cases it is acceptable for integration tests to fail as they rely on mulitple parts. Integration testing will be able to check if the created unit works with the overall architecture while also potentially highlighting any issues not caught by unit testing. 

The testing will be done using automated assertion based tests. We will use Selenium to develop the tests which will be used to verify if specific elements and outputs are observed given the inputs. Assertion based testing will make it easy to see if there is a bug in the code as the output will be false if there is an issue.

Tests will be set up such that we manually choose inputs (see test case design), perform a minimal series of actions to achieve the desired output, and then assert the expected outputs to verify that the functionality matches the specifiations.

To develop the tests there are three main tools that will be used. Pytest will be used to for the tests with code split up into specific folders allowing us to focus on individual aspects of the design. Selenium will be used to assert inputs and navigate the webpage for the tests. Lastly, GitHub actions will be used for CI and will be set up to work on pull requests into main only (see test procedures)

The final important aspect of the test strategy are the standards. As explained previously, we will adhere to PEP8 conventions, and ensuring such with Pylint. Standardized naming is very important for tests and makes creating tests easier and clearer. It will be clear as to what is being tested and if there are any problems, what the bug is. Tests will be named including the tested method, the expected input/state, and the behaviour (i.e. loginUser_userDoesNotExist_someException())

## Test Plans
The items we are testing are the features from R1, R2, R3, R7 and R8, including the frontend and the backend. These include all of the methods outlined in the function description 
table. There may be more unit tests added in as needed, depending on how successful
integration testing is.

As stated previously, the levels of testing that we are going to be used are unit testing
and integration testing. Unit testing to validate software components are fulfilling their specifications, and integration testing to validate that the data flows properly 
from each software component. System testing and acceptance testing cannot be 
done at this time as R4, R5 and R6 have yet to implemented.

There is no specific order while doing unit testing. However, while integrating the
unit tests, we will test R2 --> R1 --> R3 --> R7. This is because to verify login, registration
needs to be implemented. And to go the general user page, the user needs to be registered
and logged in. Lastly for a user to login out, they must be logged in. R8 is independent
of these tests as it does not have any dependency on the others.

We will use the pytest environment when testing modules within python. To validate
the tests across systems, we will be using python's virtualenv, which is a tool for creating
isolated Python environments containing their own copy of python. All selenium will be
done with Google Chrome as the chosen web browser

All of the unit tests are going to be explicitly divided up between group members, and 
they are responsible for validating those specific tests. Therefore, when integrating testing
begins, if there is a bug that is clearly from an overlooked unit test, the individual
responsible for that test will be responsible for identifying what was overlooked. However,
in instances where the source of bug is clear and there is an simple solution, an individual may fix the bug to avoid people waiting on each other. The person responsible for the feature's
unit testing will be informed of the bug and solution. They should then validate the solution, 
and review their unit tests to ensure no other bugs remain.

We want to be able to cover as close to 100% of the items we want to test as possible.
Instances at which there would be slightly less than 100% coverage may be due to 
setup tasks like database creation being omitted from testing.

## Test case design
All requirements will be tested with positive and negative cases. For example, requirements specifying the username formatting will input a valid and invalid username as test cases. Requirements with quantitative specifications, such as a character limit, will be tested with boundary cases as well. Note that a boundary case and negative case can be represented by the same test. 

Each test case will be partitioned specifically according to the requirement's inputs. Thus, a test resulting in a negative response will test one input requirement specifically. For example, invalid usernames may contain special characters, a space in the middle, or too many characters. This will be covered by 3 partitions, each with positive and negative cases and a boundary case for the character limit. 

Integration testing will be conducted by mocking the server and using assert statements in Selenium. Unit testing will be conducted using assert statements. An example is shown below:

```
# Negative case
# Expected output = "Fail: too short"
user.name = "a"
assert len(user.name) > 2, "Fail: too short"
```
All test results will be collected by pytest. If an assertion evaluates to false, an exception will be thrown with a specified message. 

## Test procedures

Locally, different test levels can be run independently,
as each test level will be assigned to a folder.
Thus, different test levels can be run using commands such as these.

```
pytest qa327_test # test all
pytest qa327_test/backend # test backend
pytest qa327_test/integration # test integration
pytest qa327_test/frontend # test frontend
```

The overall test command will then be run on all pull requests into main.
Restricting the rate at which CI is applied will reduce the budget,
while maintaining our overall confidence about the codebase on the main branch.
For pull requests on feature branches,
it is presumed that team members will run tests individually.
However, if somebody forgets to, continuous integration will catch the error
when the pull request to main is opened.

## Test Results

The pytest framework will be leveraged to generate test results.
The output format will be HTML,
to demonstrate the output in a clear manner.
A plugin such as [pytest-html](https://pypi.org/project/pytest-html/)
can be used to achieve this.