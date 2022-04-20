# Election-Analysis
## Overview of Election Audit
The purpose of this project was to help Seth and Tom audit the election results and pass on the findings to the election commission. Python and Visual studio code were used to create the code to analyze the data. 
## Election Audit Results
![image](https://user-images.githubusercontent.com/102090016/164312081-e470d5cb-38e8-44df-8d94-04795fce85b4.png)


- 369,711 votes were cast in this congressional election
- County vote breakdown
  - Jefferson: 10.5% (38,855 votes)
  - Denver: 82.8% (306, 055 votes)
  - Arapahoe: 6.7% (24, 801 votes)
 - Denver was the county with the largest number of votes
 - Candidate breakdown
  - Charles Casper Stockham: 23.0% (38,855 votes)
  - Diana DeGette: 82.8% (306,055 votes)
  - Raymon Anthony Doane: 6.7% (24, 801 votes) 
- Winning Candidate
    - Diana DeGette won 82.8% of the votes which consisted of 24, 801 votes
## Election Audit Summary
The script for this project can be modified to a variety of different uses. The dictionary and lists in this project can be expanded to inlcude a wider variety of candidates and counties to gather more data. Additionally, the code (below) used to find the county with the largest voter turnout can also be modified to find the reverse and determine which county had the lowest voter turnout. This information could be used to assess voter turnout and possibly determine ways to increase turnout. 

    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        votes2 = county_votes.get(county_name)
        # 6c: Calculate the percentage of votes for the county.
        county_percentage = float(votes2)/float(total_votes)*100
        county_results = (f"{county_name}: {county_percentage:.1f}% ({votes2:,})\n" f"\n")
         # 6d: Print the county results to the terminal.
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes2 > largest_votes):
            largest_votes = votes2
            largest_county = (f"-------------------------\n" 
            f"County with largest voter turout: {county_name}\n" 
            f"-------------------------\n")
