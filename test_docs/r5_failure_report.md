<table>
    <tbody>
        <tr>
            <th>Test Name</th>
            <th>Test Purpose</th>
            <th>Output Incorrectness</th>
            <th>Error Source</th>
            <th>Fix</th>
        </tr>
        <tr>
            <td>test_r5_5_neg</td>
            <td>Date must be given in the format YYYYMMDD</td>
            <td>Didn't give any error message for invalid date formats</td>
            <td>Data was parsed at the start of the update_post() function in frontend.py; if the format was incorrect, parse_date() returned nothing. Since it returned nothing, the function thought that no new date was inputted and didn't update the database. However, it returned a misleading message that the ticket was successful updated.</td>
            <td>Implemented parse_date() into is_valid_date() in the backend to check both at the same time.</td>
        </tr>
        <tr>
            <td>test_r5_*_neg</td>
            <td>Tests incorrect formatting for ticket name, quantity, price and expiration date</td>
            <td>Didn't match flash messages</td>
            <td>There were typos in the flashed formatting error messages in frontend.py. "<i>Incorrect</i>" was spelt
                incorrectly.</td>
            <td>Corrected the typos in frontend.py</td>
        </tr>
    </tbody>
</table>