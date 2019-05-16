import unittest

from dvclib.util import get_7zip_archive_stats

class UtilTests(unittest.TestCase):

	def test_get_7zip_archive_stats_returns_expected_stats_for_Bej_test(self):
# Last line from a real '7za l' call to backup 7z archive for Bej test.
		test_line = '2018-09-10 10:04:16        12847911693   9120876783  5270 files, 1386 folders\n'
		total_size, num_files = get_7zip_archive_stats(test_line)
		self.assertEqual(total_size, 12847911693)
		self.assertEqual(num_files, 5270)

	def test_get_7zip_archive_stats_returns_expected_stats_for_multivolume_test(self):
# Tail lines from a real '7za l' call to backup 7z archive for Lal-vivek/M207.
# See https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/106#note_14099.
		test_line = '2019-05-02 20:29:20        38254357389  18276614652  10490 files, 2305 folders\n\nArchives: 1\nVolumes: 2\nTotal archives size: 18276706330\n'
		total_size, num_files = get_7zip_archive_stats(test_line)
		self.assertEqual(total_size, 38254357389)
		self.assertEqual(num_files, 10490)

