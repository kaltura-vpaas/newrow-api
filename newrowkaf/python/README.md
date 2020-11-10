# newrow-api/newrowkaf/python
Python scripts to run Newrow APIs via newrowkaf.

## Setup
1. Use python 3.x
1. Get KalturaClient python client library: pip install KalturaApiClient
1. Populate the values at the top of *settings.py* that are specific to your Kaltura account.

## Run
1. rooms.py: get a list of all resourceIds in your Kaltura account
2. session-info.py: pass a resourceId argument to get info about the last session that took place in this resource
