import os
import csv
from typing import final 

# Path to csv file
filePath = os.path.join("Resources","budget_data.csv")
with open(filePath,'r') as file: 
    data = csv.reader(file)
    # Get header
    header = next(data)
    # Initialise variables 
    # Number of months (also number of rows)
    noOfMonths = 0
    # Net total of Profit/Loss
    netTotal = 0
    # Changes in profit/loss
    changes = []
    # Convert data to a list object to make data easier to manipulate
    datList = []

    # Number of months is equal to number of rows (not including header)
    # Loops through file and counts rows
    for row in data:
        noOfMonths += 1
        netTotal += int(row[1])
        datList.append(row)

    # Create a change list
    for i in range(noOfMonths -1):
        # Make changes list same length as datList (for next for loop)
        datList[i+1][1] = int(datList[i+1][1])
        datList[i][1] = int(datList[i][1])
        if i == 0:
            changes.append(datList[i+1][1]-datList[i][1])
        changes.append(datList[i+1][1] - datList[i][1])

    # Caluclate average change for entire period
    averageChange = round(sum(changes[1:])/(len(changes)-1),2)

    # Initialise date and amount variables
    # Greatest Increase
    incDate = ""
    incAmount = datList[0][1]
    # Greatest Decrease
    decDate = ""
    decAmount = datList[0][1]

    # Find greatest increase/decrease in profits and correspondiong dates
    for index in range(noOfMonths):
        if changes[index] > incAmount :
            incAmount = changes[index]
            incDate = datList[index][0]
        if changes[index] < decAmount :
            decAmount = changes[index]
            decDate =  datList[index][0]

# Print the results to a txt file

with open('results.txt',"w") as results:
    title = "Financial Analysis"
    finalList = ['Financial Analysis',
    '-'*(len(title)+10),
    f'Total Months: {noOfMonths}',
    f'Total: ${netTotal}',
    f'Average Change: ${averageChange}',
    f'Greatest Increase in Profits: {incDate} (${incAmount})',
    f'Greatest Increase in Profits: {decDate} (${decAmount})']
    for element in finalList:
        results.write(element + "\n")