import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
# include the try except finally error catcher
# remember to close database (db.close())
try:
    db = mysql.connector.connect(**config)
    
    cursor = db.cursor()
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    
    teams = cursor.fetchall()
# team query
    print("\n-- DISPLAYING TEAM RECORDS --")
    for team in teams: 
        print("Team ID: {}\nTeam Name: {}\nMascot: {}\n".format(team[0], team[1], team[2]))

    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    players = cursor.fetchall()
# player query
    print ("\n-- DISPLAYING PLAYER RECORDS --")

    for p in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}\n".format(p[0], p[1], p[2], p[3]))

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
