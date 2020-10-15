# Test Cases Summary

|  Specification | Test Case ID   |  Purpose  |
|---|---|---|
|  If the user hasn't logged in, show the login page | R1.1| Validates that if there is no user currently logged in, the login page is shown  |  
| The login page has a message that by default says 'please login'  |  R1.2| Checks that the login page shows a welcome message 'please login' |  
| If the user has logged in, redirect to the user profile page  | R1.3  |  Validates that is a user is logged into the system, they are redirected to the profile page |   
| The login page provides a login form which requests two fields: email and passwords - Positive  | R1.4.1| Validates that the login page correctly shows an email and password field if no errors occur  |
| The login page provides a login form which requests two fields: email and passwords - Negative	| R1.4.2| Validates that when the login form is not loaded correctly with an email and password field, the page is reloaded	|  
|  The login form can be submitted as a POST request to the current URL /login | R1.5   | Checks that the login form can be submitted as a POST request to the same URL  |   
| Email and password both cannot be empty  | R1.6  | Checks that when a user attempts to login, the email and password fields cannot be empty  | 
|  Email has to follow addr-spec defined in RFC 5322 - Positive | R1.7.1  |  Validates that the entered email follows RFC 5322 specifications | 
|Email has to follow addr-spec defined in RFC 5322 - Negative	| R1.7.2  |	Validates that if the email entered does not follow RFC 5322 specifications, an appropriate error message is shown to the user|
| Password has to meet the required complexity - Positive  | R1.8.1  |  Validates that the entered password meets the required complexity |   
| Password has to meet the required complexity - Negative  | R1.8.2  | Validates that if the password entered does not meet the required complexity, an appropriate error message is shown to the user  | 
| For any formatting errors, render the login page and show the message 'email/password format is incorrect'  | R1.9  |  Checks that if there are any formatting errors to the email and password, the login page is reloaded and the user is shown an error message | 
| If email/password are correct, redirect to /  | R1.10  | Checks that if the email and password is correct, the user is redirected to the home page with no errors  |  
| Otherwise, redirect to /login and show message 'email/password combination incorrect'  | R1.11  | If there are any errors outside of the above, the user is redirected to the /login page with the appropriate error message  |
| 	If the user has logged in, redirect back to the user profile page /  | R2.1  | Checks if the user has logged in, and validates that user gets redirected to the user profile page /  | 
| otherwise, show the user registration page  | R2.2  | validates that the registration page is shown  |  
| the registration page shows a registration form requesting: email, user name, password, password2  | R2.3  | Checks that registration page has elements for email, user name, password and password2  |   
|  The registration form can be submitted as a POST request to the current URL (/register) | R2.4  | Validates the registration form can be submitted and redirects user to /register   | 
| 	Email, password, password2 all have to satisfy the same required as defined in R1  | R2.5.1  | Validates that if the correct email, password and password2, that the form can submits without errors  |  
| 	Email, password, password2 all have to satisfy the same required as defined in R1  | R2.5.2  |  Validates that when an incorrect email is entered in the form, it will not submit and an corresponding error message is displayed |
| 	Email, password, password2 all have to satisfy the same required as defined in R1  | R2.5.3  | Validates that when an incorrect password is entered in the form, it will not submit and an corresponding error message is displayed  |
| 	Email, password, password2 all have to satisfy the same required as defined in R1  | R2.5.4  | Validates that when an incorrect password2 is entered in the form, it will not submit and an corresponding error message is displayed  |
| 	Password and password2 have to be exactly the same  | R2.6.1  | Validates that if a password and password2 are the exact the same, the registration form submits successfully  |
| 	Password and password2 have to be exactly the same  | R2.6.2  | Validates that if a password and password2 are not the exact the same, the registration form will not submit and an corresponding error message is displayed |      
| User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character.  | R2.7.1  | Validates that if the correct user name is entered in the form, the registration form submits successfully   | 
| User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character.  | R2.7.2  | Validates that if a user name that is not either non-empty, alphanumeric-only, or has a space as the first or last character, the registration form will not submit and an corresponding error message is displayed  | 
| 	User name has to be longer than 2 characters and less than 20 characters.  | R2.8.1  | Validates that if the user name entered is great than 2 but less than 20 characters, the registration form submits successfully  | 
| 	User name has to be longer than 2 characters and less than 20 characters.  | R2.8.2 |  Validates that if a user name is either less than 3 characters or greater than 19 characters is entered, the registration form will not submit and an corresponding error message is displayed |   
| For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute)  | R2.9  | Validates that if there is any formatting errors, it redirects back to /login and shows the message '{} format is incorrect.'.format(the_corresponding_attribute)  |   
| If the email already exists, show message 'this email has been ALREADY used'  | R2.10  | Validates that if the email already exists, show message 'this email has been ALREADY used'  | 
| 	If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page  | R2.11  | Validates if no error regarding the inputs following the rules above, a new user is created, the balance is set to 5000, and it goes back to the /login page  |
|   |   |   |   
|   |   |   | 
|   |   |   |  
|   |   |   |   
|   |   |   | 
|   |   |   |  
|   |   |   |   
|   |   |   | 
|   |   |   |  
| The name of the sold ticket has to be alphanumeric-only | R4.1.1 | Check if the selling actions succeed with an alphanumeric ticket name |   
| The name of the sold ticket has to be alphanumeric-only | R4.1.2 | Check if the selling actions fail when the ticket name has a special character in it |
| The name of the sold ticket cannot contain a space before  | R4.1.3 | Check if the selling actions fail when the ticket name begins with a space  |  
| The name of the sold ticket cannot contain a space after  | R4.1.4 | Check if the selling actions fail when the ticket name ends with a space |   
| The length of the sold ticket name has to be less than 60 characters | R4.2.1  | Check if selling actions suceed with a ticket name less than 60 characters | 
| The length of the sold ticket name has to be less than 60 characters | R4.2.2  | Check if selling actions fail with a ticket name greater than 60 characters |  
| The quantity of a sold ticket must be greater than 1 and less than 100 | R4.3.1  | Check if selling actions succeed with ticket quantity greater than 0 and less than 100 |   
| The quantity of a sold ticket must be greater than 1 and less than 100  | R4.3.2  | Check if selling actions fail with ticket quantity less than 1  | 
| The quantity of a sold ticket must be greater than 1 and less than 100  | R4.3.3  | Check if selling actions fail with ticket quantity greater than 100 |  
| The price of a sold ticket must be greater than 10 and less than 100  | R4.4.1  | Check if selling actions suceed with ticket price within range  |   
| The price of a sold ticket must be greater than 10 and less than 100  | R4.4.2  | Check if selling actions fail with ticket price less than 10  | 
| The price of a sold ticket must be greater than 10 and less than 100 | R4.4.3  | Check if selling actions fail with ticket price greater than 100  |  
| The date of a sold ticket must be given in the format YYYYMMDD  | R4.5.1  | Check if selling actions suceed with ticket date in YYYYMMD format |   
| The date of a sold ticket must be given in the format YYYYMMDD  | R4.5.2  | Check if selling actions fail with ticket date in alternative format | 
| The date of a sold ticket must be given in the format YYYYMMDD | R4.5.3  | Check if selling actions fail with ticket date in YYYYDDMM format  |  
| For any errors, redirect back to `/` and show an error message | R4.6.1  | Check if selling actions succeed when valid ticket is sold  |   
| For any errors, redirect back to `/` and show an error message  | R4.6.2  | Check if selling actions fail and are redirected when an invalid ticket is sold | 
| The added new ticket information will be on the user profile page | R4.7  | Check if ticket is present on profile page after selling valid ticket  |  
| The name of the updated ticket has to be alphanumeric-only | R5.1.1 | Check if the updating actions succeed with an alphanumeric ticket name |   
| The name of the updated ticket has to be alphanumeric-only | R5.1.2 | Check if the updating actions fail when the ticket name has a special character in it |
| The name of the updated ticket cannot contain a space before  | R5.1.3 | Check if the updating actions fail when the ticket name begins with a space  |  
| The name of the updated ticket cannot contain a space after  | R5.1.4 | Check if the updating actions fail when the ticket name ends with a space |   
| The length of the updated ticket name has to be less than 60 characters | R5.2.1  | Check if updating actions suceed with a ticket name less than 60 characters | 
| The length of the updated ticket name has to be less than 60 characters | R5.2.2  | Check if updating actions fail with a ticket name greater than 60 characters |  
| The quantity of a updated ticket must be greater than 1 and less than 100 | R5.3.1  | Check if updating actions succeed with ticket quantity greater than 0 and less than 100 |   
| The quantity of a updated ticket must be greater than 1 and less than 100  | R5.3.2  | Check if updating actions fail with ticket quantity less than 1  | 
| The quantity of a updated ticket must be greater than 1 and less than 100  | R5.3.3  | Check if updating actions fail with ticket quantity greater than 100 |  
| The price of a updated ticket must be greater than 10 and less than 100  | R5.4.1  | Check if updating actions suceed with ticket price within range  |   
| The price of a updated ticket must be greater than 10 and less than 100  | R5.4.2  | Check if updating actions fail with ticket price less than 10  | 
| The price of a updated ticket must be greater than 10 and less than 100 | R5.4.3  | Check if updating actions fail with ticket price greater than 100  |  
| The date of a updated ticket must be given in the format YYYYMMDD  | R5.5.1  | Check if updating actions suceed with ticket date in YYYYMMD format |   
| The date of a updated ticket must be given in the format YYYYMMDD  | R5.5.2  | Check if updating actions fail with ticket date in alternative format | 
| The date of a updated ticket must be given in the format YYYYMMDD | R5.5.3  | Check if updating actions fail with ticket date in YYYYDDMM format  |  
| The ticket of the given name must exist | R5.6.1  | Check if updating actions suceed with existing ticket |
| The ticket of the given name must exist | R5.6.2  | Check if updating actions fail with nonexistent ticket | 
| For any errors, redirect back to `/` and show an error message | R5.7.1  | Check if updating actions suceed during a valid ticket update |   
| For any errors, redirect back to `/` and show an error message | R5.7.2  | Check if updating actions fail during an invalid ticket update |
| The name of the ticket has to be alphanumeric-only  | R6.1.1  | Check if the buying actions succeed with an alphanumeric ticket name |   
| The name of the ticket has to be alphanumeric-only  | R6.1.2  | Check if the buying actions fail when the ticket name has a special character in it  | 
| Space in the ticket name is only allowed if it is not the first or last character  | R6.1.3  | Check if the buying action succeeds when the ticket name has a space not as the first or last character  |   
| Space in the ticket name is only allowed if it is not the first or last character  | R6.1.4  | Check if the buying action fails when the ticket name has a space as the first character  | 
| Space in the ticket name is only allowed if it is not the first or last character  | R6.1.5  | Check if the buying action fails when the ticket name has a space as the last character  | 
| The name of the ticket is no longer than 60 characters  | R6.2.1  | Check if the buying action is successful if the ticket name is 60 characters long |   
| The name of the ticket is no longer than 60 characters  | R6.2.2  | Check if the buying action is successful if the ticket name is more than 60 characters long  |
| The quantity of the tickets has to be more than 0, and less than or equal to 100  | R6.3.1  | Check if buying action succeeds if ticket quantity is 3, which is greater than 0 but less than 101  | 
| The quantity of the tickets has to be more than 0  | R6.3.2  | Check if buying action fails if ticket quantity is 0   |   
| The quantity of the tickets has to be less than or equal to 100  | R6.3.3  | Check if buying action fails if ticket quantity is greater than 100  |
| The ticket name exists in the database  | R6.4.1  | Check if buying action succeeds if ticket name exists in database | 
| The ticket name exists in the database  | R6.4.2  | Check if buying action fails if ticket name does not exist in database  |   
| The ticket quantity is more than the quantity requested to buy  | R6.4.3  | Check if buying action succeeds if ticket quantity is more than requested to buy  |
| The ticket quantity is more than the quantity requested to buy  | R6.4.4  | Check if buying action fails if ticket quantity is less than requested to buy  |
| The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%)  | R6.5.1  | Check if buying action succeeds when the user has more balance than the ticket price * quantity + service fee (35%) + tax (5%) |
| The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%)  | R6.5.2  | Check if buying action fails when the user has less balance than the ticket price * quantity + service fee (35%) + tax (5%)  |
| For any errors, redirect back to / and show an error message  | R6.6.1  | Check if an error occurs, it redirects to `/` and shows an error message  |
| If the user has logged out, invalidate the current session and redirect to the login page.  | R7.1.1  | Check if the user has logged out, they're redirected to the login page and current session is invalidated  |
| After logging out, the user shouldn't be able to access restricted page  | R7.1.2  | Check if after logging out, the user cannot access restricted pages  |
| For any other requests except the ones specified in R1-7, return a 404 error  | R8  | Check if an unspecified request returns a 404 error  |



# How did the team organize the documentation of the test cases?
In summary, a branch, `specifications`, was created to store all the test cases before they were finalized and merged into `master`. This would be done in a team meeting where everyone could review the test cases all together. Specific branches for each group member, corresponding to their assigned specifications, were created that branched off of `specifications`. For example, Nicole was assigned R6, R7, and R8 to complete test cases for. As can be seen on GitHub, Nicole created a branch `R678_specifications`. In these specification specific branches, each member was able to push their own test cases. From there, they could open a pull request to merge with `specifications`, where it would be reviewed and approved by other members individually.

# What was our understanding of how the chosen testing framework to test the front end? When and how will it be running directly on GitHub?

Selenium is the testing framework designated for the front end.
The testing scripts will be run through the use
of GitHub's continuous integration (CI) features.
These tests will be run on each pull request,
such that the team will immediately know 
if regressive changes are introduced.
It should be noted that this testing framework
is used strictly for integration testing,
and does not have direct access to backend data.

# How will we organize different test case code files? 
We will make a folder for each requirement in the `/specs` folder. We will also structure our process the same way we organized the test case documentation.