import numpy as np
import pandas as pd
import argparse
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('start_date')
	parser.add_argument('end_date')
	parser.add_argument('freq')
	args = vars(parser.parse_args())
	# Now args is a dictionary
	print(args)
	# {'start_date': '2019-01-01', 'end_date': '2019-12-31', 'freq': '30'}
	print("\n")
	start_date = args['start_date']
	end_date = args['end_date']
	freq = args['freq']
	print(start_date)
	print("\n")
	print(end_date)
	print("\n")
	print(freq)
	print("\n")



