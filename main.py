import json
import csv
import threading

import dweepy

from tilt import Tilt

def one_round(thing='default-thing'):
	samples = []
	index = 0
	for dweet in dweepy.listen_for_dweets_from(thing):
		tilt = Tilt( dweet )
		if tilt.isValid:
			index += 1
			samples.append( tilt )

	print '%5i: %s' % (
		index,
		tilt
	)

if __name__ == '__main__':
	# Wait for a message
	print 'Waiting for start...'
	for dweet in dweepy.listen_for_dweets_from('si-hacks-2015-05-16-blah-start'):
		print dweet
		try:
			runner = threading.Thread(
				target=one_round,
				kwargs=dict(
					thing=dweet['content']['thing']
				)
			)
			runner.start()
			runner.join( 1000 )
		except:
			print 'error'
			raise

		print 'Waiting for another start...'

		#	threading.thread()
		#	run_that_stuff()
