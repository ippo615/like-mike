import json 
import csv
import os
import re
import sys
import threading
import subprocess

import dweepy

from tilt import Tilt

def compute_score( data, dataFilename, thing, axis ):
	#playerFilename = '%s.csv' % thing
	#dumpToCsv( data, playerFilename )
	subprocess.call( [
		'python',
		'clean_data.py',
		dataFilename,
		axis
	] )
	return load_score_compare( '%s_total.csv' % thing )

def load_score_compare( scoreFilename ):
	# return the last row of data
	with open( scoreFilename ) as f:
		reader = csv.DictReader( f )
		lastRow = None
		for row in reader:
			lastRow = row
		return (
			lastRow['likemike'],
			lastRow['likemike_comment']
		)

def dumpToCsv(data,filename):
	with open(filename, 'w') as csvfile:
		writer = csv.DictWriter(csvfile, 'x,y,z,created,thing'.split(','))
		writer.writeheader()
		for row in data:
			writer.writerow( row.as_dict() )


def push_score( thing, score, text ):
	dweepy.dweet_for(
		'%s-score' % thing, {
			'score': score,
			'text': text
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
		(score,text) = compute_score(
			samples,
			'%s-data.csv' % thing,
			'%s-data-combined.csv' % thing
		)
		# TODO: Push score to client
		push_score( thing, score, text )

	#print '%5i: %s' % (
	#	index,
	#	tilt
	#)

def simple_test(thing):
	return compute_score( None, 'data-set2.csv', 'ill-fated-anger', 'x' )

if __name__ == '__main__':
	# Wait for a message
	print simple_test( 'data-set2' )

def blah():
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


