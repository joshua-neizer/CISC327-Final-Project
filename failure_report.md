<table><tbody>
<tr>
    <th>Test Name</th>
    <th>Test Purpose</th>
    <th>Output Incorrectness</th>
    <th>Error Source</th>
    <th>Fix</th>
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

</tbody></table>