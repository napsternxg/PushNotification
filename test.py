import json
import time

jsonStr = {
	"sample": {
		"name": "Shubhanshu Mishra",
	 	"networks": [
				"facebook",
				"twitter",
				"linkedin"
	 	]
	}
}

i = 0

"""
	The block of code below works properly on the Node Server without crashing it.
	You need to invoke this script each time to make it edit response.json file
"""

jsonStr['sample']['name'] = "Shubhanshu Mishra" + str(i);
fStr = json.dumps(jsonStr)
with open('response.json', 'w') as f:
		f.write(fStr)
f.closed

"""
	UnComment all the lines below to make this test program edit the response.json file, but it crashes the Node Server
	Keep it commented if you want to use it as test. Uncomment the block above this comment.
"""


while True:
	i += 100
	print i
	jsonStr['sample']['name'] = "Shubhanshu Mishra" + str(i);
	fStr = json.dumps(jsonStr)
	#f = open("response.json", "w")
	with open('response.json', 'w') as f:
		f.write(fStr)
	f.closed
	#f.write(fStr)
	print "Written to file: " + fStr
	#f.close()
	time.sleep(5)

