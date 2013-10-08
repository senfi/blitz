import json
import time
from pygeocoder import Geocoder

json_streets = open('streets.json')
streetsjson = json.load(json_streets)

for street in streetsjson["streets"]:
  name = street["name"]
  city = street["city"]
  search_phrase = name+","+city
  
  try:
    results = Geocoder.geocode(search_phrase)
  except:
    print "Have to wait because Google API limits QUERIES..."
    time.sleep(2)
    results = Geocoder.geocode(search_phrase)
  
  geometry = results.raw[0]["geometry"]
  formatted_address = results.raw[0]["formatted_address"]
  print "found for " + search_phrase + ": " + formatted_address + "\n   " + json.dumps(geometry["location"]) 
  
  street.update(geometry)
  street["formatted_address"] = formatted_address

with open('streets_geolocation.json', 'w') as outfile:
  json.dump(streetsjson, outfile, indent=2)