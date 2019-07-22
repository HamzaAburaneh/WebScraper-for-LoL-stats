import requests
from bs4 import BeautifulSoup

def getWebpage(champion):
   url = 'https://rankedboost.com/league-of-legends/counter/' + champion

   page = requests.get(url)

   getWinPlayBanRate(page)

   return getCounterChampions(page)

def getCounterChampions(page):
     # Parses LoLProfile champion webpage to find the counter
     # # champions given the lane you are playing that champion in
     champList = []

     soup = BeautifulSoup(page.text, 'html.parser')

     counterChampions = soup.find_all(class_='RecommendedCounterName', string = True)

     for champion in counterChampions:
       champList.append(champion.findAll(text = True))

     champList = [x[0] for x in champList]

     return formatChampList(champList)

def getWinPlayBanRate(page):
     # Parses LoLProfile champion webpage to find the counter
     # # champions given the lane you are playing that champion in
     statsList = []

     soup = BeautifulSoup(page.text, 'html.parser')

     stats = soup.find_all(class_='WinRateStat', string = True)

     print(champName + " has a " + statsList[0].text + " winrate, " + statsList[1].text + " pick rate, " + statsList[2].text + " ban rate.")


def formatChampList(champList):
    strongAgainst = []
    weakAgainst   = []
    counter = 0
    for x in champList:
      if counter < 3:
        weakAgainst.append(x)
        counter += 1
      else:
        strongAgainst.append(x)
        counter += 1

    print(champName + " is Strong against these champions: " + ", ".join(strongAgainst))
    print()
    print(champName + " is weak against these champions: " + ", ".join(weakAgainst))
 
print()
champName = input('Enter your champions name: ')
print()
getWebpage(champName)
