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

print(vote_total)
print(candidates)
print(candidate_votes)
print(f"{candidates[0]}: {candidate_votes[0]/vote_total*100:.3f}% ({candidate_votes[0]})")
print(f"{candidates[1]}: {candidate_votes[1]/vote_total*100:.3f}% ({candidate_votes[1]})")
print(f"{candidates[2]}: {candidate_votes[2]/vote_total*100:.3f}% ({candidate_votes[2]})")
print(f"{candidates[3]}: {candidate_votes[3]/vote_total*100:.3f}% ({candidate_votes[3]})")