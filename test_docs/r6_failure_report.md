<table><tbody>
<tr>
    <th>Test Name</th>
    <th>Test Purpose</th>
    <th>Output Incorrectness</th>
    <th>Error Source</th>
    <th>Fix</th>
</tr>

<tr>
    <td>test_ticket_exists()</td>
    <td>Verify that ticket must exist in DB to be purchased</td>
    <td>invalid syntax</td>
    <td>Was trying to cast string with (str) but it's str(...)</td>
    <td>Updated syntax</td>
</tr>

<tr>
    <td>geekbase.py</td>
    <td>Defined universal functions and objects</td>
    <td>undefined name "Ticket"</td>
    <td>Not imported into geekbase.py</td>
    <td>Imported into geekbase.py</td>
</tr>

<tr>
    <td>test_invalid_ticketname()</td>
    <td>Verify ticket name is correctly formatted</td>
    <td>R6Test has no function 'assert_url()'</td>
    <td>Wrong syntax</td>
    <td>changed to .get_current_url() and compared</td>
</tr>

<tr>
    <td>test_ticket_quant()</td>
    <td>Verify that ticket quantity must be >0 and <=100</td>
    <td>Cannot concatenate int to str</td>
    <td>Wrong syntax</td>
    <td>Converted string to int, then back to string</td>
</tr>

<tr>
    <td>test_invalid_balance()</td>
    <td>Verify that user's balance is high enough to buy purchase + tax</td>
    <td>Flash not found for 'Account balance is too low'</td>
    <td>Was logging in with TEST_USER, not BAD_USER</td>
    <td>Mocked logging in with correct user</td>
</tr>

</tbody></table>