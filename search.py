""" search.py

Usage:
	search.py <blast_file> <sequences_file>

"""

import docopt
import results
import sequences

import logging

if __name__ == "__main__":

	logging.basicConfig(level=logging.INFO)

	args = docopt.docopt(__doc__)

	blastpath = args["<blast_file>"]
	seqpath =  args["<sequences_file>"]

	with open(blastpath, 'r') as f:
		result_list = results.parse_for_results(f)
	
	logging.info("Got {} results".format(len(result_list)))

	with open(seqpath, 'r') as f:
		seq_list = sequences.parse_for_sequences(f)

	logging.info("Got {} sequences".format(len(seq_list)))

	significant_results = filter(lambda r: results.is_significant(r), result_list)
	significant_results = list(significant_results)

	logging.info("Got {} significant results".format(len(significant_results)))
	
	original_sequences = []

	for sig_result in significant_results:
		sequence_name = results.get_name(sig_result)
		original_sequence = sequences.find_by_name(seq_list, sequence_name)
		sequences.print_seq(original_sequence)
		