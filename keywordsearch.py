#Source https://stackoverflow.com/questions/17308872/check-whether-string-is-in-csv

import csv

with open('all_yaks.csv', 'rt') as f:
     reader = csv.reader(f, delimiter=' ')
     for row in reader:
          for field in row:
              if field == "Broken":
                  print "Broken is in file"
                  print row
              if field == "Printer":
                  print "Printer is in file"
                  print row
              if field == "Wifi":
                  print "Wifi is in file"
                  print row
              if field == "Secure":
                  print "Secure is in file"
                  print row