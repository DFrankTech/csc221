#Project: Reading Data from a Spreadsheet
Say you have a spreadsheet of data from the 2010 US Census and you have the boring task of going through its thousands of rows to count both the total population and the number of census tracts for each county. (A census tract is simply a geographic area defined for the purposes of the census.) Each row represents a single census tract.

This is what your program does:
1. Reads the data from the Excel spreadsheet
2. Counts the number of census tracts in each county
3. Counts the total population of each county
4. Prints the results

This means your code will need to do the following:
1. Open and read the cells of an Excel document with the openpyxl module.
2. Calculate all the tract and population data and store it in a data structure.
3. Write the data structure to a text file with the .py extension using the pprint module.
