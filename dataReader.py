import requests 
from random import randint

def potholeChecker(vibration, dif):
    if vibration > 0 and (dif > 40 and dif < 150):
        return True
    return False
        #threshhold for a derivative

def locationGenerator(change):         #generates random coordinates along I-95
    x = 34.535730 + change
    y = (-79.233051 + 1.014439 * (change))
    return (x,y)

output = open("potholeData.csv", "w")

r = requests.get('http://riot-hackathon.bright-wolf.net/api/sensors/history?sensor_id=1000038&from=2015-10-02T15:41:23Z', auth=('alim.ladha', 'wolfpuck'))

print r.status_code
r.encoding
r.text
x = r.json()
matches =  x['queryresult']['matches']
elevation1 = None
elevation2 = None
change = 0.0      #used for testing
for entry in matches:
    point = ''
    vibration = entry['analog_channel_1']
    if elevation1 == None:
        elevation1 = entry['analog_channel_3']
        continue
    elevation2 = elevation1
    elevation1 = entry['analog_channel_3']
    #location = {'latitude' : 35.7694934, 'longitude' :-78.6790169, 'altitude' : 0.0}
    local = locationGenerator(change)
    location = {'latitude' : local[0], 'longitude' :local[1], 'altitude' : 0.0}
    latitude = location['latitude']
    longitude = location['longitude']
    #print (str(vibration) + ',' + str(elevation) + ',' + 'location')
    dif = elevation2-elevation1
    change = change + .001111
    if potholeChecker(vibration, dif):
        output.write((str(vibration) + ',' + str(dif) + ',' + str(latitude) + ',' + str(longitude) + '\n'))
    output.flush()

output.close()
