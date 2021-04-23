# This script outputs all sessions in a given room.
# https://smart.newrow.com/backend/api/analytics/sessions

import requests
from datetime import datetime

page = 0
third_party_room_id = XXXXXX
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8', 'Authorization': 'Bearer INSERT_TOKEN' }

# Print header
print("Session ID,Room Name,Start,End,Participants,Duration")

while True:
    url = 'https://smart.newrow.com/backend/api/analytics/sessions?third_party_room_id=%d&page=%d' % (third_party_room_id, page)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        responseJson = response.json()

        # if you encounter a "year is out of range" error the timestamp
        # may be in milliseconds, try `ts /= 1000` in that case
        # also can use utcfromtimestamp rather than fromtimestamp
                
        # Get data for each session
        for session in responseJson['data']['sessions']:
            startDate = datetime.fromtimestamp(int(session['start_date'])).strftime('%Y-%m-%d %H:%M:%S')
            endDate = datetime.fromtimestamp(int(session['end_date'])).strftime('%Y-%m-%d %H:%M:%S')
            print(u"%s,%s,%s,%s,%s,%s" % (session['id'], session['room_name'], startDate, endDate, session['participants_count'], session['duration']))

        # Check if last page
        if responseJson['data']['next_page'] == "":
            break
        page += 1
