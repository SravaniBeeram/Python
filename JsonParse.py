import json
import urllib

data = urllib.urlopen(raw_input("enter url:")).read()

info = json.loads(data)
test = info["comments"]
print 'User count:', len(test)
sum = 0
for item in test:
    sum = sum + item["count"]
print sum	
	
