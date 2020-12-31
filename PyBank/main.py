# import modules
import os
import csv

# create path to read csv file
budget_csv = os.path.join("Resources", "budget_data.csv")

print("Financial Analysis")
print("-------------------------")

# with open(budget_csv) as csvfile:
#     csvreader = csv.reader(csvfile, delimiter = ",")

#     csv_header = next(csvfile)

#     months = list(csvreader)
#     count = len(months)

# with open(budget_csv) as csvfile:
#     csvreader = csv.reader(csvfile, delimiter = ",")

#     csv_header = next(csvfile)
#     total = 0
#     for row in csvreader:
#         total += int(row[1])

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    profit_loss = []
    change = []
    date = []
    csv_header = next(csvfile)
    
    for row in csvreader:
        date.append(row[0])
        profit_loss.append(int(row[1]))

    num_dates = len(date)
    total_profit_loss = sum(profit_loss)

    for row in range(1,len(profit_loss)):
        change.append(profit_loss[row] - profit_loss[row-1])

        max_change = max(change)
        min_change = min(change)

        total_change = sum(change)
        average_change = total_change / len(change)

print(f"Total Months: {num_dates}")
print(f"Total: ${total_profit_loss}") 
print(f"Average Change: ${average_change}")
print(f"Greatest Increase: {max_change}")
print(f"Greatest Decrease: {min_change}")