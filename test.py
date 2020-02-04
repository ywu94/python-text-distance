import unittest
import pytextdist

class parametrizedTestCase(unittest.TestCase):
	def __init__(self, methodName="runTest", **kwargs):
		"""
		Any parameterized tests should inherit this class
		"""
		super(parametrizedTestCase, self).__init__(methodName)
		self.kwargs = kwargs

	@staticmethod
	def parametrize(testcase_class, **kwargs):
		"""
		Create a suite containing all tests taken from the given subclass, passing them the parameter "param".
		"""
		test_names = unittest.TestLoader().getTestCaseNames(testcase_class)
		suite = unittest.TestSuite()
		for name in test_names:
			suite.addTest(testcase_class(methodName=name, **kwargs))
		return suite

class pytextdist_test(parametrizedTestCase):
	def test_preprocessing(self):
		self.assertEqual(pytextdist.preprocessing.word_preprocessing(self.kwargs["preprocess_q"]), self.kwargs["word_preprocess_ans"])
		self.assertEqual(pytextdist.preprocessing.sentence_preprocessing(self.kwargs["preprocess_q"]), self.kwargs["sentence_preprocess_ans"])

	def test_edit_distance(self):
		self.assertEqual(pytextdist.edit_distance.levenshtein_distance(self.kwargs["phrase_1"], self.kwargs["phrase_2"]), self.kwargs["lev_d"])
		self.assertEqual(pytextdist.edit_distance.hamming_distance(self.kwargs["phrase_1"], self.kwargs["phrase_2"]), self.kwargs["h_d"])
		self.assertEqual(pytextdist.edit_distance.lcs_distance(self.kwargs["phrase_1"], self.kwargs["phrase_2"]), self.kwargs["lcs_d"])	
		self.assertEqual(pytextdist.edit_distance.damerau_levenshtein_distance(self.kwargs["phrase_1"], self.kwargs["phrase_2"]), self.kwargs["d_lev_d"])
		self.assertEqual(round(pytextdist.edit_distance.jaro_similarity(self.kwargs["phrase_1"], self.kwargs["phrase_2"]),2), self.kwargs["d_jaro"])
		self.assertEqual(round(pytextdist.edit_distance.jaro_winkler_similarity(self.kwargs["phrase_1"], self.kwargs["phrase_2"]),2), self.kwargs["d_jaro_wi"])

	def test_vector_similarity(self):
		self.assertEqual(round(pytextdist.vector_similarity.cosine_similarity(self.kwargs["sentence_1"], self.kwargs["sentence_2"]), 2), self.kwargs["cos_s"])
		self.assertEqual(round(pytextdist.vector_similarity.jaccard_similarity(self.kwargs["sentence_1"], self.kwargs["sentence_2"]), 2), self.kwargs["jac_s"])
		self.assertEqual(round(pytextdist.vector_similarity.sorensen_dice_similarity(self.kwargs["sentence_1"], self.kwargs["sentence_2"]), 2), self.kwargs["sor_s"])
		self.assertEqual(round(pytextdist.vector_similarity.qgram_similarity(self.kwargs["sentence_1"], self.kwargs["sentence_2"]), 2), self.kwargs["qgr_s"])


test_cases = [
	{
		"preprocess_q": "They have 5 length-2 common subsequences: (AB), (AC), (AD), (BD), and (CD)",
		"word_preprocess_ans": "theyhavelengthcommonsubsequencesabacadbdandcd",
		"sentence_preprocess_ans": ["they","have","length","common","subsequences","ab","ac","ad","bd","and","cd"],
		"phrase_1": "bededqowd",
		"phrase_2": "beeddqpdw",
		"lev_d": 5,
		"h_d": 5,
		"lcs_d": 6,
		"d_lev_d": 3,
		"d_jaro": 0.84,
		"d_jaro_wi": 0.87,
		"sentence_1": "For Paperwork Reduction Act Notice, see your tax return instructions. For Paperwork Reduction Act Notice, see your tax return instructions.",
		"sentence_2": "For Disclosure, Privacy Act, and Paperwork Reduction Act Notice, see separate instructions. Form 1040",
		"cos_s": 0.38,
		"jac_s": 0.22,
		"sor_s": 0.36,
		"qgr_s": 0.15,

	},
	{
		"preprocess_q": "They have 5 length-2 common subsequences: (AB), (AC), (AD), (BD), and (CD)",
		"word_preprocess_ans": "theyhavelengthcommonsubsequencesabacadbdandcd",
		"sentence_preprocess_ans": ["they","have","length","common","subsequences","ab","ac","ad","bd","and","cd"],
		"phrase_1": "bededqowd",
		"phrase_2": "bededqowd",
		"lev_d": 0,
		"h_d": 0,
		"lcs_d": 0,
		"d_lev_d": 0,
		"d_jaro": 1.0,
		"d_jaro_wi": 1.0,
		"sentence_1": "For Disclosure, Privacy Act, and Paperwork Reduction Act Notice, see separate instructions. Form 1040",
		"sentence_2": "For Disclosure, Privacy Act, and Paperwork Reduction Act Notice, see separate instructions. Form 1040",
		"cos_s": 1.0,
		"jac_s": 1.0,
		"sor_s": 1.0,
		"qgr_s": 1.0,

	},
]

if __name__ == "__main__":
	for test_case in test_cases:
		suite = unittest.TestSuite()
		suite.addTest(parametrizedTestCase.parametrize(pytextdist_test, **test_case))
		unittest.TextTestRunner().run(suite)