import urllib
import requests
import json
import time
import datetime

url_base = 'https://api-v3.mbta.com'
routeID = 'Orange'
stopID = 70005
directionID = 1

def getPredictions(routeID, stopID, directionID = None):
  url = '{}/predictions?filter[route]={}&filter[stop]={}&filter[direction_id]={}'.format(url_base, routeID, stopID, directionID)

  predictions = []
  try:
    rawResponse = requests.get(url)
    predictions = rawResponse.json()['data']
  except: 
    print "error!"
  return predictions

def getArrivalTimePredictions(routeID, stopID, directionID = None):
  predictions = getPredictions(routeID, stopID, directionID)
  return [p['attributes']['arrival_time'].encode('utf-8') for p in predictions]

def get_first(iterable, default=None):
    if iterable:
        for item in iterable:
            return item
    return default

now = datetime.datetime.now()
now_time = now.strftime("%H:%M")

arrival = get_first(getArrivalTimePredictions(routeID, stopID, directionID))
arrival = arrival[:16]
arrival = datetime.datetime.strptime(arrival, "%Y-%m-%dT%H:%M")
arrival_time = arrival.strftime("%H:%M")

def countdown(arrival_time, current_time):
  estimated_time = arrival - now
  if estimated_time.seconds/60 <= 10:
    return estimated_time.seconds/60
  else: 
    return 10

print 'It is now:', now_time
print 'The next inbound train at Stony Brook arrives at:', arrival_time
print 'It will arrive in', countdown(arrival_time, now_time), 'minutes'
