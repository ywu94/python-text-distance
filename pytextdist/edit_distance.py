from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
logger = logging.getLogger(__name__)

from .input_validator import input_validator
from .preprocessing import phrase_preprocessing

@input_validator(str, str)
def levenshtein_distance(phrase_1, phrase_2, grain="char", ignore_non_alnumspc=True, ignore_space=True, ignore_numeric=True, ignore_case=True):
	"""
	Get Levenshtein distance between two text phrases
	|
	| Argument
	| | phrase_1, phrase_2: text phrases to compare
	|
	| Parameter
	| | grain: "char" or "word", grain for edit
	|
	| Parameter for preprocessing
	| | ignore_non_alnumspc: whether to remove all non alpha/numeric/space characters
	| | ignore_space: whether to remove all spaces if grain is character
	| | ignore_numeric: whether to remove all numeric characters
	| | ignore_case: whether to convert all alpha characters to lower case
	|
	| Output
	| | distance (type: int)
	"""
	# Preprocess text phrase into list of edit units
	l_1 = phrase_preprocessing(phrase_1, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	l_2 = phrase_preprocessing(phrase_2, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	len_1, len_2 = len(l_1), len(l_2)

	# Early exit if one of the lists is empty
	if len_1 == 0 or len_2 == 0: return max(len_1,len_2)

	# Dynamic programming solver
	manipulation = [[0 for _ in range(len_2+1)] for _ in range(len_1+1)]
	for row in range(len_1+1): manipulation[row][0] = row
	for col in range(len_2+1): manipulation[0][col] = col

	# Allowed edit: insert, delete, substitute
	for i in range(1,len_1+1):
		for j in range(1, len_2+1):
			cost = 1 if l_1[i-1] != l_2[j-1] else 0
			manipulation[i][j] = min(manipulation[i-1][j-1]+cost, manipulation[i-1][j]+1, manipulation[i][j-1]+1)

	return manipulation[-1][-1]

@input_validator(str, str)
def levenshtein_similarity(phrase_1, phrase_2, grain="char", ignore_non_alnumspc=True, ignore_space=True, ignore_numeric=True, ignore_case=True):
	"""
	Get Levenshtein similarity between two text phrases
	|
	| Formula
	| | 1 - (Levenshtein distance / longest length among two)
	|
	| Argument
	| | phrase_1, phrase_2: text phrases to compare
	|
	| Parameter
	| | grain: "char" or "word", grain for edit
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
	# Preprocess text phrase into list of edit units
	l_1 = phrase_preprocessing(phrase_1, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	l_2 = phrase_preprocessing(phrase_2, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	len_1, len_2 = len(l_1), len(l_2)

	# Early exit if one of the lists is empty
	if len_1 == 0 and len_2 == 0: return 1
	if len_1 == 0 or len_2 == 0: return 0

	# Dynamic programming solver
	manipulation = [[0 for _ in range(len_2+1)] for _ in range(len_1+1)]
	for row in range(len_1+1): manipulation[row][0] = row
	for col in range(len_2+1): manipulation[0][col] = col

	# Allowed edit: insert, delete, substitute
	for i in range(1,len_1+1):
		for j in range(1, len_2+1):
			cost = 1 if l_1[i-1] != l_2[j-1] else 0
			manipulation[i][j] = min(manipulation[i-1][j-1]+cost, manipulation[i-1][j]+1, manipulation[i][j-1]+1)

	similarity = 1 - manipulation[-1][-1]/max(len_1,len_2)

	return similarity

@input_validator(str, str)
def lcs_distance(phrase_1, phrase_2, grain="char", ignore_non_alnumspc=True, ignore_space=True, ignore_numeric=True, ignore_case=True):
	"""
	Get Longest common subsequence distance between two text phrases
	|
	| Argument
	| | phrase_1, phrase_2: text phrases to compare
	|
	| Parameter
	| | grain: "char" or "word", grain for edit
	|
	| Parameter for preprocessing
	| | ignore_non_alnumspc: whether to remove all non alpha/numeric/space characters
	| | ignore_space: whether to remove all spaces if grain is character
	| | ignore_numeric: whether to remove all numeric characters
	| | ignore_case: whether to convert all alpha characters to lower case
	|
	| Output
	| | distance (type: int)
	"""
	# Preprocess text phrase into list of edit units
	l_1 = phrase_preprocessing(phrase_1, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	l_2 = phrase_preprocessing(phrase_2, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	len_1, len_2 = len(l_1), len(l_2)

	# Early exit if one of the lists is empty
	if len_1 == 0 or len_2 == 0: return max(len_1,len_2)

	# Dynamic programming solver
	manipulation = [[0 for _ in range(len_2+1)] for _ in range(len_1+1)]
	for row in range(len_1+1): manipulation[row][0] = 0
	for col in range(len_2+1): manipulation[0][col] = 0

	# Allowed edit: insert, delete
	for i in range(1,len_1+1):
		for j in range(1, len_2+1):
			manipulation[i][j] = manipulation[i-1][j-1] + 1 if l_1[i-1] == l_2[j-1] else max(manipulation[i][j-1], manipulation[i-1][j])

	distance = len_1 + len_2 - 2 * manipulation[-1][-1]

	return distance

@input_validator(str, str)
def lcs_similarity(phrase_1, phrase_2, grain="char", ignore_non_alnumspc=True, ignore_space=True, ignore_numeric=True, ignore_case=True):
	"""
	Get longest common subsequence similarity between two text phrases
	|
	| Formula
	| | 1 - (longest common subsequence / sum of lengths)
	|
	| Argument
	| | phrase_1, phrase_2: text phrases to compare
	|
	| Parameter
	| | grain: "char" or "word", grain for edit
	|
	| Parameter for preprocessing
	| | ignore_non_alnumspc: whether to remove all non alpha/numeric/space characters
	| | ignore_space: whether to remove all spaces if grain is character
	| | ignore_numeric: whether to remove all numeric characters
	| | ignore_case: whether to convert all alpha characters to lower case
	|
	| Output
	| | distance (type: int)
	"""
	# Preprocess text phrase into list of edit units
	l_1 = phrase_preprocessing(phrase_1, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	l_2 = phrase_preprocessing(phrase_2, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	len_1, len_2 = len(l_1), len(l_2)

	# Early exit if one of the lists is empty
	if len_1 == 0 and len_2 == 0: return 1
	if len_1 == 0 or len_2 == 0: return 0

	# Dynamic programming solver
	manipulation = [[0 for _ in range(len_2+1)] for _ in range(len_1+1)]
	for row in range(len_1+1): manipulation[row][0] = 0
	for col in range(len_2+1): manipulation[0][col] = 0

	# Allowed edit: insert, delete
	for i in range(1,len_1+1):
		for j in range(1, len_2+1):
			manipulation[i][j] = manipulation[i-1][j-1] + 1 if l_1[i-1] == l_2[j-1] else max(manipulation[i][j-1], manipulation[i-1][j])

	distance = len_1 + len_2 - 2 * manipulation[-1][-1]

	similarity = 1 - distance/(len_1+len_2)

	return similarity

@input_validator(str, str)
def damerau_levenshtein_distance(phrase_1, phrase_2, grain="char", ignore_non_alnumspc=True, ignore_space=True, ignore_numeric=True, ignore_case=True):
	"""
	Get Damerau-Levenshtein distance between two text phrases
	|
	| Argument
	| | phrase_1, phrase_2: text phrases to compare
	|
	| Parameter
	| | grain: "char" or "word", grain for edit
	|
	| Parameter for preprocessing
	| | ignore_non_alnumspc: whether to remove all non alpha/numeric/space characters
	| | ignore_space: whether to remove all spaces if grain is character
	| | ignore_numeric: whether to remove all numeric characters
	| | ignore_case: whether to convert all alpha characters to lower case
	|
	| Output
	| | distance (type: int)
	"""
	# Preprocess text phrase into list of edit units
	l_1 = phrase_preprocessing(phrase_1, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	l_2 = phrase_preprocessing(phrase_2, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	len_1, len_2 = len(l_1), len(l_2)

	# Early exit if one of the lists is empty
	if len_1 == 0 or len_2 == 0: return max(len_1,len_2)

	# Dynamic programming solver
	manipulation = [[0 for _ in range(len_2+1)] for _ in range(len_1+1)]
	for row in range(len_1+1): manipulation[row][0] = row
	for col in range(len_2+1): manipulation[0][col] = col

	# Allowed edit: insert, delete, substitute, transpose of adjacent characters
	for i in range(1,len_1+1):
		for j in range(1, len_2+1):
			cost_1 = 1 if l_1[i-1] != l_2[j-1] else 0
			if i >= 2 and j >= 2:
				cost_2 = 1 if l_1[i-2] == l_2[j-1] and l_1[i-1] == l_2[j-2] else 9527
				manipulation[i][j] = min(manipulation[i-1][j-1]+cost_1, manipulation[i-2][j-2]+cost_2, manipulation[i-1][j]+1, manipulation[i][j-1]+1)
			else:
				manipulation[i][j] = min(manipulation[i-1][j-1]+cost_1, manipulation[i-1][j]+1, manipulation[i][j-1]+1)

	return manipulation[-1][-1]

@input_validator(str, str)
def damerau_levenshtein_similarity(phrase_1, phrase_2, grain="char", ignore_non_alnumspc=True, ignore_space=True, ignore_numeric=True, ignore_case=True):
	"""
	Get Damerau-Levenshtein similarity between two text phrases
	|
	| Formula
	| | 1 - (Levenshtein distance / longest length among two)
	|
	| Argument
	| | phrase_1, phrase_2: text phrases to compare
	|
	| Parameter
	| | grain: "char" or "word", grain for edit
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
	# Preprocess text phrase into list of edit units
	l_1 = phrase_preprocessing(phrase_1, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	l_2 = phrase_preprocessing(phrase_2, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	len_1, len_2 = len(l_1), len(l_2)

	# Early exit if one of the lists is empty
	if len_1 == 0 and len_2 == 0: return 1
	if len_1 == 0 or len_2 == 0: return 0

	# Dynamic programming solver
	manipulation = [[0 for _ in range(len_2+1)] for _ in range(len_1+1)]
	for row in range(len_1+1): manipulation[row][0] = row
	for col in range(len_2+1): manipulation[0][col] = col

	# Allowed edit: insert, delete, substitute, transpose of adjacent characters
	for i in range(1,len_1+1):
		for j in range(1, len_2+1):
			cost_1 = 1 if l_1[i-1] != l_2[j-1] else 0
			if i >= 2 and j >= 2:
				cost_2 = 1 if l_1[i-2] == l_2[j-1] and l_1[i-1] == l_2[j-2] else 9527
				manipulation[i][j] = min(manipulation[i-1][j-1]+cost_1, manipulation[i-2][j-2]+cost_2, manipulation[i-1][j]+1, manipulation[i][j-1]+1)
			else:
				manipulation[i][j] = min(manipulation[i-1][j-1]+cost_1, manipulation[i-1][j]+1, manipulation[i][j-1]+1)

	similarity = 1 - manipulation[-1][-1]/max(len_1,len_2)
	
	return similarity

@input_validator(str, str)
def jaro_similarity(phrase_1, phrase_2, grain="char", ignore_non_alnumspc=True, ignore_space=True, ignore_numeric=True, ignore_case=True):
	"""
	Get Jaro similarity between two text phrases
	|
	| Argument
	| | phrase_1, phrase_2: text phrases to compare
	|
	| Parameter
	| | grain: "char" or "word", grain for edit
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
	# Preprocess text phrase into list of edit units
	l_1 = phrase_preprocessing(phrase_1, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	l_2 = phrase_preprocessing(phrase_2, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	len_1, len_2 = len(l_1), len(l_2)

	# Early exit if one of the lists is empty
	if len_1 == 0 and len_2 == 0: return 1
	if len_1 == 0 or len_2 == 0: return 0

	# Search for match
	search_step = max(max(len_1, len_2)//2-1, 0)
	match_cnt = 0
	available_1, available_2 = [True for _ in range(len_1)], [True for _ in range(len_2)]
	match_1, match_2 = [], []
	for index_1, char_1 in enumerate(l_1):
		for index_2 in range(max(index_1-search_step, 0), min(index_1+search_step+1, len_2)):
			if char_1 == l_2[index_2]:
				if available_1[index_1] and available_2[index_2]:
					match_cnt += 1
					available_1[index_1], available_2[index_2] = False, False
					match_1.append(index_1)
					match_2.append(index_2)

	# Early exit if there's no match
	if match_cnt == 0: return 0

	# Find transpose
	match_str_1 = [l_1[i] for i in sorted(match_1)]
	match_str_2 = [l_2[i] for i in sorted(match_2)]
	transpose_cnt = sum([1 for a, b in zip(match_str_1, match_str_2) if a != b])/2

	similarity = (match_cnt/len_1 + match_cnt/len_2 + (match_cnt-transpose_cnt)/match_cnt)/3

	return similarity

@input_validator(str, str, p=float)
def jaro_winkler_similarity(phrase_1, phrase_2, p=0.1, grain="char", ignore_non_alnumspc=True, ignore_space=True, ignore_numeric=True, ignore_case=True):
	"""
	Get Jaro-Winkler similarity between two text phrases
	|
	| Argument
	| | phrase_1, phrase_2: text phrases to compare
	|
	| Parameter
	| | p: constant scaling factor, should not exceed 0.25
	| | grain: "char" or "word", grain for edit
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
	assert 0 < p < 0.25, "".format(p)

	# Preprocess text phrase into list of edit units
	l_1 = phrase_preprocessing(phrase_1, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	l_2 = phrase_preprocessing(phrase_2, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	len_1, len_2 = len(l_1), len(l_2)

	# Early exit if one of the lists is empty
	if len_1 == 0 and len_2 == 0: return 1
	if len_1 == 0 or len_2 == 0: return 0
	
	# Search for match
	search_step = max(max(len_1, len_2)//2-1, 0)
	match_cnt = 0
	available_1, available_2 = [True for _ in range(len_1)], [True for _ in range(len_2)]
	match_1, match_2 = [], []
	for index_1, char_1 in enumerate(l_1):
		for index_2 in range(max(index_1-search_step, 0), min(index_1+search_step+1, len_2)):
			if char_1 == l_2[index_2]:
				if available_1[index_1] and available_2[index_2]:
					match_cnt += 1
					available_1[index_1], available_2[index_2] = False, False
					match_1.append(index_1)
					match_2.append(index_2)

	# Early exit if there's no match
	if match_cnt == 0: return 0

	# Find transpose
	match_str_1 = [l_1[i] for i in sorted(match_1)]
	match_str_2 = [l_2[i] for i in sorted(match_2)]
	transpose_cnt = sum([1 for a, b in zip(match_str_1, match_str_2) if a != b])/2

	# Calculate Jaro similarity
	jaro_similarity = (match_cnt/len_1 + match_cnt/len_2 + (match_cnt-transpose_cnt)/match_cnt)/3

	# Find common prefix
	l_common_prefix, index = 0, 0
	while l_common_prefix < 5 and index < len_1 and index < len_2:
		if l_1[index] != l_2[index]: break
		l_common_prefix += 1
		index += 1

	similarity = jaro_similarity + l_common_prefix*p*(1-jaro_similarity)

	return similarity

@input_validator(str, str)
def hamming_distance(phrase_1, phrase_2, grain="char", ignore_non_alnumspc=True, ignore_space=True, ignore_numeric=True, ignore_case=True):
	"""
	Get Hamming distance between two text phrases
	|
	| Argument
	| | phrase_1, phrase_2: text phrases to compare
	|
	| Parameter
	| | grain: "char" or "word", grain for edit
	|
	| Parameter for preprocessing
	| | ignore_non_alnumspc: whether to remove all non alpha/numeric/space characters
	| | ignore_space: whether to remove all spaces if grain is character
	| | ignore_numeric: whether to remove all numeric characters
	| | ignore_case: whether to convert all alpha characters to lower case
	|
	| Output
	| | distance (type: int)
	"""
	# Preprocess text phrase into list of edit units
	l_1 = phrase_preprocessing(phrase_1, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	l_2 = phrase_preprocessing(phrase_2, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	len_1, len_2 = len(l_1), len(l_2)

	# Early exit if one of the lists is empty
	if len_1 == 0 or len_2 == 0: return max(len_1,len_2)

	# Raise exception two lists have different length
	if len_1 != len_2: raise Exception("Can't calculate hamming distance between phrases of different lengths")

	# Calculate hamming distance
	distance = 0
	for x, y in zip(l_1, l_2): distance += (1 if x != y else 0)

	return distance

@input_validator(str, str)
def hamming_similarity(phrase_1, phrase_2, grain="char", ignore_non_alnumspc=True, ignore_space=True, ignore_numeric=True, ignore_case=True):
	"""
	Get Hamming similarity between two text phrases
	|
	| Formula
	| | 1 - (Hamming distance / longest length among two)
	|
	| Argument
	| | phrase_1, phrase_2: text phrases to compare
	|
	| Parameter
	| | grain: "char" or "word", grain for edit
	|
	| Parameter for preprocessing
	| | ignore_non_alnumspc: whether to remove all non alpha/numeric/space characters
	| | ignore_space: whether to remove all spaces if grain is character
	| | ignore_numeric: whether to remove all numeric characters
	| | ignore_case: whether to convert all alpha characters to lower case
	|
	| Output
	| | distance (type: int)
	"""
	# Preprocess text phrase into list of edit units
	l_1 = phrase_preprocessing(phrase_1, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	l_2 = phrase_preprocessing(phrase_2, grain=grain, ignore_non_alnumspc=ignore_non_alnumspc, ignore_numeric=ignore_numeric, ignore_case=ignore_case, ignore_space=ignore_space)
	len_1, len_2 = len(l_1), len(l_2)

	# Early exit if one of the lists is empty
	if len_1 == 0 and len_2 == 0: return 1
	if len_1 == 0 or len_2 == 0: return 0

	# Raise exception two lists have different length
	if len_1 != len_2: raise Exception("Can't calculate hamming distance between phrases of different lengths")

	# Calculate hamming distance
	distance = 0
	for x, y in zip(l_1, l_2): distance += (1 if x != y else 0)

	similarity = 1 - distance/len_1

	return similarity
