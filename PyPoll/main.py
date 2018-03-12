import os 
import csv

csv_data1 = os.path.join('raw_data','election_data_1.csv')


with open(csv_data1,'r') as csvfile:
    csvreader1 = csv.reader(csvfile,delimiter=',')
    for row in csvreader1:
        if row[0] == int:
            




print("Election Results")
print("-----------------")
print("Total Votes: " + totalVotes)
print("-----------------")
print("Rogers: "+ )
print("Gomez: " + )
print("Brentwood: " + )
print("Higgins: "+ )
print("------------------")
print("Winner: " + )
print("------------------")