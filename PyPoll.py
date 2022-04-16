#The data we need to retrieve.
import csv
import os
# Assign a variable to load a file from a path
file_to_load =os.path.join("Resources", "election_results.csv")
# Open the election results
with open(file_to_load) as election_data:
    print(election_data)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:
    #Write three counties to the file
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\n")
    txt_file.write("Denver\n")
    txt_file.write("Jefferson")
#Open the election results and read the file
with open(file_to_load) as election_data:
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    #Print the header row
    headers = next(file_reader)
    print(headers)
    
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. Th total number of votes each candidate won
# 5. The winner of the elction based on popular vote
