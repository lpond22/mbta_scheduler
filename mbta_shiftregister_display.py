from mbta_api_client import MbtaApi3Client
from dateutil import parser
from pytz import timezone
import pytz
import math
from datetime import datetime
from shiftregister import ShiftRegister

def get_register():
  return ShiftRegister(10,9,11)

def clear_register(register):
  register.values = [0,0,0,0,0,0,0,0]

def get_wait_times(api_client, train_line, stop):
  predicted_arrival_times = client.getArrivalTimePredictions(MbtaApi3Client.routeIds[train_line],
    MbtaApi3Client.stopIds[stop])

  utc_parsed_times = [parser.parse(pat).astimezone(pytz.utc) for pat in predicted_arrival_times]

  return [math.trunc((t - datetime.now(pytz.utc)).seconds/60) for t in utc_parsed_times]


client = MbtaApi3Client(MbtaApi3Client.neds_api_key)

utc_now = datetime.now(pytz.utc)

predicted_arrival_times = client.getArrivalTimePredictions(MbtaApi3Client.routeIds['orange'],
  MbtaApi3Client.stopIds['downtown_crossing_forest_hills'])

utc_parsed_times = [parser.parse(pat).astimezone(pytz.utc) for pat in predicted_arrival_times]

wait_times_in_min = [math.trunc((t - utc_now).seconds/60) for t in utc_parsed_times]

print("Wait times at Downtown Crossing for Orange line to Forest Hills are {}".format(get_wait_times(client, 'orange', 'downtown_crossing_forest_hills')))
print("Wait times at Downtown Crossing for Orange line to Oak Grove are {}".format(get_wait_times(client, 'orange', 'downtown_crossing_oak_grove')))
print("Wait times at Downtown Crossing for Red line to Alewife are {}".format(get_wait_times(client, 'red', 'downtown_crossing_alewife')))
print("Wait times at Downtown Crossing for Red line to Ashmont/Braintree are {}".format(get_wait_times(client, 'red', 'downtown_crossing_ashmont_braintree')))
print("Wait times at State Street for Orange line to Forest Hills are {}".format(get_wait_times(client, 'orange', 'state_street_forest_hills')))
print("Wait times at State Street for Orange line to Oak Grove are {}".format(get_wait_times(client, 'orange', 'state_street_oak_grove')))
print("Wait times at State Street for Blue line to Bowdoin are {}".format(get_wait_times(client, 'blue', 'state_street_bowdoin')))
print("Wait times at State Street for Blue line to Wonderland are {}".format(get_wait_times(client, 'blue', 'state_street_wonderland')))
