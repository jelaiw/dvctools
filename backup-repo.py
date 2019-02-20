import subprocess
import pathlib
import os
from shutil import rmtree
import logging

from dvclib.git import parse_path, git_fsck, git_lfs_fsck
from dvclib.backup import exists_backup, backup_repo, is_empty_repo, exists_repo

# See https://docs.python.org/3/howto/logging.html#logging-advanced-tutorial.
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('backup.log')
file_handler.setFormatter(formatter)

# Set the root logger to debug.
#logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger().setLevel(logging.INFO)

# Set up logger.
logger = logging.getLogger(__name__)
logger.addHandler(file_handler)

# Read list of git repos (to back up) from a named input file.
# See https://docs.python.org/3.6/library/io.html#i-o-base-classes.
repo_list_filename = 'repo-list.txt'
with open(repo_list_filename) as f:
	lines = f.readlines()
# Remove trailing newline.
repos = [line.rstrip() for line in lines]
logger.info('Read %d git repo URLs from %s.', len(repos), repo_list_filename)

# Figure out what git repos need a backup.
repos_to_backup = list()
for git_repo_url in repos:
	logger.debug('Peek at %s.', git_repo_url)
	if not exists_repo(git_repo_url):
		logger.warn('Repo %s no longer exists!', git_repo_url)
	elif is_empty_repo(git_repo_url):
		logger.warn('Ignore %s for backup, repo is empty.', git_repo_url)
	elif not exists_backup(git_repo_url):
		repos_to_backup.append(git_repo_url)
		logger.debug('Backup needed.')
	else:
		logger.debug('Skip, backup exists.')

logger.info('Need backup for %d of %d git repos.', len(repos_to_backup), len(repos))

# Backup each git repo.
for git_repo_url in repos_to_backup:
	logger.info('Begin backup for %s.', git_repo_url)

	# Parse a git repo URL for GitLab namespace, which we attempt to preserve in the DVC backups directory structure.
	namespace_path = parse_path(git_repo_url)

	# Make sure this path exists on filesystem.
	# See https://docs.python.org/3/library/pathlib.html.
	# I liked pathlib the best, but see https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory-in-python for other options.
	pathlib.Path(namespace_path).mkdir(parents=True, exist_ok=True)

	# Think CCTS-Microbiome/Bej-Asim/M140-analysis/M140-analysis.
	git_repo_path = os.path.join(namespace_path, os.path.basename(namespace_path))

	# See https://docs.python.org/3.6/library/subprocess.html#using-the-subprocess-module.
	# Clone git repo to target directory.
	logger.info('Begin git clone of %s to %s.', git_repo_url, git_repo_path)
	# Try --progress if we want what we see at the terminal. Pass for now.
	# See https://stackoverflow.com/questions/32685568/git-clone-writes-to-sderr-fine-but-why-cant-i-redirect-to-stdout.
	cp = subprocess.run(['git', 'lfs', 'clone', git_repo_url, git_repo_path], check=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
	# See https://docs.python.org/3.6/library/subprocess.html#subprocess.CompletedProcess.stdout, especially regarding how stdout and stderr are combined.
	logger.debug(cp.stdout)

	logger.info('Check git repo integrity.')
	git_fsck(git_repo_path)
	git_lfs_fsck(git_repo_path)

	archive_name = backup_repo(git_repo_path)
	logger.info('Backup of %s to %s completed!', git_repo_url, archive_name)

	logger.info('Remove %s for clean up.', git_repo_path)
	# See https://docs.python.org/3/library/shutil.html#shutil.rmtree.
	rmtree(git_repo_path)
