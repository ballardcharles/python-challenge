# import modules
import os
import csv

# create path to read csv file
budget_csv = os.path.join("Resources", "budget_data.csv")

print("Financial Analysis")
print("-------------------------")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvfile)

    months = list(csvreader)
    count = len(months)

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvfile)
    total = 0
    for row in csvreader:
        total += int(row[1])

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(csvfile)
    
    max_increase = max(csvreader, key=lambda row: int(row[1]))

average = total / count

print(f"Total Months: {count}")
print(f"Total: ${total}") 
print(f"Average Change: ${average}")
print(f"Greatest Increase: {str(max_increase)}")
