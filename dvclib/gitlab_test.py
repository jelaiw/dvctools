from dvclib.gitlab import fork_new_project
import unittest
from unittest.mock import MagicMock
import gitlab

class GitLabTests(unittest.TestCase):

	def test_fork_new_project_raises_assert_error_on_wrong_gitlab_api_version(self):
		mock_gl = MagicMock(spec=gitlab.Gitlab, api_version='3')

		with self.assertRaises(AssertionError):
			fork_new_project(mock_gl, "foo", "bar", 1)
