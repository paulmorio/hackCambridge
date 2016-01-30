
# To surpress the annoying warnings for duration of hackathon
import urllib3
urllib3.disable_warnings()
import sys

# Connecting to the hod client.
from havenondemand.hodindex import HODClient
client = HODClient(apikey='f8a8a049-4a76-4145-8ba5-a0a28eabd5cd', apiversiondefault=1)

for line in file('whatsapp.txt'):
	line = line.strip("\n")
	a, b, text = line.split(":", 2)
	b = b[5:]
	print text

	data = {'text': text}

	r = client.post('analyzesentiment', data)
	sentiment = r.json()['aggregate']['sentiment']
	score = r.json()['aggregate']['score']
	print(text + " | " + sentiment + " | " + str(score))
