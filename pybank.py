# Importing the necessary libraries for reading csv files
import os
import csv
# Setting the path for the csv file
csvpath = os.path.join("..","budget_data.csv")
#Setting Varibales
total_months = 0
total_net = 0
average = 0
net_change_list = []
greatest_increase_in_profits = ["",0]
greatest_decrease_in_profits = ["",0]
month_of_change = []
#Open the csv file
with open (csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    first_row = next(csvreader)
    total_months = total_months+1
    total_net = total_net + int(first_row[1])
    previous_net = int(first_row[1])
    for row in csvreader:
        total_months = total_months +1
        total_net = total_net +int(row[1])
        change_net = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list = net_change_list + [change_net]
        if change_net > greatest_increase_in_profits[1]:
            greatest_increase_in_profits[0]=row[0]
            greatest_increase_in_profits[1]=change_net
        if change_net < greatest_decrease_in_profits[1]:
            greatest_decrease_in_profits[0]=row[0]
            greatest_decrease_in_profits[1]=change_net

#Printing the results   
print("                   Pybank Assignment") 
print("-------------------Financial Analysis-------------------")
#The total number of months included in the dataset
print(f"The total number of months included in the dataset:")
print(total_months)
#The net total amount of Profit/Losses over the entire period
print(f"The net total amount of Profit/Losses over the entire period:")
print(total_net)
#The average of the changes in Profit/Losses over the entire period
average_of_the_change = sum(net_change_list)/total_months
print(f"The average of the changes in Profit/Losses over the entire period:")
print(average_of_the_change)
#The greatest increase in profits (date and amount) over the entire period
print(f"The greatest increase in profits (date and amount) over the entire period:")
print(greatest_increase_in_profits)
#The greatest decrease in losses (date and amount) over the entire period
print(f"The greatest decrease in losses (date and amount) over the entire period:")
print(greatest_decrease_in_profits)


