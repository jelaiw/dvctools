import unittest

from dvclib.git import parse_path, parse_hash, short_hash

class GitTests(unittest.TestCase):

	def test_parse_path_returns_expected_namespace_for_Bej_test(self):
		namespace = parse_path('git@gitlab.rc.uab.edu:CCTS-Microbiome/Bej-Asim/M140-analysis.git')
		self.assertEqual(namespace, 'CCTS-Microbiome/Bej-Asim/M140-analysis')

	def test_parse_hash_returns_expected_hash_for_Bej_test(self):
		hash = parse_hash('78dea3f7714cde9732def1c4ae566bb383a665d6        HEAD')
		self.assertEqual(hash, '78dea3f7714cde9732def1c4ae566bb383a665d6')

	def test_short_hash_returns_expected_short_hash_for_Bej_test(self):
		hash = short_hash('78dea3f7714cde9732def1c4ae566bb383a665d6')
		self.assertEqual(hash, '78dea3f7');
