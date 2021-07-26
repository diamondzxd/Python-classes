from Bank import Bank
from tkinter import *


win=Tk()

def AddRecord():
    acno=txtAcno.get(1.0,END)
    name=txtName.get(1.0,END)
    branch=txtBranch.get(1.0,END)
    balance=txtBalance.get(1.0,END)
    b=Bank(acno,name,branch,balance)

    output=b.GetAcno()+b.GetName()+b.GetBranch()+b.GetBalance()

    lblResult['text']=output
    


lblAcno=Label(win,text="Account Number")
lblName=Label(win,text="Name")
lblBranch=Label(win,text="Branch")
lblBalance=Label(win,text="Balance")

txtAcno=Text(win,height=1,width=40)
txtName=Text(win,height=1,width=40)
txtBranch=Text(win,height=1,width=40)
txtBalance=Text(win,height=1,width=40)

btnCommand=Button(win,text="Add Record",command=AddRecord)

lblResult=Label(win,text='',height=5,width=40)

lblAcno.pack()
txtAcno.pack()
lblName.pack()
txtName.pack()
lblBranch.pack()
txtBranch.pack()
lblBalance.pack()
txtBalance.pack()
btnCommand.pack()
lblResult.pack()








