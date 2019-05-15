#! python

import requests
import webbrowser

# SpaceX API:
# https://api.spacexdata.com/v3/launches/latest

spacex_url = 'https://api.spacexdata.com/v3/launches/latest'
response = requests.get(spacex_url)
response = response.json()

# What is the mission name?
print('The latest mission name is: ' + response['mission_name'])

# What is the local launch date?
print('The local launch date is: ' + response['launch_date_local'])

# What is the rocket name?
print('The rocket name is: ' + response['rocket']['rocket_name'])

# tell the user, "PRESS ENTER TO ACCESS"
input('\nPRESS ENTER TO ACCESS A VIDEO LINK\n')

# open a link in browser webbrowser.open()
webbrowser.open(response['links']['video_link'])
