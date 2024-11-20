# Author   : Eduardo Suarez del Valle
# Email    : esuarez@umass.edu
# Spire ID : 34750477

import math

# This function is provided to you as is.
# Do NOT change this function.
def distance(gps1, gps2):
  '''Return distance, in meter, between two GPS coordinates
  A GPS coord is a 2-element tuple of latitude and longitude'''
  R = 6372800  # Earth radius in meters
  lat1, lon1, lat2, lon2 = gps1[0], gps1[1], gps2[0], gps2[1]
  phi1, phi2 = math.radians(lat1), math.radians(lat2)
  dphi       = math.radians(lat2 - lat1)
  dlambda    = math.radians(lon2 - lon1)
  a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
  return 2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a))

# stations and data_today are two global dictionaries provided
# to you as examples for testing your functions.
# You can keep them as is.

stations = {
  'UMCS1': {'gps': (42.3949101,-72.5304337), 'sponsor':'UMass CICS'},
  'BOSTA': {'gps': (42.2140122,-71.3254988), 'sponsor':'UMass Boston'},
  'UMCS2': {'gps': (42.3949206,-72.5304524), 'sponsor':'UMass CICS'},
  'BOSTB': {'gps': (42.3760882,-71.1098623), 'sponsor':'Harvard'},
  'BOSTH': {'gps': (42.3564454,-71.0457016), 'sponsor':'Harvard'},
  'NASA8': {'gps': (38.8937545,-77.0145761), 'sponsor':'NASA'},
  'UMEN1': {'gps': (42.3950000,-72.5300000), 'sponsor':'UMass Eng'},
  'AMHER': {'gps': (42.3951000,-72.5320000)},
  'H2B4A': {'gps': (42.2470947,-72.7105421), 'sponsor':'UMass CICS'},
}

data_today = {
  'BOSTA': {'tempC': 12.2, 'humidity': 59},
  'BOSTB': {'tempC': 11.5, 'wind': 25},
  'UMCS1': {'tempC': 10.5, 'humidity': 66},
  'UMEN1': {'tempF': 50.9},
  'UMCS2': {'wind': 135, 'humidity': 25},
  'H2B4A': {'tempF': 51.8},
  'NASA8': {'tempC': 22},
  'AMHER': {'tempF': 64.4}
}

# ---------- WRITE YOUR FUNCTIONS BELOW ----------
def get_stations_by_loc(target=(0, 0), radius=1000):
    result = set()
    for station, info in stations.items():
        gps = info.get('gps')
        if gps and distance(target, gps) <= radius:
            result.add(station)
    return result


def get_avg_temp(target=(0, 0), radius=1000, celsius=True):
  nearby_stations = get_stations_by_loc(target, radius)
  total_temp = 0
  count = 0

  for station in nearby_stations:
    if station in data_today:
      station_data = data_today[station]

      if 'tempC' in station_data:
        temp = station_data['tempC']
        if not celsius:
          temp = temp * 9 / 5 + 32
        total_temp += temp
        count += 1

      elif 'tempF' in station_data:
        temp = station_data['tempF']
        if celsius:
          temp = (temp - 32) * 5 / 9
        total_temp += temp
        count += 1

  if count == 0:
    return None  # No stations with temperature data
  elif total_temp == 0:
    return 0  # Sum of temperatures is 0
  else:
    return total_temp / count  # Return the average


# ========== YOUR IMPLEMENTATIONS END HERE ==========

# You can uncomment each block of code below to test your functions.
# The expected outputs are in the lab description

print(get_stations_by_loc((42.39,-72.53), 1))
print(get_stations_by_loc((42.39,-72.53)))
print(get_stations_by_loc(radius=200000, target=(42.39,-72.53)))
# print(get_stations_by_loc(radius=10**6))

# print(get_avg_temp((42.39,-72.53), 1))
# print(get_avg_temp((42.39,-72.53)))
print(get_avg_temp(radius=50000, target=(42.214,-71.325)))
# print(get_avg_temp((42.214,-71.325), 50000, celsius=False))
# print(get_avg_temp(radius=10**6))

# The following two lines are for testing your functions
# in the Questionnaire part of this lab
# print(get_stations_by_sponsor('UMass CICS'))
# print(get_set_of_sponsors())


