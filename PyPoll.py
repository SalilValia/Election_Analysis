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

#Candidate Options and candidate votes
candidate_options = [] 
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
        # Add to the total vote count.
        total_votes += 1
        #Print the candidate name from each row.
        candidate_name = row[2]
        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of cadidates.
            candidate_options.append(candidate_name)
            # Begin tracking the candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

#Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file
            
        
    #Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate liste.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the candidate name and percentage of votes.
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes})\n")
        
        #Print each candidate's voter count and percentage to the terminal. 
        print(candidate_results)
        txt_file.write(candidate_results)


        # Determine winning vote count and candidate
        #To do: print out the winning candidate, vote count and percentage to terminal 
        # Determine if the votes are greter than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = vote and winning_percent = vote_percentage
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    #Print the winning candidates' results to the terminal.        
    winning_candidate_summary = (
        f"--------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------\n")    
    print(winning_candidate_summary)
    #Save the winning candidate's results to the text file. 
    txt_file.write(winning_candidate_summary)    

    



