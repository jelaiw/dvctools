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

# Return full commit hash for HEAD of master for repo at git repo URL.
def get_remote_head_commit_hash(git_repo_url):
# See https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/81#note_9046.
	cp = subprocess.run(['singularity', 'exec', '--bind', '/data', '/share/apps/ngs-ccts/simg/dvctools-0.3.simg', 'git', 'ls-remote', git_repo_url, 'HEAD'], check=False, stdout=subprocess.PIPE, universal_newlines=True)
	return parse_hash(cp.stdout)

# Parse git ls-remote output and return the full commit hash.
# git ls-remote git@gitlab.rc.uab.edu:CCTS-Microbiome/Bej-Asim/M140-analysis.git HEAD
def parse_hash(ls_remote_output):
	# See https://docs.python.org/3.7/library/stdtypes.html#str.split.
	# split() behavior with no sep arg is exactly what we want.
	return ls_remote_output.split()[0]

# Return abbreviated git commit hash given full commit hash.
def short_hash(full_hash):
	return full_hash[:8] # First eight characters.
