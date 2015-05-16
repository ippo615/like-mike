import json
import dateutil.parser

import dweepy

class Dweep( object ):
	def __init__( self, dictionary ):
		self.thing = dictionary['thing']
		self.content = dictionary['content']
		self.created = dateutil.parser.parse( dictionary['created'] )

	def __str__( self ):
		return '%s @ %s:\n%s\n' % (
			self.thing,
			self.created,
			json.dumps(
				self.content,
				separators=(',', ':'),
				indent = 2
			)
		)

for dweep in dweepy.get_dweets_for('pricey-fork'):
	#print dweep
	#print dateutil.parser.parse( dweep['created'] )
	print Dweep( dweep )

