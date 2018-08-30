import subprocess
import re
import pathlib
import os
from shutil import rmtree

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

# Back up git repo to a single file, right now, a 7zip archive.
def backup_repo(path_to_repo):
	cwd = os.getcwd() 

	# Parent directory of CCTS-Microbiome/Bej-Asim/M140-analysis/M140-analysis.
	namespace_path = os.path.dirname(path_to_repo)
	os.chdir(namespace_path)
	# Put together a 7zip archive name.
	git_repo_dir_name = os.path.basename(path_to_repo)
	commit_hash = get_head_commit_hash(git_repo_dir_name)
	archive_name = "{}-{}.7z".format(git_repo_dir_name, commit_hash)

	subprocess.run(['7za', 'a', archive_name, git_repo_dir_name], check=False)

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
	namespace_path = parse_path(git_repo_url)

	# Make sure this path exists on filesystem.
	# See https://docs.python.org/3/library/pathlib.html.
	# I liked pathlib the best, but see https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory-in-python for other options.
	pathlib.Path(namespace_path).mkdir(parents=True, exist_ok=True)

	# Think CCTS-Microbiome/Bej-Asim/M140-analysis/M140-analysis.
	git_repo_path = os.path.join(namespace_path, os.path.basename(namespace_path))

	# See https://docs.python.org/3.6/library/subprocess.html#using-the-subprocess-module.
	# Clone git repo to target directory.
	subprocess.run(['singularity', 'exec', '--bind', '/data', '/share/apps/ngs-ccts/simg/dvctools-0.3.simg', 'git', 'lfs', 'clone', git_repo_url, git_repo_path], check=False)

	# Check git repo integrity.
	git_fsck(git_repo_path)
	git_lfs_fsck(git_repo_path)

	# Back up git repo to a single file.
	backup_repo(git_repo_path)

	# Clean up.
	# See https://docs.python.org/3/library/shutil.html#shutil.rmtree.
	rmtree(git_repo_path)
