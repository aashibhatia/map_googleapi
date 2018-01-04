import googlemaps
from datetime import datetime


gmaps = googlemaps.Client(key= 'AIzaSyClvVs5zAQyAUoajVRqYmIUpax1AVbw0vM')
addr=input("write the address???").replace(' ','+')

# Geocoding an address
geocode_result = gmaps.geocode(addr)

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
origin=input("type origin:")
dest=input("type destination:")
directions_result = gmaps.directions(origin,
                                     dest,
                                     mode="transit",
                                     departure_time=now)

print(geocode_result)
print()
print(directions_result.tolist)
