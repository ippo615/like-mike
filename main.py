import json
import csv

import dweepy

from tilt import Tilt

thingName = 'ill-fated-anger'
eventPostfix = 'events'

eventName = '%s-%s' % (
	thingName,
	eventPostfix
)

# Some orientation guidelines (note +-180 is close to +- 0):
# upsidedown: 86.0, 2.0, 50.0
# upright: -86.0, 2.0, 70.0
# flat (screen up): -4.0, 2.0, 260.0
# flat (screen down): 179.0, -3.0, 300.0
# rightside down: -4.0, -83.0, 26.0
# leftside down: -179.0, 88.0, 296.0

#dweepy.dweet_for(
#	eventName, {
#	'major_thingy': 'start'
#})

data = []
for dweep in reversed(dweepy.get_dweets_for(thingName)):
	#print dweep
	#print dateutil.parser.parse( dweep['created'] )
	tilt = Tilt( dweep )
	if tilt.isValid:
		data.append( tilt )

	#if 'major_thingy' in d.content:
	#	print d.content['major_thingy']

for row in data:
	print row

def dumpToCsv(data):
	with open('data.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, 'x,y,z,created,thing'.split(','))
		writer.writeheader()
		for row in data:
			writer.writerow( row.as_dict() )
