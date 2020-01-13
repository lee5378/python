# 
# Desc: Python script to automate Google search from a CSV list of terms
# Auth: David Lee
# Date: 1-12-2020
#

# Import libraries
import csv
import bs4
import google
from googlesearch import search

# Define variables
rownum = 2
output_list = []
search_string = '_'

# Define functions
# Function googlethis will take the input string and google it for us
def googlethis(search_string):

    output_list.clear()
    for i in search(search_string, 
                    tld='com', 
                    lang='en', 
                    num=10,  
                    start=0, 
                    stop=3, 
                    pause=2.0 
                   ):
        output_list.append(i)
        print(i)   

# Function analyze_csv opens the csv file and iterates through to pick search terms for googlethis
def analyze_csv(csv_file,csv_row):
    
    f1 = open('Outfile.csv', 'w', newline='')
    c1 = csv.writer(f1)

    with open(csv_file,'r') as f:
        reader = list(csv.reader(f))
        column_counter = 1
        for row in reader[csv_row]:
            if column_counter > 14:
                search_term = row
                remark = str('The search term ' + str(search_term) + ' yielded:')

                print('---------------')
                c1.writerow(['---------------'])
                
                print('The search term ',search_term,' yielded:')
             
                c1.writerow([remark])

                googlethis(search_term)
                for row in output_list:
                    c1.writerow([row])
                
            column_counter+=1

# Main program
print('Which row of the spreadsheet (top header row is 1) do you wish to search on?')
rownum = int(input())
analyze_csv('ClimateTreeMaster.csv',rownum)
