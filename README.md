# Election_Analysis

## Project Purpose
Our purpose for this challange was to get a better understanding on how python works. Python is a powerful tool that can be uesd to pull date, place it into another file, and also save it to a different file as well. Python can also be difficult at times and you need to make sure you are double and triplechecking your change to make sure everything is running smoothly. Spelling error and in my case indentations are very essential in making python run smoothly. 

## Overview of Election Audit 
A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election. 

1. Calculate the total number of votes cast.
2. Get a Complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidate won.
5. Calculate the amount of votes and percentage per county.
6. Calculate the counties with the largest county voter turnouts. 
7. Determine the winner of the election based on popular vote.

## Election Audit Results
- There were a total of 369,711 votes cast in the election
- The counties that were counted in the election were:
  - Jefferson County
  - Denver County
  - Arapahoe County
- The county results were:
   - Jefferson county received 10.5% of the total votes casted with 38,855 votes cast
   - Denver county received 82.8% of the total votes casted with 306,055 votes cast
   - Arapahoe county received 6.7% of the total votes casted with 24,801 votes cast
- The county with the Largest voter turnout was:
  -Denver county with 306,055 votes cast, reached 82.8% of the total votes cast in the whole election. 
- The Candidates were:
  - Charles Gasper Stockham
  - Diana DeGette
  - Raymon Anthony Doane 
- The candidates results were:
  -Charles Gasper Stockham received 23% of the votes and 85,213 number of votes.
  -Diana DeGette recieved 73.8% of the votes and 272,892 number of votes.
  -Raymon Anthony Doane received 3.1% of the votes and 11,606 number of votes
- The winner of the election was:
  - Diana Degette was the winner receiving 73.8% of the votes and 272,892 number of total votes.
  
## Election Audit Summary
This script that was written for this election audit project is a useful too that can be used for future elections that entails election counting and auditing needs. wE weare able to pull data from the csv file that had 3 different types of data from the columns: Ballot, County, and Candidate voted for. We read the file and analyzed the data by converting it into a text file to understand it better. We were able to use Python to classify the candidates (Charles, Diana, and Raymon) as a list. With that information we were able to create a dictionary to be able to store the names of the candidates as a key and the number of votes they received as a value. We were able to use the same coding format that we used for finding the sum of votes per county to find the county with the largest voter turnout. Using if and statments, we were able to run the data script to pull information like, how many candiates received x amount of votes, percentages from the votes, and was also able to calculate who won the elction. After pulling that information, python was also able to print out the results in a text file to make it more easier to read. 

A couple of examples of how we can use this same script model would be talling up votes for the presendtial election for the country. We can also use this scrpt and tally the number of votes for any major leagues sports All-Star games selctions or even Hall Of Fame induction votes. you can break down the votes by states, political parties, what age were the voters (for elections), or by retired/active players, fans, and league officials(for All-star votes). All in all this script is and will be a very helpful tool to use in the future. 
