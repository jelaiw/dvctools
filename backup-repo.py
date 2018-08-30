import subprocess
import re
import pathlib
import os

# Parse a git repo URL for GitLab namespace as a path.
def parse_path(git_repo_url):
	# See https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/81#note_8797 for implementation decision-making.
	# See https://docs.python.org/3/howto/regex.html for a refresher.
	# git@gitlab.rc.uab.edu:CCTS-Microbiome/Bej-Asim/M140-analysis.git
	pattern = re.compile('git@gitlab.rc.uab.edu:(\S+).git')
	match = pattern.match(git_repo_url)
	return match.group(1)

# Run git fsck in git repo at given path.
def git_fsck(path_to_repo):
	cwd = os.getcwd() # Save cwd.
	os.chdir(path_to_repo)
	# Run git fsck via dvctools "guaranteed DVC stack".
	subprocess.run(['singularity', 'exec', '--bind', '/data', '/share/apps/ngs-ccts/simg/dvctools-0.3.simg', 'git', 'fsck'], check=False)
	# Change working directory back.
	os.chdir(cwd)

# Run git lfs fsck in git repo at given path.
def git_lfs_fsck(path_to_repo):
	cwd = os.getcwd() # Save cwd.
	os.chdir(path_to_repo)
	# Run git lfs fsck via dvctools "guaranteed DVC stack".
	subprocess.run(['singularity', 'exec', '--bind', '/data', '/share/apps/ngs-ccts/simg/dvctools-0.3.simg', 'git', 'lfs', 'fsck'], check=False)
	# Change working directory back.
	os.chdir(cwd)

# Read list of git repos (to back up) from a named input file.
# See https://docs.python.org/3.6/library/io.html#i-o-base-classes.
with open('repo-list.txt') as f:
	lines = f.readlines()

# Remove trailing newline.
repos = [line.rstrip() for line in lines]

# Back up each git repo.
for git_repo_url in repos:
	# Parse a git repo URL for GitLab namespace, which we attempt to preserve in the DVC backups directory structure.
	path = parse_path(git_repo_url)

	# Make sure this path exists on filesystem.
	# See https://docs.python.org/3/library/pathlib.html.
	# I liked pathlib the best, but see https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory-in-python for other options.
	pathlib.Path(path).mkdir(parents=True, exist_ok=True)

	# See https://docs.python.org/3.6/library/subprocess.html#using-the-subprocess-module.
	# Clone git repo to target directory.
	subprocess.run(['singularity', 'exec', '--bind', '/data', '/share/apps/ngs-ccts/simg/dvctools-0.3.simg', 'git', 'lfs', 'clone', git_repo_url, path], check=False)

	# Check git repo integrity.
	git_fsck(path)
	git_lfs_fsck(path)
