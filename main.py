import requests
from bs4 import BeautifulSoup

championNames = [
  'Aatrox',
  'Ahri',
  'Akali',
  'Alistar',
  'Amumu',
  'Anivia',
  'Annie',
  'Ashe',
  'Aurelion Sol',
  'Azir',
  'Bard',
  'Blitzcrank',
  'Brand',
  'Braum',
  'Caitlyn',
  'Camille',
  'Cassiopeia',
  'ChoGath',
  'chogath',
  'Corki',
  'Darius',
  'Diana',
  'Dr.Mundo',
  'mundo',
  'Draven',
  'Ekko',
  'Elise',
  'Evelynn',
  'Ezreal',
  'Fiddlesticks',
  'Fiora',
  'Fizz',
  'Galio',
  'Gangplank',
  'Garen',
  'Gnar',
  'Gragas',
  'Graves',
  'Hecarim',
  'Heimerdinger',
  'Illaoi',
  'Irelia',
  'Ivern',
  'Janna',
  'Jarvan',
  'jarvan',
  'Jax',
  'Jayce',
  'Jhin',
  'Jinx',
  'KaiSa',
  'Kalista',
  'Karma',
  'Karthus',
  'Kassadin',
  'Katarina',
  'Kayle',
  'Kayn',
  'Kennen',
  'KhaZix',
  'khazix',
  'Kindred',
  'Kled',
  'KogMaw',
  'kogmaw',
  'LeBlanc',
  'Lee Sin',
  'Leona',
  'Lissandra',
  'Lucian',
  'Lulu',
  'Lux',
  'Malphite',
  'Malzahar',
  'Maokai',
  'Master Yi',
  'Miss Fortune',
  'Mordekaiser',
  'Morgana',
  'Nami',
  'Nasus',
  'Nautilus',
  'Neeko',
  'Nidalee',
  'Nocturne',
  'Nunu',
  'Olaf',
  'Orianna',
  'Ornn',
  'Pantheon',
  'Poppy',
  'Pyke',
  'Qiyana',
  'Quinn',
  'Rakan',
  'Rammus',
  'RekSai',
  'reksai',
  'Renekton',
  'Rengar',
  'Riven',
  'Rumble',
  'Ryze',
  'Sejuani',
  'Shaco',
  'Shen',
  'Shyvana',
  'Singed',
  'Sion',
  'Sivir',
  'Skarner',
  'Sona',
  'Soraka',
  'Swain',
  'Sylas',
  'Syndra',
  'Tahm Kench',
  'Taliyah',
  'Talon',
  'Taric',
  'Teemo',
  'Thresh',
  'Tristana',
  'Trundle',
  'Tryndamer',
  'Twisted Fate',
  'Twitch',
  'Udyr',
  'Urgot',
  'Varus',
  'Vayne',
  'Veigar',
  'VelKoz',
  'velkoz',
  'Vi',
  'Viktor',
  'Vladimir',
  'Volibear',
  'Warwick',
  'Wukong',
  'Xayah',
  'Xerath',
  'Xin Zhao',
  'Yasuo',
  'Yorick',
  'Yuumi',
  'Zac',
  'Zed',
  'Ziggs',
  'Zilean',
  'Zoe',
  'Zyra',
]

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
while(True)
    champName = input('Enter a valid champion name: ')
    if champName in championNames
        break
print()
getWebpage(champName)

