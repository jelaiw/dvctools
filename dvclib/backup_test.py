import unittest
from unittest.mock import patch

from dvclib.backup import create_backup_file_name, is_empty_repo

class BackupTests(unittest.TestCase):
	# See https://docs.python.org/3/library/unittest.mock.html.
	# Especially, see https://docs.python.org/3/library/unittest.mock.html#where-to-patch.
	# See https://www.toptal.com/python/an-introduction-to-mocking-in-python.
	# Maybe, see https://medium.com/@yeraydiazdiaz/what-the-mock-cheatsheet-mocking-in-python-6a71db997832.
	@patch('dvclib.backup.get_remote_head_commit_hash', return_value='88dea3f7714cde9732def1c4ae566bb383a665d6')
	def test_create_backup_file_name_returns_expected_name_for_Bej_test(self, mocked_dvclib_backup_get_remote_head_commit_hash):
		git_repo_url = 'git@gitlab.rc.uab.edu:CCTS-Microbiome/Bej-Asim/M140-analysis.git'
		expected_name = 'CCTS-Microbiome/Bej-Asim/M140-analysis/M140-analysis-88dea3f.7z'
		self.assertEqual(expected_name, create_backup_file_name(git_repo_url))

	@patch('dvclib.backup.get_remote_head_commit_hash', return_value='')
	def test_is_empty_repo_returns_true_for_empty_repo(self, mocked_dvclib_backup_get_remote_head_commit_hash):
		git_repo_url = 'git@gitlab.rc.uab.edu:CCTS-Microbiome/chen-dq/sross-denovo.git'
		self.assertTrue(is_empty_repo(git_repo_url))

	@patch('dvclib.backup.get_remote_head_commit_hash', return_value='88dea3f7714cde9732def1c4ae566bb383a665d6')
	def test_is_empty_repo_returns_false_for_repo_with_at_least_one_commit(self, mocked_dvclib_backup_get_remote_head_commit_hash):
		git_repo_url = 'git@gitlab.rc.uab.edu:CCTS-Microbiome/chen-dq/sross-denovo.git'
		self.assertFalse(is_empty_repo(git_repo_url))
