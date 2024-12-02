import csv

with open("25 Archivos CSV\\CSV.csv") as CSV:
    reader = csv.reader(CSV)
    for row in reader:
        print(row)