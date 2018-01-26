
# function to get current local time
def get_time():
	# importing python libraries to capture date and time
	from time import asctime, localtime, time

	# get current local time
	current_time = asctime(localtime(time()))

	# parse the string to get the hr and mins
	[day, month, date, time_stamp, year] = current_time.split(" ")
	[hr, mins, secs] = time_stamp.split(":")

	utterance = "Current Time is " + hr + " " + mins
	return utterance

# calling text to speech api of aws polly
def speak_polly(text_utterance):
	# using aws polly for speech synthesis
	call_polly = "aws polly synthesize-speech --voice-id Joanna --output-format mp3 output.mp3 --text \"" + text_utterance + "\""

	# run the command
	import os
	os.system(call_polly)

	# play audio
	os.system("omxplayer -o local output.mp3")

# calling festival for text to speech
def speak_festival(text_utterance):
	import os
	call_fest = "echo \"" + text_utterance + "\" | festival --tts"
	os.system(call_fest)

# gets the weather data from Open Weather Map
def get_weather(city):
	import urllib2
	import json

	# api-key for open weather map
	API_KEY = open("weather-api.key").read()
	web_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&APPID=" + API_KEY
	weather_data = urllib2.urlopen(web_url).read()
	weather = json.loads(weather_data)

	utterance = "Outside Temperature is " + str(weather['main']['temp']) + " degree celsius"
	return utterance

import time
while(1):
	# tell the current time
	tell_time = get_time()
	speak_polly(tell_time)

	# tell the current temperature
	tell_weather = get_weather("bangalore,india")
	speak_polly(tell_weather)

	# set timer 
	time.sleep(1800)
