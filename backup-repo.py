import subprocess

# Read list of git repos (to back up) from input file.
# See https://docs.python.org/3.6/library/io.html#i-o-base-classes.
with open('repo-list.txt') as f:
	lines = f.readlines()

# Remove trailing newline.
repos = [line.rstrip() for line in lines]

# Back up each git repo.
for repo in repos:
	# See https://docs.python.org/3.6/library/subprocess.html#using-the-subprocess-module.
	# Clone git repo.
	subprocess.run(['singularity', 'exec', '--bind', '/data', '/share/apps/ngs-ccts/simg/dvctools-0.3.simg', 'git', 'lfs', 'clone', repo], check=False)
