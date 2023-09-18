Test Engineer’s homework questions

Task:
Bonus task to check some coding skills:
Assume you already have client ID and secret key, which are needed for getting a
new token (the same API as in the last question.)
Please write a mechanism to return a token to the caller. If the token has not yet
been generated - request a new one and return it, if the token has already been
requested - return it again, if it’s expired - use refresh token endpoint to get a new
access token and return that one. All subsequent requests for the access token
should now return the new token until it’s expired.

Please, execute code in token_oper.py file.

1. It will generate file (if it doesn`t exist) user_data.json to store users data.
2. It will search by secret_id for existing token in file user_data.json
3. If token found, it will check experation time.
4. If token expired, token will be refreshed returned and saved to user_data.json file.
5. If token found and not expired it will be returned.
6. IF token not found, token will be generated and saved to user_data.json file.