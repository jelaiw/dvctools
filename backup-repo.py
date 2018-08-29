import subprocess
import re
import pathlib

# Parse a git repo URL for GitLab namespace path.
def parse_path(git_repo_url):
	# See https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/81#note_8797 for implementation decision-making.
	# See https://docs.python.org/3/howto/regex.html for a refresher.
	pattern = re.compile('git@gitlab.rc.uab.edu:(\S+).git')
	match = pattern.match(git_repo_url)
	return match.group(1)

# Read list of git repos (to back up) from input file.
# See https://docs.python.org/3.6/library/io.html#i-o-base-classes.
with open('repo-list.txt') as f:
	lines = f.readlines()

# Remove trailing newline.
repos = [line.rstrip() for line in lines]

# Back up each git repo.
for git_repo_url in repos:
	# Parse a git repo URL for GitLab namespace path, which we attempt to preserve in the DVC backups directory structure.
	path = parse_path(git_repo_url)

	# Make sure this path exists on filesystem.
	# See https://docs.python.org/3/library/pathlib.html.
	# I liked pathlib the best, but see https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory-in-python for other options.
	pathlib.Path(path).mkdir(parents=True, exist_ok=True)

	# See https://docs.python.org/3.6/library/subprocess.html#using-the-subprocess-module.
	# Clone git repo to target directory.
	subprocess.run(['singularity', 'exec', '--bind', '/data', '/share/apps/ngs-ccts/simg/dvctools-0.3.simg', 'git', 'lfs', 'clone', git_repo_url, path], check=False)
