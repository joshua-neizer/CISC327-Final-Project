|Test Name| Test Purpose | Output Incorrectness|Error Source |Fix|
|---|---|---|--|---|
|test_logout_redirect| If the user is logged out, invalidate the current session and redirect user to the `/login`| Element {#email} was not present after 10 seconds| Accidentally doubled the log in process, so the element di not exist | Only logged in and input information once rather than twice|