# import modules
import os
import csv

# create path to read csv file
poll_csv = os.path.join("Resources", "election_data.csv")

# define variables
vote_total = 0
candidates = []
candidate_votes = []

with open(poll_csv) as csvfile:

    poll_data = csv.reader(csvfile, delimiter = ",")

    next(csvfile)

    for row in poll_data:
        vote_total = vote_total + 1

        if row[2] in candidates:
            candidate_index = candidates.index(row[2])
            candidate_votes[candidate_index] = candidate_votes[candidate_index] + 1
        else:
            candidates.append(row[2])
            candidate_votes.append(1)

max_votes = candidates[candidate_votes.index(max(candidate_votes))]

print("Election Results")
print("------------------------")
print(f"Total Votes: {vote_total}")
print("------------------------")
for row in range(len(candidates)):
    print(f"{candidates[row]}: {candidate_votes[row]/vote_total*100:.3f}% ({candidate_votes[row]})")
print("------------------------")
print(f"Winner: {max_votes}")
print("------------------------")