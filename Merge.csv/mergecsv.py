'''
challenge:
    write a Python function to merge multiple CSV files.

    - input:
        - list of input files(list), path outputfile
        - function should be robust enough to merge even though headers don't match
'''
import csv
filePath = 'C:/Users/bebid/Desktop/Projects/Projects/Merge/sample1.csv'
with open(filePath,'r') as file:
    file = csv(file)
    file.reader()