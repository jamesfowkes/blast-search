""" sequences.py

Usage:
	sequences.py <seq_file>

"""

import docopt

def split_into_sequences(lines):

	result = []
	results = []

	for line in lines:
		if line.startswith(">Gene"):
			results.append(result)
			result = [line]
		else:
			result.append(line)

	return results

def parse_for_sequences(f):

	lines = f.readlines()
	lines = [l.strip() for l in lines]

	return split_into_sequences(lines)

def find_by_name(to_search, name):

	for seq in to_search:
		if len(seq) and name in seq[0]:
			return seq

	return None

def print_seq(seq):
	for l in seq:
		print(l)

	print("")

if __name__ == "__main__":

	args = docopt.docopt(__doc__)

	filepath = args["<seq_file>"]

	with open(filepath, 'r') as f:
		results = parse_for_sequences(f)
	
	for res in results:
		print(res)