import unittest

from dvclib.util import parse_7za_list_output

class UtilTests(unittest.TestCase):

	def test_parse_7za_list_output_returns_expected_numbers_for_Bej_test(self):
# Last line from a real '7za l' call to backup 7z archive for Bej test.
		test_line = '2018-09-10 10:04:16        12847911693   9120876783  5270 files, 1386 folders\n'
		total_size, num_files = parse_7za_list_output(test_line)
		self.assertEqual(total_size, 12847911693)
		self.assertEqual(num_files, 5270)
