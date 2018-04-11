from mbta_api_client import MbtaApi3Client
from dateutil import parser
from pytz import timezone
import pytz
import math
from datetime import datetime

colors = {
  'orange': '\x1b[0;33;40m',
  'blue': '\x1b[0;34;40m',
  'red': '\x1b[0;31;40m',
  'reset': '\x1b[0m',
}

def get_wait_times(api_client, train_line, stop):
  predicted_arrival_times = client.getArrivalTimePredictions(MbtaApi3Client.routeIds[train_line],
    MbtaApi3Client.stopIds[stop])

  utc_parsed_times = [parser.parse(pat).astimezone(pytz.utc) for pat in predicted_arrival_times]
  # print("UTC now: {}".format(datetime.now(pytz.utc)))
  # print("UTC parsed predicted arrival minutes: {}".format(utc_parsed_times))

  return [math.trunc((t - datetime.now(pytz.utc)).total_seconds()/60.0) for t in utc_parsed_times]


client = MbtaApi3Client(MbtaApi3Client.neds_api_key)

print("Wait times at Downtown Crossing for {}Orange line{} to Forest Hills are {}".format(colors['orange'], colors['reset'], get_wait_times(client, 'orange', 'downtown_crossing_forest_hills')))
print("Wait times at Downtown Crossing for {}Orange line{} to Oak Grove are {}".format(colors['orange'], colors['reset'], get_wait_times(client, 'orange', 'downtown_crossing_oak_grove')))
print("Wait times at Downtown Crossing for {}Red line{} to Alewife are {}".format(colors['red'], colors['reset'], get_wait_times(client, 'red', 'downtown_crossing_alewife')))
print("Wait times at Downtown Crossing for {}Red line{} to Ashmont/Braintree are {}".format(colors['red'], colors['reset'], get_wait_times(client, 'red', 'downtown_crossing_ashmont_braintree')))
print("Wait times at State Street for {}Orange line{} to Forest Hills are {}".format(colors['orange'], colors['reset'], get_wait_times(client, 'orange', 'state_street_forest_hills')))
print("Wait times at State Street for {}Orange line{} to Oak Grove are {}".format(colors['orange'], colors['reset'], get_wait_times(client, 'orange', 'state_street_oak_grove')))
print("Wait times at State Street for {}Blue line{} to Bowdoin are {}".format(colors['blue'], colors['reset'], get_wait_times(client, 'blue', 'state_street_bowdoin')))
print("Wait times at State Street for {}Blue line{} to Wonderland are {}".format(colors['blue'], colors['reset'], get_wait_times(client, 'blue', 'state_street_wonderland')))
