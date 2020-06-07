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



#nationality = []

ip = input('Enter standings type (Drivers or Constructors):')
rnd = (js['MRData']['total'])
for i in range(int(rnd)):
    if ip == 'Drivers':
        pos = []
        driver = []
        constructor = []
        points = []
        wins = []
        url1 = baseurl + season + '/' + str(i+1) + '/driverStandings.json'
        goto1 = urllib.request.urlopen(url1, context=ctx)
        data1 = goto1.read().decode()
        js1 = json.loads(data1)
        j1 = json.dumps(js1, indent=4)
        for element in range(len(js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'])):
            pos.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][element]['position'])
            driver.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][element]['Driver']['givenName'] + ' ' + js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][element]['Driver']['familyName'])
            constructor.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][element]['Constructors'][0]['name'])
            points.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][element]['points'])
            wins.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][element]['wins'])
        table = PrettyTable(['Position','Driver','Constructor','Points','Wins'])
        for element in range(len(js1['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'])):
            table.add_row([pos[element],driver[element],constructor[element],points[element],wins[element]])
        print('Driver Standings After Round',i+1)
        print(table)

    if ip == 'Constructors':
        pos = []
        nationality = []
        constructor = []
        points = []
        wins = []
        url1 = baseurl + season + '/' + str(i + 1) + '/constructorStandings.json'
        goto1 = urllib.request.urlopen(url1, context=ctx)
        data1 = goto1.read().decode()
        js1 = json.loads(data1)
        j1 = json.dumps(js1, indent=4)
        for element in range(len(js1['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings'])):
            pos.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings'][element]['position'])
            constructor.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings'][element]['Constructor']['name'])
            nationality.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings'][element]['Constructor']['nationality'])
            points.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings'][element]['points'])
            wins.append(js1['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings'][element]['wins'])
        table = PrettyTable(['Position', 'Constructor', 'Nationality', 'Points', 'Wins'])
        for element in range(len(js1['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings'])):
            table.add_row([pos[element], constructor[element], nationality[element], points[element], wins[element]])
        print('Constructor Standings After Round', i + 1)
        print(table)