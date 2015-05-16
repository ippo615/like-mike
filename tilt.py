import dateutil.parser

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
