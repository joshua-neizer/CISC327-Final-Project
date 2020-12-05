# Whitebox Test for buy_ticket()
## Methodology

In this whitebox test case, decision coverage will be applied. This will trigger every decision in both ways. The completion criterion will be a test case for each side of each decision.

## Mocking Data
Unless otherwise specified, the user object below will serve as the input for `user`. For all tests, only one ticket will be mocked in the database, shown below. Each test case may only differ in elements of the `user`, which will be specified in the input.

```
test_user = User(
	email = 'test_frontend@test.com',
	name = 'test_frontend',
	password = generate_password_hash('test_frontend'),
	balance = 500
)
```
```
test_ticket = Ticket(
    name = `justinbieber`
    seller_id = 1
    price = 100
    quantity = 1
    expires = 20211031
)
```
## Test Summary
<table><tbody>

<tr>
<th>Decision</th>
<th>Outcome</th>
<th>user</th>
<th>name</th>
<th>buy_quantity</th>
<th>Test Case</th>
</tr>

<tr>
<td> if ticket is None:</td>
<td>True</td>
<td>test_user</td>
<td>'wontexist'</td>
<td>1</td>
<td></td>
</tr>

<tr>
<td> if ticket is None:</td>
<td>False</td>
<td>test_user</td>
<td>'justinbieber'</td>
<td>1</td>
<td></td>
</tr>

<tr>
<td> if ticket.quantity < buy_quantity:</td>
<td>True</td>
<td>test_user</td>
<td>'justinbieber'</td>
<td>2</td>
<td></td>
</tr>

<tr>
<td> if ticket.quantity < buy_quantity:</td>
<td>False</td>
<td>test_user</td>
<td>'justinbieber'</td>
<td>1</td>
<td></td>
</tr>

<tr>
<td> if user.balance < ticket_cost:</td>
<td>True</td>
<td>test_user.balance = 10</td>
<td>'justinbieber'</td>
<td>1</td>
<td></td>
</tr>

<tr>
<td> if user.balance < ticket_cost:</td>
<td>False</td>
<td>test_user</td>
<td>'justinbieber'</td>
<td>1</td>
<td></td>
</tr>

</table></tbody>

## T1
