#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

#add our dependencies
import csv
import os

path = os.path.join("C:", "Documents", "GitHub", "Election_Analysis")

# Assign a variable for the file to load and the path.
#this is what it was suppoed to be file_to_load = os.path.join(".." "Resources", "election_results.csv")
file_to_load = os.path.join(path, "Resources", "election_results.csv")

# Assign a variable to save file to a path
file_to_save = os.path.join(path, "analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0 

#Candidate Options
candidate_options = []

#1. Declare the empty dictionary. 
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#open the election results and read the file.
with open(file_to_load) as election_data:

    #Read the file object witht he reader function.
    file_reader = csv.reader(election_data)

    #Read and print the header row.
    headers = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        #Print the candidate name from each row.
        candidate_name = row[2]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of cadidates.
            candidate_options.append(candidate_name)

            #2. Begin tracking the candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
    
    #Determine the percentage of votes for each candidate by looping through thw counts.
    # 1. Iterate through the candidate liste.
    for candidate_name in candidate_votes:
        #2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

        #3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        #4. Print the candidate name and percentage of votes.
        print(f"{candidate_name}: received {vote_percentage}% of the vote.")

        # Determine winning vote count and candidate

        #1. Determine if the votes are greter than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #2. If true then set winning_count = vote and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage

            #3. Set the winning_candidate equalto the candidate's name.
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"--------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------\n")
    print(winning_candidate_summary)

    
    #To do: print out the winning candidate, vote count and percentage to terminal 
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        

    


    #print the candidate vote dictionary
    print(candidate_votes)

# 3. Print the total votes.
print(total_votes)


#To do: read and analyze data here.

#use the open statement to open the file as a text file. 
outfile = open(file_to_save, "w")

#Write some data to the file. 
outfile.write("Hello World")

#close the file
outfile.close()


#Open the election results and read the file.
with open(file_to_save, "w") as txt_file:

    #Write some data to the file.
    #Write the three counties to the file and removed Hello World and make into separate lines
    txt_file.write("Counties in the Election\n---------\nArapahoe\nDenver\nJefferson")
    






#Using the with statement open the file as a text file
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
