<table><tbody>
<tr>
    <th>Test Name</th>
    <th>Test Purpose</th>
    <th>Output Incorrectness</th>
    <th>Error Source</th>
    <th>Fix</th>
</tr>

<tr>
    <td>test_login_submit()</td> 
    <td>Verify that login form can be submitted as POST request to URL /login</td>
    <td>get_current_url() takes 1 positional argument but 2 were given</td>
    <td>Used the function incorrectly</td>
    <td>Removed extra argument</td>
</tr>

<tr>
    <td>test_form_data_missing()</td>
    <td>Verify that email and password both cannot be empty</td>
    <td>Error message sent to wrong message ID</td>
    <td>Assert error message is matching</td>
    <td>Updated test case with correct ID</td>
</tr>

<tr>
    <td>test_login_submit()</td>
    <td>Verify that login form can be submitted as POST request to URL /login</td>
    <td>Incorrect URL</td>
    <td>Asserted incorrect URL</td>
    <td>Adjusted assertion to correct URL</td>>
</tr>

<tr>
    <td>test_email_rfc_specs()</td>
    <td>Verify that valid emails can be used to login</td>
    <td>Incorrect URL</td>
    <td>Asserted base_url instead of base_url+'/'</td>
    <td>Adjusted assertion to correct URL</td>>
</tr>

<tr>
    <td>test_invalid_email_rfc_specs()</td>
    <td>Verify that emails that do not follow RFC5322 cannot be used to login</td>
    <td>Element #email_error_message not present</td>
    <td>Error messages are sent to #login_message</td>
    <td>Adjusted assertion to correct message and ID</td>>
</tr>



</tbody></table>