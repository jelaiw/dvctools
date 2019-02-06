import subprocess
import os
import glob
import logging

from dvclib.git import parse_path, get_head_commit_hash, get_remote_head_commit_hash, short_hash

# Back up git repo to a single file, right now, a 7zip archive.
def backup_repo(path_to_repo):
	cwd = os.getcwd() # Save current working directory for later.
	# Parent directory of CCTS-Microbiome/Bej-Asim/M140-analysis/M140-analysis.
	namespace_path = os.path.dirname(path_to_repo)
	os.chdir(namespace_path)
	# Construct 7zip archive name.
	git_repo_dir_name = os.path.basename(path_to_repo)
	commit_hash = get_head_commit_hash(git_repo_dir_name)
	archive_name = get_7zip_archive_name(git_repo_dir_name, commit_hash)
	# Create a new 7zip archive with 15 GB volumes.
	cp = subprocess.run(['7za', 'a', archive_name, git_repo_dir_name, '-v15g'], check=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
	# Log debug output.
	logger = logging.getLogger(__name__)
	logger.debug(cp.stdout)
	# Return to working directory.
	os.chdir(cwd)
	return archive_name

def get_7zip_archive_name(git_repo_dir_name, commit_hash):
	return "{}-{}.7z".format(git_repo_dir_name, commit_hash)

# Return true if a backup exists for HEAD of git repo at given URL.
# git@gitlab.rc.uab.edu:CCTS-Microbiome/Bej-Asim/M140-analysis.git
def exists_backup(git_repo_url):
	backup_file_name = create_backup_file_name(git_repo_url)
	# See https://docs.python.org/3/library/glob.html#glob.glob.
	glob_pattern = backup_file_name + '*'
	return len(glob.glob(glob_pattern)) > 0

# Return true if git repo is "empty" (i.e. no commits).
# See https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/103#note_12151.
def is_empty_repo(git_repo_url):
	commit_hash = get_remote_head_commit_hash(git_repo_url)
	# Consider a better way to do this. For now, let's just use the fact that get_remote_head_commit_hash() returns an empty string for a git repo with no commits.
	# See https://stackoverflow.com/questions/9573244/most-elegant-way-to-check-if-the-string-is-empty-in-python.
	return not bool(commit_hash)

# Return backup file name for git repo URL.
def create_backup_file_name(git_repo_url):
	# CCTS-Microbiome/Bej-Asim/M140-analysis
	namespace_path = parse_path(git_repo_url)
	project_name = os.path.basename(namespace_path) # M140-analysis
	# 78dea3f7
	commit_hash = short_hash(get_remote_head_commit_hash(git_repo_url))
	# M140-analysis-78dea3f7.7z
	archive_name = get_7zip_archive_name(project_name, commit_hash)
	# CCTS-Microbiome/Bej-Asim/M140-analysis/M140-analysis-78dea3f.7z
	return os.path.join(namespace_path, archive_name)
