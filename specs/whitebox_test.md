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
    name = 'justinbieber'
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
<td>T2</td>
</tr>

<tr>
<td> if ticket is None:</td>
<td>False</td>
<td>test_user</td>
<td>'justinbieber'</td>
<td>1</td>
<td>T1</td>
</tr>

<tr>
<td> if ticket.quantity < buy_quantity:</td>
<td>True</td>
<td>test_user</td>
<td>'justinbieber'</td>
<td>2</td>
<td>T3</td>
</tr>

<tr>
<td> if ticket.quantity < buy_quantity:</td>
<td>False</td>
<td>test_user</td>
<td>'justinbieber'</td>
<td>1</td>
<td>T1</td>
</tr>

<tr>
<td> if user.balance < ticket_cost:</td>
<td>True</td>
<td>test_user.balance = 10</td>
<td>'justinbieber'</td>
<td>1</td>
<td>T4</td>
</tr>

<tr>
<td> if user.balance < ticket_cost:</td>
<td>False</td>
<td>test_user</td>
<td>'justinbieber'</td>
<td>1</td>
<td>T1</td>
</tr>

</table></tbody>

## T1
Test Data: 

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
    name = 'justinbieber'
    seller_id = 1
    price = 100
    quantity = 1
    expires = 20211031
)
```
Mocking:
* Mock backend.sell_ticket(user, 'justinbieber', 1, 100, 20211031)
* Mock backend.get_user() to return a test_user instance

Actions:
* Open /login
* Enter test_user's email and password into elements `#email` and `#password` respectively
* Click element `input[type="submit"]`
* Enter `justinbieber` into element `#buy_name`
* Enter `1` into element `#buy_quantity`
* Click element `#buy_submit`
* Assert that `#buy_message.text` equal `Ticket bought successfully`

## T2
Test Data: 

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
    name = 'justinbieber'
    seller_id = 1
    price = 100
    quantity = 1
    expires = 20211031
)
```
Mocking:
* Mock backend.sell_ticket(user, 'justinbieber', 1, 100, 20211031)
* Mock backend.get_user() to return a test_user instance

Actions:
* Open /login
* Enter test_user's email and password into elements `#email` and `#password` respectively
* Click element `input[type="submit"]`
* Enter `wontexist` into element `#buy_name`
* Enter `1` into element `#buy_quantity`
* Click element `#buy_submit`
* Assert that `#buy_message.text` equal `No such ticket exists`

## T3
Test Data: 

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
    name = 'justinbieber'
    seller_id = 1
    price = 100
    quantity = 1
    expires = 20211031
)
```
Mocking:
* Mock backend.sell_ticket(user, 'justinbieber', 1, 100, 20211031)
* Mock backend.get_user() to return a test_user instance

Actions:
* Open /login
* Enter test_user's email and password into elements `#email` and `#password` respectively
* Click element `input[type="submit"]`
* Enter `justinbieber` into element `#buy_name`
* Enter `2` into element `#buy_quantity`
* Click element `#buy_submit`
* Assert that `#buy_message.text` equal `Not enough tickets available`

## T4
Test Data: 

```
test_user = User(
	email = 'test_frontend@test.com',
	name = 'test_frontend',
	password = generate_password_hash('test_frontend'),
	balance = 10
)
```
```
test_ticket = Ticket(
    name = 'justinbieber'
    seller_id = 1
    price = 100
    quantity = 1
    expires = 20211031
)
```
Mocking:
* Mock backend.sell_ticket(user, 'justinbieber', 1, 100, 20211031)
* Mock backend.get_user() to return a test_user instance

Actions:
* Open /login
* Enter test_user's email and password into elements `#email` and `#password` respectively
* Click element `input[type="submit"]`
* Enter `wontexist` into element `#buy_name`
* Enter `1` into element `#buy_quantity`
* Click element `#buy_submit`
* Assert that `#buy_message.text` equal `Account balance is too low`