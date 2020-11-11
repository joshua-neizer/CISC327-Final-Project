<table><tbody>
<tr>
    <th>Test Name</th>
    <th>Test Purpose</th>
    <th>Output Incorrectness</th>
    <th>Error Source</th>
    <th>Fix</th>
</tr>

<tr>
    <td>test_login_redirects()</th>
    <td>Verify that '/' redirects to login</th>
    <td>#login_input doesn't exist</th>
    <td>Login input element has different ID</th>
    <td>Update spec with correct ID</th>
</tr>

<tr>
    <td>test_hi_user()</th>
    <td>Verify that 'Hi user' message displays</th>
    <td>'Welcome user' message is displayed</th>
    <td>Harcoded string is incorrect</th>
    <td>Adjusted string in HTML template</th>
</tr>

<tr>
    <td>test_logout_link()</th>
    <td>Verify that logout link is visible</th>
    <td>Logout link cannot be found</th>
    <td>Logout link does not have ID</th>
    <td>Added ID to logout link</th>
</tr>

</tbody></table>