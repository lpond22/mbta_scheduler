import requests
import json

class MbtaApi3Client:
    url_base = 'https://api-v3.mbta.com'
    neds_api_key = '5e44686f7e394dab992135e893b8a9f4'
    routeIds = {
        'orange': 'Orange',
        'red': 'Red',
        'blue': 'Blue',
        'green_b': 'Green-B',
        'green_c': 'Green-C',
        'green_d': 'Green-D',
        'green_e': 'Green-E'
    }
    stopIds = {
        'downtown_crossing_alewife': 70078,
        'downtown_crossing_ashmont_braintree': 70077,
        'downtown_crossing_forest_hills': 70020,
        'downtown_crossing_oak_grove': 70021,
        'stony_brook_oak_gove': 70005,
        'stony_brook_forest_hills': 70004,
        'state_street_oak_grove': 70023,
        'state_street_forest_hills': 70022,
        'state_street_bowdoin': 70041,
        'state_street_wonderland': 70042
    }

    def __init__(self, apiKey):
        self.apiKey = apiKey

    def getPredictions(self, routeID, stopID, directionID = None):
        predictionsUrl = '{}/predictions?filter[route]={}&filter[stop]={}&filter[direction_id]={}'
        url = predictionsUrl.format(self.url_base, routeID, stopID, directionID)

        predictions = []
        try:
            rawResponse = requests.get(url)
            predictionsJson = rawResponse.json()
        except:
            print("Error getting predictions from MBTA API!")
        # import pdb; pdb.set_trace()
        return predictionsJson['data']

    def getArrivalTimePredictions(self, routeID, stopID, directionID = None):
        predictions = self.getPredictions(routeID, stopID, directionID)
        return [p['attributes']['arrival_time'].encode('utf-8') for p in predictions]
