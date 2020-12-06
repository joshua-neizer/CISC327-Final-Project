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
    <td>geekbase.py</td>
    <td>Defined universal functions and objects</td>
    <td>undefined name "Ticket"</td>
    <td>Not imported into geekbase.py</td>
    <td>Imported into geekbase.py</td>
<tr>

</tr>
</tbody></table>