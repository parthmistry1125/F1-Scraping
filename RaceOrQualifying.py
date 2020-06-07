import urllib.request,urllib.parse,urllib.error
import ssl
import json
from prettytable import PrettyTable

# Ignore SSL Certification errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

driver = []
q1 = []
q2 = []
q3 = []
pos = []
constructor = []
grid = []
points = []
status = []
season = input('Enter season:')
race = input('Enter race name:')
race = race + ' Grand Prix'
event = input('Enter event (Race or Qualifying):')
baseurl = 'http://ergast.com/api/f1/'

url1 = 'http://ergast.com/api/f1/' + season + '.json'
goto1 = urllib.request.urlopen(url1, context=ctx)
data1 = goto1.read().decode()
js1 = json.loads(data1)
j1 = json.dumps(js1, indent=4)
for i in range(len(js1['MRData']['RaceTable']['Races'])):
    if js1['MRData']['RaceTable']['Races'][i]['raceName'] == race:
        rnd = js1['MRData']['RaceTable']['Races'][i]['round']
        print('Round ' + rnd)

if event == 'Race':
    try:
        url = baseurl + season + '/' + rnd + '/results.json'
        goto = urllib.request.urlopen(url, context=ctx)
        data = goto.read().decode()
        js = json.loads(data)
        j = json.dumps(js, indent=4)
        for i in range(len(js['MRData']['RaceTable']['Races'][0]['Results'])):
            pos.append(js['MRData']['RaceTable']['Races'][0]['Results'][i]['position'])
            driver.append(js['MRData']['RaceTable']['Races'][0]['Results'][i]['Driver']['givenName'] + ' ' + js['MRData']['RaceTable']['Races'][0]['Results'][i]['Driver']['familyName'])
            constructor.append(js['MRData']['RaceTable']['Races'][0]['Results'][i]['Constructor']['name'])
            grid.append(js['MRData']['RaceTable']['Races'][0]['Results'][i]['grid'])
            points.append(js['MRData']['RaceTable']['Races'][0]['Results'][i]['points'])
            status.append(js['MRData']['RaceTable']['Races'][0]['Results'][i]['status'])
        table = PrettyTable(['Position','Grid','Driver', 'Constructor', 'Status','Points'])
        for i in range(len(js['MRData']['RaceTable']['Races'][0]['Results'])):
            try:
                table.add_row([pos[i],grid[i],driver[i],constructor[i],status[i],points[i]])
            except:
                continue
        print(js['MRData']['RaceTable']['Races'][0]['season'] + ' ' + js['MRData']['RaceTable']['Races'][0]['raceName'])
        print('Race Result:')
        print(table) #Displays the race result for the asked Grand Prix
    except:
        print('There was no such Grand Prix that season')  #If no such Grand Prix was scheduled that season

else:
    if season < '2003':
        print('Data not available.') #This constraint is placed as qualifying data pre 2003 was not available
    else:
        try:
            url = baseurl + season + '/' + rnd + '/qualifying.json'
            goto = urllib.request.urlopen(url, context=ctx)
            data = goto.read().decode()
            js = json.loads(data)
            j = json.dumps(js, indent=4)
            for i in range(len(js['MRData']['RaceTable']['Races'][0]['QualifyingResults'])):
                driver.append(js['MRData']['RaceTable']['Races'][0]['QualifyingResults'][i]['Driver']['givenName'] + ' ' + js['MRData']['RaceTable']['Races'][0]['QualifyingResults'][i]['Driver']['familyName'])
                constructor.append(js['MRData']['RaceTable']['Races'][0]['QualifyingResults'][i]['Constructor']['name'])
                pos.append(js['MRData']['RaceTable']['Races'][0]['QualifyingResults'][i]['position'])
            for i in range(len(js['MRData']['RaceTable']['Races'][0]['QualifyingResults'])):
                q1.append(js['MRData']['RaceTable']['Races'][0]['QualifyingResults'][i]['Q1'])
                try:
                    q2.append(js['MRData']['RaceTable']['Races'][0]['QualifyingResults'][i]['Q2'])
                except:
                    q2.append('')
                try:
                    q3.append(js['MRData']['RaceTable']['Races'][0]['QualifyingResults'][i]['Q3'])
                except:
                    q3.append('')
            table = PrettyTable(['Position', 'Driver', 'Constructor', 'Q1', 'Q2', 'Q3'])
            for i in range(len(js['MRData']['RaceTable']['Races'][0]['QualifyingResults'])):
                try:
                    table.add_row([pos[i], driver[i], constructor[i], q1[i], q2[i], q3[i]])
                except:
                    continue
            print(js['MRData']['RaceTable']['Races'][0]['season'] + ' ' + js['MRData']['RaceTable']['Races'][0]['raceName'])
            print('Qualifying Result:')
            print(table) #Displays the qualifying result for the Grand Prix
        except:
            print('There was no such Grand Prix that season') #If no such Grand Prix was scheduled that season



