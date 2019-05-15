#! python

import requests
import webbrowser

# SpaceX API:
# https://api.spacexdata.com/v3/launches/latest

spacex_url = 'https://api.spacexdata.com/v3/launches/latest'
response = requests.get(spacex_url)
response = response.json()
# mission name
print('The mission name is: ' + response['mission_name'])
# launch date local
print('The local launch date is: ' + response['launch_date_local'])
# 1 other piece of info
print('The rocket name is: ' + response['rocket']['rocket_name'])
# tell the user, "PRESS ENTER TO ACCESS"
video_link = input('PRESS ENTER TO ACCESS A VIDEO LINK')
#print(response['links']['video_link'])
# open a link in browser webbrowser.open()
webbrowser.open(response['links']['video_link'])
