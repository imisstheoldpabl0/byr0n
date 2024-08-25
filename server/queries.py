CREATE_USERS_TABLE = (
    """CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR,
        email VARCHAR,
        password VARCHAR,
        login_status BOOLEAN DEFAULT FALSE
    );"""
)

GET_USERS_IN_DB = (
    """SELECT * FROM users"""
)

INSERT_USER_RETURN_ID = (
    """INSERT INTO users (username, email, password, login_status) 
       VALUES (%s, %s, %s, %s) RETURNING id;"""
)

DELETE_ALL_USERS_IN_DB = (
    """DROP TABLE users"""
)

CHECK_USER_IN_DB = (
    """SELECT id FROM users WHERE username = %s OR email = %s"""
)

CHECK_LOGIN_CREDENTIALS = (
    """SELECT id FROM users WHERE username = %s AND password = %s RETURNING id"""
)

UPDATE_LOGIN_STATUS = (
    """UPDATE users SET login_status = TRUE WHERE username = %s AND password = %s RETURNING id"""
)