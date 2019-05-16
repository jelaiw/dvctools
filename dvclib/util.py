# Parse 7za list output and return total size and number of files as integers.
# 2018-09-10 10:04:16        12847911693   9120876783  5270 files, 1386 folders
def get_7zip_archive_stats(output):
	lines = output.splitlines()
	last_line = lines[-1]
	stats_line = last_line # Assume single volume.

	if last_line.startswith("Total archives size:"): # Handle multiple volumes.
		stats_line = lines[-5]

	tokens = stats_line.split()
	total_size = tokens[2]
	num_files = tokens[4]

	return int(total_size), int(num_files)
