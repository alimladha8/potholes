'''
Created on Oct 3, 2015

@author: seanhudson
'''
import requests 

#output = open("potholeData.csv", "w")

r = requests.get('http://riot-hackathon.bright-wolf.net/api/techsmart/sensors/history?sensor_id=1000038&from=2015-10-02T15:41:23:149Z', auth=('alim.ladha', 'wolfpuck'))
#'http://riot-hackathon.bright-wolf.net/api/sensors?org_id=techsmart/'
print r.status_code
#r.headers['application/json; charset=utf8']
#'application/json; charset=utf8'
r.encoding
#'utf-8'
r.text
#u'{"type":"User"...'
r.json()



#output.close()