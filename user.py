# -------------------------------------------------------------------------------------------------
#                                          Flying circus
#                                  user login and logout handlers
#                                              v 1.0
# -------------------------------------------------------------------------------------------------

from flask import session
import const as c


users = {
    'john@doe.com': '$2b$12$/TYFvXOy9wDQUOn5SKgTzedwiqB6cm.UIfPewBnz0kUQeK9Eu4mSC',
    'wally-e@pixar.com': 'qwerty'
}


# ---------------------------------- login and logout functions -----------------------------------

def is_logged() -> bool:
    """ Checks if user is logged. """
    return True if c.SV_USERNAME in session else False


def valid_login(username: str, password: str) -> bool:
    """ Validates user and password: whether they exist in the database. """
    return True if username in users and users[username] == password else False
