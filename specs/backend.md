# Methodology

Inputs have been partitioned to cover each possible case
that can be distinctly differentiated.
Given that the inputs to this function are 
strings with nontrivial lengths,
exhaustive testing is not feasible.

# Partitions

## Partition B1

Input: Email does not exist

Output: None

## Test case B1.1

- Mock no users
- assert `login_user(email='missing@email.com',password='doesnotmatter')` is None

## Partition B2

Input: Email does exist, password is incorrect

Output: None

## Test case B2.1

- Mock user with `email='missing@email.com', password='CorrectPassword99!'`
- assert `login_user(email='missing@email.com',password='WrongPassword99!')` is None

## Partition B3

Input: Email does exist, password is correct

Output: None

## Test case B3.1

- Mock user with `email='missing@email.com', password='CorrectPassword99!', balance=140, name=myuser`
- get user via `login_user(email='missing@email.com',password='CorrectPassword99!')`
- assert that user email is 'missing@email.com'
- assert that user balance is 140
- assert that user name is myuser

## Partition B4

Input: Email is incorrect, password is correct

Output: None

Note that given any sane implementation,
this test case should be unecessary as looking up by password is obviously bad.
However, this is black-box testing so we don't assume sanity.

## Test case B3.1

- Mock user with `email='correct-email@gmail.com', password='CorrectPassword99!', balance=140, name=myuser`
- get user via `login_user(email='wrong-email@gmail.com',password='CorrectPassword99!')`
- assert that user is None