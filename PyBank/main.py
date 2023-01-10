# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

# Import dependencies
import os
import csv

# Define variables
Date = []
profit_loss_changes =[]

total_months = 0
total_profit_loss = 0
prior_month_pl = 0
current_month_pl = 0
profit_loss_change = 0



# change directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# path to the budget_data file from the resources folder
budgetfile_csvpath = os.path.join('Resources', 'budget_data.csv')

# Open and read csv
with open(budgetfile_csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvfile)
    # Read through each row of data
    for row in csvreader:
        total_months += 1
        prior_month_pl = int(row[1])
        total_profit_loss += prior_month_pl
    # print(total_profit_loss)
    # print(total_months)
    if (total_months != 1):
        profit_loss_change = current_month_pl - prior_month_pl
         
    else:
        # compute change in profit loss
        profit_loss_change = current_month_pl

    # add the original dates to the date list
    Date.append(row[0])
    profit_loss_changes.append(profit_loss_change)

#sum and average of the changes in "Profit/Losses" over the entire period
total_profit_loss_change= sum(profit_loss_changes)
average_change = round(total_profit_loss_change/(total_months - 1), 2)
print(average_change)

# highest and lowest changes in "Profit/Losses" over the entire period
greatest_increase = max(profit_loss_changes)
greatest_decrease = min(profit_loss_changes)
print(greatest_increase)
print(greatest_decrease)

    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
highest_month_index = profit_loss_changes.index(greatest_increase)
lowest_month_index = profit_loss_changes.index(greatest_decrease)

greatest_increase_date = Date[highest_month_index]
greatest_decrease_date = Date[lowest_month_index]
print(greatest_increase_date)
print(greatest_decrease_date)

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {total_months}")
print(f"Total:  ${total_profit_loss}")
print(f"Average Change:  ${average_change}")
print(f"Greatest Increase in Profits:  {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Losses:  {greatest_decrease_date} (${greatest_decrease})")


# -->>  Export a text file with the results
Pybank_file = os.path.join("Output", "financial_analysis_result.txt")
with open(Pybank_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {total_months}\n")
    outfile.write(f"Total:  ${total_profit_loss}\n")
    outfile.write(f"Average Change:  ${average_change}\n")
    outfile.write(f"Greatest Increase in Profits:  {greatest_increase_date} (${greatest_increase})\n")
    outfile.write(f"Greatest Decrease in Losses:  {greatest_decrease_date} (${greatest_decrease})\n")