#this script will help a small town to modernize their voting candidates system,provided by a csv file
"""
we will have to calculate:
-the tota numbers of votes of cast
-a completed list of candidates who receibed votes
-the percentage of votes each candidate won
-the total number of votes each candidate won
-the winner of the election based on popular vote

 """

#importing the modules
import pandas as pd
import statistics as st
import csv
import os

#Decided to use pandas to get a detailed data info and store it on separated list
votingResults = pd.read_csv('PyPoll/Resources/election_data.csv')
votingResults.info()
print(len(votingResults['Ballot ID'].unique()))
print(votingResults['Candidate'].unique())
print(votingResults['County'].unique())
candidates = votingResults["Candidate"].unique()
counties = votingResults['County'].unique()

"""
whith this Detailed data info we discovered:
 -there are only 3 candidates, and 3 conties voted
 -candidates: Charles, Diana, Raymon
 -conties: Jefferson, Denver, Arapahoe
 -No one voted twice
"""
#opening the file
def Voting_Analysis():
    with open('PyPoll/Resources/election_data.csv') as results_csv:
        #Defining variables
        results = csv.reader(results_csv)
        header = next(results)
        total_votes = 0
        dic_candidates_votes = {}
        winner_votes = 0
        winner_name = ''

        for rows in results:
            #Counting how many voted
            total_votes +=1
            #storing the data on a dictionarie counting the votes per candidate
            if rows[2] not in dic_candidates_votes:
                dic_candidates_votes[rows[2]] = 1
            else:
                dic_candidates_votes[rows[2]]+=1
        #Looping throught dic_candidate to determine the WINNER
        for winner in dic_candidates_votes.items():
            candidate,votes = winner
            if votes>winner_votes:
                winner_votes = votes
                winner_name = candidate
          
        #printing stage
        print('Election Results \n ')
        print('-'*30+ '\n')
        print(f'Total votes: {total_votes} \n')
        print('-'*30+ '\n')
        #Printing the results over the dic we have already created
        for stats in dic_candidates_votes.items():
            candidate,votes = stats
            print(f'{candidate}: {round((votes/total_votes)*100,3)}% ({votes}) \n')
        print('-'*30+ '\n')
        print(f'The winner is: {winner_name} with: {winner_votes} votes')

        #Storing on a .TXT file stage
        with open('PyPoll/Analysis_Voting_FinalReport.txt','w') as final_report:
            final_report.write('Election Results \n')
            final_report.write('-'*30+ '\n')
            final_report.write(f'Total votes: {total_votes} \n')
            final_report.write('-'*30+ '\n')
            for stats in dic_candidates_votes.items():
                candidate,votes = stats
                final_report.write(f'{candidate}: {round((votes/total_votes)*100,3)}% ({votes}) \n')
            final_report.write('-'*30+ '\n')
            final_report.write(f'The winner is: {winner_name} with: {winner_votes} votes')

Voting_Analysis()

        
