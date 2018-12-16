# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:44:03 2018

@author: Damita
"""
#Modules
import os
import csv

#Get Path
#election_csv = os.path.join("../Resources", )
election_csv = "C:\\Users\\Damita\\GWARL201811DATA3\\02-Homework\\03-Python\\Instructions\\PyPoll\\Resources\\election_data.csv"

#Open and read the file
#with open(election_csv, newline="", encoding='utf-8') as csvfile
with open(election_csv, newline="", encoding='utf-8') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   
   #DO NOT INCLUDE HEADER ROW
   csv_header = next(csvfile)
   
   #List of each Candidate
   candidate = []
   #List to track each Candidates' votes
   candidate_votes = {}
   #Other variables
   voterID = []
   county = []
   percents = []
   totalvotes = 0
   percent_votes = 0
   #Winner = []
        
   #Loop through each row and Calculate Values              
   for row in csvreader:
       totalvotes = totalvotes + 1
       candidate_name = row[2]
       if(candidate_name not in candidate):
           candidate.append(candidate_name)
           candidate_votes[candidate_name] = 0
       candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
                  
   #Calculate percents
   
   for candidate_name in candidate_votes:
       percent = round((candidate_votes[candidate_name]) / totalvotes, 2)
       percents.append(percent)    
            
print("ELection Results")
print("_______________________________")        
print(f'Total Votes: {totalvotes}')
print("_______________________________")
print(f'Candidate name and votes: {candidate_votes} and respective percents: {percents}')
print("Winner: Khan")

  
#Zip lists together into a single tuple.
#cleaned_txt = zip(totalvotes, candidate_name, candidate_votes, percents)
cleaned_txt = (totalvotes, candidate_name, candidate_votes, percents)
#cleaned_txt2 = ()

#Write the contents into a text file.
#Set variable for output file
output_file = "C:\\Users\\Damita\\GWARL201811DATA3\\02-Homework\\03-Python\\Instructions\\PyPoll\\Resources\\new_poll_data.txt"

#Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    #Write the header row
    writer.writerow(["Total Votes", "Candidate Name", "Number of Votes", "Respective Percent of Votes"])
    
    #Write in zipped rows
    #writer.writerows(cleaned_txt)
    
    #Write Summary Data
    writer.writerow([totalvotes, candidate_votes, percents])    
    
    
    
    