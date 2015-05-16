import dweepy

from tilt import Tilt

thingName = 'opposite-test'

samples = []
index = 0
for dweet in dweepy.listen_for_dweets_from(thingName):
	tilt = Tilt( dweet )
	if tilt.isValid:
		index += 1
		samples.append( tilt )

	print '%5i: %s' % (
		index,
		tilt
	)
