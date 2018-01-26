
# function to capture image with Pi Camera
def capture_image(image_file):
	import picamera
	from time import sleep
	camera = picamera.PiCamera()
	camera.vflip = True
	camera.start_preview(fullscreen=True)
	sleep(5)
	camera.capture(image_file)
	camera.stop_preview()

# calling text-to-speech api of aws polly
def speak_polly(text_utterance):

        # using aws polly for speech synthesis
        call_polly = "aws polly synthesize-speech --voice-id Joanna --output-format mp3 output.mp3 --text \"" + text_utterance + "\""

        # run the command
        import os
        os.system(call_polly)

        # play audio
        os.system("omxplayer -o local output.mp3")


# image recognition code
# takes image file as input and
# returns the list of items recognized in the image
def image_recognition(image_file):

	# import aws boto3 library
	import boto3

	items = []

	# list of labels to be ignored as stop-words
	stoplist = ['Flora', 'Fruit', 'Produce', 'Plant', 'Vegetable', 'Food']

	# calling aws rekognition api on image-file
	client = boto3.client('rekognition')
	with open(image_file, "rb") as image:
		# object recognition from the image
		result = client.detect_labels(Image={'Bytes': image.read()}, MaxLabels=20, MinConfidence=50)
		# processing json output to get image labels
		for label in result['Labels']:
			if label['Name'] not in stoplist:
				items.append(label['Name'])

	return items

image_file = "image.jpg"
capture_image(image_file)
items = image_recognition(image_file)
print items

# creating output text for speech-synthesis
if len(items) == 0:
	speak_polly("Found no items in the fridge.")
else:
	text = "I found following items in the fridge: " + ", ".join(items)
	speak_polly(text)