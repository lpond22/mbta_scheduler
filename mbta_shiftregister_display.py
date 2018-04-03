from mbta_api_client import MbtaApi3Client
import time
import datetime
from shiftregister import ShiftRegister

def get_register():
  return ShiftRegister(10,9,11)

def clear_register(register):
  register.values = [0,0,0,0,0,0,0,0]


client = MbtaApi3Client(MbtaApi3Client.neds_api_key)

now = datetime.datetime.now()
now_time = now.strftime("%H:%M")

predicted_arrival_times = client.getArrivalTimePredictions(MbtaApi3Client.routeIds['orange'],
  MbtaApi3Client.stopIds['downtown crossing'])

