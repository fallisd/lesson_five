import csv
import re

ifile = 'victorian_serial_novels_unedited.csv'
ofile = 'victorian_serial_novels_edited_dates.csv'


fileContents = csv.DictReader(open(ifile, 'r'))


writer = csv.DictWriter(open(ofile, 'w'), fileContents.fieldnames, quotechar='"', lineterminator='\n')
writer.writeheader()


for row in fileContents:
  match = re.search(r'(\d{4})-(\d{4})', row['date_created'])
  if match:
    row['date_created'] = re.sub(r'(\d{4})-(\d{4})', match.group(1) + '/' + match.group(2), row['date_created'], 1)
  
  writer.writerow(row)