<table><tbody>
<tr>
    <th>Test Name</th>
    <th>Test Purpose</th>
    <th>Output Incorrectness</th>
    <th>Error Source</th>
    <th>Fix</th>
</tr>

<tr>
    <td>test_r2_2</td>
    <td>Validates that registration page will show if user isn't logged in</td>
    <td>Could not find #register</td>
    <td>register.html</td>
    <td>Added #register id to form in register.html</td>
</tr>

<tr>
    <td>test_r2_4</td>
    <td>Validates registration can be submitted as a POST request</td>
    <td>Login page did not contain success message when registration fulfilled POST request</td>
    <td>register_post() in frontend.py on line 70</td>
    <td>Used the flash method from the flask library to pass a message to login.html then redirected, rather than rendering login.html with the message and not redirecting</td>
</tr>

<tr>
    <td>test_r2_5_neg_email</td>
    <td>Validates that all emails submitted have the correct format</td>
    <td>Test failed because html did not allow empty field to be submitted so no error message was passed to the page from frontend.py</td>
    <td>register.html</td>
    <td>Removed required attribute in input fields</td>
</tr>

<tr>
    <td>test_r2_5_neg_password2</td>
    <td>Validates that all password2s submitted have the correct format</td>
    <td>No test associated</td>
    <td>register_post() in frontend.py on lines 54 to 56</td>
    <td>Used the same format for the password format check, but passed password2 as the argument</td>
</tr>

<tr>
    <td>test_r2_9</td>
    <td>Ensures that for any formatting error, the user is redirected to the login page with the error message</td>
    <td>The user was not redirected to the login page</td>
    <td>register_post() in frontend.py on line 46</td>
    <td>Changed the redirect page to be the login page along with flashing the message to /login</td>
</tr>

<tr>
    <td>test_r2_10</td>
    <td>Checks to see if the user already exists</td>
    <td>Was treated as a formatting error</td>
    <td>register_post in frontend.py on line 66</td>
    <td>Adjusted the error handling so that it is independent from the formatting errors by rendering register.html with the message instead of redirecting to /login</td>
</tr>

<tr>
    <td>test_login_redirects()</td>
    <td>Verify that '/' redirects to login</td>
    <td>#login_input doesn't exist</td>
    <td>Login input element has different ID</td>
    <td>Update spec with correct ID</td>
</tr>

<tr>
    <td>test_hi_user()</td>
    <td>Verify that 'Hi user' message displays</td>
    <td>'Welcome user' message is displayed</td>
    <td>Harcoded string is incorrect</td>
    <td>Adjusted string in HTML template</td>
</tr>

<tr>
    <td>test_logout_link()</td>
    <td>Verify that logout link is visible</td>
    <td>Logout link cannot be found</td>
    <td>Logout link does not have ID</td>
    <td>Added ID to logout link</td>
</tr>

<tr>
    <td>test_tickets_listed()</td>
    <td>Verify that ticket information is listed</td>
    <td>Ticket information cannot be found</td>
    <td>Selectors are incorrect / Ticket information missing</td>
    <td>Redesigned test selectors and added ticket information to HTML template</td>
</tr>

<tr>
    <td>test_sell_form()</td>
    <td>Verify that sell form exists</td>
    <td>Sell form not found</td>
    <td>Selectors are incorrect</td>
    <td>Adjusted DOM IDs in test case</td>
</tr>

<tr>
    <td>test_sell_posts()</td>
    <td>Verify that sell form POSTs correctly</td>
    <td>Cannot verify POST easily with selenium</td>
    <td>Test case made incorrect assumptions about selenium usage</td>
    <td>Redesign test case to add message to page</td>
</tr>

<tr>
    <td>test_logout_redirect()</td>
    <td>If the user is logged out, invalidate the current session and redirect user to the /login page</td>
    <td>AssertionError: assert  web element == 'Please Login'</td>
    <td>Asserting equality between an element and a string</td>
    <td>Get text from element, rather than compare element</td>
</tr>

<tr>
    <td>test_logout_restricted()</td>
    <td>After logging out, the user shouldn't be able to access restricted page</td>
    <td>No Such Element Exception: unable to locate element id: #error404</td>
    <td>Test design was wrong, doesn't reroute to 404error. Simply redirects to /login</td>
    <td>Assert URL was /login after opening base_url</td>
</tr>

</tbody></table>