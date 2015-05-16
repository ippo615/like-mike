import dweepy

thingName = 'ill-fated-anger'

scoreName = '%s-score' % thingName
endName = '%s-end' % thingName

dweepy.dweet_for(
	scoreName, {
	'score': '13'
})
