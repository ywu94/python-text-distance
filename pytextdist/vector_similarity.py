from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import logging
logger = logging.getLogger(__name__)

from .input_validator import input_validator
from .preprocessing import phrase_preprocessing, ngram_counter

@input_validator(str, str, n=int)
def cosine_similarity(phrase_1, phrase_2, n=1, grain="word", ignore_non_alnumspc=True, ignore_space=True, ignore_numeric=True, ignore_case=True):
	"""
	Get cosine similarity between two text phrases
	|
	| Argument
	| | phrase_1, phrase_2: text phrases to compare
	|
	| Parameter
	| | n: number of continuous tokens to group
	| | grain: "char" or "word", grain for building vector
	|
	| Parameter for preprocessing
	| | ignore_non_alnumspc: whether to remove all non alpha/numeric/space characters
	| | ignore_space: whether to remove all spaces if grain is character
	| | ignore_numeric: whether to remove all numeric characters
	| | ignore_case: whether to convert all alpha characters to lower case
	|
	| Output
	| | similarity (type: float)
	"""
	l_1 = phrase_preprocessing(phrase_1, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	counter_1 = ngram_counter(l_1, n=n)
	l_2 = phrase_preprocessing(phrase_2, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	counter_2 = ngram_counter(l_2, n=n)

	numerator = sum([counter_1[x] * counter_2[x] for x in set(counter_1.keys()) & set(counter_2.keys())])
	denominator = math.sqrt(sum([v**2 for v in counter_1.values()])) * math.sqrt(sum([v**2 for v in counter_2.values()]))
	similarity = numerator/denominator

	return similarity

@input_validator(str, str, n=int)
def jaccard_similarity(phrase_1, phrase_2, n=1, grain="word", ignore_non_alnumspc=True, ignore_space=True, ignore_numeric=True, ignore_case=True):
	"""
	Get jaccard similarity between two text phrases
	|
	| Argument
	| | phrase_1, phrase_2: text phrases to compare
	|
	| Parameter
	| | n: number of continuous tokens to group
	| | grain: "char" or "word", grain for building vector
	|
	| Parameter for preprocessing
	| | ignore_non_alnumspc: whether to remove all non alpha/numeric/space characters
	| | ignore_space: whether to remove all spaces if grain is character
	| | ignore_numeric: whether to remove all numeric characters
	| | ignore_case: whether to convert all alpha characters to lower case
	|
	| Output
	| | similarity (type: float)
	"""
	l_1 = phrase_preprocessing(phrase_1, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	counter_1 = ngram_counter(l_1, n=n)
	unique_token_1 = set(counter_1.keys())
	l_2 = phrase_preprocessing(phrase_2, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	counter_2 = ngram_counter(l_2, n=n)
	unique_token_2 = set(counter_2.keys())

	numerator = len(unique_token_1 & unique_token_2)
	denominator = len(unique_token_1 | unique_token_2)
	similarity = numerator/denominator

	return similarity

@input_validator(str, str, n=int)
def sorensen_dice_similarity(phrase_1, phrase_2, n=1, grain="word", ignore_non_alnumspc=True, ignore_space=True, ignore_numeric=True, ignore_case=True):
	"""
	Get Sorense Dice similarity between two text phrases
	|
	| Argument
	| | phrase_1, phrase_2: text phrases to compare
	|
	| Parameter
	| | n: number of continuous tokens to group
	| | grain: "char" or "word", grain for building vector
	|
	| Parameter for preprocessing
	| | ignore_non_alnumspc: whether to remove all non alpha/numeric/space characters
	| | ignore_space: whether to remove all spaces if grain is character
	| | ignore_numeric: whether to remove all numeric characters
	| | ignore_case: whether to convert all alpha characters to lower case
	|
	| Output
	| | similarity (type: float)
	"""
	l_1 = phrase_preprocessing(phrase_1, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	counter_1 = ngram_counter(l_1, n=n)
	unique_token_1 = set(counter_1.keys())
	l_2 = phrase_preprocessing(phrase_2, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	counter_2 = ngram_counter(l_2, n=n)
	unique_token_2 = set(counter_2.keys())

	numerator = 2 * len(unique_token_1 & unique_token_2)
	denominator = len(unique_token_1) + len(unique_token_2)
	similarity = numerator/denominator

	return similarity

@input_validator(str, str, n=int)
def qgram_similarity(phrase_1, phrase_2, n=1, grain="word", ignore_non_alnumspc=True, ignore_space=True, ignore_numeric=True, ignore_case=True):
	"""
	Get Q-Gram similarity between two text phrases
	|
	| Argument
	| | phrase_1, phrase_2: text phrases to compare
	|
	| Parameter
	| | n: number of continuous tokens to group
	| | grain: "char" or "word", grain for building vector
	|
	| Parameter for preprocessing
	| | ignore_non_alnumspc: whether to remove all non alpha/numeric/space characters
	| | ignore_space: whether to remove all spaces if grain is character
	| | ignore_numeric: whether to remove all numeric characters
	| | ignore_case: whether to convert all alpha characters to lower case
	|
	| Output
	| | similarity (type: float)
	"""
	l_1 = phrase_preprocessing(phrase_1, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	counter_1 = ngram_counter(l_1, n=n)
	l_2 = phrase_preprocessing(phrase_2, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	counter_2 = ngram_counter(l_2, n=n)

	numerator = sum([abs(counter_1.get(key,0)-counter_2.get(key,0)) for key in set(counter_1.keys())|set(counter_2.keys())])
	denominator = sum([max(counter_1.get(key,0), counter_2.get(key,0)) for key in set(counter_1.keys())|set(counter_2.keys())])
	similarity = 1 -  numerator/denominator

	return similarity

















