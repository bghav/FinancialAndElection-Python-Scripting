import os

import csv

import sys

csvpath = os.path.join('PyPoll','Resources','election_data.csv')

# Track various voting parameters

total_votes = 0
ballot_list=[]
candidate_votes=[]
khan_votes=0
li_votes=0
otooley_votes=0
correy_votes=0
khan_percent=0
li_percent=0
otooley_percent=0
correy_percent=0

with open(csvpath) as election_data:
    reader = csv.reader(election_data)
    
    # Read the header row
    header = next(reader)
    
    # Extract first row
    first_row = next(reader)
    total_votes += 1
    khan_votes+=1
     
    for row in reader:
    
    # Track the total
        
        total_votes += 1

    #while total_votes <3521001:
        candidate = row[2]

        if candidate=="Khan":
            khan_votes+=1

        elif candidate=="Li":
            li_votes+=1
        elif candidate=="Correy":
            correy_votes+=1
        else:
            otooley_votes+=1
     
        khan_percent=(khan_votes/total_votes)*100
        khan_percent=round(khan_percent)
        
        li_percent=(li_votes/total_votes)*100
        li_percent=round(li_percent)
        
        correy_percent=(correy_votes/total_votes)*100
        correy_percent=round(correy_percent)
        
        otooley_percent=(otooley_votes/total_votes)*100
        otooley_percent=round(otooley_percent)

print('ELECTION RESULTS')
print('---------------------------')
print ('Total Votes: ',total_votes)
print('---------------------------')
print (f"Kahn: {khan_percent,'%',khan_votes}")
print (f"Li: {li_percent,'%',li_votes}")
print (f"Correy: {correy_percent,'%',correy_votes}")
print (f"O'Tooley: {otooley_percent,'%',otooley_votes}")
print('---------------------------')
print('Winner Khan')

sys.stdout = open("votingresults.txt", "w")
print('ELECTION RESULTS')
print('---------------------------')
print ('Total Votes: ',total_votes)
print('---------------------------')
print (f"Kahn: {khan_percent,'%',khan_votes}")
print (f"Li: {li_percent,'%',li_votes}")
print (f"Correy: {correy_percent,'%',correy_votes}")
print (f"O'Tooley: {otooley_percent,'%',otooley_votes}")
print('---------------------------')
print('Winner Khan')
sys.stdout.close()   
