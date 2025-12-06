import csv
import os

#headings to the CSV and example data
headers = ['Name','Email','Phone Number','Purchases']

file_path = "currentReceipts.csv"

#Adds the data inputed into a spreadsheet. if the csv does not exist, create it
def addData(name, email, phone, purchase):
    dataline = [name, email, phone, purchase]

    if os.path.exists(file_path):
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(dataline)
    else:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerow(dataline)



