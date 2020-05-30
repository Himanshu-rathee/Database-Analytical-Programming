import csv

# read a csv file
with open("titanic.csv") as f:
    read = csv.reader(f)
    for row in read :
        print(row)

# write to a csv file
csvData = [['Person', 'Age'], ['Peter', '22'], ['Jasmine', '21'], ['Sam', '24']]
with open("write_csv", 'w') as f :
    writer = csv.writer(f)
    writer.writerows(csvData)