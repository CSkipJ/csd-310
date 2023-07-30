# pysports_join_queries.py
# written by Charles Jones
# https://github.com/CSkipJ/csd-310
# 30 July 2023
# This script is used to test the inner join queries in the pysports db

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

    # create an INNER JOIN query to connect the player 
    # and team tables by team_id and display the results.
    query = 'SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id'

    cursor = db.cursor()
    cursor.execute(query)
    players = cursor.fetchall()

    print("-- DISPLAYING TEAM RECORDS -- \n")

    for player in players:
        print(f'PLayer ID: {player[0]} \n'
              f'First Name: {player[1]} \n'
              f'Last Name: {player[2]} \n' 
              f'Team: {player[3]} \n' )
        
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
