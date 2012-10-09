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
jsonStr['sample']['name'] = "Shubhanshu Mishra" + str(i);
fStr = json.dumps(jsonStr)
with open('response.json', 'w') as f:
		f.write(fStr)
f.closed
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
"""
