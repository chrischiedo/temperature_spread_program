# Copyright 2017 Chrispine O. Chiedo. All Rights Reserved.

""" 
This is a Python program that reads data from a provided input file (weather.dat).
The program then prints the maximum spread to the standard output.

It is a solution to the JUMO interview coding problem.  
"""

import os.path
from operator import itemgetter


data_file = "data/weather.dat"

#defines a private function to get the path to the data_file
def _getPath():
	''' Returns a valid path for the data file.
    Tries to use the user's home directory, otherwise defaults
    to the current working directory(cwd) '''

	try:
		file_path = os.environ['HOMEPATH'] or os.environ['HOME']
		if not os.path.exists(file_path):
			file_path = os.getcwd()
	except Exception:
		file_path = os.getcwd()
	return file_path

def main(filename):
	path = os.path.join(_getPath(), data_file)
	
	fr = open(path, 'r')

	# Read and ignore the first two lines from the data_file
	heading_row = fr.readline()
	empty_line = fr.readline()

	# Initialize an empty dictionary to hold {day: spread} key-value pairs
	spread_dict = {}

	# Read through the data_file line by line
	for line in fr:
		# Parse each line from data_file by stripping and splitting on whitespaces
		line = line.strip()
	    
		cols = line.split()

	    # The first column corresponds to the days of the month
		day = cols[0]

	    # The second column corresponds to the maximum daily temperatures
	    # Split on '*' to do away with the asterick
		max_temp = float(cols[1].split('*')[0])

	    # The third column corresponds to the minimum daily temperatures
		min_temp = float(cols[2].split('*')[0])

	    # Checking if the last line is reached
		if(day != "mo"):
	    	# Calculating the temperature spread
			temp_spread = float(max_temp - min_temp)

	    	# Storing the results in the dictionary 
			spread_dict.update({day: temp_spread})

	# Closing the file after end of reading
	fr.close()

	# Sorting the resulting dictionary in descending order
	sorted_spread_dict = sorted(spread_dict.items(), key=itemgetter(1), reverse=True)
	
	# Print out the maximum spread to standard output
	print("The day with the highest temperature spread is:")
	print("Day: " + str(sorted_spread_dict[0][0]) + " " + "Spread: " + str(int(sorted_spread_dict[0][1])))

if __name__ == "__main__": main(data_file)