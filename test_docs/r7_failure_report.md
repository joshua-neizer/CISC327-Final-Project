|Test Name| Test Purpose | Output Incorrectness|Error Source |Fix|
|---|---|---|--|---|
|test_logout_redirect| If the user is logged out, invalidate the current session and redirect user to the `/login`| AssertionError: assert  web element == 'Please Login' | Asserting equality between an element and a string  | Get text from element, rather than compare element|