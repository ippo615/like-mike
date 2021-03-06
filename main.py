import json 
import csv
import os
import re
import sys
import threading
import subprocess
import time

import dweepy

from tilt import Tilt

def compute_score( data, dataFilename, thing, axis ):
	#playerFilename = '%s.csv' % thing
	dumpToCsv( data, dataFilename )
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
	push_score( thing, score, '' )
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
			thing,
			'x'
		)
		# TODO: Push score to client
		push_score( thing, score, text )

	#print '%5i: %s' % (
	#	index,
	#	tilt
	#)

def test_round(thing='default-thing'):
	push_score( thing, 2, 'Just getting warmed up' )
	time.sleep(8)
	push_score( thing, 4, 'You could use some practice' )
	time.sleep(4)
	push_score( thing, 8, 'You are getting there' )
	time.sleep(6)
	push_score( thing, 1, 'Try harder' )
	time.sleep(4)
	push_score( thing, 8, 'You are getting there' )
	time.sleep(7)
	push_score( thing, 10, 'You rock like Mike' )
	time.sleep(5)
	push_score( thing, 12, 'OMG!!! You have outperformed Mike' )
	time.sleep(3)
	push_score( thing, 10, 'You rock like Mike' )

def simple_test(thing):
	return compute_score( None, 'data-set2.csv', 'ill-fated-anger', 'x' )

def blah_test():
	print simple_test( 'data-set2' )

if __name__ == '__main__':
	# Wait for a message
	print 'Waiting for start...'
	for dweet in dweepy.listen_for_dweets_from('si-hacks-2015-05-16-blah-start', timeout=10):
		print dweet
		try:
			runner = threading.Thread(
				#target=one_round,
				target=test_round,
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
			'stop':'now'
		} )
		print 'Waiting for another start...'

		#	threading.thread()
		#	run_that_stuff()
