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

	@staticmethod
	def normalizeAngle( angle ):
		return angle

	def __init__( self, dictionary ):
		try:
			self.x = Tilt.normalizeAngle(
				float( dictionary['content']['tilt_x'] )
			)
			self.y = Tilt.normalizeAngle(
				float( dictionary['content']['tilt_y'] )
			)
			self.z = Tilt.normalizeAngle(
				float( dictionary['content']['tilt_z'] )
			)
			self.isValid = True
		except KeyError:
			self.x = 0
			self.y = 0
			self.z = 0
			self.isValid = False
		self.thing = dictionary['thing']
		self.created = dateutil.parser.parse( dictionary['created'] )
		self.content = dictionary['content']

	def as_dict( self ):
		return dict(
			thing = self.thing,
			created = self.created,
			x = self.x,
			y = self.y,
			z = self.z
		)

	def __str__( self ):
		return '% +5.0f, % +5.0f, % +5.0f, %s, %s' % (
			self.x,
			self.y,
			self.z,
			self.created,
			self.thing
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

for t in data:
	print t
