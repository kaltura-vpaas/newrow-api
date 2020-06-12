import requests
import pprint
import urllib.parse
from settings import *

# Pretty printer for json output
pp = pprint.PrettyPrinter(indent=2)

# Set resourceId to default
resourceId = defaultResourceId

# GET /rooms
# https://smart.newrow.com/backend/api/rooms
roomsApiJson = """
{
	"method": "GET",
	"action": "rooms",
	"params": {
	}
}"""
roomsApi = urllib.parse.quote(roomsApiJson)

# Get request url for sessions API call
request = getRequestURL(roomsApi, resourceId)

response = requests.get(request)
if response.status_code ==  200:
    responseJson = response.json()
    print("-------------")
    #print(responseJson)
    pp.pprint(responseJson)
else:
    print("Error! Response status code: : %d" % response.status_code)
