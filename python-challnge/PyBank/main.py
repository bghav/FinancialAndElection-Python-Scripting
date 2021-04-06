import os

import csv

import sys


csvpath = os.path.join('PyBank','Resources','budget_data.csv')

# Track various financial parameters
total_months = 0
month_of_change = []
net_change_list = []
total_net = 0
avg_change=0
change=0
low_change=0
currentvalue=0
prev=0
max_month=0
min_month=0


with open(csvpath) as budget_data:
   reader = csv.reader(budget_data)
   # Read the header row
   header = next(reader)
   
   # Extract first row to avoid appending to net_change_list
   
   first_row = next(reader)
   total_months += 1
   total_net += int(first_row[1])
   prev_net = int(first_row[1])
   
   
   for row in reader:
      
       # Track the total
       total_months += 1
       total_net += int(row[1])  #1st loop                  2ndloop                      3rd loop
       currentvalue= int(row[1])  #864000    prev = 0       currentvalue = 986455
       change=currentvalue-prev   #864000 - 0 = 86400        change = 986455-86400 = 10000
       net_change_list.append(change)
       month_of_change.append(row[0])
       prev=currentvalue  #prev = 986455

#net_change_list = [867400, 10000, -500]
# month_of_change = ['jan-10', 'feb-10', 'mar-10']

net_change_list = net_change_list[1:]
month_of_change = month_of_change[1:]
avg_change=sum(net_change_list)/len(net_change_list)
avg_change=round(avg_change)
change=max(net_change_list)
max_month=str(month_of_change[net_change_list.index(max(net_change_list))])
low_change=min(net_change_list)
min_month=str(month_of_change[net_change_list.index(min(net_change_list))])

print('FINANCIAL ANALYSIS')
print('------------------------------------')
print ('Total Months: ',total_months)
print ('Total: ',total_net)
print('Average Change: ',avg_change)
print('Greatest Increase in Profits: ',max_month,'(',change,')')
print('Greatest Decrease in Profits: ',min_month,'(',low_change,')')

sys.stdout = open("results.txt", "w")

print('FINANCIAL ANALYSIS')
print('------------------------------------')
print ('Total Months: ',total_months) 
print ('Total: ',total_net)
print('Average Change: ',avg_change)
print('Greatest Increase in Profits: ',change) 
print('Greatest Decrease in Profits: ',low_change)

sys.stdout.close()   