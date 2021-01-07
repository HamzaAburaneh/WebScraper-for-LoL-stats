import requests
from bs4 import BeautifulSoup
 
#update championNames as more champs have been added.
championNames=[
'aatrox','ahri','akali','alistar','amumu','anivia','annie','ashe','aurelion sol','azir','bard','blitzcrank','brand','braum','caitlyn','camille','cassiopeia',
'choGath','chogath','corki','darius','diana','dr.Mundo','mundo','draven','ekko','elise','evelynn','ezreal','fiddlesticks','fiora','fizz','galio','gangplank','garen','gnar',
'gragas','graves','hecarim','heimerdinger','illaoi','irelia','ivern','janna','jarvan','jarvan','jax','jayce','jhin','jinx','kaiSa','kalista','karma','karthus','kassadin',
'katarina','kayle','kayn','kennen','kha\'zix','kindred','kled','kog \'maw','kogmaw','leblanc','lee sin','leona','lissandra','lucian','lulu','lux','malphite','malzahar','maokai',
'master yi','miss fortune','mordekaiser','morgana','nami','nasus','nautilus','neeko','nidalee','nocturne','nunu','olaf','orianna','ornn','pantheon','poppy','pyke','qiyana',
'quinn','rakan','rammus','reksai','renekton','rengar','riven','rumble','ryze','sejuani','shaco','shen','shyvana','singed','sion','sivir','skarner','sona','soraka','swain',
'sylas','syndra','tahm kench','taliyah','talon','taric','teemo','thresh','tristana','trundle','tryndamere','twisted fate','twitch','udyr','urgot','varus','vayne','veigar',
'velKoz','velkoz','vi','viktor','vladimir','volibear','warwick','wukong','wayah','werath','xin zhao','yasuo','yorick','yuumi','zac','zed','ziggs','zilean','zoe','zyra'
] 

validChampion = True
menu          = True

def getWebpage(champion):
   url = 'https://rankedboost.com/league-of-legends/counter/' + champion
   page = requests.get(url)
   getWinPlayBanRate(page)
   return getCounterChampions(page)

def getCounterChampions(page):
     champList = []
     soup = BeautifulSoup(page.text, 'html.parser')
     counterChampions = soup.find_all(class_='RecommendedCounterName', string = True)
     for champion in counterChampions:
       champList.append(champion.findAll(text = True))
     champList = [x[0] for x in champList]
     return formatChampList(champList)

def getWinPlayBanRate(page):
     soup = BeautifulSoup(page.text, 'html.parser')
     stats = soup.find_all(class_='StatsTD', string = True)
     print(champName + " has a " + stats[0].text + " winrate, " + stats[1].text + " pick rate, " + stats[2].text + " ban rate.")

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
    print(champName + " is Weak against these champions: " + ", ".join(weakAgainst))
    print()

while(menu):
    print()
    while(validChampion):
        champName = input('Enter a valid champion name: ')
        if champName.lower() in championNames:
            validChampion = False
    print()
    getWebpage(champName)
    menuExit = input('Would you like to search for another champion (y/n)? ')
    if menuExit == 'n':
        menu = False
    else:
        validChampion = True
