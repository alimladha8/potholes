'''
Created on Oct 3, 2015

@author: seanhudson
'''
import requests 

r = requests.get('http://riot-hackathon.bright-wolf.net/api/sensors/history?sensor_id=1000038&from=2015-10-02T15:41:23:149Z', auth=('alim.ladha', 'wolfpuck'))
print r.status_code
#r.headers['application/json; charset=utf8']
#'application/json; charset=utf8'
r.encoding
#'utf-8'
r.text
#u'{"type":"User"...'
r.json()