# Description of Changes
The template files provided had to be altered to conduct front-end unit testing. The following table summarizes the changes made:

<table>
<tbody>
<tr>
    <th>File</th>
    <th>Changes Made</th>
    <th>Purpose</th>
</tr>

<tr>
    <td>base.html</td>
    <td>Added a html flash template that allows messages from different pages to flash said message to the current page. All pages will now automatically inherit this template.</td>
    <td>Allows templates to flash error messages for invalid formatting, wrong password and user combinations, and other requirements in a simple and clean manner.</td>
</tr>

<tr>
    <td>index.html</td>
    <td>Added in HTML code for tickets, Selling tickets, Updating tickets and buy tickets</td>
    <td>Provides a template for all tickets to be seen, purchased, updated and sold by the user on the main page.</td>
</tr>

<tr>
    <td>login.html</td>
    <td>Changed line 5 to have an id of 'login_message' and have a static message of "Please Login".  </td>
    <td>Since we changed all messaging between pages to use the flash function from the flask library, we decided to leave the login message static. Therefore, the error messages are flashed to the html elements that are inherited from base.html, rather than to the 'login_message' id. Also, the id name was changed to differentiate it from the other message ids that typically display error messages.</td>
</tr>

<tr>
    <td>register.html</td>
    <td>Removed required attributes from the input fields</td>
    <td>The required attributes conflicted with the R2 requirements testing. In particular, it made it difficult to check if our frontend.py file would error check an empty string inputs as the required attribute would not let an empty field be submitted. Therefore, they were removed to validate our error checking.</td>
</tr>
</tbody>
</table>
