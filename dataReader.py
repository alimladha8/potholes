'''
Created on Oct 3, 2015

@author: seanhudson
'''
import requests 

def potholeChecker(vibration, dif):
    if vibration > 0 and dif > 0:
        return True
    return False
        #threshhold for a derivative

output = open("potholeData.csv", "w")

r = requests.get('http://riot-hackathon.bright-wolf.net/api/sensors/history?sensor_id=1000038&from=2015-10-02T15:41:23Z', auth=('alim.ladha', 'wolfpuck'))

print r.status_code
r.encoding
r.text
x = r.json()
matches =  x['queryresult']['matches']
elevation1 = None
elevation2 = None
for entry in matches:
    point = ''
    vibration = entry['analog_channel_1']
    if elevation1 == None:
        elevation1 = entry['analog_channel_3']
        continue
    elevation2 = elevation1
    elevation1 = entry['analog_channel_3']
    location = {'latitude' : 35.7694934, 'longitude' :-78.6790169, 'altitude' : 0.0}
    latitude = location['latitude']
    longitude = location['longitude']
    #print (str(vibration) + ',' + str(elevation) + ',' + 'location')
    dif = elevation2-elevation1
    if potholeChecker(vibration, dif):
        output.write((str(vibration) + ',' + str(dif) + ',' + str(latitude) + ',' + str(longitude) + '\n'))
    output.flush()

output.close()