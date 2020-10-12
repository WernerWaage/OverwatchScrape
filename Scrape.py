# Imports
import datetime
import json
import requests
from ScrapeFunctions import simple_get
from bs4 import BeautifulSoup

# Settings
vAnonymousMode = 0
# Remember that the profile has to be public
vProfileLink = 'https://playoverwatch.com/en-us/career/pc/Yell0w-2522'



vUserid =  vProfileLink.replace('https://playoverwatch.com/en-us/career/pc/','',1)
vUserid =  vUserid.replace('/','')
vSource = 			'Python'
vInternalIp = 		''
vValue = 			'0' # Casting required if Int
vType =				'overwatch'
vGroup = 			'Werner'
vJSON = 			''
vUsername = 		'Werner'
vPassword = 		''
vSeason = '23'
now = datetime.datetime.now()
vLocation = 'EU'
vDraw = '0'
vLost = '0'
vPlayed = '0'
vWon = '0'
vTime = '0'
countRole = 0

raw_html = simple_get(vProfileLink)
if raw_html is None :
    print("No data found")
else :
    print("Data loaded")
    print("-----------")
 
soup = BeautifulSoup(raw_html, 'html.parser')
print(soup.title.string)

for data in soup.findAll('h1',{'class':'header-masthead'}):
   vName = data.text
   print(vName)

for data in soup.findAll('div',{'class':'competitive-rank'})[0]:
    countRole += 1
    if countRole == 1 :
        vSkillrating = data.text
    elif countRole == 2 :
        ratingDps = data.text
    elif countRole == 3 :
        ratingDps = data.text
    else:
        ratingSupport = data.text


    countRole += 1

print(vSkillrating + " Tank Rating")
print(ratingDps + " DPS Rating")
print(ratingSupport + " Support Rating")

newsoup = soup.find("div", {"id": "competitive"})
for data in newsoup.findAll('tr',{'data-stat-id':'0x086000000000042E'}):
    vLost = data.text.replace('Games Lost','',1)
    print(vLost + " games lost")
for data in newsoup.findAll('tr',{'data-stat-id':'0x0860000000000385'}):
    vPlayed = data.text.replace('Games Played','',1)
    print(vPlayed + " games played this season")
for data in newsoup.findAll('tr',{'data-stat-id':'0x08600000000003F5'}):
    vWon = data.text.replace('Games Won','',1)
    print(vWon + " games won")

if vPlayed is None:
    vPlayed = 0
#else:
#    print("vPlayed ok!")
	
vDraw = str(int(vPlayed) - int(vLost) - int(vWon))
print(vDraw + " draws")

for data in newsoup.findAll('tr',{'data-stat-id':'0x0860000000000026'}):
    vTime = data.text.replace('Time Played','',1)
    print(vTime + " playtime")

userdata = {
  "id":vUserid,
  "profilename": vName,
  "skillrating": vSkillrating,
  "games": vPlayed,
  "losses": vLost,
  "wins": vWon
}
vJSON = json.dumps(userdata)
#print("-------------")
print(vJSON)

# Upload info as webrequest
#vRequestString = 'http://api.overminds.org/?u='+vName+'&username='+vUserid+'&sr='+vSkillrating+'&t='+vType+'&won='+vWon+'&lost='+vLost+'&played='+vPlayed+'&draw='+vDraw+'&playtime='+vTime+'&season='+vSeason+'&location='+vLocation+''
#r = requests.get(vRequestString)
#r.status_code
#r.headers['content-type']
#print(r.text)

#print(vRequestString)