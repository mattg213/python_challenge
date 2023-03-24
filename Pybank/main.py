import os
import csv    

budget_csv = os.path.join("Resources", "budget_data.csv")


# Read the csv and convert it into a list of dictionaries
with open(budget_csv) as profit_data:
    reader = csv.reader(profit_data)

    # use of next to skip first title row in csv file
    next(reader) 

    # create lists
    profit = []
    date = []
    change = []

    # loop for sum of column 1 which is profit/loss in csv file and counted total months which is column 0 
    for row in reader:

        profit.append(float(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total: $", sum(profit))


    # loop for total of difference between all row of column profits to find total revenue change, max revenue change and min revenue change. 
    for i in range(1,len(profit)):
        change.append(profit[i] - profit[i-1])  
        avg_change = sum(change)/len(change)
        max_change = max(change)
        min_change = min(change)
        max_change_date = str(date[change.index(max(change))+1])
        min_change_date = str(date[change.index(min(change))+1])    
        
    print("Average Change: $", round((avg_change)))
    print("Greatest Increase:", max_change_date,"($", max_change,")")
    print("Greatest Decrease:", min_change_date,"($", min_change,")")

csvpath = os.path.join('Analysis', 'financial_analysis.txt')
with open(csvpath,'w') as text_file:
    print("Financial Analysis", file=text_file)
    print("-----------------------------------", file=text_file)
    print("Total Months:", len(date), file=text_file)
    print("Total: $", sum(profit), file=text_file)
    print("Average Change: $", round((avg_change)), file=text_file)
    print("Greatest Increase:", max_change_date,"($", max_change,")", file=text_file)
    print("Greatest Decrease:", min_change_date,"($", min_change,")", file=text_file)