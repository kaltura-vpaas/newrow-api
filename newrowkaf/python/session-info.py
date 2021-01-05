import requests
import pprint
import sys
import urllib.parse
from settings import *

# Pretty printer for json output
pp = pprint.PrettyPrinter(indent=2)

# Set resourceId
if len(sys.argv) > 1:
    resourceId = sys.argv[1]
else:
    resourceId = defaultResourceId

#####################################################################
# GET LIST OF ALL SESSIONS IN THE RESOURCE ID
#   GET /analytics/sessions
#   https://smart.newrow.com/backend/api/analytics/sessions
#   *** No params needed since passing resourceId and filtering by it.
#####################################################################
sessionsApiJson = """
{
	"method": "GET",
	"action": "analytics/sessions",
	"params": { }
}"""
sessionsApi = urllib.parse.quote(sessionsApiJson)

# Get request url for sessions API call
sessionsRequest = getRequestURL(sessionsApi, resourceId)

# Make sessions request
sessionsResponse = requests.get(sessionsRequest)
if sessionsResponse.status_code == 200:
    sessionsResponseJson = sessionsResponse.json()
    #print(sessionsResponseJson)

    # TODO: need to account for pagination; currently assuming that 'total_count'
    # accounts for all sessions in one page of results, which is often not the case.
    print("--------------------------------------")
    print("| Last session in resourceId %s |" % resourceId)
    print("--------------------------------------")
    numSessions = sessionsResponseJson['data']['total_count']
    pp.pprint(sessionsResponseJson['data']['sessions'][numSessions - 1])
    sessionId = sessionsResponseJson['data']['sessions'][numSessions - 1]['id']

    #####################################################################
    # GET INFO ABOUT EACH PARTICIPANT IN THE SESSION
    #   GET /analytics/session-attendees
    #   https://smart.newrow.com/backend/api/analytics/session-attendees
    #   *** populate session_id with valid value (this is a newrow session Id)
    #####################################################################
    attendeesApiJson = """
    {
	    "method": "GET",
	    "action": "analytics/session-attendees",
	    "params": {
            "session_id": %s
	    }
    }""" % sessionId

    attendeesApi = urllib.parse.quote(attendeesApiJson)

    # Get request url for session-attendees API call
    attendeesRequest = getRequestURL(attendeesApi, resourceId)

    # Make session-attendees request
    attendeesResponse = requests.get(attendeesRequest)
    if attendeesResponse.status_code == 200:
        attendeesResponseJson = attendeesResponse.json()

        print("\n--------------------------------------")
        print("| Session attendees (count = %d)      |" % attendeesResponseJson['data']['total_count'])
        print("--------------------------------------")
        #print(attendeesResponseJson)
        #pp.pprint(attendeesResponseJson['data']['session_attendance'])

        # Get data for each participant in the session
        for participant in attendeesResponseJson['data']['session_attendance']:
            #####################################################################
            # GET MORE DATA ABOUT THE USER
            #   GET /users/<id>
            #   https://smart.newrow.com/backend/api/users/<id>
            #####################################################################
            usersApiJson = """
            {
	            "method": "GET",
	            "action": "users/%s",
	            "params": { }
            }""" % participant['user_id']
            usersApi = urllib.parse.quote(usersApiJson)

            # Get request url for this API call
            usersRequest = getRequestURL(usersApi, resourceId)

            # Make users request
            usersResponse = requests.get(usersRequest)
            if usersResponse.status_code == 200:
                usersResponseJson = usersResponse.json()

                # First print data from session-attendees API, then from user API
                print("\n--------------------------------------")
                print("%s" % participant['user_name'])
                print("--------------------------------------")
                pp.pprint(participant)
                print("")
                print("More user info:")
                pp.pprint(usersResponseJson['data'])
            else:
                print("Error! Users response status code: : %d" % sessionsResponse.status_code)
            print("--------------------------------------")
    else:
        print("Error! Session attendees response status code: : %d" % sessionsResponse.status_code)

else:
    print("Error! Sessions response status code: : %d" % sessionsResponse.status_code)

print("")
