#Python script to analyze financial records of a company
import os
import csv

#Store the path of the desired file
budget_path = os.path.join('.','Resources', 'budget_data.csv')

#Lists to store data from file
months = []
profit = []

#Read budget_data.csv file
with open(budget_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip the header column
    header = next(csvreader)

    #Create lists from the columns in budget_data.csv
    for row in csvreader:
            months.append(row[0])
            profit.append(row[1])

#Store value of the total number of months in the list of months, and length of the profit list
Total_months = len(months)
Profit_Length = len(profit)

#Set initial value of the total profit to equal zero
Total_profit = 0

#Add all the values in the list of profit/loss together to determine total profit
for number in profit:
    Total_profit = int(Total_profit) + int(number)

#Create a list of profit changes between consectuive months
Change = []

#Iterate through the profit list, and subtract consectutive values from one another to create a Change list
for x in range(Profit_Length):
    if x > 0:
        difference = int(profit[x])- int(profit[x-1])
        Change.append(difference)

#Set Total Change equal to zero
Total_change = 0

#Find the sum, or Total change, of the Change list
for number in Change:
    Total_change = float(Total_change) + float(number)

#Calculate average for the list of changes, and store it
Average_change = round(Total_change / len(Change),2)

#Set the greatest increase and greatest decrease values to zero
Greatest_increase = 0
Greatest_decrease = 0

#Loop through data to find greatest increase and greatest decrease values, and set the
#index number in the change list equal to the index of the months list + 1
for i,x in enumerate(Change):
    if x > Greatest_increase:
        Greatest_increase = x
        index = i
        Increase_month = months[i+1]
    elif x < Greatest_decrease:
        Greatest_decrease = x
        index = i
        Decrease_month = months[i+1]

#Print all Financial Analysis information in terminal
print("Financial Analysis")
print("-------------------------------")      
print("Total Months: " +str(Total_months))
print("Total : $" + str(Total_profit))
print("Average Change: $" + str(Average_change))
print("Greatest Increase in Profits: " + str(Increase_month) +" ($" + str(Greatest_increase) +")")
print("Greatest Decrease in Profits: " + str(Decrease_month) +" ($" + str(Greatest_decrease) +")")

#Print all Financial Analysis information in a text file
f = open("Financial_Analysis.txt", 'w')
f.write("Financial Analysis\n")
f.write("-------------------------------\n")      
f.write("Total Months: " +str(Total_months) + "\n")
f.write("Total : $" + str(Total_profit) +"\n")
f.write("Average Change: $" + str(Average_change) + "\n")
f.write("Greatest Increase in Profits: " + str(Increase_month) +" ($" + str(Greatest_increase) +")\n")
f.write("Greatest Decrease in Profits: " + str(Decrease_month) +" ($" + str(Greatest_decrease) +")\n")