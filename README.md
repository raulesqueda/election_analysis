# Election_Analysis
First project using Python
## Project Overview

A Colorado Broad of Elections employee has given the following task to complete the election audit of a recent local congressional election.
  1. Calculate the total number of votes cast.
  2. Get a complete list of candidates who recieved votes.
  3. Calculate the total number of votes each candidate recieved
  4. Calculate the percentage of votes each candidate won.
  5. Determine the winner of the election based on popular vote.
  
## Resources
  Data Source: election_results.cvs
  Software: Python 3.9.6, Visual Studio Code 
  
## Summary
The analysis of the election show that:
There were **369,711 votes** cast in the election.

The candidates were: 
  1. Charles Casper Stockham,
  2. Diana DeGette,
  3. Raymon Anthony Doane.
    
The candidate results were:
  1. Charles Casper Stockham recieved 23.0% of the vote and 85,213 number of votes.
  2. Diana DeGette recieved 73.8% of the vote and 272,892 number of votes.
  3. Raymon Anthony Doane recieved 3.1% of the vote and 11,606 number of votes.
   
The winner of the election was **Diana DeGette** recieved 73.8% of the vote and 272,892 number of votes.

## Election Analysis Challenge

### 1.	Overview of Election Audit: 
We were asked by Seth and Tom to help them to analyze the results of the congressional election in three counties in the state of Colorado, United States. For this purpose, we develop a code in python to present the results of the elections with the information of the file called “election_results.csv”. 

Seth and Tom present the results to the authorities, but now, **the election audit request requested some additional data for the audit**. We were asked to present the voter turnout for each county, the percentage of votes from each county out of the total count and the county with the highest turnout. For this data, we use the code we develop before and we add more coding to get the information we were asked by the authorities.

### 2.	Election-Audit Results: 
The results of the additional data asked by the election audit will be presented in the next list:

1.	How many votes were cast in this congressional election? The total vote for the congressional election was **369,711 votes**.

![Total_votes](https://github.com/raulesqueda/election_analysis/blob/main/Resources/total_votes.PNG)

2.	Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct. In the three counties, the highest percentage of the votes were presented in **Denver (82.8%)**, followed by Jefferson (10.5%) and the rest of the votes was in the Arapahoe county (6.7%)

![County_votes](https://github.com/raulesqueda/election_analysis/blob/main/Resources/county_votes.PNG)

3.	Which county had the largest number of votes? As we mentioned before, Denver was the county of the state which has the largest number of votes.

![County_votes_highest](https://github.com/raulesqueda/election_analysis/blob/main/Resources/county_votes_highest.PNG)
 
4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received. In this congressional election, we have information of three candidates: Charles Casper Stockham, Diana DeGette and Raymon Anthony Doane, this was **the distribution of the voting for the candidates**:
 
![Candidate_votes](https://github.com/raulesqueda/election_analysis/blob/main/Resources/candidates_voting.PNG) 
 
5. 	Which candidate won the election, what was their vote count, and what was their percentage of the total votes? The candidate who won this election were **Diana DeGette with the 73.8% of the votes (272,892 voters)**.

![Candidate_winner](https://github.com/raulesqueda/election_analysis/blob/main/Resources/candidate_winner.PNG) 
 
### 3.	Election-Audit Summary: 

The code we provided to the election authorities proved it can be used to get more information about the results of the election. If we have more elections and more information, we can use the code to finding more insights and results of the voting, for example, we can know in which county we had more votes and the percentage of the registered voters who voting in each election. Also, we can adapt this code and shared it to other states for developing a larger database in which we can have more information about the results of voting in.
