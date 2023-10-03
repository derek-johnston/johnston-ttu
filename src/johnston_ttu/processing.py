"""
processing.py
Developed By: Derek Johnston @ Texas Tech University

Special-purpose functions for data cleaning and pre-processing.
"""
def remove_ena_labels(filename):
	"""
	They Keysight ENA creates two extra lines of metadata at the 
	top of a measurement .CSV file. These should be removed so
	that datafiles can be imported into Pandas.
	
	Keyword Arguments:
	filename -- the file name (and path) to the .CSV to be cleaned.
	"""
	line_buffer = [] # Pull each line out of the file, and write back all but the last two.
	with open(f"{filename}.csv", "r") as fp:
		line_buffer = fp.readlines()
	with open(f"{filename}_p.csv", "w") as fp:
		for number, line in enumerate(line_buffer):
			if number >= 2:
				fp.write(line)
