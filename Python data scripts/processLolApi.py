# importing the requests library 
import requests 
import time
import sys
from csv import DictReader
import mysql.connector

try:
  mydb = mysql.connector.connect(
    user='dbmasteruser', 
    password='#(KT.%KXF~?oa0((3C]B+c:D$_u|~%7%',
    host='ls-ab4099840472652cffcf8a93ff831350de0b9549.cxjoxjn3ihvz.us-west-2.rds.amazonaws.com',
    database='league',
    port='3306')
  mycursor = mydb.cursor()

  #sql query to insert data into db
  sql = "INSERT INTO champions (game_id, champion_id, team_id, damage_dealt, assists, kills, total_healing, total_minions_killed, win, first_blood_kill, first_dragon, first_tower_kill, vision_score, game_duration) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"

  print("Connection to server successful")
except:
  print(sys.exc_info()[0], "occurred.")

#for each gameId in the kaggle csv itterate through them
with open('Challenger_Ranked_Games.csv','r') as file:
  csvDictReader = DictReader(file)

  returned504Times = 0 # number of times there has been a 504 status returned
  startingRow = 20981 # = how many rows to skip. if you want to start on the 5th row then skip 3, which ever row you want to start on enter thnumber minus 2
  i = 0

  # reminder last one added 4224690113
  for row in csvDictReader:

    # skips the number of rows as startingRow. Change starting row to start processing at a specific row
    if i < startingRow:
      i = 1 + i
      continue

    gameId = row['gameId']
    gameDuraton = row['gameDuraton']

    #skips row if duration is less than 15 minutes
    if int(gameDuraton) < 900:
      continue

    apiKey = "RGAPI-32f744bb-303d-4be6-b23b-2bab400fb04c"
    # api-endpoint 
    URL = "https://kr.api.riotgames.com/lol/match/v4/matches/" + gameId + "?api_key=" + apiKey

    # sending get request and saving the response as response object 
    r = requests.get(url = URL) 

    # if the request encounters an error it will check if it is too many requests, if it is, then it will pause for 2 minutes and one second, other errors stop the program
    if r.status_code != 200:
      if r.status_code == 429 or r.status_code == 504:
        returned504Times = returned504Times + 1
        print("\nStatus 504, sleeping program for 1 seconds\n")
        time.sleep(1)

        if returned504Times > 2:
          print("\n Status 504 3 times in a row, sleeping for 30 seconds \n")
          returned504Times = 0
          time.sleep(30)
  
        continue
      else:
        print("Error: " + str(r.status_code) + " returned by Riot API")
        sys.exit(0)

    # extracting data in json format 
    data = r.json() 

    #run this 10 times per request
    def returnedData(data, iterations):
      try:
        if data["participants"][iterations]["teamId"] == 100:
          firstDragon = data["teams"][0]["firstDragon"]
        else:
          firstDragon = data["teams"][1]["firstDragon"]

        if data["teams"][0]["firstTower"] == False & data["teams"][1]["firstTower"] == False:
          firstTowerKill = False
        else:
          firstTowerKill = data["participants"][iterations]["stats"]["firstTowerKill"]

        #(gameId, championId, teamId, damageDealt, assists, kills)
        return (data["gameId"], #gameId
                data["participants"][iterations]["championId"], #championId
                data["participants"][iterations]["teamId"], #teamId
                data["participants"][iterations]["stats"]["totalDamageDealt"], #damageDealt
                data["participants"][iterations]["stats"]["assists"], #assists
                data["participants"][iterations]["stats"]["kills"], #kills
                data["participants"][iterations]["stats"]["totalHeal"], #totalHealing
                data["participants"][iterations]["stats"]["totalMinionsKilled"], #totalMinionsKilled
                data["participants"][iterations]["stats"]["win"], #win
                data["participants"][iterations]["stats"]["firstBloodKill"], #firstBloodKill
                firstDragon, #firstDragon
                firstTowerKill, #firstTowerKill
                data["participants"][iterations]["stats"]["visionScore"], #visionScore
                data["gameDuration"]) #gameDuration
      except:
        print(sys.exc_info()[0], "occurred in returnedData function.")
        sys.exit(0)

    #call function 10 times per request, add each object to the array
    game = []
    for a in range(10):
      value = returnedData(data,a)
      game.append(value)
    
    #send data to to database
    try:
      mycursor.executemany(sql, game)
      mydb.commit()
      print(mycursor.rowcount, " rows were inserted for game id", data["gameId"])
    except:
      print(sys.exc_info()[0], "occurred in trying to execute sql update")


 


#TeamId 100 = Blue side participents 1 through 5
#TeamId 200 = Red side participents 6 through 10
