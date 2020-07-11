# importing the requests library 
import requests 
import time
import sys
from csv import DictReader

#for each gameId in the kaggle csv itterate through them
with open('Challenger_Ranked_Games.csv','r') as file:
  csvDictReader = DictReader(file)
  for row in csvDictReader:
    gameId = row['gameId']

    # api-endpoint 
    URL = "https://kr.api.riotgames.com/lol/match/v4/matches/" + gameId + "?api_key=RGAPI-1b4b5a24-db0d-4031-b75a-ce22428d6c9b"

    # sending get request and saving the response as response object 
    r = requests.get(url = URL) 

    # if the request encounters an error it will check if it is too many requests, if it is, then it will pause for 2 minutes and one second, other errors stop the program
    if r.status_code != 200:
      if r.status_code == 429:
        print("Error 429, sleeping program for 121 seconds")
        time.sleep(121)
      else:
        print("Error: " + str(r.status_code) + "returned by Riot API")
        sys.exit(0)

    # extracting data in json format 
    data = r.json() 

    #run this 10 times per request
    def returnedData(data, value):
      return {"gameId": data["gameId"], 
              "championId": data["participants"][value]["championId"], 
              "teamId": data["participants"][value]["teamId"], 
              "damageDealt": data["participants"][value]["stats"]["totalDamageDealt"], 
              "assists": data["participants"][value]["stats"]["assists"], 
              "kills": data["participants"][value]["stats"]["kills"], 
              "totalHealing": data["participants"][value]["stats"]["totalHeal"], 
              "totalMinionsKilled": data["participants"][value]["stats"]["totalMinionsKilled"], 
              "win": data["participants"][value]["stats"]["win"]}

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