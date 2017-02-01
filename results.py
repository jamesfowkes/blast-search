""" results.py

Usage:
	results.py <blast_file>

"""

import docopt
import logging

def split_into_results(lines):

	result = []
	results = []

	for line in lines:
		if line.startswith("Query="):
			results.append(result)
			result = [line]
		else:
			result.append(line)

	results.append(result)
	
	return results

def parse_for_results(f):

	lines = f.readlines()
	lines = [l.strip() for l in lines]

	return split_into_results(lines)[1:]

def is_significant(result):
	return any([l.startswith("Sequences producing significant alignments") for l in result])

def get_name(result):
	return result[0].split("= ")[1]

if __name__ == "__main__":

	logging.basicConfig(level=logging.INFO)

	args = docopt.docopt(__doc__)

	filepath = args["<blast_file>"]

	with open(filepath, 'r') as f:
		results = parse_for_results(f)

	logging.getLogger(__name__).info("Found {} sequences".format(len(results)))
	logging.getLogger(__name__).info("First: {}".format(get_name(results[0])))
	logging.getLogger(__name__).info("Last: {}".format(get_name(results[-1])))
	
	for res in results:
		print(get_name(res))