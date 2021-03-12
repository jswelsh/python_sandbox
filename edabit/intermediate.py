def stuttering_function(word):
	stutter_word = word[0:2]
	return stutter_word + '... ' + word[0:2] + '... ' + word + '?'
print('in...in...increasing?', ':', stuttering_function('increasing'))
