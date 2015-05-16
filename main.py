import json
import dateutil.parser

import dweepy

thingName = 'tight-respect'
eventPostfix = 'events'

eventName = '%s-%s' % (
	thingName,
	eventPostfix
)

class Tilt( object ):
	def __init__( self, dictionary ):
		self.thing = dictionary['thing']
		try:
			self.x = float( dictionary['content']['tilt_x'] )
			self.y = float( dictionary['content']['tilt_y'] )
			self.z = float( dictionary['content']['tilt_z'] )
			self.isValid = True
		except KeyError:
			self.x = 0
			self.y = 0
			self.z = 0
			self.isValid = False
		self.content = dictionary['content']
		self.created = dateutil.parser.parse( dictionary['created'] )

	def __str__( self ):
		return '%s, %s, %s' % (
			self.x,
			self.y,
			self.z
		)

#dweepy.dweet_for(
#	eventName, {
#	'major_thingy': 'start'
#})

for dweep in reversed(dweepy.get_dweets_for(thingName)):
	#print dweep
	#print dateutil.parser.parse( dweep['created'] )
	d = Tilt( dweep )
	if d.isValid:
		print d 

	#if 'major_thingy' in d.content:
	#	print d.content['major_thingy']
