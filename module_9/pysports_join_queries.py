import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
# use try except, finally from module 8
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

# Inner Join
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()
    # print statement for output
    print("\n   -- DISPLAYING PLAYER RECORDS --")
    # put in print for output with formatting
    for p in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}\n".format(p[0], p[1], p[2], p[3]))
    print("\n")
    input("Press 'Enter' key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
