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

# Match paths to multivolume 7zip archives.
paths = glob("**/*.7z.001", recursive=True)
# Add paths to "legacy" 7zip archives.
paths.extend(glob("**/*.7z", recursive=True))

# Parse 7za list archive output for summary statistics of interest.
data = list()
for path in paths:
	# Call 7za l and save standard output.
	cp = subprocess.run(['7za', 'l', path], check=False, stdout=subprocess.PIPE, universal_newlines=True)

	tot_size, num_files = get_7zip_archive_stats(cp.stdout)
	data.append( (path, tot_size, num_files) )

# Write tab-delimited output.
for row in data:
	path, tot_size, num_files = row
	print( "{}\t{}\t{}".format(path, tot_size, num_files) )
