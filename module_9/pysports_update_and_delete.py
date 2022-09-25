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
# CLOSE THE DATABASE
try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor()
    cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES('Smeagol', 'Shire Folk', 1)")

    db.commit()
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()
# Insert query   
    print(" -- DISPLAYING PLAYERS AFTER INSERT --")
    for p in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}\n".format(p[0], p[1], p[2], p[3]))
    print("\n")
# Update query
    cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
    
    print(" -- DISPLAYING PLAYERS AFTER UPDATE --")
    for p in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}\n".format(p[0], p[1], p[2], p[3]))
    print("\n")
# Delete query
    cursor.execute("DELETE FROM player WHERE first_name = 'Smeagol'")
    
    print(" -- DISPLAYING PLAYERS AFTER DELETE --")
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
