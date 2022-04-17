#The data we need to retrieve.
from ast import FormattedValue
import csv
import os
# Assign a variable to load a file from a path
file_to_load =os.path.join("Resources", "election_results.csv")
# Open the election results
with open(file_to_load) as election_data:
    print(election_data)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#NEW VARIABLES
#Initialize a total vote counter
total_votes = 0
#Declare a new list for candidate options
candidate_options = []
#Make a dictionary to count votes for each candidate
candidate_votes = {}
#Winning Candidate and Winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#Open the election results and read the file
with open(file_to_load) as election_data:
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    #Read the header row.
    headers = next(file_reader)
    #Print the header row
    for row in file_reader:
        #Add to total vote count
        total_votes += 1
        #Print the candidate name for each row
        candidate_name = row[2]
        #Determine if the candidate is not already in the current list
        if candidate_name not in candidate_options:
            #Add the candidate name to the list of options
            candidate_options.append(candidate_name)
            #Track votes for each candidate
            candidate_votes[candidate_name] = 0
        #Add a vote to the candidate's count 
        candidate_votes[candidate_name] += 1

    with open(file_to_save, "w") as txt_file:
        election_results = (f"\nElection Results\n" f"-------------------------\n" f"Total Votes: {total_votes:,}\n" f"-------------------------\n")
        print(election_results, end ="")
        #save the final vote count to the text file
        txt_file.write(election_results)
        #Percentage of votes each candidate won
    #iterate through the candidate list
        for candidate_name in candidate_votes:
        #Find votes for each candidate
            votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes in floating points
            vote_percentage = float(votes)/float(total_votes) * 100       
        #Write candidate results to txt file
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            txt_file.write(candidate_results)
            #Determine if vote count is greater than the winning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then winning count = votes and winning % = vote %
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name
        #print each candidate's name, their vote count, and their percentage of votes
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #Print winning candidate name, vote count, and percentage
        winning_candidate_summary = (f"--------------------\n" f"Winner: {winning_candidate}\n" f"Winning Vote Count: {winning_count:,}\n" f"Winning Percentage: {winning_percentage:.1f}%\n" f"---------------------\n")
        #print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)
