/*

					NAME:   CHRISPINE O. CHIEDO
					EMAIL:  chrispinechiedo@gmail.com
					GITHUB: github.com/theafricanengineer
					MOBILE: +254(0) 729 506 507
*/

		TITLE: A DESCRIPTION OF MY SOLUTION TO THE JUMO INTERVIEW CODING PROBLEM
-------------------------------------------------------------------------------------------------------------------------------------

INTRODUCTION:

This text file contains the full description of my solution to the jumo coding interview question.

PROBLEM DEFINITION:

The interview question required one to write a program that would read data from a provided file (weather.dat) containing weather data
for a single month as space-separated values, and give as its output the row with the maximum spread, where spread is defined as the
difference between the maximum temperature in a particular day (MxT) and the corresponding minimum temperature for that day (MnT).

REQUIREMENTS:

	1. Functional Requirements
		-> The program should read as its input data from the provided file (weather.dat)
		-> The program should then give as its output the row with the maximum spread
		-> When the program is run, it should print the day of the month and the maximum spread to the standard output
	2. Non-Functional Requirements
		-> The code should be well-organized and readable
		-> The program should produce a correct and efficient solution to the problem
		-> The solution should have a 'readme.txt' file detailing how to run the program and the assumptions (if any) made.

IMPLEMENTATION APPROACH:

	-> The program imports two modules, 'os.path' and 'itemgetter' from the 'operator' module
	-> The program defines two functions, a private _getPath() function that takes no arguments and a main() function that takes the
	   data_file as its argument
	-> The program starts by trying to locate the path to the data file (weather.dat)
	-> After successfully locating the data file, the program then reads in the data from the file line by line
	-> The first two lines are ignored (the first line has row headings while the second line is entirely empty)
	-> Each line read is then parsed into a list by stripping and splitting on whitespaces.
	-> The result is that the first column, cols[0] holds the day(Dy), the second column, cols[1] holds the maximum temperature(MxT)
	   and the third column, cols[2] holds the minimum temperature(MnT).
	-> The temperature spread is then calculated by getting the difference between the extracted MxT and MnT values and stored in a
	   dictionary as key-value pairs i.e. {day: temp_spread}
	-> The last line containing the monthly averages is ignored
	-> After all the temperature spreads have been calculated and stored in the dictionary, the dictionary is sorted in descending order
	-> The key-value pair at the first position in the sorted dictionary (i.e. position 0) is then printed to the standard output as the
	   maximum temperature spread.

ASSUMPTIONS MADE:
	-> The maximum temperature for the month (97) and the minimum temperature for the month (32) were labelled with an asterick just to
	   single them out and that they had no other special meaning.
	-> The data was assumed not to have any special outliers that would tend to skew our results.
	-> The data from the file was also assumed to be fairly consistent.
	-> It was assumed that the weather data file is of a small size and therefore no further speed optimization would be required (that 
	   the execution speed will be fast enough).  


DIRECTORY STRUCTURE:

The program has the following directory structure:
	| temperature_spread_program/ ................ The main program directory
		| data/               ................ A child directory containing the data file
		      |weather.dat    ................ The weather data file
		| readme.txt          ................ A 'readme' text file having all the information about the program
		| maxtempspread.py    ................ The Python script that contains the solution code

HOW TO RUN THE PROGRAM:

	1. Set-up
	-> In order to run the program, Python version 3 should be installed. If Python version 2 is used,then minor changes should be made
	   to the source code (for example, while 'print' is a statement in Python 2, it is a function in Python 3)
	-> The program should then be downloaded and extracted into a local directory in a location of your choice

	2. Running the application
	-> In order to run the application, open a terminal program (applies to Linux and MacOS X) and navigate into the directory where the
	   contents of the downloaded program were extracted (For Windows users use command prompt instead)
	-> While in the root of the directory, run the application as follows: 
		
		$ python maxtempspread.py
	
	-> Note that if you have both versions of Python installed on your machine, then you may be required to explicitly target a particular
	   version as follows:

		$ python3 maxtempspread.py           # This uses Python 3 exclusively

	-> The expected output (assuming that everything goes well) is as follows:
		
		The day with the highest temperature spread is:
		Day: 9 Spread: 54
		  
TECHNICAL RESOURCES:

	1. Programming Environment
	The program was developed on a linux machine running Ubuntu 16.04LTS operating system.

	2. Text Editors
	-> The text editor used for writing the source code was Sublime Text.
	-> The 'readme.txt' file was created using the 'gedit' text editor.
	
	3. Programming Language
	The programming language chosen for implementing the solution was Python version 3.5.2
	The reason for this choice is that Python is well suited for data analysis problems (like the one provided in this coding problem)

CONCLUSION:

	-> The solution to this coding problem took roughly one and a half days (~36 hours).
	-> Much of that time was used researching for the best solution possible.
	-> The implementation of the final solution in code only took about a quarter of the time.
 

N/B: The program can be tweaked slightly to give the minimum spread as well (mintempspread.py).


----------------------------------------------------END---------------------------------------------------------------------------------








