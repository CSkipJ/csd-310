# pysports_update_and_delete.py
# written by Charles Jones
# https://github.com/CSkipJ/csd-310
# 30 July 2023
# This script is used to test the update and delete functions in MySQL

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


    cursor = db.cursor()

    #insert new record
    cursor.execute('INSERT INTO player (first_name, last_name, team_id) VALUES("Smeagol", "Shire Folk", 1)')
    cursor.execute('SELECT player.player_id, player.first_name, player.last_name, team.team_name ' 
                   'FROM player INNER JOIN team ON player.team_id = team.team_id')

    # print all players after insert
    players = cursor.fetchall()

    print("-- DISPLAYING PLAYERS AFTER INSERT -- \n")

    for player in players:
        print(f'PLayer ID: {player[0]} \n'
              f'First Name: {player[1]} \n'
              f'Last Name: {player[2]} \n' 
              f'Team: {player[3]} \n' )
        
    # update team for new inserted record
    cursor.execute('UPDATE PLAYER '
                   'SET team_id = 2, '
                   'first_name = "Gollum", '
                   'last_name = "Ring Stealer" '
                   'WHERE first_name = "Smeagol"' )
    cursor.execute('SELECT player.player_id, player.first_name, player.last_name, team.team_name ' 
                   'FROM player INNER JOIN team ON player.team_id = team.team_id')
        
    print("-- DISPLAYING PLAYERS AFTER UPDATE -- \n")

    # print all players after update
    players = cursor.fetchall()

    for player in players:
        print(f'PLayer ID: {player[0]} \n'
              f'First Name: {player[1]} \n'
              f'Last Name: {player[2]} \n' 
              f'Team: {player[3]} \n' )

    # delete new inserted player record
    print("-- DISPLAYING PLAYERS AFTER DELETE-- \n")
    cursor.execute('DELETE FROM player WHERE first_name = "Gollum"')
    cursor.execute('SELECT player.player_id, player.first_name, player.last_name, team.team_name ' 
                   'FROM player INNER JOIN team ON player.team_id = team.team_id')
    
        # print all players after delete
    players = cursor.fetchall()

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
