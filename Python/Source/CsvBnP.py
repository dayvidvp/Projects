import csv
import pandas as pd
with open ('d:\downloads\BE07001663149266EUR-Archive-20180101-20181129.CSV', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')

    for row in csv_reader:
      print(row)


