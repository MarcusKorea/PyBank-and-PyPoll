import os
import csv


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


    # Set winner to the first person in the list
    winner = ""

    # Find the winner
    for index in range(len(candidates)-1):
        if index == 0:
            if candidates[index][2] > candidates[index + 1][2]:
                winner = candidates[0]
            else:
                winner = candidates[1]
            index += 1
        else:
            if winner[2] < candidates[index][2]:
                winner = candidates[index]

    # Output
    title = "Election Results"
    finalList = [title,
                '-'* (len(title) + 9),
                f"Total Votes: {votes}",
                '-'* (len(title) + 9),
                f"{candidates[0][0]}: {candidates[0][1]}% ({candidates[0][2]})",
                f"{candidates[1][0]}: {candidates[1][1]}% ({candidates[1][2]})",
                f"{candidates[2][0]}: {candidates[2][1]}% ({candidates[2][2]})",
                f"{candidates[3][0]}: {candidates[3][1]}% ({candidates[3][2]})",
                '-'* (len(title) + 9),
                f'Winner: {winner[0]}',
                '-'* (len(title) + 9)]
    # Path to Output file
    outPath = os.path.join("analysis","results.txt")

    # Write output to txt file
    with open(outPath,'w') as results:
        for element in finalList:
            results.write(element+ "\n")
