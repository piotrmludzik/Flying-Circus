# -------------------------------------------------------------------------------------------------
#                                          Flying circus
#                                  user login and logout handlers
#                                              v 1.0
# -------------------------------------------------------------------------------------------------

import const as c


users = {
    'john@doe.com': '$2b$12$/TYFvXOy9wDQUOn5SKgTzedwiqB6cm.UIfPewBnz0kUQeK9Eu4mSC',
    'wally-e@pixar.com': 'qwerty'
}


# ---------------------------------- login and logout functions -----------------------------------

def valid_login(username: str, password: str) -> bool:
    return True if username in users and users[username] == password else False
