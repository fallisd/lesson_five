import csv
import re

ifile = 'victorian_serial_novels_unedited.csv'
ofile = 'victorian_serial_novels_edited.csv'


fileContents = csv.DictReader(open(ifile, 'r'))


writer = csv.DictWriter(open(ofile, 'w'), fileContents.fieldnames, quotechar='"', lineterminator='\n')
writer.writeheader()


for row in fileContents:
  row['genre'] = row['genre'].replace('book', 'books')
  row['resource_type'] = row['resource_type'].replace('text', 'Text')


  match = re.search(r'http://voyager.library.uvic.ca/cgi-bin/Pwebrecon.cgi\?BBID=(\d*)', row['related_url'])
  if match:
    row['related_url'] = 'http://voyager.library.uvic.ca/vwebv/holdingsInfo?bibId=' + match.group(1)
  
  #row['related_url].replace('cgi-bin/Pwebrecon.cgi?BBID=', 'vwebv/holdingsInfo?bibId=')
  

  writer.writerow(row)
