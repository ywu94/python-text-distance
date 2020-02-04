from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
logger = logging.getLogger(__name__)

from collections import Counter

from .input_validator import input_validator

def word_preprocessing(word, ignore_non_alnumspc=True, ignore_space=True, ignore_numeric=True, ignore_case=True):
	"""
	Function for word preprocessing
	|
	| Argument
	| | word: a string to be processed 
	|
	| Parameter
	| | ignore_non_alnumspc: whether to remove all non alpha/numeric/space characters
	| | ignore_space: whether to remove all spaces
	| | ignore_numeric: whether to remove all numeric characters
	| | ignore_case: whether to convert all alpha characters to lower case
	|
	| Output
	| | processed string (type: str)
	"""
	if ignore_non_alnumspc: word = "".join(filter(lambda x: x.isalnum() or x.isspace(), word))
	if ignore_space: word = "".join(filter(lambda x: not x.isspace(), word))
	if ignore_numeric: word = "".join(filter(lambda x: not x.isnumeric(), word))
	if ignore_case: word = word.lower()
	return word

def sentence_preprocessing(sentence, ignore_non_alnumspc=True, ignore_numeric=True, ignore_case=True):
	"""
	Function for sentence preprocessing
	|
	| Argument
	| | sentence: a string to be processed
	|
	| Parameter
	| | ignore_non_alnumspc: whether to remove all non alpha/numeric/space characters
	| | ignore_numeric: whether to remove all numeric characters
	| | ignore_case: whether to convert all alpha characters to lower case
	|
	| Output
	| | list of strings (type: list[str])
	"""
	l_words = sentence.split()
	l_words = list(
		filter(lambda x: x!="", 
			map(lambda x: word_preprocessing(x, 
				ignore_non_alnumspc=ignore_non_alnumspc, 
				ignore_numeric=ignore_numeric, 
				ignore_case=ignore_case,
				ignore_space=False), l_words
			)
		)
	)
	return l_words

def phrase_preprocessing(phrase, grain="char", ignore_non_alnumspc=True, ignore_space=True, ignore_numeric=True, ignore_case=True):
	"""
	Function for preprocessing given phrase
	|
	| Argument
	| | phrase: a string to be processed 
	|
	| Parameter
	| | grain: character or word
	| | ignore_non_alnumspc: whether to remove all non alpha/numeric/space characters
	| | ignore_space: whether to remove all spaces
	| | ignore_numeric: whether to remove all numeric characters
	| | ignore_case: whether to convert all alpha characters to lower case
	|
	| Output
	| | list of strings (type: list[str])
	"""
	assert grain in ("char", "word"), "Illegal grain input: {}".format(grain)
	if grain == "char": 
		return list(word_preprocessing(phrase, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space))
	else:
		return sentence_preprocessing(phrase, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case)

@input_validator(list, n=int)
def ngram_counter(list_of_token, n=2):
	"""
	Function for converting a list of ordered tokens into n-grams.
	| Argument
	| | list_of_token: a list of ordered tokens to be processed.
	| 
	| Parameter
	| | n: number of continuous tokens to group
	|
	| Output
	| | dictionary of count of ngrams (type: collections.Counter)
	"""
	if len(list_of_token) < n: raise Exception("Can't get {}-gram from input of length {}".format(n, len(list_of_token)))
	ngram_cnt = Counter([' '.join(list_of_token[index:index+n]) for index in range(len(list_of_token)-n+1)])
	return ngram_cnt





































