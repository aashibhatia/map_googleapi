import urllib3.request
import json
end='https://maps.googleapis.com/maps/api/distancematrix/json?'
api='AIzaSyClvVs5zAQyAUoajVRqYmIUpax1AVbw0vM'
origin= input('place where you are?').replace('','+')
dest=input('place you want to reach').replace('','+')
nav_request='origins={}&destinations={}&key={}'.format(origin,dest,api)
_url=end+nav_request
http=urllib3.PoolManager()
response=http.request('GET',_url).read()
print(response)
direction= json.loads(response)

print(direction)



