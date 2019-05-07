# Parse last line of 7za list output and return total size and number of files as integers.
# 2018-09-10 10:04:16        12847911693   9120876783  5270 files, 1386 folders
def parse_7za_list_output(last_line):
	tokens = last_line.split()
	total_size = tokens[2]
	num_files = tokens[4]
	return int(total_size), int(num_files)
