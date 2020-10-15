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
|   | R4.1.1  | Buy ticket name is alphanumeric - positive  |   
|   | R4.1.2  | Buy ticket name is alphanumeric - negative - invalid character |
|   | R4.1.3  | Buy ticket name is alphanumeric - negative - space before  |  
|   | R4.1.4  | Buy ticket name is alphanumeric - negative - space after |   
|   | R4.2.1  | Buy ticket name length is acceptable - positive | 
|   | R4.2.2  | Buy ticket name length is acceptable - negative - ticket name too long |  
|   | R4.3.1  | Buy ticket quantity is acceptable - positive  |   
|   | R4.3.2  | Buy ticket quantity is acceptable - negative - quantity too small  | 
|   | R4.3.3  | Buy ticket quantity is acceptable - negative - ticket quantity too great |  
|   | R4.4.1  | Buy ticket price is acceptable - positive  |   
|   | R4.4.2  | Buy ticket price is acceptable - negative - ticket price too small  | 
|   | R4.4.3  | Buy ticket price is acceptable - negative - ticket quantity too great  |  
|   | R4.5.1  |  |   
|   | R4.5.2  |   | 
|   | R4.5.3  |   |  
|   | R4.6.1  |   |   
|   | R4.6.2  |   | 
|   | R4.7  |   |  
|   | R5.1.1  |   |   
|   | R5.1.2  |   | 
|   | R5.1.3  |   |  
|   | R5.1.4  |   |   
|   | R5.2.1  |   | 
|   | R5.2.2  |   |  
|   | R5.3.1  |   |   
|   | R5.3.2  |   | 
|   | R5.3.3  |   |  
|   | R5.4.1  |   |   
|   | R5.4.2  |   | 
|   | R5.4.3  |   |   
|   | R5.5.1  |   | 
|   | R5.5.2  |   | 
|   | R5.5.3  |   |   
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
| The quantity of the tickets has to be more than 0, and less than or equal to 100  | R6.3.1  |   | 
| The quantity of the tickets has to be more than 0  | R6.3.2  |   |   
| The quantity of the tickets has to be less than or equal to 100  | R6.3.3  |   |
| The ticket name exists in the database  | R6.4.1  |   | 
| The ticket name exists in the database  | R6.4.2  |   |   
| The ticket quantity is more than the quantity requested to buy  | R6.4.3  |   |
| he ticket quantity is more than the quantity requested to buy  | R6.4.4  |   |
| The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%)  | R6.5.1  |   |
| The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%)  | R6.5.2  |   |
| For any errors, redirect back to / and show an error message  | R6.6.1  |   |
| If the user has logged out, invalidate the current session and redirect to the login page.  | R7.1.1  |   |
| After logging out, the user shouldn't be able to access restricted page  | R7.1.1  |   |
| For any other requests except the ones specified in R1-7, return a 404 error  | R8  |   |



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