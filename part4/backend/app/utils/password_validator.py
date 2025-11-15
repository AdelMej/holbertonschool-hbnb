import re


def verify_password(password):
    """
    Validate a password against a set of security rules.

    The function checks the following criteria, in order:
      - Minimum length of 8 characters
      - Contains at least one lowercase letter
      - Contains at least one uppercase letter
      - Contains at least one digit
      - Contains at least one special character (!@#$%^&*(),.?":{}|<>)
      - Does not contain spaces

    Returns:
        tuple:
            (bool)  True if the password is valid, otherwise False.
            (str)   A message describing the validation result.
    """

    # verify length
    if len(password) < 8:
        return False, "Password must be at least 8 characters"

    # verify Lowercase
    if not re.search(r"[a-z]", password):
        return False, "Password must contain a lowercase letter"

    # verify Uppercase
    if not re.search(r"[A-Z]", password):
        return False, "password must contain an uppercase letter"

    # verify digit
    if not re.search(r"\d", password):
        return False, "password must contain a digit"

    # verify special characters
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must include a special character."

    # verify spaces
    if " " in password:
        return False, "Password cannot contain spaces."

    return True, "Password is valid."
