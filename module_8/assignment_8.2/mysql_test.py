# mysql_test.py 

import mysql.connector
from mysql.connector import errorcode

# Basic config options for db connection
config = {
    "user": "pysports_user",
    "password": "password123",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# unpack config options in connect or fail out
try:
    db = mysql.connector.connect(**config)
    print(f"\n Database user {config['user']} connected to MySQL on host {config['host']} with database {config['database']}")
    input("Press any key to continue...")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
finally:
    db.close()
