# Title Sections

from pathlib import Path
import csv

csvpath = ("../budget_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    date = []
    profit = []
    profit_change = []
    list1 = []
    
    list1.append("Financial Analysis")
    list1.append("----------------------------")

    for row in csvreader:
        date.append(row[0])
        profit.append(float(row[1]))       

# The total number of months included in the dataset.

    str1 = "Total Months:" + str(len(date))
    list1.append(str1)

# The net total amount of Profit/Losses over the entire period.

    str2 = "Total:" + str(round(sum(profit)))
    list1.append(str2)

# The average of the changes in Profit/Losses over the entire period.

    for x in range(1,len(profit)):
        profit_change.append(profit[x] - profit[x-1])
        average_profit_change = sum(profit_change) / len(profit_change)              
               
    str3 = "Average Change: $" + str(round(average_profit_change,2))
    list1.append(str3)

# The greatest increase in profits (date and amount) over the entire period.
    maximum_profit_change = (max(profit_change))
    maximum_profit_change_date = str(date[profit_change.index(max(profit_change))+1])
    
    str4 = "Greatest Increase in Profits:" + str(maximum_profit_change_date) + "($" + str(round(maximum_profit_change)) + ")"  
    list1.append(str4)
    
# The greatest decrease in losses (date and amount) over the entire period.

    minimum_profit_change = (min(profit_change))
    minimum_profit_change_date = str(date[profit_change.index(min(profit_change))+1])
    
    str5 = "Greatest Decrease in Profits:" + str(minimum_profit_change_date)+ "($" + str(round(minimum_profit_change)) + ")"
    list1.append(str5)
    
    output_path = Path("PyBank_output.txt")    

    with open(output_path, 'w') as file:
        for i in list1:
            print(i)
            file.write(i + "\n")