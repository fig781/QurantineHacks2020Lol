# importing the requests library 
import requests 
import time
import sys
from csv import DictReader

#for each gameId in the kaggle csv itterate through them
with open('Challenger_Ranked_Games.csv','r') as file:
  csvDictReader = DictReader(file)

  returned504Times = 0

  for row in csvDictReader:
    gameId = row['gameId']
    gameDuraton = row['gameDuraton']

    if int(gameDuraton) < 900:
      continue
    # api-endpoint 
    URL = "https://kr.api.riotgames.com/lol/match/v4/matches/" + gameId + "?api_key=RGAPI-940383e9-e7bf-4c88-9b36-efcc9179f9ec"

    # sending get request and saving the response as response object 
    r = requests.get(url = URL) 

    # if the request encounters an error it will check if it is too many requests, if it is, then it will pause for 2 minutes and one second, other errors stop the program
    if r.status_code != 200:
      if r.status_code == 429 or r.status_code == 504:
        returned504Times = returned504Times + 1
        print("\nStatus 504, sleeping program for 1 seconds\n")
        time.sleep(1)

        if returned504Times > 2:
          print("\n Status 504 3 times in a row, sleeping for 120 seconds \n")
          returned504Times = 0
          time.sleep(120)
  
        continue
      else:
        print("Error: " + str(r.status_code) + "returned by Riot API")
        sys.exit(0)

    # extracting data in json format 
    data = r.json() 

    #run this 10 times per request
    def returnedData(data, iterations):

      if data["participants"][iterations]["teamId"] == 100:
        firstDragon = data["teams"][0]["firstDragon"]
      else:
        firstDragon = data["teams"][1]["firstDragon"]

      return {"gameId": data["gameId"], 
              "championId": data["participants"][iterations]["championId"], 
              "teamId": data["participants"][iterations]["teamId"], 
              "damageDealt": data["participants"][iterations]["stats"]["totalDamageDealt"], 
              "assists": data["participants"][iterations]["stats"]["assists"], 
              "kills": data["participants"][iterations]["stats"]["kills"], 
              "totalHealing": data["participants"][iterations]["stats"]["totalHeal"], 
              "totalMinionsKilled": data["participants"][iterations]["stats"]["totalMinionsKilled"], 
              "win": data["participants"][iterations]["stats"]["win"],
              "firstBloodKill": data["participants"][iterations]["stats"]["firstBloodKill"],
              "firstDragon": firstDragon,
              "firstTowerKill": data["participants"][iterations]["stats"]["firstTowerKill"],
              "visionScore": data["participants"][iterations]["stats"]["visionScore"]}

    #call function 10 times per request, add each object to the array
    game = []
    for i in range(10):
      value = returnedData(data,i)
      game.append(value)
    
    print(game)


#send this data to to database 


#TeamId 100 = Blue side participents 1 through 5
#TeamId 200 = Red side participents 6 through 10
# need per champion, 10 of thse per request: champion id, side they were on, damage dealt, assists, kills, total healing, starting side, cs