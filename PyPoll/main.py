# import modules
import os
import csv

# specify source path
election_csv=os.path.join("election_data.csv")

# create list to store data
Candidate=[]


# open the csv file
with open (election_csv,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')

    # skip header
    header = next(csvfile)

    for row in csvreader:

        # list all candidate names
        Candidate.append(row[2])

# Calculate total vote
Total_Vote = len(Candidate)

# print summary
print("Election Results")
print("------------------------------")
print(f'Total Votes: {Total_Vote}')
print ("-----------------------------")
