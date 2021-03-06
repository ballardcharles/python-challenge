# import modules
import os
import csv

# create path to read csv file
budget_csv = os.path.join("Resources", "budget_data.csv")

# open csv file to analysis data
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    # define empty lists to store profit/loss data, set change in revenue list to start with 0 as the first month will have no change
    profit_loss = []
    change = [0]
    date = []
    csv_header = next(csvfile)
    
    # loop through the csv file to compile the date and profit_loss lists
    for row in csvreader:
        date.append(row[0])
        profit_loss.append(int(row[1]))

    # determine the total number of months in the list and sum the total profit for the timeframe
    num_dates = len(date)
    total_profit_loss = sum(profit_loss)

    # loop through list to determine the difference between each month of the list, find the largest and smallest difference and the average change 
    for row in range(1,len(profit_loss)):
        change.append(profit_loss[row] - profit_loss[row-1])

        # find the greatest increase and decrease in profits 
        max_change = max(change)
        min_change = min(change)

        total_change = sum(change)
        # calculate average change in profit
        average_change = total_change / (len(change)-1)

        # find the corresponding date to the greatest increase and decrease in profit
        max_change_date = str(date[change.index(max(change))])
        min_change_date = str(date[change.index(min(change))])

# create summary data variable to hold profit/loss analysis
summary_data = (
    f"Financial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {num_dates}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${round(average_change, 2)}\n"
    f"Greatest Increase in Profits: {max_change_date} (${max_change})\n"
    f"Greatest Decrease in Profits: {min_change_date} (${min_change})\n"
)
# print profit/loss summary to terminal
print(summary_data)

# Specify the file to write to
output = os.path.join("Analysis", "PyBank.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output, 'w') as txtfile:

    txtfile.write(summary_data)