# This script outputs all rooms of a Newrow account.
# It implements the GET /rooms API.
# https://smart.newrow.com/backend/api/rooms/

import requests

third_party_id = "1_d6iwjn08" # can be resource ID or meeting entry I
page = 0
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8', 'Authorization': 'Bearer XXXX' }
chatType = "moderators" # questions, public, moderators

while True:
    url = 'https://smart.newrow.com/backend/api/analytics/room-messages?third_party_room_id=%s&type=%s&page=%d' % (third_party_id, chatType, page)
    roomMessagesResponse = requests.get(url, headers=headers)
    if roomMessagesResponse.status_code == 200:
        roomMessagesResponseJson = roomMessagesResponse.json()
        #print roomsResponseJson['data']['next_page']
        #print roomsResponseJson['data']['total_count']
                
        for roomMessage in roomMessagesResponseJson['data']['messages']:
            #print("Got a room message")
            print(u"%s: %s" % (roomMessage['third_party_user_id'], roomMessage['message']))

        # Check if last page
        if roomMessagesResponseJson['data']['next_page'] == None:
            break
        page += 1
