import argparse
import csv
import pandas as pd
pd.set_option('display.max_rows', 50, 'display.min_rows', 50)

parser = argparse.ArgumentParser()
parser.add_argument("-csv", "--filename", dest = "csv", default = "filename.csv", help="csv location")

args = parser.parse_args()

filename = args.csv
#filename = 'filename.csv'

with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    print(f'The available fields in {filename} are: {headers}')

df = pd.read_csv(filename)

# Trends in from addresses
from_trends = df['From: (Name)'].value_counts(normalize=True) * 100
print('Trends in from addresses: (percentage of total):')
print(from_trends)

# Trends in email subject
subject_trends = df['Subject'].value_counts(normalize=True) * 100
print('Trends in email Subject:')
print(subject_trends)
