# import modules
import os
import csv

# create path to read csv file
poll_csv = os.path.join("Resources", "election_data.csv")

# define variables and lists
vote_total = 0
candidates = []
candidate_votes = []

# open election results csv 
with open(poll_csv) as csvfile:

    poll_data = csv.reader(csvfile, delimiter = ",")

    next(csvfile)

    # iterate through election results tabulating vote totals, creating list of candidats and how many votes was cast for each candidate
    for row in poll_data:
        # counting total number of votes cast
        vote_total = vote_total + 1
        # using if statement to create list of candidates and tabulate each candidates votes
        if row[2] in candidates:
            candidate_index = candidates.index(row[2])
            candidate_votes[candidate_index] = candidate_votes[candidate_index] + 1
        else:
            candidates.append(row[2])
            candidate_votes.append(1)

# determining which candidate received the most votes
winner = candidates[candidate_votes.index(max(candidate_votes))]

# print election results to the terminal
print("Election Results")
print("------------------------")
print(f"Total Votes: {vote_total}")
print("------------------------")
for row in range(len(candidates)):
    print(f"{candidates[row]}: {candidate_votes[row]/vote_total*100:.3f}% ({candidate_votes[row]})")
print("------------------------")
print(f"Winner: {winner}")
print("------------------------")

# # Specify the file to write to
output = os.path.join("Analysis", "PyPoll.txt")

# # Open the file using "write" mode. Specify the variable to hold the contents.  Write election results to txt file
with open(output, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("------------------------\n")
    txtfile.write(f"Total Votes: {vote_total}\n")
    txtfile.write("------------------------\n")
    for row in range(len(candidates)):
        txtfile.write(f"{candidates[row]}: {candidate_votes[row]/vote_total*100:.3f}% ({candidate_votes[row]})\n")
    txtfile.write("------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("------------------------\n")