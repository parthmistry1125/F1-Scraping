import urllib.request,urllib.parse,urllib.error
import ssl
import json
from prettytable import PrettyTable

# Ignore SSL Certification errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

season = input('Enter the season:')
baseurl = 'http://ergast.com/api/f1/'
url = baseurl + season + '.json'
goto = urllib.request.urlopen(url,context=ctx)
data = goto.read().decode()
js = json.loads(data)
j = json.dumps(js,indent=4)

rnd = []
raceName = []
date = []
time = []
circuitName = []
locality = []
country = []
url = []
pos = []
driver = []
constructor = []
nationality = []
points = []
wins = []
baseurl = 'http://ergast.com/api/f1/'

for i in range(len(js['MRData']['RaceTable']['Races'])):
    rnd.append(js['MRData']['RaceTable']['Races'][i]['round'])
    raceName.append(js['MRData']['RaceTable']['Races'][i]['raceName'])
    date.append(js['MRData']['RaceTable']['Races'][i]['date'])
    circuitName.append(js['MRData']['RaceTable']['Races'][i]['Circuit']['circuitName'])
    locality.append(js['MRData']['RaceTable']['Races'][i]['Circuit']['Location']['locality'])
    country.append(js['MRData']['RaceTable']['Races'][i]['Circuit']['Location']['country'])
    url.append(js['MRData']['RaceTable']['Races'][i]['url'])
try:
    for i in range(len(js['MRData']['RaceTable']['Races'])):
        time.append(js['MRData']['RaceTable']['Races'][i]['time'])
    table = PrettyTable(['Round', 'Race Name', 'Date','Time','Circuit Name', 'Locality', 'Country', ])
    for i in range(len(js['MRData']['RaceTable']['Races'])):
        table.add_row([rnd[i], raceName[i], date[i],time[i],circuitName[i], locality[i], country[i]])
    print(table)

except:
    print('Time not available.')
    table = PrettyTable(['Round','Race Name','Date','Circuit Name','Locality','Country',])
    for i in range(len(js['MRData']['RaceTable']['Races'])):
        table.add_row([rnd[i],raceName[i],date[i],circuitName[i],locality[i],country[i]])
    print(table)


#res = input('Enter the season (Yes or No):')
res1 = input('Enter round (Yes or No):') #This asks if the user wants results after a specific round
standings = input('Enter standings type (Drivers or Constructors):') #This asks which standings the user wants

if res1 == 'No' and standings == 'Drivers':
    url1 = baseurl + season + '/driverStandings.json'
    goto1 = urllib.request.urlopen(url1,context=ctx)
    data1 = goto1.read().decode()
    js1 = json.loads(data1)
    j1 = json.dumps(js1,indent=4)
    #print(j1)
    for i in range(len(js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'])):
        pos.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][i]['position'])
        driver.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][i]['Driver']['givenName'] + ' ' +js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][i]['Driver']['familyName'])
        constructor.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][i]['Constructors'][0]['name'])
        points.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][i]['points'])
        wins.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][i]['wins'])
    table = PrettyTable(['Position','Driver','Constructor','Points','Wins'])
    for i in range(len(js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'])):
        table.add_row([pos[i],driver[i],constructor[i],points[i],wins[i]])
    print(table) #This displays driver standings after season end

if res1 == 'No' and standings == 'Constructors':
    url1 = baseurl + season + '/constructorStandings.json'
    goto1 = urllib.request.urlopen(url1,context=ctx)
    data1 = goto1.read().decode()
    js1 = json.loads(data1)
    j1 = json.dumps(js1,indent=4)
    for i in range(len(js1['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings'])):
        pos.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings'][i]['position'])
        constructor.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings'][i]['Constructor']['name'])
        nationality.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings'][i]['Constructor']['nationality'])
        points.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings'][i]['points'])
        wins.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings'][i]['wins'])
    table = PrettyTable(['Position','Constructor','Nationality','Points', 'Wins'])
    for i in range(len(js1['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings'])):
        table.add_row([pos[i],constructor[i],nationality[i],points[i], wins[i]])
    print(table) #This displays constructor standings after season end

if res1 == 'Yes' and standings == 'Drivers':
    rnd1 = input('Enter round:')
    url1 = baseurl + season + '/' + rnd1 + '/driverStandings.json'
    goto1 = urllib.request.urlopen(url1,context=ctx)
    data1 = goto1.read().decode()
    js1 = json.loads(data1)
    j1 = json.dumps(js1,indent=4)
    #print(j)
    for i in range(len(js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'])):
        pos.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][i]['position'])
        driver.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][i]['Driver']['givenName'] + ' ' +js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][i]['Driver']['familyName'])
        constructor.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][i]['Constructors'][0]['name'])
        points.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][i]['points'])
        wins.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][i]['wins'])
    table = PrettyTable(['Position','Driver','Constructor','Points','Wins'])
    for i in range(len(js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'])):
        table.add_row([pos[i],driver[i],constructor[i],points[i],wins[i]])
    print(table) #This displays driver standings after a particular round

if res1 == 'Yes' and standings == 'Constructors':
    rnd1 = input('Enter round:')
    url1 = baseurl + season + '/' + rnd1 + '/constructorStandings.json'
    goto1 = urllib.request.urlopen(url1,context=ctx)
    data1 = goto1.read().decode()
    js1 = json.loads(data1)
    j1 = json.dumps(js1,indent=4)
    for i in range(len(js1['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings'])):
        pos.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings'][i]['position'])
        constructor.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings'][i]['Constructor']['name'])
        nationality.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings'][i]['Constructor']['nationality'])
        points.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings'][i]['points'])
        wins.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings'][i]['wins'])
    table = PrettyTable(['Position','Constructor','Nationality','Points', 'Wins'])
    for i in range(len(js1['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings'])):
        table.add_row([pos[i],constructor[i],nationality[i],points[i], wins[i]])
    print(table) #This displays constructor standings after a particular round


