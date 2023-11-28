from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.simpledialog import askstring

#Function for default radiobutton
def set_default():
    prev_bal.delete(0,END)
    prev_bal.config(state = DISABLED)

    checkbox1.deselect()
    checkbox1.config(state = DISABLED)
    checkbox2.deselect()
    checkbox2.config(state = DISABLED)
    checkbox3.deselect()
    checkbox3.config(state = DISABLED)
    checkbox4.deselect()
    checkbox4.config(state = DISABLED)

    numpc1.delete(0,END)
    numpc1.config(state = DISABLED)
    numpc2.delete(0,END)
    numpc2.config(state = DISABLED)
    numpc3.delete(0,END)
    numpc3.config(state = DISABLED)
    numpc4.delete(0,END)
    numpc4.config(state = DISABLED)

    amt1.delete(0,END)
    amt1.config(state = DISABLED)
    amt2.delete(0,END)
    amt2.config(state = DISABLED)
    amt3.delete(0,END)
    amt3.config(state = DISABLED)
    amt4.delete(0,END)
    amt4.config(state = DISABLED)

    total_dep.delete(0, END)
    total_dep.config(state = DISABLED)
    current_bal.delete(0, END)
    current_bal.config(state = DISABLED)
    btn_compute.config(state = DISABLED)

#Function for deposit radiobutton
def set_deposit():
    prev_bal.config(state = NORMAL)
    btn_compute.config(state = NORMAL)
    checkbox1.config(state = NORMAL)
    checkbox2.config(state = NORMAL)
    checkbox3.config(state = NORMAL)
    checkbox4.config(state = NORMAL)
    total_dep.config(state = 'readonly')
    current_bal.config(state = 'readonly')

#Function for withdraw radiobutton
def set_withdraw():
    prev_bal.config(state = NORMAL)
    btn_compute.config(state = NORMAL)
    checkbox1.config(state = DISABLED)
    checkbox2.config(state = DISABLED)
    checkbox3.config(state = DISABLED)
    checkbox4.config(state = DISABLED)

#Function to check if any of the checkbuttons are selected
def set_CheckButtons():
    if var1.get():
        numpc1.config(state = NORMAL)
    else:
        numpc1.delete(0, END)
        numpc1.config(state = DISABLED)
    
    if var2.get():
        numpc2.config(state = NORMAL)
    else: 
        numpc2.delete(0, END)
        numpc2.config(state = DISABLED)
    
    if var3.get():
        numpc3.config(state = NORMAL)
    else:
        numpc3.delete(0, END)
        numpc3.config(state = DISABLED)
    
    if var4.get():
        numpc4.config(state = NORMAL)
    else:
        numpc4.delete(0, END)
        numpc4.config(state = DISABLED)

#Function for compute button that solves for deposit and withdrawal transactions
def compute():
    totalDeposit = 0
    oneK = 1000
    five = 500
    two = 200
    one = 100
    CurBal = 0

    try:
        previous_bal = float(prev_bal.get())
    except ValueError:
        check_prev_bal = askstring("Error", "Input a correct positive integer!")
        previous_bal = float(check_prev_bal)
        prev_bal.delete(0, END)
        prev_bal.insert(0, previous_bal)
    
    if transaction_type.get() == "deposit":
        if var1.get():
            try:
                num = int(numpc1.get())
            except ValueError:
                inputNum = askstring("Error", "Input a correct positive integer!")
                num = int(inputNum)
                numpc1.delete(0, END)
                numpc1.insert(0, num)
            
            totalDeposit += num * oneK
            
            amt1.config(state = NORMAL)
            amt1.delete(0, END)
            amt1.insert(0, num * oneK)
            amt1.config(state = 'readonly')
        else:
            amt1.config(state = NORMAL)
            amt1.delete(0, END)
            amt1.config(state = DISABLED)
                
        if var2.get():
            try:
                num = int(numpc2.get())
            except ValueError:
                inputNum = askstring("Error", "Input a correct positive integer!")
                num = int(inputNum)
                numpc2.delete(0, END)
                numpc2.insert(0, num)
                
            totalDeposit += num * five
            
            amt2.config(state = NORMAL)
            amt2.delete(0, END)
            amt2.insert(0, num * five)
            amt2.config(state = 'readonly')
        else:
            amt2.config(state = NORMAL)
            amt2.delete(0, END)
            amt2.config(state = DISABLED)
                
        if var3.get():
            try:
                num = int(numpc3.get())
            except ValueError:
                inputNum = askstring("Error", "Input a correct positive integer!")
                num = int(inputNum)
                numpc3.delete(0, END)
                numpc3.insert(0, num)
                
            totalDeposit += num * two
            
            amt3.config(state = NORMAL)
            amt3.delete(0, END)
            amt3.insert(0, num * two)
            amt3.config(state = 'readonly')
        else:
            amt3.config(state = NORMAL)
            amt3.delete(0, END)
            amt3.config(state = DISABLED)
                
        if var4.get():
            try:
                num = int(numpc4.get())
            except ValueError:
                inputNum = askstring("Error", "Input a correct positive integer!")
                num = int(inputNum)
                numpc4.delete(0, END)
                numpc4.insert(0, num)

            totalDeposit += num * one
            
            amt4.config(state = NORMAL)
            amt4.delete(0, END)
            amt4.insert(0, num * one)
            amt4.config(state = 'readonly')
        else:
            amt4.config(state = NORMAL)
            amt4.delete(0, END)
            amt4.config(state = DISABLED)
            
        CurBal += previous_bal + totalDeposit
        
        total_dep.config(state = NORMAL)
        total_dep.delete(0, END)
        total_dep.insert(0, totalDeposit)
        total_dep.config(state = 'readonly')
        
        current_bal.config(state = NORMAL)
        current_bal.delete(0, END)
        current_bal.insert(0, CurBal)
        current_bal.config(state = 'readonly')
        
    if transaction_type.get() == "withdraw":
        wd = askstring("Withdraw", "Enter Amount:")
        try:
            withdraw_amt = float(wd)
        except ValueError:
            wd = askstring("Withdraw", "Input numbers only!\nEnter Amount:")
            withdraw_amt = float(wd)
        
        if withdraw_amt < previous_bal:
            CurBal = previous_bal - withdraw_amt
            current_bal.config(state = NORMAL)
            current_bal.delete(0, END)
            current_bal.insert(0, CurBal)
            current_bal.config(state = 'readonly')
        else:
            newWD = askstring("Withdraw", "Insufficient Funds!\nEnter Amount: ")
            try:
                withdraw_amt = float(newWD)
            except ValueError:
                messagebox.showerror("Error", "Input numbers only!")
            CurBal = previous_bal - withdraw_amt
            current_bal.config(state = NORMAL)
            current_bal.delete(0, END)
            current_bal.insert(0, CurBal)
            current_bal.config(state = 'readonly')

# Create Window and Widgets
frame = Tk()
frame.title("Transactions")
frame.geometry("450x250")
frame.config(background = '#CBB3E1')

lbl_transaction = Label(text = "Type transaction:", background = '#CBB3E1')
lbl_transaction.grid(row = 0, column = 0, sticky = W)
transaction_type = StringVar()
transaction_type.set("default")

# Transaction type radio buttons
defaultrd = Radiobutton(text="Default", variable = transaction_type, value = "default", background = '#CBB3E1', command = set_default)
defaultrd.grid(row = 0, column = 1, sticky = W)
depositrd = Radiobutton(text = "Deposit", variable = transaction_type, value = "deposit", background = '#CBB3E1', command = set_deposit)
depositrd.grid(row = 0, column = 2, sticky = W)
withdrawrd = Radiobutton(text = "Withdraw", variable = transaction_type, value = "withdraw", background = '#CBB3E1', command = set_withdraw)
withdrawrd.grid(row = 0, column = 3, sticky = W)

# Previous Balance
lbl_prev_bal = Label(text = "Previous Balance:", background = '#CBB3E1')
lbl_prev_bal.grid(row = 1, column = 0, sticky = W)
prev_bal = Entry(frame, state = DISABLED)
prev_bal.grid(row = 1, column = 1)

# Denomination
lbl_denomination = Label(text = "Denomination", background = '#CBB3E1')
lbl_denomination.grid(row = 2, column = 0, sticky = W)

#variable values for check function
var1 = BooleanVar()
var2 = BooleanVar()
var3 = BooleanVar()
var4 = BooleanVar()

checkbox1 = Checkbutton(frame, text = "1,000", variable = var1, background = '#CBB3E1', state = DISABLED, command = set_CheckButtons)
checkbox1.grid(row = 3, column = 0, sticky = W)
checkbox2 = Checkbutton(frame, text = "500", variable = var2, background = '#CBB3E1', state = DISABLED, command = set_CheckButtons)
checkbox2.grid(row = 4, column = 0, sticky = W)
checkbox3 = Checkbutton(frame, text = "200", variable = var3, background = '#CBB3E1', state = DISABLED, command = set_CheckButtons)
checkbox3.grid(row = 5, column = 0, sticky = W)
checkbox4 = Checkbutton(frame, text = "100", variable = var4, background = '#CBB3E1', state = DISABLED, command = set_CheckButtons)
checkbox4.grid(row = 6, column = 0, sticky = W)

# Number of Pieces
lbl_num_pieces = Label(text = "Number of Pieces", background = '#CBB3E1')
lbl_num_pieces.grid(row = 2, column = 1, sticky = W)
numpc1 = Entry(frame, state = DISABLED)
numpc1.grid(row = 3, column = 1)
numpc2 = Entry(frame, state = DISABLED)
numpc2.grid(row = 4, column = 1)
numpc3 = Entry(frame, state = DISABLED)
numpc3.grid(row = 5, column = 1)
numpc4 = Entry(frame, state = DISABLED)
numpc4.grid(row = 6, column = 1)

# Amount
lbl_amount = Label(text = "Amount", background = '#CBB3E1')
lbl_amount.grid(row = 2, column = 2, sticky = W)
amt1 = Entry(frame, state = DISABLED)
amt1.grid(row=3, column=2)
amt2 = Entry(frame, state = DISABLED)
amt2.grid(row = 4, column = 2)
amt3 = Entry(frame, state = DISABLED)
amt3.grid(row = 5, column = 2)
amt4 = Entry(frame, state = DISABLED)
amt4.grid(row = 6, column = 2)

# Total Deposit
lbl_total_deposit = Label(text = "Total Deposit:", background = '#CBB3E1')
lbl_total_deposit.grid(row = 7, column = 0, sticky = W)
total_dep = Entry(frame, state = DISABLED)
total_dep.grid(row = 7, column = 1)

# Current Balance
lbl_current_balance = Label(text = "Current Balance:", background = '#CBB3E1')
lbl_current_balance.grid(row = 8, column = 0, sticky = W)
current_bal = Entry(frame, state = DISABLED)
current_bal.grid(row = 8, column = 1)

#Compute Button
btn_compute = Button(text = "COMPUTE", background = '#CBB3E1', state = DISABLED, command = compute)
btn_compute.grid(row = 9, column = 0, columnspan = 3)

frame.mainloop()