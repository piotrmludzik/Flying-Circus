# -------------------------------------------------------------------------------------------------
#                                          Flying circus
#                                  user login and logout handlers
#                                              v 1.0
# -------------------------------------------------------------------------------------------------

from flask import session
import bcrypt
import const as c


users = {
    'john@doe.com': '$2b$12$/TYFvXOy9wDQUOn5SKgTzedwiqB6cm.UIfPewBnz0kUQeK9Eu4mSC',
    'wally-e@pixar.com': '$2b$12$udIf8lX4P5EkuYwLSTiZxuAV527ZOSHJvDIQ1wzlvuHO2sw41mzia'
}


# ---------------------------------- login and logout functions -----------------------------------

def is_logged() -> bool:
    """ Checks if user is logged. """
    return True if c.SV_USERNAME in session else False


def valid_login(username: str, password: str) -> bool:
    """ Validates user and password: whether they exist in the database. """
    return True if (username in users) and (password_verify(password, users[username])) else False


# ------------------------------ encryption and decryption functions ------------------------------

# def password_hash(plaintext_password) -> str:
#     """ By using bcrypt, the salt is saved into the hash itself. """
#     hashed_bytes = bcrypt.hashpw(plaintext_password.encode('utf-8'), bcrypt.gensalt())
#     return hashed_bytes.decode('utf-8')


def password_verify(plaintext_password, hashed_password) -> bool:
    """ Returns True if plaintext password match with hashed_password, else returns False. """
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plaintext_password.encode('utf-8'), hashed_bytes_password)