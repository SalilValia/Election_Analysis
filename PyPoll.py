#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

#add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join('C:', 'Documents', 'GitHub', 'Election_Analysis', "Resources", "election_results.csv")

# Assign a variable to save file to a path
file_to_save = os.path.join('C:', 'Documents', 'GitHub', 'Election_Analysis', "analysis", "election_analysis.txt")

#Open the election results and read the file.

with open(file_to_load) as election_data:

    reader = csv.reader(election_data)
    print(reader)


# Print the file object
print(election_data)
    
#Assign a variable to for the file to load and a path
file_to_load = 'Resources/election_results.csv'

#open the election results and read the file. 
election_data = open(file_to_load, 'r')

#To do: perform analysis

#close the file. 
election_data.close()

#Open the election results and read the file.
with open(file_to_load) as election_data:
    #Need to read and anlysis the data here
    #Also need to read the file with a reader function
    file_reader = csv.reader(election_data)
