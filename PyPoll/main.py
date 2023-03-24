from operator import index
import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')
# output for txt file
output = '''Election Results
-------------------------
Total Votes:'''

 # Read the csv and convert 
with open(csvpath, encoding= 'utf') as csvfile:
     #Initialising reader to read csvfile                   
    csvreader = csv.reader(csvfile, delimiter = ',')
    
     # use of next to skip first title row in csv file
    next(csvreader)
    
    total_votes = []
    candidates_votes = ()

    # loop for total number of votes 

    for line in csvreader:
        total_votes.append(line[2])

# calculate total count by number of rows        
total_count = len(total_votes)
# output for txt file
output = output + str(total_count) + "\n" + "-------------------------" + "\n"

# create lists
candidates = list(set(total_votes))
votes_per_candidate = []
percentage = []

# votes per candidate 
for candidate in candidates:
    votes_per_candidate.append(total_votes.count(candidate))

# percentage of votes for each candidate
for i in range (len(candidates)):
    percentage = votes_per_candidate[i]/total_count*100
    output = output + f'{candidates[i]}: {round(percentage,3)}% ({votes_per_candidate[i]}) \n'
# the winner
index_of_winner = votes_per_candidate.index(max(votes_per_candidate))
output = output + f"-------------------------\nWinner: {candidates[index_of_winner]}\n-------------------------"   


# export result to text file and print on terminal
print(output)
csvpath = os.path.join('Analysis', 'election_results.txt')
with open(csvpath,'w') as textfile:
    textfile.write(output)