# Test Cases Summary

|  Specification | Test Case ID   |  Purpose  |
|---|---|---|
|   | R1.1|   |  
|   |  R1.2|  |   
|   | R1.3  |   |   
|   |  R1.4 |   |  
|   | R1.5   |   |   
|   | R1.6  |   | 
|   | R1.7   |   |  
|   | R1.8  |   |   
|   | R1.9  |   | 
|   | R1.10  |   |  
|   | R1.11  |   |
|   | R2.1  |   | 
|   | R2.2  |   |  
|   | R2.3  |   |   
|   | R2.4  |   | 
|   | R2.5  |   |  
|   | R2.6  |   |   
|   | R2.7  |   | 
|   | R2.8  |   |  
|   | R2.9  |   |   
|   | R2.10  |   | 
|   | R2.11  |   |  
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
|   | R5.6.1  |   |
|   | R5.6.2  |   | 
|   | R5.7.1  |   |   
|   | R5.7.2  |   |
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