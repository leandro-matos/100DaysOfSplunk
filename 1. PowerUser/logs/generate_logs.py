import random
import json
import logging
import sys
import os
import time

from datetime import datetime
def commitCrime():

	# list of sample values
	suspects = ['Miss Scarett','Professor Plum','Miss Peacock','Mr. Green','Colonel Mustard','Mrs. White', 'Mr. Red', 'Mr. Gates']
	weapons = ['candlestick','knife','lead pipe','revolver','rope','wrench','splunk']
	rooms = ['kitchen','ballroom','conservatory','dining room','cellar','billiard room','library','lounge','hall','study','swimming pool']
	curr_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
	return {"timestamp":curr_time,"killer":random.choice(suspects), "weapon":random.choice(weapons), "location":random.choice(rooms), "victim":"Mr Boddy"}
	
# Para windows e linux usar o path sempre com a “/”
path= "G:/2. splunk/100DaysOfSplunk/1. PowerUser/logs/generate.log"

# filetxt = open(path, 'w')
# read = filetxt.read()
# print(read)

for i in range(10000):
	filetxt = open(path, 'a')
	event = commitCrime()
	event.update({"action":"success"})
	event.update({"crime_type":"single"})
	event.update({"crime_number":i})
	filetxt.write(json.dumps(event))
	filetxt.write("\n")
filetxt.close()
