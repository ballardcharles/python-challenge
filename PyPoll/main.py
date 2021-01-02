# import modules
import os
import csv

# create path to read csv file
poll_csv = os.path.join("Resources", "election_data.csv")

with open(poll_csv) as csvfile:
    poll_data = csv.reader(csvfile, delimiter = ",")

    total_votes = []
    next(csvfile)

    for row in poll_data:
        total_votes.append(row[2])

print(len(total_votes))