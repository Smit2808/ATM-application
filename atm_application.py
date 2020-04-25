from tkinter import *
from PIL import ImageTk,Image #for image or icon

# for making window 
root = Tk()
root.title("ATM APPLICATION")
root.iconbitmap("icon.ico")
wit = Entry(root, width=30, borderwidth=5)
depo = Entry(root, width=30, borderwidth=5)
balance = 1000 
e = Entry(root, width=30, borderwidth=5)
e.grid(row=0,column=1,padx=10)
pin_label = Label(root, text="Pin code: ").grid(row=0,column=0)

def balance():
	global balance
	balance = 1000
	show_bal = Label(root, text="Your Balance is "+str(balance)).grid(row=6,column=0,columnspan=2,pady=10)

def check():
	global balance 
	#amount = "Amount is: "+wit.get()
	#label = Label(root,text=amount).grid(row=9,column=0,columnspan=2,pady=10)
	if int(wit.get()) >= balance:
		low = Label(root, text="Not enough balance to withdraw").grid(row=9,column=0,columnspan=2,pady=10)
	else:
		balance = balance - int(wit.get())
		wit_succ = Label(root, text="After withdrawing remaining balance is: "+str(balance)).grid(row=9,column=0,columnspan=2,pady=10)
					
def Withdraw():
	wit.grid(row=7,column=1,padx=10,pady=10)
	wit_amount = Label(root, text="Withdrawal Amount: ").grid(row=7,column=0,pady=10)
	check_btn = Button(root, text="check", command=check).grid(row=8,column=0,columnspan=2,pady=10)

def add():
	global balance
	balance = balance + int(depo.get())
	depo_succ = Label(root, text="After depositing balance is: "+str(balance)).grid(row=13,column=0,columnspan=2,pady=10)
def Deposit():
	depo.grid(row=10,column=1,padx=10,pady=10)
	depo_amount = Label(root, text="Depositing Amount: ").grid(row=10,column=0,pady=10)
	add_depo = Button(root, text="Add deposit", command=add).grid(row=11,column=0,columnspan=2,pady=10)

def confirm():
	bal_btn = Button(root, text="Balance",command=balance).grid(row=2,column=0,columnspan=2,pady=10)
	wit_btn = Button(root, text="Withdraw",command=Withdraw).grid(row=3,column=0,columnspan=2,pady=10)
	dep_btn = Button(root, text="Deposit",command=Deposit).grid(row=4,column=0,columnspan=2,pady=10)
	ext_btn = Button(root, text="Exit",command=root.quit).grid(row=5,column=0,columnspan=2,pady=10)

confirm_pin = Button(root, text="CONFIRM", command=confirm).grid(row=1,column=0,columnspan=2,pady=10)

root.mainloop()