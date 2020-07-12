import mysql.connector

mydb = mysql.connector.connect(
  user='dbmasteruser', 
  password='#(KT.%KXF~?oa0((3C]B+c:D$_u|~%7%',
  host='ls-ab4099840472652cffcf8a93ff831350de0b9549.cxjoxjn3ihvz.us-west-2.rds.amazonaws.com',
  database='league',
  port='3306')

mycursor = mydb.cursor()

sql = "INSERT INTO champions (game_id, champion_id, team_id, damage_dealt, assists, kills, total_healing, total_minions_killed, win, first_blood_kill, first_dragon, first_tower_kill, vision_score) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"
val = [
  (4247263043, 7, 100, 71369, 3, 3, 4006, 133, False, True, False, False, 14)
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")