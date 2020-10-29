# Design Document

## Structure

For the most part, the structure of this software
will match the template.
However,
logic that can be easily separated,
such as login / register validation,
should be refractored into other files.
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

TODO Josh describe the difference in responsibilities between frontend and backend.

## Function Descriptions

| Function Name | Description |
| -- | -- |
| is_valid_password() | Returns boolean indicating whether password is valid, according to R1 and R2 |
| valid_rfc_local_part()| Returns boolean indicating whether local portion of email address is valid, according to RFC 5322 | 
| valid_rfc_domain() | Returns boolean indicating whether domain portion of email address is valid, according to RFC 5322 |
| is_valid_email() | Returns boolean indicating if email address is valid according to RFC 5322 - uses 2 helper functions |
| is_valid_username() | Returns boolean indicating whether username is valid according to R1 and R2 |
| register_get() | Redirects user to home page if logged in, otherwise redirects them to register |
| TODO: Josh finish the table please :) | |

## Code Style

To establish a consistent and clear coding style,
the team has decided to follow 
[PEP-8](https://www.python.org/dev/peps/pep-0008/)
conventions.
To guarantee that the team adheres to these guidelines,
the PyLint tool will be used.
A custom linter configuration will also be created from
the default template,
such that style rules can be adjusted to
the team's preference and application.

## Test Plan

Test cases of different levels,
such as frontend, backend, and integration tests
will be organized into separate folders.
Using this method,
different levels of tests can be run in isolation.
This will be especially useful for team members
who are working on frontend and backend tests,
and don't want the integration tests 
slowing down their development.
Given that each level of testing is independent,
there are minimal restrictions on the testing order.
However, frontend and backend testing should be
attempted before integration testing,
as these will find bugs more explicitly.
Team members will be assigned as in charge of test cases
by endpoint / function.
If the team is unclear on who is in charge of
a particular test case,
then commands such as `git blame` can be used to determine
who was working on a module.

In terms of environments and tooling,
the provided tools has been determined to be sufficient.
That is, PyTest will be used for unit tests,
and Selenium will be applied for integration testing.
By choosing this standard workflow,
reproducing test results in a cloud environment
should be seamless.
One thign that the team will have to pay attention to
is explicitly adding dependencies to `requirements.txt`,
such that third party libraries are also installed on
the cloud environment.
To minimize budget costs,
CI will only be run on pull requests.
As such, most of the testing will occur locally
on the machines of the team members.
By the time a pull request is made,
it should ideally already be passing tests,
though CI will confirm this.