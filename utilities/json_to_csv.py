import csv, json
from datetime import datetime

# infile = open('../data/json/parents_dec17_now.json', 'r')
# outfile = open ('../parents_dec17_now.csv', 'w')

infile = open('../data/json/me_all.json', 'r')
outfile = open ('../data/csv/me_all.csv', 'w')

inputFile = infile  # open json file
outputFile = outfile  # load csv file
data = json.load(inputFile)  # load json content
inputFile.close()  # close the input file
output = csv.writer(outputFile)  # create a csv.write

output.writerow(data['data'][0].keys())   # header row
for row in data['data']:
    # print(row['date'])
    # print(datetime.fromtimestamp(float(row['date'][:-3]), ).isoformat())
    # output.writerow(row.values()) # values row
    output.writerow([row['temperature'], datetime.fromtimestamp(float(row['date'][:-3]), ).isoformat()])