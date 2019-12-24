#
# Desc:         Python script to load Employee IDs over from CSV
# Author:       David Lee
# Last revised: 12-24-2019
#

import csv

f1 = open('ACL.csv', 'r')
f2 = open('EmployeesID.csv', 'r')
f3 = open('OutFile.csv', 'w', newline='')

c1 = csv.reader(f1)
c2 = csv.reader(f2)
c3 = csv.writer(f3)

masterlist = list(c2)

for hosts_row in c1:  
    found = False
    for master_row in masterlist:
        results_row = hosts_row        
        if (hosts_row[2] == master_row[2] and
            hosts_row[3] == master_row[1]):
            results_row[1] = master_row[0]      # f2.readline() # Edit the second column
            c3.writerow(results_row)            # output the line\
            found = True
            break
    if not found:    
        c3.writerow(results_row)        
        
f1.close()
f2.close()
f3.close()
