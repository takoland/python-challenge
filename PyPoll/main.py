import os 
import csv

csv_data1 = os.path.join('raw_data','election_data_1.csv')


with open(csv_data1,'r') as csvfile:
    csvreader1 = csv.reader(csvfile,delimiter=',')
    for row in csvreader1:
        totalVotes = sum(1 for row in csvfile) - 1

        if row[2] = Roger:
            totalRoger = count

        if row[2] = Gomez:
            totalGomez = count

        if row[2] = Brentwood:
            totalBrentwood = count

        if row[2] = Higgins:
            totalHiggins = count



print("Election Results")
print("-----------------")
print("Total Votes: " + totalVotes)
print("-----------------")
print("Rogers: "+ totalRoger)
print("Gomez: " + totalGomez)
print("Brentwood: " + totalBrentwood)
print("Higgins: "+ totalHiggins)
print("------------------")
print("Winner: " + winner)
print("------------------")