import pymongo
from pymongo import MongoClient
from tkinter import *
import time;
import datetime
import random

from tkinter import messagebox
client = MongoClient()
db = client.renin
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
log = ' '
cost1 = 0
total1 = 0
Billno = ' '
def loginemp():
    root3 = Tk()
    root3.overrideredirect(True)
    root3.geometry("{0}x{1}+0+0".format(root3.winfo_screenwidth(), root3.winfo_screenheight()))
    root3.title("Store Name")
    #-------------------------------------------------------------------------------------------------------------------------------------------
    Titlecard = Frame(root3, width = 1280, height = 100, bd = 7, bg = 'dodgerblue', relief = GROOVE)
    Titlecard.pack(side = 'top', anchor = CENTER, fill = X)
    rt = time.strftime("%d/%m/%y")
    body  = Frame(root3, width = 1280, height = 600, bd = 9, bg = 'dodgerblue3', relief = FLAT)
    body.pack(side = 'top',fill = BOTH)
    login = Frame(body, width = 600, height = 600, bd = 7, bg = 'Steelblue2', relief = RAISED)
    login.pack(side = TOP, anchor = CENTER, fill = Y, ipady = 100,ipadx = 10) 
    #-------------------------------------------------------------------------------------------------------------------------------------------
    Username = StringVar()
    Password = StringVar()
    Values1 = ['Username :','Password :']
    Values = [Username, Password]
    #-------------------------------------------------------------------------------------------------------------------------------------------
    def clear():
         for y in Values:
              y.set("")
    def exiit():
         qexit = messagebox.askyesno("SHOP NAME","DO YOU WISH TO EXIT")
         if qexit > 0:
              root3.destroy()
    def signup():
         root3.destroy()
         emplyrentry()
    def logn():
         Username2 = str(Username.get())
         Password2 = str(Password.get())
         
         empen = db.Emplyrrentry.find_one({"name":Username2})
         log1 = str(empen['name'])
         global log
         log = log1
         if len(Username.get()) == 0 or len(Password.get()) == 0:
              messagebox.showerror("Customer Details", "Incorrect Entry")
         elif str(empen['name']) != Username2 or str(empen['Password']) != Password2:
              messagebox.showerror("Customer Details", "Incorrect Entry")
         elif str(empen['name']) == Username2 and str(empen['Password']) == Password2:
              root3.destroy()
              selectionscreen()
         else:
              messagebox.showerror("Customer Details", "Incorrect Entry")
    #-------------------------------------------------------------------------------------------------------------------------------------------
    date1 = Label(Titlecard, text = "DATE:" + rt,relief = GROOVE, width = 17, bd  = 7,bg = 'white', fg = 'black',font = ('arial', 15, 'italic'))
    date1.pack(side = RIGHT, anchor = NW, pady = 15)

    Title = Label(Titlecard, text = "SHOP NAME", relief = GROOVE, width = 15 , bd = 7, bg = 'dodgerblue4',
                  fg = 'lightSkyblue2', font = ('arial', 20, 'italic'))
    Title.pack(side = LEFT,pady = 15, ipadx = 35, padx =45)

    logintitle = Label(login, text = "LOGIN", relief = FLAT, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'Steelblue', font = ('arial', 20, 'italic'))
    logintitle.grid(row = 0, column = 0, columnspan = 3)
    r = 1
    for t in Values1:
         Label(login, text=t, relief=FLAT,width=10,padx = 10, pady = 10, bd = 6, fg = 'black',bg = 'Steelblue2',
               font = ('arial', 15, 'bold')).grid(row=r,column=0)
         r = r + 1
    Entry(login, relief=SUNKEN,font = ('arial', 15, 'italic'), textvariable = Username,
               bd = 9, insertwidth = 3).grid(row=1,column=1,pady = 20)
    Entry(login, relief=SUNKEN,font = ('arial', 15, 'italic'), show ="*",textvariable = Password,
               bd = 9, insertwidth = 3).grid(row=2,column=1,pady = 20)
   #-------------------------------------------------------------------------------------------------------------------------------------------
    btn1 = Button(login, text = "LOGIN",command = logn, relief = RAISED, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue2', font = ('arial', 20, 'italic')).grid(row = 4, column = 0, columnspan = 3)
    btn2 = Button(login, text = "CLEAR",command = clear, relief = RAISED, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue2', font = ('arial', 20, 'italic')).grid(row = 5, column = 0, columnspan = 3)
    btn3 = Button(login, text = "SIGNUP",command = signup, relief = RAISED, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue2', font = ('arial', 20, 'italic')).grid(row = 7, column = 0, columnspan = 3)
    btn4 = Button(login, text = "EXIT",command = exiit, relief = RAISED, width = 10 , bd = 6, bg = 'red',
                       fg = 'black', font = ('arial', 20, 'italic')).grid(row = 8, column = 0, columnspan = 3)
    #-------------------------------------------------------------------------------------------------------------------------------------------
    root3.mainloop()

def selectionscreen():
    root2 = Tk()
    root2.overrideredirect(True)
    root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
    root2.title("Store Name")
    #-------------------------------------------------------------------------------------------------------------------------------------------
    Titlecard = Frame(root2, width = 1280, height = 100, bd = 7,bg = 'lightblue', relief = "flat")
    Titlecard.pack(side = TOP,anchor = W ,fill = X)
    Body = Frame(root2, width = 1280, height = 700, bd = 7, bg = 'white', relief = "sunken")
    Body.pack(side = TOP, anchor = CENTER, fill = BOTH,ipady = 15)
    Exit = Frame(Body, width = 400, height = 50, bd = 8, bg = 'white', relief =FLAT)
    Exit.pack(side = BOTTOM, anchor = CENTER, fill = X)
    Buttons = Frame(Body, width = 640, height = 300, bd = 8, bg = 'blue', relief = "groove")
    Buttons.pack(side = BOTTOM,anchor =S,fill = Y,pady = 25)
    #-------------------------------------------------------------------------------------------------------------------------------------------
    MsgTitle = Label(Body, text = "Creating bills Since Big Bang!!", relief = RAISED, width = 15, padx = 16, pady = 16, bd = 7, fg = 'darkred', bg = 'red',font = ('arial', 15, 'italic'))
    MsgTitle.pack(side = TOP, anchor = N, fill = X)
    #-------------------------------------------------------------------------------------------------------------------------------------------
    def Cust():
        root2.destroy()
        customerentry()
    def Chngstcks():
        root2.destroy()
        stockmaintenance()
    def createbills():
        root2.destroy()
        createbill()
    def view():
        root2.destroy()
        viewscreen()
    def back():
        root2.destroy()
        loginemp()
    #-------------------------------------------------------------------------------------------------------------------------------------------
    btn5 = Button(Exit, font = ('arial', 15, 'italic'),text = "BACK",command = back)
    btn5.pack(side = BOTTOM, anchor = S,expand = 5,ipadx = 35)
    #-------------------------------------------------------------------------------------------------------------------------------------------
    btn1 = Button(Buttons, font = ('arial', 20, 'italic'), text = "ADD CUSTOMERS",command = Cust)
    btn1.grid(row = 1, column = 0,pady = 10,padx = 10)
    btn2 = Button(Buttons, font = ('arial', 20, 'italic'), text = "CHANGE STOCKS",command = Chngstcks)
    btn2.grid(row = 1, column = 1,pady = 10,padx = 10)
    btn3 = Button(Buttons, font = ('arial', 20, 'italic'), text = "     CREATE BILLS",command = createbills)
    btn3.grid(row = 2, column = 0,pady = 10,padx = 10)
    btn4 = Button(Buttons, font = ('arial', 20, 'italic'), text = "     VIEW DETAILS",command = view)
    btn4.grid(row = 2, column = 1,pady = 10,padx = 10)
    #-------------------------------------------------------------------------------------------------------------------------------------------
    rt = time.strftime("%d/%m/%y")
    date1 = Label(Body, text = "DATE:" + rt,relief = GROOVE, width = 17, bd  = 7,bg = 'white', fg = 'black',font = ('arial', 15, 'italic'))
    date1.pack(side = RIGHT, anchor = NW)
    root2.mainloop()              
#-------------------------------------------------------------------------------------------------------------------------------------------    
def emplyrentry():
    root4= Tk()
    root4.overrideredirect(True)
    root4.geometry("{0}x{1}+0+0".format(root4.winfo_screenwidth(), root4.winfo_screenheight()))
    root4.title("SHOP --")
    #-----------------------------------------------------------------------------------------------------#
    Username = StringVar()
    Password = StringVar()
    Re_enterPassword = StringVar()
    Address = StringVar()
    Phonenumber = StringVar()
    Email = StringVar()
    Values1 = ['Location :','Phone number:','Email:']
    Values = [Address,Phonenumber,Email] 
    #-----------------------------------------------------------------------------------------------------#
    def create():
         Username1 = str(Username.get())
         Password1 = str(Password.get())
         Re_enterPassword1 = str(Re_enterPassword.get())
         Address1 = str(Address.get())
         Phnumber1 = str(Phonenumber.get())
         Email1 = str(Email.get())
         if len(Username1) == 0:
              messagebox.showerror("Customer Details", "Enter Name")
         elif len(Password1) == 0:
              messagebox.showerror("Customer Details", "Enter Password")
         elif len(Address1) == 0:
              messagebox.showerror("Customer Details", "Enter Location")
         elif len(Phnumber1) != 10 :
                messagebox.showerror("Customer Details", "Invalid  Phone Number")
         elif len(Email1) == 0:
              messagebox.showerror("Customer Details", "Invalid Email ID") 
         elif Username1.isalpha() == False:
              messagebox.showerror("Customer Details", "Invalid Name")
         elif Address1.isalpha() == False:
              messagebox.showerror("Customer Details", "Invalid Location")
         elif Phnumber1.isdigit() == False:
             messagebox.showerror("Customer Details", "Invalid  Phone Number")
         elif '@' not in Email1 and '.com' not in Email1:
              messagebox.showerror("Customer Details", "Invalid Email ID")
         elif Password1 != Re_enterPassword1:
              messagebox.showerror("Customer Details", "Incorrect Password")
         else:
              unm = Username1
              pswd =  Password1
              Ads =  Address1
              Ph =  Phnumber1
              Em = Email1
              db.Emplyrrentry.insert_one({"name":unm,"Password":pswd,"Address":Ads,"phonenum":Ph,"Email":Em})
    def clear():
         for j in Values:
              j.set("")
    def back():
         root4.destroy()
         loginemp()
    #-----------------------------------------------------------------------------------------------------#
    Titlecard = Frame(root4, width = 1280, height = 100, bd = 7, bg = 'dodgerblue', relief = GROOVE)
    Titlecard.pack(side = 'top', anchor = CENTER, fill = X)
    rt = time.strftime("%d/%m/%y")
    body  = Frame(root4, width = 1280, height = 600, bd = 9, bg = 'dodgerblue3', relief = FLAT)
    body.pack(side = 'top',fill = BOTH)
    login = Frame(body, width = 700, height = 500, bd = 7, bg = 'Steelblue2', relief = RAISED)
    login.pack(side = TOP,anchor = CENTER, fill = Y,ipadx = 100)
    loginbtns = Frame(body, width = 700, height = 50, bd = 7, bg = 'Steelblue2', relief = RAISED)
    loginbtns.pack(side = BOTTOM,anchor = CENTER, fill = X,ipady = 10)
    date1 = Label(Titlecard, text = "DATE:" + rt,relief = GROOVE, width = 17, bd  = 7,bg = 'white', fg = 'black',font = ('arial', 15, 'italic'))
    date1.pack(side = RIGHT, anchor = NW, pady = 15,ipadx = 20)
    Title = Label(Titlecard, text = "SHOP NAME", relief = GROOVE, width = 10 , bd = 7, bg = 'dodgerblue4',
                  fg = 'lightSkyblue2', font = ('arial', 20, 'italic')).pack( anchor = N, pady = 15,ipadx = 20)

    logintitle = Label(login, text = "CREATE ACCOUNT", relief = FLAT, width = 16 , bd = 6, bg = 'Steelblue2',
                       fg = 'Steelblue', font = ('arial', 20, 'italic'))
    logintitle.grid(row = 0, column = 0, columnspan = 3)

    Label(login, text='Username', relief=FLAT,width=16,padx = 10, pady = 10, bd = 6, fg = 'black',bg = 'Steelblue2',
          font = ('arial', 15, 'bold')).grid(row=1,column=0)
    Entry(login, relief=SUNKEN,font = ('arial', 15, 'italic'), textvariable = Username,
          bd = 9, insertwidth = 3).grid(row=1,column=1,pady = 15,ipadx = 15,columnspan = 3)
    Label(login, text='Password', relief=FLAT,width=16,padx = 10, pady = 10, bd = 6, fg = 'black',bg = 'Steelblue2',
          font = ('arial', 15, 'bold')).grid(row=2,column=0)
    Entry(login, relief=SUNKEN,font = ('arial', 15, 'italic'), show ="*", textvariable = Password,
          bd = 9, insertwidth = 3).grid(row=2,column=1,pady = 15,ipadx = 15,columnspan = 3)
    Label(login, text='Re-enter Password', relief=FLAT,width=16,padx = 10, pady = 10, bd = 6, fg = 'black',bg = 'Steelblue2',
          font = ('arial', 15, 'bold')).grid(row=3,column=0)
    Entry(login, relief=SUNKEN,font = ('arial', 15, 'italic'), show ="*", textvariable = Re_enterPassword,
          bd = 9, insertwidth = 3).grid(row=3,column=1,pady = 15,ipadx = 15,columnspan = 3)  
    r = 4
    for t in Values1:
         Label(login, text=t, relief=FLAT,width=16,padx = 10, pady = 10, bd = 6, fg = 'black',bg = 'Steelblue2',
               font = ('arial', 15, 'bold')).grid(row=r,column=0)
         r = r + 1
    g = 4
    for c in Values:   
        Entry(login, relief=SUNKEN,font = ('arial', 15, 'italic'), textvariable = c,
                   bd = 9, insertwidth = 3).grid(row=g,column=1,pady = 15,ipadx = 15,columnspan = 3)
        g = g + 1

    btn1 = Button(loginbtns, text = "CREATE",command = create, relief = RAISED, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue2', font = ('arial', 20, 'italic')).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X,ipady = 10)
    btn2 = Button(loginbtns, text = "CLEAR",command = clear, relief = RAISED, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue2', font = ('arial', 20, 'italic')).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X,ipady = 10)
    btn3 = Button(loginbtns, text = "BACK",command = back, relief = RAISED, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue2', font = ('arial', 20, 'italic')).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X,ipady = 10)
    root4.mainloop()
def customerentry():
    root1 = Tk()
    root1.overrideredirect(True)
    root1.geometry("{0}x{1}+0+0".format(root1.winfo_screenwidth(), root1.winfo_screenheight()))
    root1.title("Customer Details")
    #-----------------------------------------------------------------------------------------------------#
    cuscount = db.Customerentry.find( { } )
    cuscount1 = db.Customerentry.find( { } ).count()
    Name = StringVar()
    IDnumber = StringVar()
    Address = StringVar()
    Phnumber = StringVar()
    Email = StringVar()
    Values = [Name,Address,Phnumber,Email]
    Values1 = ['ID number','Name','Location','Phone number','Email']
    IDnumber.set(cuscount1)
    def ADD():
        nm1 = Name.get()
        Id1 =  cuscount1
        Ad1 =  Address.get()
        Ph1 =  Phnumber.get()
        Em1 = Email.get()
        if len(nm1) == 0 or len(str(Id1)) == 0 or len(Ad1) == 0  or len(Ph1) == 0 or len(str(Em1)) == 0 or nm1.isalpha() == False  or Ad1.isalpha() == False or len(Ph1) != 10 or  '@' not in Em1 or '.com' not in Em1 :
            messagebox.showerror("Customer Details", "Invalid Field")
        else:            
            nm = Name.get()
            Id =  Id1
            Ad =  Address.get()
            Ph =  Phnumber.get()
            Em = Email.get()
            try:                
                CT = db.Customerentry.find_one({"name":nm})
                if nm1 == str(CT["name"]) or Id1 == str(CT["ID"]):
                    messagebox.showerror("Shop Name", "Existing Field")
                else:
                    db.Customerentry.insert_one({"name":nm,"ID":Id,"Address":Ad,"phonenum":Ph,"Email":Em})
            except:
                db.Customerentry.insert_one({"name":nm,"ID":Id,"Address":Ad,"phonenum":Ph,"Email":Em})
    def View():
        nm = str(Name.get())
        DET = db.Customerentry.find_one({"name":nm})
        IDnumber.set(str(DET['ID']))
        Address.set(str(DET['Address']))
        Phnumber.set(str(DET['phonenum']))
        Email.set(str(DET['Email']))            
    def btnClearDisplay():
        IDnumber.set(cuscount1)
        for e in Values:
            e.set("")           
    def iExit():
        qExit = messagebox.askyesno("Customer Details", "Do you want to exit the system")
        if qExit > 0:
            root1.destroy()
            return
    def Next():
        root1.destroy()
        selectionscreen()
    #-----------------------------------------------------------------------------------------------------#
    Titlecard = Frame(root1, width = 1280, height = 100, bd = 7,bg = 'lightblue', relief = "raise")
    Titlecard.pack(side = TOP,anchor = W ,fill = X)
    Totalbody = Frame(root1, width = 1280, height = 600,bd = 7, bg = 'skyblue', relief = "ridge")
    Totalbody.pack(side = TOP,anchor = CENTER, fill = BOTH)
    Totalbody1 = Frame(Totalbody, width = 1280, height = 600,bd = 7, bg = 'skyblue', relief = "ridge")
    Totalbody1.pack(side = TOP,anchor = CENTER, fill = Y,ipady = 10)
    Totalbody2 = Frame(root1, width = 1280, height = 600,bd = 7, bg = 'lightblue', relief = "flat")
    Totalbody2.pack(side = BOTTOM, fill = X,ipady = 10)
    #-----------------------------------------------------------------------------------------------------#
    Titlelbl = Label(Titlecard, font = ('arial', 30, 'italic'), text = " Customer Entries ", fg = 'black', bg = "lightblue", bd = 10)
    Titlelbl.pack(anchor = CENTER)
    r = 0
    for t in Values1:
         Label(Totalbody1, text=t, relief=FLAT,width=15,padx = 25, pady = 30, bd = 9, fg = 'black',bg = 'skyblue',
               font = ('arial', 15, 'bold')).grid(row=r,column=0)
         r = r + 1    
    Entry(Totalbody1, relief=SUNKEN,font = ('arial', 15, 'italic'), textvariable = IDnumber,state = DISABLED,
              bd = 9, insertwidth = 3).grid(row=0,column=1)    
    g = 1
    for c in Values:   
        Entry(Totalbody1, relief=SUNKEN,font = ('arial', 15, 'italic'), textvariable = c,
              bd = 9, insertwidth = 3).grid(row=g,column=1)
        g = g + 1
    #-----------------------------------------------------------------------------------------------------#
    btn1 = Button(Totalbody2, font = ('arial', 15, 'italic'),text = "ADD",command = ADD).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X)
    btn2 = Button(Totalbody2, font = ('arial', 15, 'italic'),text = "SEARCH",command = View).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X)
    btn3 = Button(Totalbody2, font = ('arial', 15, 'italic'),text = "CLEAR",command = btnClearDisplay).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X)
    btn4 = Button(Totalbody2, font = ('arial', 15, 'italic'),text = "BACK",command = Next).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X)

def viewscreen():
    root7 = Tk()
    root7.overrideredirect(True)
    root7.geometry("{0}x{1}+0+0".format(root7.winfo_screenwidth(), root7.winfo_screenheight()))
    root7.title("Customer Details")
        #-------------------------------------------------------------------------------------------------------------------------------------------
    Titlecard = Frame(root7, width = 1280, height = 100, bd = 7,bg = 'lightblue', relief = "flat")
    Titlecard.pack(side = TOP,anchor = W ,fill = X)
    Body = Frame(root7, width = 1280, height = 700, bd = 7, bg = 'white', relief = "sunken")
    Body.pack(side = TOP, anchor = CENTER, fill = BOTH,ipady = 15)
    Exit = Frame(Body, width = 400, height = 50, bd = 8, bg = 'white', relief =FLAT)
    Exit.pack(side = BOTTOM, anchor = CENTER, fill = X)
    Buttons = Frame(Body, width = 640, height = 300, bd = 8, bg = 'blue', relief = "groove")
    Buttons.pack(side = BOTTOM,anchor =S,fill = Y,pady = 25)
    #-------------------------------------------------------------------------------------------------------------------------------------------
    MsgTitle = Label(Body, text = "Creating bills Since Big Bang!!", relief = RAISED, width = 15, padx = 16, pady = 16, bd = 7, fg = 'darkred', bg = 'red',font = ('arial', 15, 'italic'))
    MsgTitle.pack(side = TOP, anchor = N, fill = X)    
    #-------------------------------------------------------------------------------------------------------------------------------------------
    def viewstockpage():
        root7.destroy()
        viewstock()         
    def viewEmployeepage():
        root7.destroy()
        viewEmployee()
    def viewCustomerpage():
        root7.destroy()
        viewCustomer()        
    def back():
        root7.destroy()
        selectionscreen()
    btn5 = Button(Exit, font = ('arial', 15, 'italic'),text = "BACK",command = back)
    btn5.pack(side = LEFT, anchor = S,expand = 5,ipadx = 35)
    btn3 = Button(Exit, font = ('arial', 15, 'italic'),text = "View Stock details",command = viewstockpage)
    btn3.pack(side = LEFT, anchor = S,expand = 5,ipadx = 35)
    btn4 = Button(Exit, font = ('arial', 15, 'italic'),text = "View Employee details",command = viewEmployeepage)
    btn4.pack(side = LEFT, anchor = S,expand = 5,ipadx = 35)
    btn2 = Button(Exit, font = ('arial', 15, 'italic'),text = "View Customer details",command = viewCustomerpage)
    btn2.pack(side = LEFT, anchor = S,expand = 5,ipadx = 35)
    #-------------------------------------------------------------------------------------------------------------------------------------------
    rt = time.strftime("%d/%m/%y")
    date1 = Label(Body, text = "DATE:" + rt,relief = GROOVE, width = 17, bd  = 7,bg = 'white', fg = 'black',font = ('arial', 15, 'italic'))
    date1.pack(side = RIGHT, anchor = NW)
def viewstock():
    root8 = Tk()
    root8.overrideredirect(True)
    root8.geometry("{0}x{1}+0+0".format(root8.winfo_screenwidth(), root8.winfo_screenheight()))
    root8.title("Customer Details")
        #-------------------------------------------------------------------------------------------------------------------------------------------
    Titlecard = Frame(root8, width = 1280, height = 100, bd = 7,bg = 'lightblue', relief = "flat")
    Titlecard.pack(side = TOP,anchor = W ,fill = X)
    Body = Frame(root8, width = 1280, height = 700, bd = 7, bg = 'white', relief = "sunken")
    Body.pack(side = TOP, anchor = CENTER, fill = BOTH,ipady = 15)
    Exit = Frame(Body, width = 400, height = 50, bd = 8, bg = 'white', relief =FLAT)
    Exit.pack(side = BOTTOM, anchor = CENTER, fill = X)
    Buttons = Frame(Body, width = 640, height = 300, bd = 8, bg = 'blue', relief = "groove")
    Buttons.pack(side = BOTTOM,anchor =S,fill = Y,pady = 25)
    stocks = db.Stockmain.find( { } )
    stocks1 = db.Stockmain.find( { } ).count()
    stock = ['Item Name','Size','Total tems','Cost per item','discount per item']
##    Buttons1 = Frame(Body, width = 640, height = 300, bd = 8, bg = 'blue', relief = "groove")
##    Buttons1.pack(side = BOTTOM,anchor =S,fill = Y,pady = 25)
    #-------------------------------------------------------------------------------------------------------------------------------------------
    height = stocks1
    width = 5
    for i in range(len(stock)):
        a = Label(Buttons, text=stock[i], width = 17, bd  = 7, relief = "raise")
        a.grid(row=0, column=i)
    for i in range(height): #Rows
        for j in range(width): #Columns
            b = Label(Buttons, text=stocks[i]['ItemName'], width = 17, bd  = 7)
            b.grid(row=(i+1), column=0)
            c = Label(Buttons, text=stocks[i]['Size'], width = 17, bd  = 7)
            c.grid(row=(i+1), column=1)
            d = Label(Buttons, text=stocks[i]['TotalItems'], width = 17, bd  = 7)
            d.grid(row=(i+1), column=2)
            e = Label(Buttons, text=stocks[i]['Costperitem'], width = 17, bd  = 7)
            e.grid(row=(i+1), column=3)
            f = Label(Buttons, text=stocks[i]['discountperitem'], width = 17, bd  = 7)
            f.grid(row=(i+1), column=4)
  #-------------------------------------------------------------------------------------------------------------------------------------------
    def viewEmployeepage():
        root8.destroy()
        viewEmployee()
    def viewCustomerpage():
        root8.destroy()
        viewCustomer()        
    def back():
        root8.destroy()
        viewscreen()
    MsgTitle = Label(Body, text = "Creating bills Since Big Bang!!", relief = RAISED, width = 15, padx = 16, pady = 16, bd = 7, fg = 'darkred', bg = 'red',font = ('arial', 15, 'italic'))
    MsgTitle.pack(side = TOP, anchor = N, fill = X)
    btn5 = Button(Exit, font = ('arial', 15, 'italic'),text = "BACK",command = back)
    btn5.pack(side = LEFT, anchor = S,expand = 5,ipadx = 35)
    btn3 = Button(Exit, font = ('arial', 15, 'italic'),text = "View Customer details",command = viewCustomerpage)
    btn3.pack(side = LEFT, anchor = S,expand = 5,ipadx = 35)
    btn4 = Button(Exit, font = ('arial', 15, 'italic'),text = "View Employee details",command = viewEmployeepage)
    btn4.pack(side = LEFT, anchor = S,expand = 5,ipadx = 35)
##    root7.mainloop()
    rt = time.strftime("%d/%m/%y")
    date1 = Label(Body, text = "DATE:" + rt,relief = GROOVE, width = 17, bd  = 7,bg = 'white', fg = 'black',font = ('arial', 15, 'italic'))
    date1.pack(side = RIGHT, anchor = NW)
    root8.mainloop()

def viewEmployee():
    root9 = Tk()
    root9.overrideredirect(True)
    root9.geometry("{0}x{1}+0+0".format(root9.winfo_screenwidth(), root9.winfo_screenheight()))
    root9.title("Customer Details")
        #-------------------------------------------------------------------------------------------------------------------------------------------
    Titlecard = Frame(root9, width = 1280, height = 100, bd = 7,bg = 'lightblue', relief = "flat")
    Titlecard.pack(side = TOP,anchor = W ,fill = X)
    Body = Frame(root9, width = 1280, height = 700, bd = 7, bg = 'white', relief = "sunken")
    Body.pack(side = TOP, anchor = CENTER, fill = BOTH,ipady = 15)
    Exit = Frame(Body, width = 400, height = 50, bd = 8, bg = 'white', relief =FLAT)
    Exit.pack(side = BOTTOM, anchor = CENTER, fill = X)
    Buttons = Frame(Body, width = 640, height = 300, bd = 8, bg = 'blue', relief = "groove")
    Buttons.pack(side = BOTTOM,anchor =S,fill = Y,pady = 25)
    Employees = db.Emplyrrentry.find( { } )
    Employee1 = db.Emplyrrentry.find( { } ).count()
    Employee = ['Name','Email','phonenum','Location']
##    Buttons1 = Frame(Body, width = 640, height = 300, bd = 8, bg = 'blue', relief = "groove")
##    Buttons1.pack(side = BOTTOM,anchor =S,fill = Y,pady = 25)

    #-------------------------------------------------------------------------------------------------------------------------------------------
    height = Employee1
    width = 5
    for i in range(len(Employee)):
        a1 = Label(Buttons, text=Employee[i], width = 17, bd  = 7, relief = "raise")
        a1.grid(row=0, column=i)
    for i in range(height): #Rows
        for j in range(width): #Columns
            b1 = Label(Buttons, text=Employees[i]['name'], width = 17, bd  = 7)
            b1.grid(row=(i+1), column=0)
            d1 = Label(Buttons, text=Employees[i]['Email'], width = 17, bd  = 7)
            d1.grid(row=(i+1), column=1)
            e1 = Label(Buttons, text=Employees[i]['phonenum'], width = 17, bd  = 7)
            e1.grid(row=(i+1), column=2)
            f1 = Label(Buttons, text=Employees[i]['Address'], width = 17, bd  = 7)
            f1.grid(row=(i+1), column=3)
  #-------------------------------------------------------------------------------------------------------------------------------------------
    def viewstockpage():
        root9.destroy()
        viewstock()
    def viewCustomerpage():
        root9.destroy()
        viewCustomer()      
    def back():
        root9.destroy()
        viewscreen()
    #-------------------------------------------------------------------------------------------------------------------------------------------
    MsgTitle = Label(Body, text = "Creating bills Since Big Bang!!", relief = RAISED, width = 15, padx = 16, pady = 16, bd = 7, fg = 'darkred', bg = 'red',font = ('arial', 15, 'italic'))
    MsgTitle.pack(side = TOP, anchor = N, fill = X)
    btn5 = Button(Exit, font = ('arial', 15, 'italic'),text = "BACK",command = back)
    btn5.pack(side = LEFT, anchor = S,expand = 5,ipadx = 35)
    btn3 = Button(Exit, font = ('arial', 15, 'italic'),text = "View Stock details",command = viewstockpage)
    btn3.pack(side = LEFT, anchor = S,expand = 5,ipadx = 35)
    btn4 = Button(Exit, font = ('arial', 15, 'italic'),text = "View Customer details",command = viewCustomerpage)
    btn4.pack(side = LEFT, anchor = S,expand = 5,ipadx = 35)
##    root7.mainloop()
    rt = time.strftime("%d/%m/%y")
    date1 = Label(Body, text = "DATE:" + rt,relief = GROOVE, width = 17, bd  = 7,bg = 'white', fg = 'black',font = ('arial', 15, 'italic'))
    date1.pack(side = RIGHT, anchor = NW)
    root9.mainloop()

def viewCustomer():
    root10 = Tk()
    root10.overrideredirect(True)
    root10.geometry("{0}x{1}+0+0".format(root10.winfo_screenwidth(), root10.winfo_screenheight()))
    root10.title("Customer Details")
        #-------------------------------------------------------------------------------------------------------------------------------------------
    Titlecard = Frame(root10, width = 1280, height = 100, bd = 7,bg = 'lightblue', relief = "flat")
    Titlecard.pack(side = TOP,anchor = W ,fill = X)
    Body = Frame(root10, width = 1280, height = 700, bd = 7, bg = 'white', relief = "sunken")
    Body.pack(side = TOP, anchor = CENTER, fill = BOTH,ipady = 15)
    Exit = Frame(Body, width = 400, height = 50, bd = 8, bg = 'white', relief =FLAT)
    Exit.pack(side = BOTTOM, anchor = CENTER, fill = X)
    Buttons = Frame(Body, width = 640, height = 300, bd = 8, bg = 'blue', relief = "groove")
    Buttons.pack(side = BOTTOM,anchor =S,fill = Y,pady = 25)
    Customers = db.Customerentry.find( { } )
    Customer1 = db.Customerentry.find( { } ).count()
    Customer = ['ID','name','Email','phone number','Location']
##    Buttons1 = Frame(Body, width = 640, height = 300, bd = 8, bg = 'blue', relief = "groove")
##    Buttons1.pack(side = BOTTOM,anchor =S,fill = Y,pady = 25)
    #-------------------------------------------------------------------------------------------------------------------------------------------
    height = Customer1
    width = 5
    for i in range(len(Customer)):
        a1 = Label(Buttons, text=Customer[i], width = 17, bd  = 7, relief = "raise")
        a1.grid(row=0, column=i)
    for i in range(height): #Rows
        for j in range(width): #Columns
            b1 = Label(Buttons, text=Customers[i]['ID'], width = 17, bd  = 7)
            b1.grid(row=(i+1), column=0)
            c1 = Label(Buttons, text=Customers[i]['name'], width = 17, bd  = 7)
            c1.grid(row=(i+1), column=1)
            d1 = Label(Buttons, text=Customers[i]['Email'], width = 17, bd  = 7)
            d1.grid(row=(i+1), column=2)
            e1 = Label(Buttons, text=Customers[i]['phonenum'], width = 17, bd  = 7)
            e1.grid(row=(i+1), column=3)
            f1 = Label(Buttons, text=Customers[i]['Address'], width = 17, bd  = 7)
            f1.grid(row=(i+1), column=4)       
  #-------------------------------------------------------------------------------------------------------------------------------------------
    def viewstockpage():
        root10.destroy()
        viewstock()       
    def viewEmployeepage():
        root10.destroy()
        viewEmployee()
    
    def back():
        root10.destroy()
        viewscreen()
    #-------------------------------------------------------------------------------------------------------------------------------------------
    MsgTitle = Label(Body, text = "Creating bills Since Big Bang!!", relief = RAISED, width = 15, padx = 16, pady = 16, bd = 7, fg = 'darkred', bg = 'red',font = ('arial', 15, 'italic'))
    MsgTitle.pack(side = TOP, anchor = N, fill = X)
    btn5 = Button(Exit, font = ('arial', 15, 'italic'),text = "BACK",command = back)
    btn5.pack(side = LEFT, anchor = S,expand = 5,ipadx = 35)
    btn3 = Button(Exit, font = ('arial', 15, 'italic'),text = "View Stock details",command = viewstockpage)
    btn3.pack(side = LEFT, anchor = S,expand = 5,ipadx = 35)
    btn4 = Button(Exit, font = ('arial', 15, 'italic'),text = "View Employee details",command = viewEmployeepage)
    btn4.pack(side = LEFT, anchor = S,expand = 5,ipadx = 35)
##    root7.mainloop()
    rt = time.strftime("%d/%m/%y")
    date1 = Label(Body, text = "DATE:" + rt,relief = GROOVE, width = 17, bd  = 7,bg = 'white', fg = 'black',font = ('arial', 15, 'italic'))
    date1.pack(side = RIGHT, anchor = NW)
    root10.mainloop()

def createbill():
    root6= Tk()
    root6.overrideredirect(True)
    root6.geometry("{0}x{1}+0+0".format(root6.winfo_screenwidth(), root6.winfo_screenheight()))
    root6.title("SHOP --")
    #-----------------------------------------------------------------------------------------------------#
    Cusnm = StringVar()
    Cusphn = StringVar()
    CusItm = StringVar()
    Count = StringVar()
    CusQty = StringVar()
    Costprice = StringVar()
    Totalprice = StringVar()
    rant = StringVar()
    cust = ["Bill.No.:","Customer Name:","Phone number:","Item Name:","Count:","Quantity:","Cost Price:","Total Price:"]
    custvar = [Cusnm,Cusphn,CusItm,Count,CusQty,Costprice,Totalprice]
    #-----------------------------------------------------------------------------------------------------#
    Titlecard = Frame(root6, width = 1280, height = 100, bd = 7, bg = 'dodgerblue', relief = GROOVE)
    Titlecard.pack(side = 'top', anchor = CENTER, fill = X)
    rt = time.strftime("%d/%m/%y")
    date1 = Label(Titlecard, text = "DATE:" + rt,relief = GROOVE, width = 15, bd  = 7,bg = 'white', fg = 'black',font = ('arial', 15, 'italic'))
    date1.pack(side = RIGHT, anchor = NW, pady = 15,ipadx = 15)
    name1 = Label(Titlecard, text = "EMPLOYEE NAME:" + str(log),relief = GROOVE, width = 20, bd  = 7,bg = 'white', fg = 'black',font = ('arial', 15, 'italic'))
    name1.pack(side = LEFT, anchor = NW, pady = 15,ipadx = 15)
    Title = Label(Titlecard, text = "SHOP NAME", relief = GROOVE, width = 10 , bd = 7, bg = 'dodgerblue4',
                  fg = 'lightSkyblue2', font = ('arial', 20, 'italic'))
    Title.pack( anchor = N, pady = 15,ipadx = 20,padx =10)
    body  = Frame(root6, width = 1280, height = 650, bd = 9, bg = 'dodgerblue3', relief = FLAT)
    body.pack(side = 'top',fill = BOTH)
    buttons = Frame(body, width = 1280, height = 50, bd = 7 , bg = 'white', relief = RAISED)
    buttons.pack(side = BOTTOM,fill = X)
    left = Frame(body, width = 600, height = 600, bd = 7 , bg = 'white', relief = RAISED)
    left.pack(side = LEFT,fill = Y)
    lftbtn = Frame(left,width = 670, height = 200, bd = 7, bg = 'blue',relief = RAISED)
    lftbtn.pack(side = BOTTOM,fill = X)
    lftentry = Frame(left, width = 670, height = 400, bd = 7 , bg = 'white', relief = RAISED)
    lftentry.pack(side = LEFT,fill = Y)
    right = Frame(body, width = 670, height = 600, bd = 7 , bg = 'grey', relief = RAISED)
    right.pack(side = RIGHT,fill = Y)
    r = 1
    for i in cust:
        Label(lftentry, text = i,relief = FLAT, width = 13, padx = 7,  pady = 3 , bd = 3, bg = 'white' ,
                     font = ('arial', 20, 'bold')).grid(row = r , column = 0)
        r = r + 1
    e = 1
    Entry(lftentry, textvariable = Cusnm, relief = SUNKEN, font = ('arial', 20, 'italic'),
                      bd = 7, insertwidth = 3).grid(row = 2 , column = 1,columnspan = 3,ipadx = 30,padx = 20,pady = 6)
    Label(lftentry, textvariable = Cusphn,relief = FLAT, width = 20, padx = 7,  pady = 3 , bd = 3, bg = 'white' ,
                     font = ('arial', 20, 'bold')).grid(row = 3 , column = 1)
    Label(lftentry, textvariable = CusQty,relief = FLAT,width = 20, padx = 7,  pady = 3 , bd = 3, bg = 'white'
          ,font = ('arial', 20, 'bold')).grid(row = 6 , column = 1)
    Label(lftentry, textvariable = Costprice,relief = FLAT,width = 20, padx = 7,  pady = 3 , bd = 3, bg = 'white'
          ,font = ('arial', 20, 'bold')).grid(row = 7 , column = 1)
    Label(lftentry, textvariable = Totalprice, relief = FLAT,width = 20, padx = 7,  pady = 3 , bd = 3, bg = 'white'
          ,font = ('arial', 20, 'italic')).grid(row = 8 , column = 1)   

    def srch():
        Cus_name =  str(Cusnm.get()).lower()
        ran = str(random.randint(10001,99999))
        cus = db.Customerentry.find_one({"name":Cus_name})
        if len(Cus_name) == 0:
            messagebox.showerror("Shop name","Incorrect Entry")
        elif type(cus) == type(None) :
            qExit = messagebox.askyesno("Customer Details", "No existing customer.Create new one?")
            if qExit > 0:
                root6.destroy()
                customerentry()            
        elif str(cus['name']) == Cus_name :
            t = Label(lftentry, textvariable = rant, relief = FLAT, font = ('arial', 20, 'italic')
                      ,bg = 'white' ,bd = 7).grid(row = 1 , column = 1,columnspan = 3
                                   ,ipadx = 20,padx = 20,pady = 6)
            r = Entry(lftentry, textvariable = CusItm, relief = SUNKEN, font = ('arial', 20, 'italic'),
                      bd = 7, insertwidth = 3).grid(row = 4 , column = 1,columnspan = 3
                                                    ,ipadx = 20,padx = 10,pady = 3)
            e = Entry(lftentry, textvariable = Count, relief = SUNKEN, font = ('arial', 20, 'italic'),
                      bd = 7, insertwidth = 3).grid(row = 5 , column = 1,columnspan = 3
                                                    ,ipadx = 20,padx = 10,pady = 3)
            phnc = str(cus['phonenum'])
            rant.set("BILL " + ran )
            Cusphn.set(phnc)
            
    def update():
        itemnm = str(CusItm.get())
        itmcnt = str(Count.get())
        try:
            itm = db.Stockmain.find_one({"ItemName":itemnm})
            cost = ((int(itm['Costperitem']) * int(itmcnt)) - int(itm['discountperitem']))
            global cost1
            cost1 = cost1 + cost
            Costprice.set(cost1)
            CP = int(itm['Costperitem'])
            qty = int(cost1 / CP)
            CusQty.set(qty)            
        except:
            qExit = messagebox.askyesno("Stock Details", "No existing product.Create new one?")
            if qExit > 0:
                root6.destroy()
                stockmaintenance()
                
    def add():
        randomm = str(rant.get())
        Cusname = str(Cusnm.get())
        phncus = str(Cusphn.get())
        itemnm = str(CusItm.get())
        itmqty = str(CusQty.get())
        itmcp = str(Costprice.get())
        itm = db.Stockmain.find_one({"ItemName":itemnm}) 
        Cp = str(Costprice.get())
        try:
            bil = db.Bill.find_one({"id":randomm})
            if bil['Item name'] == itemnm:
                bq = bil['Item quantity']
                bc = bil['Cost price']
                baq = int(bq) + int(itmqty)
                bac = int(bc) + int(itmcp)
                itmupd = int(itm['TotalItems']) - int(itmqty)
                if itmupd < 0:
                    messagebox.showerror("Shop name","Item out of stock")
                else:
                    db.Bill.update_one({"id":randomm},{"$set":{"Item quantity":baq,"Cost price":bac}})
                    db.Stockmain.update_one({"ItemName":itemnm},{"$set":{"TotalItems":itmupd}})
            else:
                itmupd = int(itm['TotalItems']) - int(itmqty)
                if itmupd < 0:
                    messagebox.showerror("Shop name","Item out of stock")
                else:
                    db.Bill.insert_one({"id":randomm,"Cust name":Cusname,"Cust phnum":phncus
                                ,"Item name":itemnm, "Item quantity":itmqty,"Cost price":itmcp})
                    db.Stockmain.update_one({"ItemName":itemnm},{"$set":{"TotalItems":itmupd}})                
        except:
            if len(randomm) == 0 or len(str(itemnm)) == 0 or len(str(itmqty)) == 0  or len(str(itmcp)) == 0:
                messagebox.showerror("Bill Entry", "Enter Fields")                
            else:
                itmupd = int(itm['TotalItems']) - int(itmqty)
                if itmupd < 0:
                    messagebox.showerror("Shop name","Item out of stock")
                else:
                    db.Bill.insert_one({"id":randomm,"Cust name":Cusname,"Cust phnum":phncus
                                ,"Item name":itemnm, "Item quantity":itmqty,"Cost price":itmcp})
                    db.Stockmain.update_one({"ItemName":itemnm},{"$set":{"TotalItems":itmupd}})        
        global total1,cost1
        try:
            cost1 = 0
            total1 = total1 + int(Cp)
            Totalprice.set(total1)        
            CusItm.set("")
            Count.set("")
            CusQty.set("")
            Costprice.set("")
        except:
            pass

    def view():
        randomm = str(rant.get())
        TP = str(Totalprice.get())
        Bill = db.Bill.find( {"id":randomm} )
        Billc = db.Bill.find( {"id":randomm} ).count()
        Bill2 = ['Bill number','Item name','Item quantity','Cost price']
      #-------------------------------------------------------------------------------------------------------------------------------------------
        height = Billc
        width = 4
        for i in range(len(Bill2)):
            a1 = Label(right, text=Bill2[i], width = 17, bd  = 7, relief = "raise")
            a1.grid(row=0, column=i,ipadx = 5,padx = 5,pady = 4)
        for i in range(height): #Rows
            for j in range(width): #Columns
                b1 = Label(right, text=Bill[i]['id'], width = 17, bd  = 7)
                b1.grid(row=(i+1), column=0)
                d1 = Label(right, text=Bill[i]['Item name'], width = 17, bd  = 7)
                d1.grid(row=(i+1), column=1)
                e1 = Label(right, text=Bill[i]['Item quantity'], width = 17, bd  = 7)
                e1.grid(row=(i+1), column=2)
                f1 = Label(right, text=Bill[i]['Cost price'], width = 17, bd  = 7)
                f1.grid(row=(i+1), column=3)
                tp1 = Label(right, text="Total Amount: ", width = 17, bd  = 7, relief = "raise")
                tp1.grid(row=(Billc+1), column=2,ipadx = 5,padx = 5,pady = 4)
                tp2 = Label(right, text=TP, width = 17, bd  = 7, relief = "groove")
                tp2.grid(row=(Billc+1), column=3,ipadx = 5,padx = 5,pady = 4)

    def clearrr():
        randomm = str(rant.get())
        Bill = db.Bill.find( {"id":randomm} )
        Billc = db.Bill.find( {"id":randomm} ).count()
        Bill2 = ['Bill number','Item name','Item quantity','Cost price']
      #-------------------------------------------------------------------------------------------------------------------------------------------
        height = Billc
        width = 4
        for i in range(len(Bill2)):
            a1 = Label(right, text=Bill2[i], width = 17, bd  = 7, relief = "raise")
            a1.grid(row=0, column=i,ipadx = 5,padx = 5,pady = 4)
        for i in range(height): #Rows
            for j in range(width): #Columns
                b1 = Label(right, text="", width = 17, bd  = 7)
                b1.grid(row=(i+1), column=0)
                d1 = Label(right, text="",width = 17, bd  = 7)
                d1.grid(row=(i+1), column=1)
                e1 = Label(right, text="", width = 17, bd  = 7)
                e1.grid(row=(i+1), column=2)
                f1 = Label(right, text="", width = 17, bd  = 7)
                f1.grid(row=(i+1), column=3)
                tp2 = Label(right, text="", width = 17, bd  = 7, relief = "groove")
                tp2.grid(row=(Billc+1), column=3,ipadx = 5,padx = 5,pady = 4)

                
    def clearr():
        rant.set("")
        Cusphn.set("")
        Costprice.set("")
        for j in custvar:
            j.set("")

    def CBill():
        randomm1 = str(rant.get())
        Billc = db.Bill.find( {"id":randomm1} ).count()
        TP = str(Totalprice.get())
        global Billno
        Billno = randomm1
        db.GBill.insert_one({"id":randomm1,"Amount of items":Billc,"Total price":TP})
        root6.destroy()
        Cbill()        


    
    def back():
        root6.destroy()
        selectionscreen()


    adbtn = Button(lftbtn, text = "SEARCH",command = srch,relief = GROOVE, width = 25, bd = 6, bg = 'snow',
                   fg = 'blue3',font = ('arial',15,'bold')).grid(row = 1 , column = 0,ipadx = 10, ipady = 5)
    rmvbtn = Button(lftbtn, text = "UPDATE",command = update,relief = GROOVE, width = 25, bd = 6, bg = 'snow',
                   fg = 'blue3',font = ('arial',15,'bold')).grid(row = 1 , column = 1,ipadx = 10, ipady = 5)
    vbtn = Button(lftbtn, text = "ADD",command = add,relief = GROOVE, width = 25, bd = 6, bg = 'snow',
                   fg = 'blue3',font = ('arial',15,'bold')).grid(row = 2 , column = 0,ipadx = 10, ipady = 5)
    srchbtn = Button(lftbtn, text = "CLEAR",command = clearr,relief = GROOVE, width = 25, bd = 6, bg = 'snow',
                   fg = 'blue3',font = ('arial',15,'bold')).grid(row = 2 , column = 1,ipadx = 10, ipady = 5)
    #-----------------------------------------------------------------------------------------------------#
    viewbtn = Button(buttons, text = "VIEW",command = view,relief = RAISED, width = 20, bd = 8 , bg = 'red', fg = 'black',
                     font = ('arial',15,'bold')).pack(side = LEFT, anchor = CENTER, expand = 2, fill = X)
    clrrbtn = Button(buttons, text = "CLEAR",command = clearrr,relief = RAISED, width = 20, bd = 8 , bg = 'red', fg = 'black',
                     font = ('arial',15,'bold')).pack(side = LEFT, anchor = CENTER, expand = 2, fill = X)
    createbillbtn = Button(buttons, text = "CREATE BILL",command = CBill,relief = RAISED, width = 20, bd = 8 , bg = 'red', fg = 'black',
                           font = ('arial',15,'bold')).pack(side = LEFT, anchor = CENTER, expand = 2, fill = X)
    bckbtn = Button(buttons, text = "BACK",command = back,relief = RAISED, width = 20, bd = 8 , bg = 'red', fg = 'black',
                           font = ('arial',15,'bold')).pack(side = LEFT, anchor = CENTER, expand = 2, fill = X)
    root6.mainloop()


def Cbill():
    rootbill = Tk()
    rootbill.overrideredirect(True)
    rootbill.geometry("{0}x{1}+0+0".format(rootbill.winfo_screenwidth(), rootbill.winfo_screenheight()))
    rootbill.title("Bill")
    #-------------------------------------------------------------------------------------------------------------------------------------------
    Titlecard = Frame(rootbill, width = 1280, height = 100, bd = 7,bg = 'lightblue', relief = "flat")
    Titlecard.pack(side = TOP,anchor = W ,fill = X)
    Body = Frame(rootbill, width = 1280, height = 700, bd = 7, bg = 'white', relief = "sunken")
    Body.pack(side = TOP, anchor = CENTER, fill = BOTH,ipady = 15)
    Exit = Frame(Body, width = 400, height = 50, bd = 8, bg = 'white', relief =FLAT)
    Exit.pack(side = BOTTOM, anchor = CENTER, fill = X)
    Buttons = Frame(Body, width = 640, height = 300, bd = 8, bg = 'light blue', relief = "groove")
    Buttons.pack(side = BOTTOM,anchor =S,fill = Y,pady = 25)
    #-------------------------------------------------------------------------------------------------------------------------------------------
    Bill = db.GBill.find_one( {"id":Billno} )
    #-------------------------------------------------------------------------------------------------------------------------------------------
    MsgTitle = Label(Body, text = "Creating bills Since Big Bang!!", relief = RAISED, width = 15, padx = 16, pady = 16, bd = 7, fg = 'darkred', bg = 'red',font = ('arial', 15, 'italic'))
    MsgTitle.pack(side = TOP, anchor = N, fill = X)
    try:
        Label(Buttons, text = "Bill Number: ",relief = FLAT,width = 20, padx = 7,  pady = 3 , bd = 3, bg = 'white'
                  ,font = ('arial', 20, 'bold')).grid(row = 0 , column = 0)
        Label(Buttons, text = "No. of Items: ",relief = FLAT,width = 20, padx = 7,  pady = 3 , bd = 3, bg = 'white'
                  ,font = ('arial', 20, 'bold')).grid(row = 1 , column = 0)
        Label(Buttons, text = "Totalprice", relief = FLAT,width = 20, padx = 7,  pady = 3 , bd = 3, bg = 'white'
                  ,font = ('arial', 20, 'italic')).grid(row = 2 , column = 0)   
        Label(Buttons, text = Bill["id"],relief = FLAT,width = 20, padx = 7,  pady = 3 , bd = 3, bg = 'white'
                  ,font = ('arial', 20, 'bold')).grid(row = 0 , column = 1)
        Label(Buttons, text = Bill["Amount of items"],relief = FLAT,width = 20, padx = 7,  pady = 3 , bd = 3, bg = 'white'
                  ,font = ('arial', 20, 'bold')).grid(row = 1 , column = 1)
        Label(Buttons, text = Bill["Total price"], relief = FLAT,width = 20, padx = 7,  pady = 3 , bd = 3, bg = 'white'
                  ,font = ('arial', 20, 'italic')).grid(row = 2 , column = 1)
    except:
        pass

    #-------------------------------------------------------------------------------------------------------------------------------------------

    def back():
        rootbill.destroy()
        createbill()
    #-------------------------------------------------------------------------------------------------------------------------------------------
    btn5 = Button(Exit, font = ('arial', 15, 'italic'),text = "OKAY",command = back)
    btn5.pack(side = BOTTOM, anchor = S,expand = 5,ipadx = 35)
    #-------------------------------------------------------------------------------------------------------------------------------------------
    rt = time.strftime("%d/%m/%y")
    date1 = Label(Body, text = "DATE:" + rt,relief = GROOVE, width = 17, bd  = 7,bg = 'white', fg = 'black',font = ('arial', 15, 'italic'))
    date1.pack(side = RIGHT, anchor = NW)
    rootbill.mainloop()
    
def stockmaintenance():
    root5= Tk()
    root5.overrideredirect(True)
    root5.geometry("{0}x{1}+0+0".format(root5.winfo_screenwidth(), root5.winfo_screenheight()))

    root5.title("SHOP --")
    #-----------------------------------------------------------------------------------------------------#
    ItemName = StringVar()
    sizE = [('Small',1),('Medium',2),('Large',3)]
    Size = IntVar()
    TotalItems = StringVar()
    Costperitem = StringVar()
    discountperitem = StringVar()

    Values1 = ['Item Name :','Size:','Total Items','Cost per item:','discount per item:']
    Values = [ItemName,TotalItems,Costperitem,discountperitem]

    #-----------------------------------------------------------------------------------------------------#
    def create():
         if TotalItems.get() == "" and Costperitem.get() == "" and ItemName.get() == "" and Size.get() == "":
              messagebox.showerror("Shop Name", "Enter Fields")

         else:
              ItemName1 = str(ItemName.get())
              Size1 = Size.get()
              TotalItems1 = int(TotalItems.get())
              Costperitem1 = int(Costperitem.get())
              discountperitem1 = float(int(Costperitem1) / 100)
              discountperitem.set(discountperitem1)
              In1 = str(ItemName.get())
              IT = db.Stockmain.find_one({"ItemName":In1})
              try:
                  IT = db.Stockmain.find_one({"ItemName":In1})
                  if ItemName1 == str(IT['ItemName']):
                      messagebox.showerror("Shop Name", "Existing Field")
                  else:
                      db.Stockmain.insert_one({"ItemName":ItemName1,"Size":Size1,"TotalItems":TotalItems1,"Costperitem":Costperitem1,"discountperitem":discountperitem1})
              except:
                  db.Stockmain.insert_one({"ItemName":ItemName1,"Size":Size1,"TotalItems":TotalItems1,"Costperitem":Costperitem1,"discountperitem":discountperitem1})



            

    def update():
         ItemName1 = str(ItemName.get())
         Size1 = Size.get()
         TotalItems1 = int(TotalItems.get())
         Costperitem1 = int(Costperitem.get())
         discountperitem1 = float(int(Costperitem1) / 100)
         discountperitem.set(discountperitem1)
         In1 = str(ItemName.get())
         try:
             IT = db.Stockmain.find_one({"ItemName":In1})
             if ItemName1 == str(IT['ItemName']):
                 e = int(IT['TotalItems'])
                 d = int(IT['Costperitem'])
                 d = int(Costperitem1)
                 e = e + int(TotalItems1)
                 TotalItems.set(e)
                 Costperitem.set(d)
                 db.Stockmain.update_one({"ItemName":ItemName1},{"$set":{"TotalItems":e,"Costperitem":d}})
         except:
             pass
                 

             
         
    def clear():
         for j in Values:
              j.set("")
         Size.set(0)
    def view():
         In = str(ItemName.get())
         ITEM = db.Stockmain.find_one({"ItemName":In})
         Size.set(int(ITEM['Size']))
         TotalItems.set(str(ITEM['TotalItems']))
         Costperitem.set(str(ITEM['Costperitem']))
         discountperitem.set(str(ITEM['discountperitem']))


    def back():
         root5.destroy()
         selectionscreen()

    #-----------------------------------------------------------------------------------------------------#
    Titlecard = Frame(root5, width = 1280, height = 100, bd = 7, bg = 'dodgerblue', relief = GROOVE)
    Titlecard.pack(side = 'top', anchor = CENTER, fill = X)
    rt = time.strftime("%d/%m/%y")

    body  = Frame(root5, width = 1280, height = 600, bd = 9, bg = 'dodgerblue3', relief = FLAT)
    body.pack(side = 'top',fill = BOTH)
    login = Frame(body, width = 700, height = 600, bd = 7, bg = 'Steelblue2', relief = RAISED)
    login.pack(side = TOP,anchor = CENTER, fill = Y,ipadx = 100,ipady = 10,pady = 10)
    loginbtns = Frame(body, width = 700, height = 50, bd = 7, bg = 'Steelblue2', relief = RAISED)
    loginbtns.pack(side = BOTTOM,anchor = CENTER, fill = X)
    date1 = Label(Titlecard, text = "DATE:" + rt,relief = GROOVE, width = 15, bd  = 7,bg = 'white', fg = 'black',font = ('arial', 15, 'italic'))
    date1.pack(side = RIGHT, anchor = NW, pady = 15,ipadx = 15)



    Title = Label(Titlecard, text = "SHOP NAME", relief = GROOVE, width = 10 , bd = 7, bg = 'dodgerblue4',
                  fg = 'lightSkyblue2', font = ('arial', 20, 'italic'))
    Title.pack( anchor = N, pady = 15,ipadx = 20,padx =10)

    logintitle = Label(login, text = "Maintaining Stocks", relief = FLAT, width = 16 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue3', font = ('arial', 20, 'italic'))
    logintitle.grid(row = 0, column = 0, columnspan = 3)



    r = 1
    for t in Values1:
         Label(login, text=t, relief=FLAT,width=16,padx = 10, pady = 15, bd = 7, fg = 'black',bg = 'Steelblue2',
               font = ('arial', 15, 'bold')).grid(row=r,column=0,ipady = 10)
         
         r = r + 1
    ##g = 1
    ##for c in Values:   
    Entry(login, relief=SUNKEN,font = ('arial', 15, 'italic'), textvariable = ItemName,
         bd = 9, insertwidth = 3).grid(row=1,column=1,pady = 10,ipadx = 15,columnspan = 3)
    Entry(login, relief=SUNKEN,font = ('arial', 15, 'italic'), textvariable = TotalItems,
         bd = 9, insertwidth = 3).grid(row=3,column=1,pady = 10,ipadx = 15,columnspan = 3)
    Entry(login, relief=SUNKEN,font = ('arial', 15, 'italic'), textvariable = Costperitem,
         bd = 9, insertwidth = 3).grid(row=4,column=1,pady = 10,ipadx = 15,columnspan = 3)
    Entry(login, relief=SUNKEN,font = ('arial', 15, 'italic'), textvariable = discountperitem,
         bd = 9, insertwidth = 3).grid(row=5,column=1,pady = 10,ipadx = 15,columnspan = 3)
    ##    g = g + 1
    t = 1
    for d,c in sizE:
         Radiobutton(login, text = d,value = c,variable=Size,indicatoron=0,bg = 'red',font = ('arial', 15, 'bold')).grid(row = 2,column = t,padx =5, ipadx =15)
         t = t + 1
    btn1 = Button(loginbtns, text = "ADD",command = create, relief = RAISED, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue2', font = ('arial', 20, 'italic')).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X)
    btn1 = Button(loginbtns, text = "UPDATE",command = update, relief = RAISED, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue2', font = ('arial', 20, 'italic')).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X)
    btn1 = Button(loginbtns, text = "VIEW",command = view, relief = RAISED, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue2', font = ('arial', 20, 'italic')).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X)
    btn2 = Button(loginbtns, text = "CLEAR",command = clear, relief = RAISED, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue2', font = ('arial', 20, 'italic')).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X)
    btn3 = Button(loginbtns, text = "BACK",command = back, relief = RAISED, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue2', font = ('arial', 20, 'italic')).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X)
    root5.mainloop()
##    stockmaintenance()
loginemp()
