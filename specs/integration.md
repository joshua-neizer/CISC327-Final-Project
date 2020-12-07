# Test Case: Creating Posting

## Step 1: Register testuser1
* Navigate to `/`
* Click `#register-button`
* Input `testuser1@gmail.com` into `#email`
* Input `testuser1` into  `#name`
* Input `Password99!` into `#password`
* Input `Password99!` into `#password2`
* Click `#btn-submit`

## Step 2: Login testuser1
* Input `testuser1@gmail.com` into `#email`
* Input `Password99!` into `#password`
* Click `#btn-submit`

## Step 3: Sell a ticket
* Input `testticket1` into `#sell-ticket-name`
* Input `21` into `#sell-ticket-quantity`
* Input `35` into `#sell-ticket-price`
* Input `20220101` into `#ticket-expiration-date`
* Click `#sell-submit`
* Assert that there is one result for selector `#tickets .ticket`
* Assert that `#tickets .ticket .name` has value `testticket1`
* Assert that `#tickets .ticket .quantity` has value `21`
* Assert that `#tickets .ticket .price` has value `35`
* Assert that `#tickets .ticket .owner` has value `testuser1@gmail.com`
* Assert that `#tickets .ticket .expires` has value `20220101`

## Step 4: Update a ticket
* Input `testticket1` into `#update-prev-ticket-name`
* Input `36` into `#update-ticket-price`
* Click `#update-submit`
* Assert that there is one result for selector `#tickets .ticket`
* Assert that `#tickets .ticket .name` has value `testticket1`
* Assert that `#tickets .ticket .quantity` has value `21`
* Assert that `#tickets .ticket .price` has value `36`
* Assert that `#tickets .ticket .owner` has value `testuser1@gmail.com`
* Assert that `#tickets .ticket .expires` has value `20220101`

# Test Case: Purchasing Ticket

## Step 0: Create ticket and seller
Create a test user and ticket by following the test case
for creating a posting.

## Step 1: Register testuser2
* Navigate to `/`
* Click `#register-button`
* Input `testuser2@gmail.com` into `#email`
* Input `testuser2` into  `#name`
* Input `Password99!` into `#password`
* Input `Password99!` into `#password2`
* Click `#btn-submit`

## Step 2: Login testuser2
* Input `testuser2@gmail.com` into `#email`
* Input `Password99!` into `#password`
* Click `#btn-submit`

## Step 3: Check User Balance
* Read balance from `#user-balance`

## Step 4: Buy ticket
* Input `testticket1` into `#buy-ticket-name`
* Input `1` into `#buy-ticket-quantity`
* Click `#buy-submit`

## Step 5: Assert that sold ticket quantity decreased
* Assert that there is one result for selector `#tickets .ticket`
* Assert that `#tickets .ticket .name` has value `testticket1`
* Assert that `#tickets .ticket .quantity` has value `21`
* Assert that `#tickets .ticket .price` has value `35`
* Assert that `#tickets .ticket .owner` has value `testuser1@gmail.com`
* Assert that `#tickets .ticket .expires` has value `20220101`

## Step 6: Assert that user balance decreased
* Read balance from `#user-balance`
* Assert that `new_balance==old_balance-21`