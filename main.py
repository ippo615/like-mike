import json
import csv
import threading

import dweepy

from tilt import Tilt

def push_score( thing, score ):
	dweepy.dweet_for(
		'%s-score' % thing, {
			'score': score
		}
	)

def one_round(thing='default-thing'):
	score = 0
	push_score( thing, score )
	samples = []
	index = 0
	for dweet in dweepy.listen_for_dweets_from(thing):
		tilt = Tilt( dweet )
		if tilt.isValid:
			index += 1
			samples.append( tilt )

		# TODO: Compute score
		# TODO: Push score to client
		# push_score( thing, score )

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
			runner.join( 1*60 ) # limit the round to 1 minute
		except:
			print 'error'
			raise

		# Tell the server that the game is over
		dweepy.dweet_for( 'si-hacks-2015-05-16-blah-end', {
			'stop':'now',
			'score':score
		} )
		print 'Waiting for another start...'

		#	threading.thread()
		#	run_that_stuff()


