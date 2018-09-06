import subprocess
import re
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

# Return abbreviated commit hash for git repo at given path.
def get_head_commit_hash(path_to_repo):
	cwd = os.getcwd() 
	os.chdir(path_to_repo)
	# See https://docs.python.org/3.6/library/subprocess.html#frequently-used-arguments regarding universal_newlines.
	cp = subprocess.run(['singularity', 'exec', '--bind', '/data', '/share/apps/ngs-ccts/simg/dvctools-0.3.simg', 'git', 'log', '-1', '--pretty=format:%h'], check=False, stdout=subprocess.PIPE, universal_newlines=True)
	os.chdir(cwd)
	return cp.stdout


