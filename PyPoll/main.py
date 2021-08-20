import os
import csv
from typing import final

filePath = os.path.join("Resources","election_data.csv")

# Read file
with open(filePath, 'r') as file:
    data = csv.reader(file)
    
    # Get header
    header = next(data)


    # Initialise variables
    votes = 0
    khanVotes = 0
    correyVotes = 0
    liVotes = 0
    tooleyVotes = 0
    names = []

    # Count amount of voters
    for row in data:
        votes += 1
        if row[2] == "Khan":
            khanVotes += 1
        elif row[2] == "Correy":
            correyVotes += 1
        elif row[2] == "Li":
            liVotes += 1
        elif row[2] == "O'Tooley":
            tooleyVotes += 1

    # Find percentage each candidate one, format to 3dp
    khanPerc = format(khanVotes/votes * 100,'.3f')
    correyPerc = format(correyVotes/votes * 100,'.3f')
    liPerc = format(liVotes/votes * 100,'.3f')
    tooleyPerc = format(tooleyVotes/votes * 100,'.3f')
    
    # Store values in list for the candidates
    candidates = [["Khan", khanPerc,khanVotes],["Correy",correyPerc,correyVotes],["Li",liPerc,liVotes],["O'Tooley",tooleyPerc, tooleyVotes]]

    khan = ["Khan", khanPerc,khanVotes]
    correy = ["Correy",correyPerc,correyVotes]
    li = ["Li",liPerc,liVotes]
    tooley = ["O'Tooley",tooleyPerc, tooleyVotes]

    winner = []
    for index in range(3):
        if candidates[index + 1][2] > candidates[index][2]:
            winner.append(candidates[0][2])

    # Output
    title = "Election Results"
    finalList = [title,
                '-'* (len(title) + 9),
                f"Total Votes: {votes}",
                '-'* (len(title) + 9),
                f"{khan[0]}: {khan[1]}% ({khan[2]})",
                f"{correy[0]}: {correy[1]}% ({correy[2]})",
                f"{li[0]}: {li[1]}% ({li[2]})",
                f"{tooley[0]}: {tooley[1]}% ({tooley[2]})",
                '-'* (len(title) + 9),
                f'Winner: {winner}',
                '-'* (len(title) + 9)]
    
    # Write output to txt file
    with open("results.txt",'w') as results:
        for element in finalList:
            results.write(element+ "\n")
