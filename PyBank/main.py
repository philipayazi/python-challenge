import os
import csv
import statistics


incomeList = []
dateList = []

budget_data = os.path.join('Resources','budget_data.csv')

with open(budget_data, mode='r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')

    next(csvreader)     
    for row in csvreader:
         incomeList.append(int(row[1]))
         dateList.append(row[0])

change = [x-y for x,y in zip(incomeList, incomeList[1:])]
totalMonths = len(incomeList)
netTotal = sum(incomeList)
avgChange = round(statistics.mean(change), 2)
maxIncome = max(incomeList)
maxIndex = incomeList.index(maxIncome)
maxDate = dateList[maxIndex]
minIncome = min(incomeList)
minIndex = incomeList.index(minIncome)
minDate = dateList[minIndex]

finAnalysis = "Financial Analysis"

breaker = '--------------------------------------'

print(finAnalysis)
print(breaker)
print('Total Months: ' + str(totalMonths))
print('Total: ' + '$' + str(netTotal))       
print('Average Change: ' + '$' + str(avgChange))
print('Greatest Increase in Profits: ' + str(maxDate) + ' ($' + str(maxIncome) + ')')
print('Greatest Decrease in Profits: ' + str(minDate) + ' ($' + str(minIncome) + ')')

output_file = os.path.join("PyBank.txt")
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow('Financial Analysis')
    writer.writerow(breaker)
    writer.writerow('Total Months: ' + str(totalMonths))
    writer.writerow('Total: ' + '$' + str(netTotal))
    writer.writerow('Average Change: ' + '$' + str(avgChange))
    writer.writerow('Greatest Increase in Profits: ' + str(maxDate) + ' ($' + str(maxIncome) + ')')
    writer.writerow('Greatest Decrease in Profits: ' + str(minDate) + ' ($' + str(minIncome) + ')')