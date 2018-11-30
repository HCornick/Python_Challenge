import os
import csv

#Store the path of the desired file
election_path = os.path.join('.','Resources', 'election_data.csv')

#Lists to store data from file
Voter = []
County = []
Candidate = []

#Read budget_data.csv file
with open(election_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip the header column
    header = next(csvreader)

    #Create lists from the columns in budget_data.csv
    for row in csvreader:
            Voter.append(row[0])
            County.append(row[1])
            Candidate.append(row[2])

#Store value of the total number of voters from the list of Voters
Total_votes = len(Voter)

#Create a list of the unique candidates, and set the first candidate to row[0] in Candidate list
Unique_candidate = []
Unique_candidate.append(Candidate[0])

#Loop through Candidate list
for x in Candidate:
    #Loop through Unique_candidate list, which only has one candidate to start
    for y in Unique_candidate:
        #If the unique candidate matches the candidate on the list, set match to 'True', and break loop
        #to test the next candidate in the candidates list
        if y == x:
            match = True
            #break if you find a match in the unique candidate list
            break
    #If match is set to 'True,' and we find a candidate on the candidates list that does not match
    #any unique candidate, then we set match to 'False'
    if match == True:
        match = False
        continue
    else:
        Unique_candidate.append(x)

Cand_votes = []
for x in Unique_candidate:
    Cand_votes.append(0)

for index,each in enumerate(Unique_candidate):
    for x in Candidate:
        if x == each:
            Cand_votes[index] += 1

print("Election Results")
print("---------------------------")
print("Total Votes: " + str(Total_votes))
print("---------------------------")
for index,x in enumerate(Cand_votes):
    Vote_percent = (100.0*x)/Total_votes
    print(str(Unique_candidate[index]) + ": " + str("%.3f" % Vote_percent) + "% (" + str(x) + ")")
print("---------------------------")
Winner = max(Cand_votes)
for index,x in enumerate(Cand_votes):
    if x == Winner:
        print("Winner: " + str(Unique_candidate[index]))
    break
print("---------------------------")

#Print all Election Results information in a text file
e = open("Election_Results.txt", 'w')
e.write("Election Results\n")
e.write("---------------------------\n")
e.write("Total Votes: " + str(Total_votes) + "\n")
e.write("---------------------------\n")
for index,x in enumerate(Cand_votes):
    Vote_percent = (100.0*x)/Total_votes
    e.write(str(Unique_candidate[index]) + ": " + str("%.3f" % Vote_percent) + "% (" + str(x) + ")\n")
e.write("---------------------------\n")
for index,x in enumerate(Cand_votes):
    if x == Winner:
        e.write("Winner: " + str(Unique_candidate[index]) + "\n")
    break
e.write("---------------------------\n")