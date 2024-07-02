'''
challenge:
    write a Python function to merge multiple CSV files.

    - input:
        - list of input files(list), path outputfile
        - function should be robust enough to merge even though headers don't match
'''
import pandas as pd
import csv
filePath = 'C:/Users/bebid/Desktop/Projects/Projects/Merge.csv/sample1.csv'
filePath2 = 'C:/Users/bebid/Desktop/Projects/Projects/Merge.csv/sample2.csv'
newfilePath = 'C:/Users/bebid/Desktop/Projects/Projects/Merge.csv/output.csv'
# df = pd.read_csv(filePath)

# print(df['Name'][0])

def merege_csv(list_file:list,newfilePath='output.csv'):
    headers_set = set()

    #get headers for each file
    for file in list_file:
        with open(file,'r') as file:
            csv_reader =  csv.reader(file)
            headers = next(csv_reader)
            headers_set.update(headers)

    headers_list = sorted(headers_set)
    #open the new file and insert new records
    with open(newfilePath,'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(headers_list)
    
        for file in list_file:
            with open(file, 'r') as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    merge_row = {header: row.get(header,'') for header in headers_list}
                    csv_writer.writerow(merge_row.values())
    print(f'Merged CSV saved to {newfilePath}')

print(merege_csv([filePath,filePath2],newfilePath))