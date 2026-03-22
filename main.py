import csv
import os
import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import tkinter.font as TKfont


#headings to the CSV and example data
headers = ['Name','Email','Phone Number','Purchases', 'Soul Numbers','Payment Type', 'Payment', 'Sales Tax', 'Sales Fee', 'Donation?']

file_path = "currentReceipts.csv"

#calculates vender fees for payment methods
def calculateFees():
    #gets the payment total and converts it to a float
    payment_total = payment_entry.get()
    payment_total = float(payment_total)

    
    method = payment_selection.get()

    #payment types ('Cash', 'Paypal', 'Venmo', 'QR Code Paypal', 'Square')
    #Calculates the fee based on the payment type
    #Paypal fixed fee = 0.09
    #Paypal and venmo = 3.49%
    #Paypal QR code = 2.29%
    #Paypal square = 2.99%

    paypal_fixed = 0.09
    paypal_fee_percent = 0.0349 #Also applies to any venmo transactions
    paypal_qr = 0.0229
    paypal_square = 0.0299


    if method == 'Cash':
        return 0
    
    if method == 'Paypal' or method == 'Venmo':
        val = payment_total * paypal_fee_percent
        val += paypal_fixed
        val = round(val, 2)
        return val
    
    if method == 'QR Code Paypal':
        val = payment_total * paypal_qr
        val += paypal_fixed
        val = round(val, 2)
        return val
    
    if method == 'Square':
        val = payment_total * paypal_square
        val += paypal_fixed
        val = round(val, 2)
        return val

#Calculates sales tax on the total payment for MA
def calculateSalesTax():
    MA_sales_tax = 0.0625

    payment_total = payment_entry.get()
    payment_total = float(payment_total)

    if v.get() == '1':
        val = payment_total * MA_sales_tax
        val = round(val, 2)
        return val
    if v.get() == '2':
        return 0
    

def tester_function():
    if v.get() == '1':
        print("A")
    if v.get() == '2':
        print("B")
    return 0
    

    

    
        

#Adds the data inputed into a spreadsheet. if the csv does not exist, create it
#headers = ['Name','Email','Phone Number','Purchases', 'Soul Numbers','Payment Type', 'Payment', 'Sales Tax', 'Sales Fee']
def addData(name, email, phone, purchase, souls, payment_type, payment, salestax, salesfee, donation):
    dataline = [name, email, phone, purchase, souls, payment_type, payment, salestax, salesfee, donation]

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
    payment = payment_entry.get()
    payment_type = payment_selection.get()


    #checks to make sure there is data in name, email, payment, and payment type
    if not name:
        messagebox.showwarning('Error', 'A name needs to be attached')
        raise Exception("Error, no name entered")

    #TODO: Make sure to validate it is an email
    if not email:
        messagebox.showwarning('Error', 'A email needs to be attached')
        raise Exception("Error, no email attached")
    
    #checks for payment and that it is a number
    if not payment:
        messagebox.showwarning("Error", "Need a payment total")
        raise Exception("Error, no payment total attached")
    
    try:
        val = payment_entry.get()
        val = float(val)
    except:
        messagebox.showwarning("Error", "Payment must be a number")
        raise Exception("Error, payment is not a number")
    
    #checks to see if a payment type is selected
    if not payment_type:
        messagebox.showwarning("Error", "Need a payment type")
        raise Exception("Error, no payment type attached")
    
    salestax = calculateSalesTax()
    salesfee = calculateFees()
    
    donation = False
    if v.get() == '2':
        donation = True
    

    #add the data to the csv
    #name, email, phone, purchase, souls, payment_type, payment, salestax, salesfee, donation
    addData(name, email, phone, products, souls, payment_type, payment, salestax, salesfee, donation)

    #delete the text out of the enties
    name_entry.delete(0, tkinter.END)
    email_entry.delete(0, tkinter.END)
    phone_entry.delete(0, tkinter.END)
    product_entry.delete(0, tkinter.END)
    soul_entry.delete(0, tkinter.END)
    payment_entry.delete(0, tkinter.END)



#Base GUI code



#creates the root screen
root = tkinter.Tk()
root.title('ED Receipt Tracker')
root.geometry("900x400")
root.resizable(False, False)

#Label and text box fonts
default_font = TKfont.Font(family='Ariel', size=18)


#Frame for the entire UI so it can be centered
centerFrame = tkinter.Frame(root)
centerFrame.pack(padx=0.5, pady=0.5, anchor='center')

centerFrame.columnconfigure(list(range(4)), weight=1)

centerFrame.rowconfigure(list(range(11)), weight=1)


#Labels for entries
name_label = tkinter.Label(master=centerFrame, text='Name:', font=default_font)
email_label = tkinter.Label(master=centerFrame, text='Email:', font=default_font)
phone_label = tkinter.Label(master=centerFrame, text='Phone:', font=default_font)
product_label = tkinter.Label(master=centerFrame, text='Product:', font=default_font)
souls_label = tkinter.Label(master=centerFrame, text='Souls:', font=default_font)
payment_label = tkinter.Label(master=centerFrame, text='Total Payment: ', font=default_font)

#Adding labels to the grid
name_label.grid(row=0, padx=5, pady=5)
email_label.grid(row=1, padx=5, pady=5)
phone_label.grid(row=2, padx=5, pady=5)
product_label.grid(row=3, padx=5, pady=5)
souls_label.grid(row=4, padx=5, pady=5)
payment_label.grid(row=5, padx=5, pady=5)

#Adding entries for the program
name_entry = tkinter.Entry(centerFrame, width=50, font=default_font)
email_entry = tkinter.Entry(centerFrame, width=50, font=default_font)
phone_entry = tkinter.Entry(centerFrame, width=50, font=default_font)
product_entry = tkinter.Entry(centerFrame, width=50, font=default_font)
soul_entry = tkinter.Entry(centerFrame, width=50, font=default_font)
payment_entry = tkinter.Entry(centerFrame, width=50, font=default_font)

#placement for the entries
name_entry.grid(row=0, column=1, padx=5, pady=5)
email_entry.grid(row=1, column=1, padx=5, pady=5)
phone_entry.grid(row=2, column=1, padx=5, pady=5)
product_entry.grid(row=3, column=1, padx=5, pady=5)
soul_entry.grid(row=4, column=1, padx=5, pady=5)
payment_entry.grid(row=5, column=1, padx=5, pady=5)

#adding a confirm button
confirm = tkinter.Button(centerFrame, text="Confirm", width=20, command=confirm_button, font=default_font)
confirm.grid(row=10, columnspan=2)



#adding in choice box for payment selection
tkinter.Label(master=centerFrame, text='Payment Type: ', font=default_font).grid(row=7, padx=5, pady=5)

#text variable for payment type
payment_type = tkinter.StringVar()

payment_selection = ttk.Combobox(master=centerFrame, width=25, textvariable=payment_type, font=default_font)

#adding selections to combobox
payment_selection['values'] = ('Cash', 'Paypal', 'Venmo', 'QR Code Paypal', 'Square')
payment_selection.grid(row=7, column=1)
payment_selection.current()

# Selection of donation or product sale
#this is the variable to get the value of the radio button
v = tkinter.StringVar(centerFrame, "1")

#making a frame for the buttons
radioContainer = tkinter.Frame(centerFrame)
radioContainer.grid(row=8, column=1)

#adding the radio buttons to the frame
product_radio_button = tkinter.Radiobutton(master=radioContainer, text="Product Sold", variable=v, value= 1, font=default_font)
donation_radio_button = tkinter.Radiobutton(master=radioContainer, text="Dontation", variable=v, value= 2, font=default_font)
product_radio_button.grid(row=0, column=0)
donation_radio_button.grid(row=0, column=1)

#temp button for testing only
#tester = tkinter.Button(centerFrame, text='test', width=20, command=tester_function, font=default_font)
#tester.grid(row=10, column=1)


#initalizes main window - NOTE: put widgets before this
root.mainloop()