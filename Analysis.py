import csv;


with open('Quellen.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')

    for columns in csv_reader:
        print(columns[3])
