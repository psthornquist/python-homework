# Title Sections

print("Financial Analysis")
print("----------------------------")

#Import file and include path

from pathlib import Path
import csv

csvpath = ("../budget_data.csv")

#Open the CSV file, use next to skip the header titles

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    date = []
    profit = []
    profit_change = []

    #Separate the 2 columns into their own variables. Column 1 is now "date" and column 2 is "profit"
    for row in csvreader:
        date.append(row[0])
        profit.append(float(row[1]))       

# The total number of months included in the dataset. Use len to find the length of the list, which will give us the total number of months because header was already removed.

    print("Total Months:", len(date))

# The net total amount of Profit/Losses over the entire period. Use sum function to get the total for the profit column. Use round to make this a whole number. 

    print("Total:", round(sum(profit)))

# The average of the changes in Profit/Losses over the entire period. To figure out the daily change, take the current day profit and subtract the previous day profit. Range starts at 1 because we don't need the first day subtracting 0. This will then be put into a new list called profit_change. To get the average, find the total of the daily changes and divide them by total number of changes. Use round function to get to 2nd decimal place. 

    for x in range(1,len(profit)):
        profit_change.append(profit[x] - profit[x-1])
        average_profit_change = sum(profit_change) / len(profit_change)              
               
    print("Average Change: $", round(average_profit_change,2))

# The greatest increase in profits (date and amount) over the entire period. Use max function to find the greated profit change in new list. Then use index function to find the original location of the date that aligns with that profit change. Add 1 to get the 2nd month out of the two months used in the equation.
    maximum_profit_change = (max(profit_change))
    maximum_profit_change_date = str(date[profit_change.index(max(profit_change))+1])
    
    print("Greatest Increase in Profits:",maximum_profit_change_date,"($",round(maximum_profit_change),")")  

# The greatest decrease in losses (date and amount) over the entire period. Same course of action as the greatest increase, but change max to min function.

    minimum_profit_change = (min(profit_change))
    minimum_profit_change_date = str(date[profit_change.index(min(profit_change))+1])
    
    print("Greatest Decrease in Profits:",minimum_profit_change_date,"($",round(minimum_profit_change),")")

 
output_path = Path("PyBank_output.txt")    

with open(output_path, 'w') as file:
    file.write()