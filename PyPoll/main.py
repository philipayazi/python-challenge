import os
import csv
import statistics


candidateList = []

election_data = os.path.join('Resources', 'election_data.csv')

with open(election_data, mode='r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    # print(csvreader)

    next(csvreader)
    for row in csvreader:
        candidateList.append(row[2])

winner = statistics.mode(candidateList)

Khan = (candidateList.count('Khan'))
Correy = (candidateList.count('Correy'))
Li = (candidateList.count('Li'))
OTooley = (candidateList.count('O\'Tooley'))

totalVotes = (Khan + Correy + Li + OTooley)


percentKhan = format((((Khan)/totalVotes) * 100), '.3f')
percentCorrey = format(((Correy/totalVotes) * 100), '.3f')
percentLi = format(((Li/totalVotes) * 100), '.3f')
percentOTooley = format(((OTooley/totalVotes) * 100), '.3f')
breaker = '-----------------------------------'


print('Election Results')
print(breaker)
print('Total Votes: ' + str(totalVotes))
print(breaker)
print('Khan: ' + percentKhan + '% (' + str(Khan) + ')')
print('Correy: ' + percentCorrey + '% (' + str(Correy) + ')')
print('Li: ' + percentLi + '% (' + str(Li) + ')')
print('O\'Tooley: ' + percentOTooley + '% (' + str(OTooley) + ')')
print(breaker)
print('Winner: ' + str(winner))

output_file = os.path.join("PyBank.txt")
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow('Election Results')
    writer.writerow(breaker)
    writer.writerow('Total Votes: ' + str(totalVotes))
    writer.writerow(breaker)
    writer.writerow('Khan: ' + percentKhan + '% (' + str(Khan) + ')')
    writer.writerow('Correy: ' + percentCorrey + '% (' + str(Correy) + ')')
    writer.writerow('Li: ' + percentLi + '% (' + str(Li) + ')')
    writer.writerow('O\'Tooley: ' + percentOTooley + '% (' + str(OTooley) + ')')
    writer.writerow(breaker)
    writer.writerow('Winner: ' + str(winner))