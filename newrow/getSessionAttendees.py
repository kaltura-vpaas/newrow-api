# This script outputs all attendees and their data of a given Newrow session.
# https://smart.newrow.com/backend/api/anaytics/session-attendees

import requests
from datetime import datetime

page = 0

# IMPORTANT: populate the following two values accordingly
session_id = XXXXX
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8', 'Authorization': 'Bearer INSERT_TOKEN' }

# Print header
print("User ID,User Name,User Email, Lti Email,Lti User ID,Time Joined, Time Left,Duration,Attention")

while True:
    url = 'https://smart.newrow.com/backend/api/analytics/session-attendees?session_id=%d&include_third_party_data=1&page=%d' % (session_id, page)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        responseJson = response.json()

        # if you encounter a "year is out of range" error the timestamp
        # may be in milliseconds, try `ts /= 1000` in that case
        # also can use utcfromtimestamp rather than fromtimestamp
                
        # Get data for each session
        for attendees in responseJson['data']['session_attendance']:
            timeJoined = datetime.fromtimestamp(int(attendees['time_joined'])).strftime('%Y-%m-%d %H:%M:%S')
            timeLeft   = datetime.fromtimestamp(int(attendees['time_left'])).strftime('%Y-%m-%d %H:%M:%S')
            print(u"%s,%s,%s,%s,%s,%s,%s,%s,%s" % (attendees['user_id'], attendees['user_name'], attendees['user_email'], attendees['lti_user_email'], attendees['lti_user_id'], timeJoined, timeLeft, attendees['duration'], attendees['attention']))

        # Check if last page
        if responseJson['data']['next_page'] == "":
            break
        page += 1
