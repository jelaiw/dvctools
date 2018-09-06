import unittest

from dvclib.git import parse_path

class GitTests(unittest.TestCase):

	def test_parse_path_returns_expected_namespace_for_Bej_test(self):
		namespace = parse_path('git@gitlab.rc.uab.edu:CCTS-Microbiome/Bej-Asim/M140-analysis.git')
		self.assertEqual(namespace, 'CCTS-Microbiome/Bej-Asim/M140-analysis')
