def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words


def sort_words (words):
	"""sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""prints the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""prints the last word after popping it off."""
	word = words.pop(-1)
	return word
def sort_sentence(sentence):
	"""takes a full sentence  and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

