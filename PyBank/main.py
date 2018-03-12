import os 
import csv

csv_data1 = os.path.join('raw_data','budget_data_1.csv')
#csv_data2 = os.path.join('..','raw_data','budget_data_2.csv')

#def financialCal(budgetData):
    #totalMonth = 
    #totalRevenue = sum(int(budgetData[1]))
    #averageChange = 
    #maxIncrease = 
    #maxDecrease = 

with open(csv_data1,'r') as csvfile:
    csvreader1 = csv.reader(csvfile,delimiter=',')
    for row in csvreader1:
        if row[1] == int:
            totalMonth = count(row)
            totalRevenue = sum(int(row[1]))

            #averageChange  
            maxIncrease = max(averageChange)
            maxDecrease = min(averageChange)
        
        #financialCal(row)

print("Financial Analysis")
print("Total Months: "+ str(totalMonth))
print("Total Revenue: "+ str(totalRevenue))
print("Average Revenue Change: "+ str(averageChange))
print("Greatest Increase in Revenue: " + str(maxIncrease))
print("Greatest Decrease in Revenue: " + str(maxDecrease))


