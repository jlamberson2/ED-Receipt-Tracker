import csv
import os
import tkinter
from tkinter import ttk
from tkinter import messagebox


#headings to the CSV and example data
headers = ['Name','Email','Phone Number','Purchases', 'Soul Numbers','Payment Type', 'Sales Tax', 'Sales Fee']

file_path = "currentReceipts.csv"

def calculateFees():
    print("This is a tester funciton, ERROR\n")

    
        

#Adds the data inputed into a spreadsheet. if the csv does not exist, create it
def addData(name, email, phone, purchase, souls):
    dataline = [name, email, phone, purchase, souls]

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
    #gets the data from the entries
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    products = product_entry.get()
    souls = soul_entry.get()

    #checks to make sure there is a name and email
    if not name:
        messagebox.showwarning('Error', 'A name needs to be attached')
        raise Exception("Error, no name entered")
    

    if not email:
        messagebox.showwarning('Error', 'A email needs to be attached')
        raise Exception("Error, no email attached")
    

    #add the data to the csv
    addData(name, email, phone, products, souls)

    #delete the text out of the enties
    name_entry.delete(0, tkinter.END)
    email_entry.delete(0, tkinter.END)
    phone_entry.delete(0, tkinter.END)
    product_entry.delete(0, tkinter.END)
    soul_entry.delete(0, tkinter.END)



#Base GUI code



#creates the root screen
root = tkinter.Tk()
root.title('ED Receipt Tracker')
root.geometry("500x300")


#Frame for the entire UI so it can be centered
centerFrame = tkinter.Frame(root)
centerFrame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

#Labels for entries
tkinter.Label(master=centerFrame, text='Name:').grid(row=0)
tkinter.Label(master=centerFrame, text='Email:').grid(row=1)
tkinter.Label(master=centerFrame, text='Phone:').grid(row=2)
tkinter.Label(master=centerFrame, text='Product:').grid(row=3)
tkinter.Label(master=centerFrame, text='Souls:').grid(row=4)
tkinter.Label(master=centerFrame, text='Total Payment: ').grid(row=6)

#Adding entries for the program
name_entry = tkinter.Entry(centerFrame, width=50)
email_entry = tkinter.Entry(centerFrame, width=50)
phone_entry = tkinter.Entry(centerFrame, width=50)
product_entry = tkinter.Entry(centerFrame, width=50)
soul_entry = tkinter.Entry(centerFrame, width=50)
payment_entry = tkinter.Entry(centerFrame, width=50)

#placement for the entries
name_entry.grid(row=0, column=1)
email_entry.grid(row=1, column=1)
phone_entry.grid(row=2, column=1)
product_entry.grid(row=3, column=1)
soul_entry.grid(row=4, column=1)
payment_entry.grid(row=6, column=1)

#adding a confirm button
confirm = tkinter.Button(centerFrame, text="Confirm", width=20, command=confirm_button)
confirm.grid(row=10)

#temp button for testing only
tester = tkinter.Button(centerFrame, text='test', width=20, command=calculateFees)
tester.grid(row=10, column=1)

#adding in choice box for payment selection
tkinter.Label(master=centerFrame, text='Payment Type: ').grid(row=7)

#text variable for payment type
payment_type = tkinter.StringVar()

payment_selection = ttk.Combobox(master=centerFrame, width=25, textvariable=payment_type)

#adding selections to combobox
payment_selection['values'] = ('Cash', 'Paypal', 'Venmo', 'QR Code Paypal', 'Square')
payment_selection.grid(row=7, column=1)
payment_selection.current()

# Selection of donation or product sale
v = tkinter.StringVar(centerFrame, "1")

#making a frame for the buttons
radioContainer = tkinter.Frame(centerFrame)
radioContainer.grid(row=8, column=1)

#adding the radio buttons to the frame
product_radio_button = tkinter.Radiobutton(master=radioContainer, text="Product Sold", variable=v, value= 1)
donation_radio_button = tkinter.Radiobutton(master=radioContainer, text="Dontation", variable=v, value= 2)
product_radio_button.grid(row=0, column=0)
donation_radio_button.grid(row=0, column=1)




#initalizes main window - NOTE: put widgets before this
root.mainloop()