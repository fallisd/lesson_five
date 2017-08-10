import csv

ifile = 'victorian_serial_novels_unedited.csv'
ofile = 'victorian_serial_novels_edited.csv'


fileContents = csv.DictReader(open(ifile, 'r'))


writer = csv.DictWriter(open(ofile, 'w'), fileContents.fieldnames, quotechar='"', lineterminator='\n')
writer.writeheader()


for row in fileContents:
  row['date_created'] = 2
  writer.writerow(row)
