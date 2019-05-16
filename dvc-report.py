import sys
import os
from glob import glob
import subprocess

from dvclib.util import get_7zip_archive_stats

# Parse command-line arguments for target directory.
if len(sys.argv) != 2:
	sys.exit(1)

target_dir = sys.argv[1]
print("Target directory = {}".format(target_dir))

# Assemble glob pattern for matching 7zip archives.
glob_pattern = os.path.join(target_dir, "**/*.7z*")
print("Glob pattern = {}".format(glob_pattern))

paths = glob(glob_pattern, recursive=True)

# Parse 7za l output for data of interest.
data = list()
for path in paths:
	# Call 7za l and save standard output.
	cp = subprocess.run(['7za', 'l', path], check=False, stdout=subprocess.PIPE, universal_newlines=True)
	# Parse total size and number of files from 7za list output.
	tot_size, num_files = get_7zip_archive_stats(cp.stdout)
	data.append( (path, tot_size, num_files) )

# Write tab-delimited output.
for row in data:
	path, tot_size, num_files = row
	print( "{}\t{}\t{}".format(path, tot_size, num_files) )
