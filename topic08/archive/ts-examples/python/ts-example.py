# importing the requests library 
import requests 

# import random library for "fake" data
import random 

import time

# api-endpoint 
URLprefix = 'https://api.thingspeak.com/update?api_key=<THINGSPEAK_CHANNEL_KEY>&field1='

while True:
    #Get data from sensor(Hardcoded random number)
    temperature = random.randrange(15, 25)

    #Create URL for Thingspeak by concatinating the temperature to URL prefix
    URL = URLprefix + str(temperature)

    # sending get request and saving the response as response object 
    response = requests.get(url = URL) 

    # printing the response from Thingspeak to console 
    print("Response from Thingspeak: "+ response.text) 

    #Sleep for a while
    time.sleep(30)

    