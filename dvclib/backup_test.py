import unittest
from unittest.mock import MagicMock

from dvclib.backup import create_backup_file_name

class BackupTests(unittest.TestCase):

	def test_create_backup_file_name_returns_expected_name_for_Bej_test(self):
		# See https://docs.python.org/3/library/unittest.mock.html.
		# This works, but need to revisit and better understand Python mocks.
		mock = MagicMock()
		mock.get_remote_head_commit_hash.return_value = '78dea3f7714cde9732def1c4ae566bb383a665d6'

		git_repo_url = 'git@gitlab.rc.uab.edu:CCTS-Microbiome/Bej-Asim/M140-analysis.git'
		expected_name = 'CCTS-Microbiome/Bej-Asim/M140-analysis/M140-analysis-78dea3f.7z'
		self.assertEqual(expected_name, create_backup_file_name(git_repo_url))
