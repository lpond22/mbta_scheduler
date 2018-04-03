import requests
import json

class MbtaApi3Client:
    url_base = 'https://api-v3.mbta.com'
    neds_api_key = '5e44686f7e394dab992135e893b8a9f4'
    routeIds = {'orange': 'Orange', 'red': 'Red'}
    stopIds = {'downtown crossing': 1234, 'stony brook': 70005}

    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.directionID = 1

    def getPredictions(self, routeID, stopID, directionID = None):
        predictionsUrl = '{}/predictions?filter[route]={}&filter[stop]={}&filter[direction_id]={}'
        url = predictionsUrl.format(self.url_base, routeID, stopID, self.directionID)

        predictions = []
        try:
            rawResponse = requests.get(url)
            predictionsJson = rawResponse.json()
        except:
            print("error!")
        return predictionsJson['data']

    def getArrivalTimePredictions(self, routeID, stopID, directionID = None):
        predictions = getPredictions(routeID, stopID, directionID)
        return [p['attributes']['arrival_time'].encode('utf-8') for p in predictions]
