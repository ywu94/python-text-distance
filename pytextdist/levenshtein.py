from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
logger = logging.getLogger(__name__)

def levenshtein_distance(text_1, text_2, ignore_space=True):
	"""
	Get Levenshtein distance between two lines of text.
	"""
	s1 = text_1.replace(' ', '').lower() if ignore_space else text_1.lower()
	s2 = text_2.replace(' ', '').lower() if ignore_space else text_2.lower()
	len_1, len_2 = len(s1), len(s2)

	if len_1 == 0 or len_2 == 0: return max(len_1,len_2)

	manipulation = [[0 for _ in range(len_2+1)] for _ in range(len_1+1)]
	for row in range(len_1+1): manipulation[row][0] = row
	for col in range(len_2+1): manipulation[0][col] = col

	for i in range(1,len_1+1):
		for j in range(1, len_2+1):
			cost = 1 if s1[i-1] != s2[j-1] else 0
			manipulation[i][j] = min(manipulation[i-1][j-1]+cost, manipulation[i-1][j]+1, manipulation[i][j-1]+1)

	distance = manipulation[-1][-1]

	return distance

def levenshtein_similarity(text_1, text_2, ignore_space=True):
	"""
	Get Levenshtein similarity between two lines of text.
	"""
	numerator = self.levenshtein_distance(text_1, text_2, ignore_space=ignore_space)
	denominator = max(len(text_1.replace(' ', '')),len(text_2.replace(' ', ''))) if ignore_space else max(len(text_1),len(text_2))
	similarity = 1-numerator/denominator

	return similarity
