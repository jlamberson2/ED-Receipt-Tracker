import csv
import os
import tkinter


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

def confirm_button():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    products = product_entry.get()

    addData(name, email, phone, products)

#Base GUI code

#creates the root screen
root = tkinter.Tk()
root.title('ED Receipt Tracker')

#Labels for entries
tkinter.Label(master=root, text='Name:').grid(row=0)
tkinter.Label(master=root, text='Email:').grid(row=1)
tkinter.Label(master=root, text='Phone:').grid(row=2)
tkinter.Label(master=root, text='Product:').grid(row=3)

#Adding entries for the program
name_entry = tkinter.Entry(root, width=50)
email_entry = tkinter.Entry(root, width=50)
phone_entry = tkinter.Entry(root, width=50)
product_entry = tkinter.Entry(root, width=50)

#placement for the entries
name_entry.grid(row=0, column=1)
email_entry.grid(row=1, column=1)
phone_entry.grid(row=2, column=1)
product_entry.grid(row=3, column=1)

#adding a confirm button
confirm = tkinter.Button(root, text="Confirm", width=20, command=confirm_button)
confirm.grid(row=4)

#initalizes main window - NOTE: put widgets before this
root.mainloop()