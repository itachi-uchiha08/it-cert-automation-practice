#!/usr/bin/env python3

#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False, "Username must not be less than {} characters.".format(minlen)
    
    # Usernames can only use letters, numbers, dots, and underscores
    if not re.match('^[a-zA-Z0-9._]*$', username):
        return False, "Usernames can only use letters, numbers, dots, and underscores."
    
    # Usernames can't begin with a number
    if username[0].isdigit():
        return False, "Usernames can't begin with a number."
    
    return True, "Username is valid."

print(validate_user("blue.kale", 3))  # (True, 'Username is valid.')
print(validate_user(".blue.kale", 3))  # (False, 'Usernames can only use letters, numbers, dots, and underscores.')
print(validate_user("red_quinoa", 4))  # (True, 'Username is valid.')
print(validate_user("_red_quinoa", 4))  # (False, "Usernames can't begin with a number.")

