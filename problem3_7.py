import csv
def problem3_7(csv_pricefile, flower):
    dit={}
    f=open(csv_pricefile)
    for row in csv.reader(f):
        dit[row[0]]=row[1]
    print(dit[flower])
