# Vote-counting process
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote


# Import dependencies
import os
import csv
import collections
from collections import Counter

# Define PyPoll's variables
voters = []
votes_per_candidate = []

# Change directory to the directory of current python script
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Path to collect data from the Resources folder
electionfile_csv_path = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(electionfile_csv_path) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csvheader = next(csvfile)


    # Read through each row of data after the header
    for row in csvreader:

        voters.append(row[2])

    # Sort the list by default ascending order
    sorted_voters = sorted(voters)

    # Arrange the sorted list by most common outcomes
    arrange_list = sorted_voters

    #count votes per candidate in most common outcome order and append to a list
    count_candidate = Counter (arrange_list) 
    votes_per_candidate.append(count_candidate.most_common())

    # calculate the percentage of votes per candicate in 3 digital points
    for item in votes_per_candidate:
       
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
   
# Print the analysis to the terminal
#print("Election Results")
#print("-------------------------")
#print(f"Total Votes:  {sum(count_candidate.values())}")
#print("-------------------------")
#print(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})")
#print(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})")
#print(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})")
#print("-------------------------")
#print(f"Winner:  {votes_per_candidate[0][0][0]}")
#print("-------------------------")


# Export a text file with the results
Pypoll_file = os.path.join("Output", "election_result.txt")
with open(Pypoll_file, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes:  {sum(count_candidate.values())}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})\n")
    outfile.write(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})\n")
    outfile.write(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner:  {votes_per_candidate[0][0][0]}\n")
    outfile.write("-------------------------\n")    