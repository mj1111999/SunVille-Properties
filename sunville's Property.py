from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import re, pymysql
from PIL import ImageTk, Image
import os
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import *
import pandas as pd
import numpy as np
import mysql.connector
import pandas.io.sql as sql
from pymysql import connect
from pandas.plotting import register_matplotlib_converters
#from mysql.connector import cursor
from mysql import *
def adjustWindow(window):
    w = 600 # width for the window size
    h = 600 # height for the window size
    ws = screen.winfo_screenwidth() # width of the screen
    hs = screen.winfo_screenheight() # height of the screen
    x = (ws/2) - (w/2) # calculate x and y coordinates for the Tk window
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y)) # set the dimensions of the screenand where it is placed
    window.resizable(False, False) # disabling the resize option for the window
    window.configure(background='white') # making the background white of the window
    

#VALIDATION AND DATABASE CONNECTION FOR THE ORDER DETAILS FORM
def verify_orderdetails():
    ORD_NUM=ord_no.get()
    if ord_no.get() and ord_amt.get() and adv_amt.get() and cust_code.get() and agt_code.get() and ord_des.get() and ent.get() and bal_amt.get() and agt_name.get():
        if all(x.isalpha() or x.isspace() for x in agt_name.get()) and (len(agt_name.get())>0):        
            if re.match("[\d]{4}-[\d]{1,2}-[\d]{1,2}",ent.get()):
                if len(ord_no.get())==6 and re.match("[0-9][0-9][0-9][0-9][0-9][0-9]",ord_no.get()):
                    if re.match("[0-9][0-9][0-9]",ord_amt.get()):
                        if re.match("[C]+[0-9][0-9][0-9][0-9][0-9]",cust_code.get()) and len(cust_code.get())==6:
                            if re.match("[0-9][0-9][0-9]",adv_amt.get()):
                                if re.match("[A]+[0-9][0-9][0-9]",agt_code.get()) and len(agt_code.get())==4:
                                    if re.match("[S]+[O]+[D]",ord_des.get()):
                                        if re.match("[0-9][0-9][0-9]",bal_amt.get()):
                                            mydb = mysql.connector.connect(host="localhost",user="root",password="",database="sales")
                                            cursor = mydb.cursor()
                                            q1=ORD_NUM
                                            query="SELECT * FROM orders WHERE ORD_NUM LIKE '%"+q1+"%'"
                                            cursor.execute(query)
                                            already_reg=cursor.fetchall()
                                            if already_reg:
                                                #messagebox.showerror("Bust!","Customer already registered",parent=screen5)
                                                Label(screen5, text="Bust! Order no. already exists", fg="red", font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
                                            else:
                                                connection = pymysql.connect(host="localhost", user="root", passwd="", database="sales")
                                                cursor = connection.cursor()
                                                insert_query ="INSERT INTO orders(ORD_NUM,ORD_AMOUNT,ADVANCE_AMOUNT,ORD_DATE,CUST_CODE,AGENT_CODE,ORD_DESCRIPTION,Agent_Name,Balance_Amount) VALUES('"+ ord_no.get() + "', '"+ ord_amt.get() + "', '"+ adv_amt.get() +"', '"+ ent.get() + "', '"+ cust_code.get() + "', '"+ agt_code.get() + "', '"+ ord_des.get() + "', '"+ agt_name.get() + "', '"+ bal_amt.get() + "' );"
                                                cursor.execute(insert_query)
                                                connection.commit()
                                                connection.close()
                                                print("DONE")
                                                Label(screen5, text="DETAILS FILLED SUCCESFULLY", fg="green", font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
                                                Button(screen5, text='DONE', width=20, font=("Open Sans", 9,'bold'), bg='brown', fg='white',command=screen5.destroy).place(x=470, y=565)
               
                                        else:
                                            Label(screen5, text="Please enter the valid Balance amount", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
                                    else:
                                        Label(screen5, text="Please enter the valid Order Description", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
                                else:
                                    Label(screen5, text="Please enter the valid Agent Code", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
                            else:
                                Label(screen5, text="Please enter the valid Advance amount", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
                        else:
                            Label(screen5, text="Please enter the valid Customer code", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
                    else:
                        Label(screen5, text="Please enter the valid order amount", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
                else:
                    Label(screen5, text="Please enter the valid order no", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
            else:
                Label(screen5, text="Please enter the valid date", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
                return            
        else:
            Label(screen5, text="Please Enter Valid Agent Name", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
            return
    else:
        Label(screen5, text="Please Fill all the details", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
#GUI FOR THE ORDER DETAILS FORM
def add_orderdetails():
    global screen5,ord_no,ord_amt,adv_amt,ord_date,cust_code,agt_code,ord_des,ent,agt_name,bal_amt
    screen5=Toplevel(screen)
    screen5.title("ADD THE ORDERS DETAILS")
    adjustWindow(screen5)
    ord_no=StringVar()
    ord_amt=StringVar()
    adv_amt=StringVar()
    ord_date=StringVar()
    cust_code=StringVar()
    agt_code=StringVar()
    ord_des=StringVar()
    agt_name=StringVar()
    bal_amt=StringVar()
    screen5.configure(bg="light blue")
    Label(screen5, text="Fill the details below", width='32', height="2", font=("Calibri", 22, 'bold'), fg='white', bg="black").place(x=50,y=0)
    Label(screen5, text="Order no:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=100)
    Entry(screen5, textvar=ord_no).place(x=250, y=100)
    Label(screen5, text="Order Amount", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=140)
    Entry(screen5, textvar=ord_amt).place(x=250, y=140)
    Label(screen5, text="Advance Amount", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=180)
    Entry(screen5, textvar=adv_amt).place(x=250, y=180)
    Label(screen5, text="Order Date", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=220)
    ent=DateEntry(screen5,width=15,bg="blue",fg="red",borderwidth=3,date_pattern='yyyy-mm-dd')
    ent.place(x=260,y=220)
    Label(screen5, text="Customer Code", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=260)
    Entry(screen5, textvar=cust_code).place(x=250, y=260)
    Label(screen5, text="Agent code", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=300)
    Entry(screen5, textvar=agt_code).place(x=250, y=300)
    Label(screen5, text="Order Description", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=340)
    Entry(screen5, textvar=ord_des).place(x=250, y=340)
    Label(screen5, text="Agent Name", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=380)
    Entry(screen5, textvar=agt_name).place(x=250, y=380)
    Label(screen5, text="Balance Amount", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=420)
    Entry(screen5, textvar=bal_amt).place(x=250, y=420)
    Button(screen5, text='Submit', width=20, font=("Open Sans", 13, 'bold'), bg='green', fg='white',command=verify_orderdetails).place(x=130, y=480)
    
def verify_customer():
   CUST_CODE =cust_code1.get()
   CUST_NAME = cust_name.get()
   CUST_CITY = cust_city.get()
   WORKING_AREA =  work_area.get()
   CUST_COUNTRY = cust_country.get()
   try:
       GRADE = grade.get()
   except:
       messagebox.showwarning("Alert","Invalid Grade",parent=screen2)
   OPENING_AMT = op_amt.get()
   RECEIVE_AMT = rcv_amt.get()
   PAYMENT_AMT = pay_amt.get()
   OUTSTANDING_AMT = out_amt.get()
   PHONE_NO = phone.get()
   AGENT_CODE= agt_code1.get()
   if cust_code1.get() and cust_name.get() and cust_city.get() and work_area.get() and cust_country.get() and op_amt.get() and rcv_amt.get() and pay_amt.get() and out_amt.get() and phone.get() and agt_code1.get() and grade.get():
       if re.match("[C]+[0-9][0-9][0-9][0-9][0-9]",cust_code1.get()) and len(cust_code1.get())==6:
           if all(x.isalpha() or x.isspace() for x in cust_name.get()) and (len(cust_name.get())>0):
               if all(y.isalpha() or y.isspace() for y in cust_city.get()) and (len(cust_city.get())>0):
                   if all(z.isalpha() or z.isspace() for z in work_area.get()) and (len(work_area.get())>0):
                       if all(w.isalpha() or w.isspace() for w in cust_country.get()) and (len(cust_country.get())>0):
                           if len(op_amt.get())==4 and op_amt.get().isdigit():
                               if len(rcv_amt.get())==4 and rcv_amt.get().isdigit():
                                   if len(pay_amt.get())==4 and pay_amt.get().isdigit():
                                       if len(out_amt.get())==4 and out_amt.get().isdigit():
                                           if len(phone.get())==10 and phone.get().isdigit():
                                               if re.match("[A]+[0-9][0-9][0-9]",agt_code1.get()) and len(agt_code1.get())==4:
                                                   if grade.get():
                                                       mydb = mysql.connector.connect(host="localhost",user="root",password="",database="sales")
                                                       cursor = mydb.cursor()
                                                       q1=CUST_CODE
                                                       query="SELECT * FROM customer WHERE CUST_CODE LIKE '%"+q1+"%'"
                                                       cursor.execute(query)
                                                       already_reg=cursor.fetchall()
                                                       if already_reg:
                                                           messagebox.showerror("Bust!","Customer already registered",parent=screen2)
                                                       else:
                                                           mydb = mysql.connector.connect(host="localhost",user="root",password="",database="sales")
                                                           cursor = mydb.cursor()
                                                           sql="INSERT INTO customer VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                                           cursor.execute(sql,(CUST_CODE,CUST_NAME,CUST_CITY,WORKING_AREA,CUST_COUNTRY,GRADE,OPENING_AMT, RECEIVE_AMT,PAYMENT_AMT,OUTSTANDING_AMT,PHONE_NO,AGENT_CODE))
                                                           mydb.commit()
                                                           print("Customer Added")
                                                           messagebox.showinfo("Success","Customer added Successfully",parent=screen2)
                                                           #return True
                                                   else:
                                                       messagebox.showerror("Error","Invalid Grade.\nHint:- The grade is a single digit number",parent=screen2)
                                                       
                                               else:
                                                   messagebox.showerror("Error","Invalid Agent Code.\n The Agent code starts from 'A' ",parent=screen2)
                                           else:
                                               messagebox.showerror("Error","Invalid Phone Number",parent=screen2)
                                       else:
                                           messagebox.showerror("Error","Invalid outstanding amount",parent=screen2)
                                   else:
                                       messagebox.showerror("Error","Invalid payment amount",parent=screen2)
                               else:
                                   messagebox.showerror("Error","Invalid Receive amount",parent=screen2)
                           else:
                               messagebox.showerror("Error","Invalid Opening amount",parent=screen2)
                       else:
                           messagebox.showerror("Error","Invalid Customer's Country",parent=screen2)
                   else:
                       messagebox.showerror("Error","Invalid Working area",parent=screen2)
               else:
                   messagebox.showerror("Error","Invalid Customer's City",parent=screen2)
           else:
               messagebox.showerror("Error","Invalid Customer Name \nMake Sure it's NOT a number",parent=screen2)
       else:
           messagebox.showerror("Error","Invalid Customer Code \nHint:The Customer Code starts from 'C' with five digit number",parent=screen2)
   else:
       messagebox.showerror("Error","Please Enter all details",parent=screen2)
       
def register_customer():
    global cust_code1,cust_name,cust_city,work_area,cust_country,grade,op_amt,rcv_amt,pay_amt,out_amt,phone,agt_code1,work_area,screen2
    screen2=Toplevel(screen)
    screen2.title("ADD THE CUSTOMER DETAILS")
    adjustWindow(screen2)
    cust_code1=StringVar()
    cust_name=StringVar()
    cust_city=StringVar()
    work_area =StringVar()
    cust_country=StringVar()
    grade=IntVar()
    op_amt=StringVar()
    rcv_amt=StringVar()
    pay_amt=StringVar()
    out_amt=StringVar()
    phone=StringVar()
    agt_code1=StringVar()    
    screen2.configure(bg="light blue")
    Label(screen2, text="Fill the details below", width='32', height="2", font=("Calibri", 22, 'bold'), fg='white', bg="black").place(x=50,y=0)
    Label(screen2, text="CUSTOMER CODE:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=100)
    Entry(screen2, textvar=cust_code1).place(x=280, y=100)
    Label(screen2, text="CUSTOMER NAME:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=140)
    Entry(screen2, textvar=cust_name).place(x=280, y=140)
    Label(screen2, text="CUSTOMER CITY:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=180)
    Entry(screen2, textvar=cust_city).place(x=280, y=180)
    Label(screen2, text="WORKING AREA:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=220)
    Entry(screen2, textvar=work_area).place(x=280, y=220)
    Label(screen2, text="CUSTOMER COUNTRY:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=260)
    Entry(screen2, textvar=cust_country).place(x=280, y=260)
    Label(screen2, text="GRADE:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=300)
    Entry(screen2, textvar=grade).place(x=280, y=300)
    Label(screen2, text="OPENING AMOUNT:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=340)
    Entry(screen2, textvar=op_amt).place(x=280, y=340)
    Label(screen2, text="RECIVING AMOUNT:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=380)
    Entry(screen2, textvar=rcv_amt).place(x=280, y=380)
    Label(screen2, text="PAYMENT Amount:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=420)
    Entry(screen2, textvar=pay_amt).place(x=280, y=420)
    Label(screen2, text="OUTSTANDING Amount:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=460)
    Entry(screen2, textvar=out_amt).place(x=280, y=460)
    Label(screen2, text="PHONE NO:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=500)
    Entry(screen2, textvar=phone).place(x=280, y=500)
    Label(screen2, text="AGENT CODE:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=540)
    Entry(screen2, textvar=agt_code1).place(x=280, y=540)
    Button(screen2, text='Submit', width=20, font=("Open Sans", 13, 'bold'), bg='green', fg='white',command=verify_customer).place(x=375, y=564)

def verify_company():
   COMPANY_ID=companyid.get()
   COMPANY_NAME = companyname.get()
   COMPANY_CITY= companycity.get()
   if companyid.get() and companyname.get() and companycity.get():
       if (len(companyid.get())==5 or len(companyid.get())==4 or len(companyid.get())==3 or len(companyid.get())==2) and companyid.get().isdigit():
           if all(x.isalpha() or x.isspace() for x in companyname.get()) and (len(companyname.get())>0):
               if all(y.isalpha() or y.isspace() for y in companycity.get()) and (len(companycity.get())>0):
                   mydb = mysql.connector.connect(host="localhost",user="root",password="",database="sales")
                   cursor = mydb.cursor()
                   q1=COMPANY_ID
                   query="SELECT * FROM company WHERE COMPANY_ID LIKE '%"+q1+"%'"
                   cursor.execute(query)
                   already_reg=cursor.fetchall()
                   if already_reg:
                       Label(screen7, text="Bust! Company already registered", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
                       #messagebox.showerror("Bust!","Agent Already Registered",parent=screen7)
                   else:
                       mydb = mysql.connector.connect(host="localhost",user="root",password="",database="sales")
                       cursor = mydb.cursor()
                       sql="INSERT INTO company VALUES(%s, %s, %s)"
                       cursor.execute(sql,(COMPANY_ID,  COMPANY_NAME ,COMPANY_CITY ))
                       mydb.commit()
                       #mydb.close()
                       #print("Company Added")
                       #messagebox.showinfo("Success","Company Added",parent=screen7)
                       Label(screen7, text="Company Added", fg="green",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
                       #return True
               else:
                   Label(screen7, text="Invalid Company City", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
                   return
           else:
               Label(screen7, text="Invalid Company Name", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
               return
       else:
           Label(screen7, text="Invalid Company ID", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
           return
   else:
       Label(screen7, text="Please fill all details", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
       return

def add_company():
    global companyid,companyname,companycity,screen7
    companyid=StringVar()
    companyname=StringVar()
    companycity=StringVar()
    screen7 = Toplevel(screen)
    screen7.title("Company Registeration Form ")
    
    adjustWindow(screen7)
    screen7.configure(bg='light blue')
    Label(screen7, text="Company Registration Form", width='32', height="2", font=("Calibri", 22, 'bold'), fg='white', bg="black").pack()
    Label(screen7, text="Company ID:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=160)
    Entry(screen7, textvar=companyid).place(x=260, y=160)
    Label(screen7, text="Company Name:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=210)
    Entry(screen7, textvar=companyname).place(x=260, y=210)
    Label(screen7, text="Company City:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=260)
    Entry(screen7, textvar=companycity).place(x=260, y=260)
    Button(screen7, text='Submit', width=20, font=("Open Sans", 13, 'bold'), bg='red', fg='white',command=verify_company).place(x=130, y=470)



         
def enter_details():
    global screen4
    screen4=Toplevel(screen)
    screen4.title("Fill the Details")
    adjustWindow(screen4)
    screen4.configure(bg="grey")
    Button(screen4, text='Add Agent Details Here', width=20, font=("Open Sans", 13, 'bold'), bg='#174873', fg='white',command=register_agent).place(x=200, y=175)
    Button(screen4, text='Add Company Details Here', width=30, font=("Open Sans", 13, 'bold'), bg='#174873', fg='white',command=add_company).place(x=150, y=225)
    Button(screen4, text='Add Customer Details Here', width=30, font=("Open Sans", 13, 'bold'), bg='#174873', fg='white',command=register_customer).place(x=150, y=275)
    Button(screen4, text='Add Order Details Here', width=20, font=("Open Sans", 13, 'bold'), bg='#174873', fg='white',command=add_orderdetails).place(x=200, y=325)    

def verify_register_agent():
   AGENT_CODE =agentcode.get()
   AGENT_NAME = agentname.get()
   WORKING_AREA = workingarea.get()
   try:
       COMMISSION = commission.get()
   except:
       messagebox.showwarning("Warning","Invalid Commision",parent=screen3)
   PHONE_NO = phoneno.get()
   COUNTRY = country.get()
   if agentcode.get() and agentname.get() and workingarea.get() and phoneno.get() and country.get() and commission.get():
       if re.match("[A]+[0-9][0-9][0-9]",agentcode.get()) and len(agentcode.get())==4:
           if all(x.isalpha() or x.isspace() for x in agentname.get()) and (len(agentname.get())>0):
               if all(y.isalpha() or y.isspace() for y in workingarea.get()) and (len(workingarea.get())>0):
                   if commission.get():
                       if len(phoneno.get())==10 and phoneno.get().isdigit():
                           if all(z.isalpha() or z.isspace() for z in country.get()) and (len(country.get())>0):
                               mydb = mysql.connector.connect(host="localhost",user="root",password="",database="sales")
                               cursor = mydb.cursor()
                               q1=AGENT_CODE
                               query="SELECT * FROM agents WHERE AGENT_CODE LIKE '%"+q1+"%'"
                               cursor.execute(query)
                               already_reg=cursor.fetchall()
                               if already_reg:
                                   Label(screen3, text="Bust! Agent already registered", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
                                   #messagebox.showerror("Bust!","Agent Already Registered",parent=screen3)
                               else:
                                   mydb = mysql.connector.connect(host="localhost",user="root",password="",database="sales")
                                   cursor = mydb.cursor()
                                   sql="INSERT INTO agents VALUES(%s, %s, %s, %s, %s, %s)"
                                   cursor.execute(sql,(AGENT_CODE,  AGENT_NAME , WORKING_AREA , COMMISSION ,PHONE_NO , COUNTRY))
                                   mydb.commit()
                                   mydb.close()
                                   print("Agent Added")
                                   messagebox.showinfo("Success","Agent Added Succesfully",parent=screen3)
                                   #return True
        
                           else:
                               messagebox.showerror("Error","Invalid Country",parent=screen3)
                       else:
                           messagebox.showerror("Error","Invalid phone number",parent=screen3)
                   else:
                       try:
                           messagebox.showerror("Error","Invalid Commision",parent=screen3)
                       except _tkinter.TclError:
                           messagebox.showwarning("Alert","Commision cannot accept other than numbers",parent=screen3)
               else:
                   messagebox.showerror("Error","Invalid Working area",parent=screen3)
           else:
               messagebox.showerror("Error","Invalid Agent name",parent=screen3)
       else:
           messagebox.showerror("Error","Invalid agent code",parent=screen3)
   else:
       messagebox.showerror("Error","Please fill all details",parent=screen3)
           
def register_agent():
    global  agentname, agentcode,workingarea,commission, phoneno, country,screen3 # making all entry field variable global
    screen3=Toplevel(screen)
    screen3.title("Agent Registeration Form ")
    adjustWindow(screen3)
    agentname = StringVar()
    workingarea = StringVar()
    commission=DoubleVar()
    phoneno= StringVar()
    country = StringVar()
    agentcode = StringVar()
    screen3.configure(bg='light blue')
    Label(screen3, text="Agent Registration Form", width='32', height="2", font=("Calibri", 22, 'bold'), fg='white', bg="black").pack()
    Label(screen3, text="Agent Code:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=160)
    Entry(screen3, textvar=agentcode).place(x=260, y=160)
    Label(screen3, text="Agent Name:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=210)
    Entry(screen3, textvar=agentname).place(x=260, y=210)
    Label(screen3, text="Working Area:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=260)
    Entry(screen3, textvar=workingarea).place(x=260, y=260)
    Label(screen3, text="Commission:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=310)
    Entry(screen3,textvar=commission).place(x=260, y=305)
    Label(screen3, text="Phone_No.:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=360)
    Entry(screen3, textvar=phoneno).place(x=260, y=360)
    Label(screen3, text="Country:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=410)
    entry_4 = Entry(screen3, textvar=country)
    entry_4.place(x=260, y=410)
    Button(screen3, text='Submit', width=20, font=("Open Sans", 13, 'bold'), bg='red', fg='white',command=verify_register_agent).place(x=130, y=470)
           
def Balance_Amount():
    conn= mysql.connector.connect(host="localhost",user="root",password="",database="sales")
    c = conn.cursor()
    c.execute("SELECT  DISTINCT AGENT_Code,Agent_Name,Balance_Amount from orders ORDER BY Balance_Amount DESC")
    rows = c.fetchall()
    total = c.rowcount
    print("Total Data Entries:"+str(total))
    
    win=Tk()
    frm = Frame(win)
    frm.pack(side=tk.TOP,padx=20,pady=80)
    tv = ttk.Treeview(frm,columns=(1,2,3),show="headings",height="30",padding=20)
    tv.pack()
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Italic", 15),fg='#174873')
    style.configure("Treeview.Insert",fg='#174873',font=("Italic", 15))
    win.configure(background='light blue')
    tv.heading(1,text="AGENT_Code:")
    tv.heading(2,text="Agent_Name:")
    tv.heading(3,text="Balance_Amount:")
    
    
    for i in rows:
        tv.insert('','end',values=i)
    win.title("Balance Data")
    win.geometry("650x500")
    win.mainloop()  

    
def Outstanding_Amount():
    conn= mysql.connector.connect(host="localhost",user="root",password="",database="sales")
    c = conn.cursor()
    c.execute("select * from (select count(cust_code) as cust_ct, sum(payment_amt), sum(outstanding_amt), cust_country from customer group by cust_country) as Q where cust_ct in (select max(cust) from (select count(cust_code) as cust, cust_country from customer group by cust_country) AS T);")
    rows = c.fetchall()
    total = c.rowcount
    print("Total Data Entries:"+str(total))
    
    win=Tk()
    frm = Frame(win)
    frm.pack(side=tk.TOP,padx=20,pady=80)
    tv = ttk.Treeview(frm,columns=(1,2,3,4),show="headings",height="06")
    tv.pack()
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Italic", 15),fg='#174873')
    win.configure(background='light blue')
    tv.heading(1,text="Order_No.")
    tv.heading(2,text="Payment_Amount:")
    tv.heading(3,text="Outstanding_Amount")
    tv.heading(4,text="Country:")

    for i in rows:
        tv.insert('','end',values=i)
    win.title("Balance_Data")
    win.geometry("1000x1000")
    win.mainloop()    
 

def fetch_records_new():
    win2=Tk()
    win2.geometry("850x850")
    global rows
    if orderno.get() or cust_code.get() or ent.get():
        if (len(orderno.get())==6 and orderno.get().isdigit()) or (re.match("[C]+[0-9][0-9][0-9][0-9][0-9]",cust_code.get()) and len(cust_code.get())==6) or (re.match("[\d]{4}-[\d]{1,2}-[\d]{1,2}",ent.get())):
            mydb= mysql.connector.connect(host="localhost",user="root",password="",database="sales")
            cursor = mydb.cursor()
            select_query="SELECT ORD_NUM,ORD_AMOUNT,ADVANCE_AMOUNT,ORD_DATE,CUST_CODE,AGENT_CODE,ORD_DESCRIPTION,Agent_Name,Balance_Amount FROM orders WHERE ORD_NUM LIKE '%"+orderno.get()+"%' AND  CUST_CODE LIKE '%"+cust_code.get()+"%' AND ORD_DATE LIKE '%"+ent.get()+"%'"
            cursor.execute(select_query)
            rows = cursor.fetchall()
            mydb.commit()
            total = cursor.rowcount
            print("Total Data Entries:"+str(total))
            messagebox.showinfo("Information","Total Data Entries:"+str(total),parent=win2)
        else:
            messagebox.showerror("Error","Invalid Credentials",parent=win2)
    else:
        messagebox.showerror("Error","Invalid Credentials",parent=win2)

    frm = Frame(win2)
    frm.pack(side=tk.LEFT,padx=20)
    tv = ttk.Treeview(frm,columns=(1,2,3,4,5,6,7,8,9),show="headings",height="30")
    
    tv.pack()
    style=ttk.Style()
    style.configure("Treeview.Heading",font=("Italic",10))
    win.configure(background='grey')
    tv.heading(1,text="Order_No.")
    tv.heading(2,text="Ord_AMOUNT:")
    tv.heading(3,text="ADVANCE_AMOUNT:")
    tv.heading(4,text="ORD_DATE:")
    tv.heading(5,text="CUST_CODE:")
    tv.heading(6,text="AGENT_CODE:")
    tv.heading(7,text="ORD_DESCRIPTION:")
    tv.heading(8,text="Agent_Name:")
    tv.heading(9,text="Balance_Amount:")
    for i in rows:
        tv.insert('','end',values=i)
    win2.title("Order Lookup")    
    win2.mainloop()

    
def Search_Order():
    #win=Tk()          
    global orderno,cust_code,ent,win
    orderno=StringVar()
    cust_code=StringVar()
    ent= StringVar()
    win=Toplevel(screen)
    adjustWindow(win)
    win.title("order details")
    win.configure(background="grey")
    Label(win, text="CHECK THE ORDER DETAILS HERE", width='32', height="2", font=("Calibri", 15, 'bold'), fg='white', bg="black").pack(padx=20,pady=10)
    Label(win, text="Order no:", font=("Open Sans", 11, 'bold'), fg='#174873', bg='light blue', anchor=W).place(x=30, y=100)
    e1=Entry(win, textvar=orderno).place(x=30, y=150)
    Label(win, text="Customer code:", font=("Open Sans", 11, 'bold'), fg='#174873', bg='light blue', anchor=W).place(x=450, y=100)
    e2=Entry(win, textvar=cust_code).place(x=450, y=150)
    Label(win, text="Order Date", font=("Open Sans", 11, 'bold'), fg='#174873', bg='light blue', anchor=W).place(x=210, y=100)
    ent = DateEntry(win,width=15,bg="blue",fg="red",borderwidth=3,date_pattern='yyyy-mm-dd')
    ent.pack(padx=180,pady=80)
    check=Button(win,text="Fetch_Order_Details",command=fetch_records_new).pack()
    #win.title("Order_Details")
    #win.geometry("650x500")
    #win.mainloop()
    #remove_orderno=Button(win,text="Discard Order No.").place(x=10,y=80)
def log_out():
    log_out=messagebox.askyesno("Logout Alert!","Are you sure you want to logout?",parent=screen2)
    if log_out>0:
        screen2.destroy()
def i_quit():
    i_quit=messagebox.askyesno("Login alert!","Are you sure you want to Exit?")
    if i_quit:
        screen.destroy()
def i_quit2():
    i_quit=messagebox.askyesno("Login alert!","Are you sure you want to go to Login Page?",parent=screen8)
    if i_quit:
        screen8.destroy()        
def welcome_page(agent_info):
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Welcome")
    img = ImageTk.PhotoImage(Image.open("D:\\Python Internship\\sunville1.jpg"))
    panel = Label(screen2,image = img)
    panel.place(x=0,y=0)
    panel.image=img
    panel.pack()
    adjustWindow(screen2)
    Label(screen2, text="Welcome " + agent_info[0][0], width='30', height="2", font=("Calibri", 15, 'bold'), fg='white', bg='#545454').place(x=0, y=150)
    img1 = ImageTk.PhotoImage(Image.open("D:\\Python Internship\\new-cover.jpeg"))
    panel1 = Label(screen2,image = img1)
    panel1.place(x=0,y=445)
    panel1.image=img1
    Label(screen2, text="", bg='light blue', width='20', height='16').place(x=0, y=204)
    Message(screen2, text='ABOUT US\n\n OUR TEAM \n\nBUY \n\n SELL \n\n RENT\n\n FAQ \n\n CONTACT US\n\n',width='180', font=("Helvetica", 10, 'bold', 'underline'), fg='#174873', bg='light blue', anchor = CENTER).place(x=0, y=204)
    Button(screen2, text='Enter your details', width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='white',command=enter_details).place(x=270, y=250)
    Button(screen2, text='ORDER LOOKUP', width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='white',command=Search_Order).place(x=270, y=300)
    Button(screen2, text='REPORT OF BALANCE.AMT', width=30, font=("Open Sans", 13, 'bold'), bg='brown', fg='white',command=Balance_Amount).place(x=220, y=350)
    Button(screen2, text='MAX.REGISTER CUSTOMER', width=30, font=("Open Sans", 13, 'bold'), bg='brown', fg='white',command=Outstanding_Amount).place(x=220, y=400)
    Button(screen2, text='INSIGHTS', width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='white',command=insights).place(x=270, y=450)
    Button(screen2, text='LOG OUT', width=10, font=("Open Sans", 13, 'bold'), bg='red', fg='white',command=log_out).place(x=490, y=10)        
def register_user():
    if fullname.get() and email.get() and password.get() and repassword.get() and gender.get():
        if country.get() == "--select your country--":
            Label(screen1, text="Please select your country", fg="red", font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
            return
        else:
            if all(x.isalpha() or x.isspace() for x in fullname.get()) and (len(fullname.get())>0):
                if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email.get()):
                    if password.get() == repassword.get() and len(password.get())>=8 and len(repassword.get())>=8:
                        gender_value = 'male'
                        if gender.get() == 2:
                            gender_value = 'female'
                        
                        mydb = mysql.connector.connect(host="localhost",user="root",password="",database="sales")
                        cursor = mydb.cursor()
                        q1=email.get()
                        query="SELECT * FROM agent_details WHERE email LIKE '%"+q1+"%'"
                        cursor.execute(query)
                        already_reg=cursor.fetchall()
                        if already_reg:
                            Label(screen1, text="Bust! User Already exists", fg="red", font=("calibri", 11), width='120', anchor=W, bg='white').place(x=0, y=570)
                        else:
                            connection = pymysql.connect(host="localhost", user="root", passwd="", database="sales") 
                            cursor = connection.cursor()
                            insert_query ="INSERT INTO agent_details (fullname, email, password,gender, country) VALUES('"+ fullname.get() + "', '"+ email.get() + "', '"+ password.get() +"', '"+ gender_value + "', '"+ country.get() + "' );"
                            cursor.execute(insert_query)
                            connection.commit() 
                            connection.close()
                            Label(screen1, text="Registration Sucess", fg="green", font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
                            Button(screen1, text='Proceed to Login ->', width=20, font=("Open Sans", 9,'bold'), bg='brown', fg='white',command=screen1.destroy).place(x=170, y=565)
                    else:
                        Label(screen1, text="Either Password does not match or Length of the password is less than than 8", fg="red", font=("calibri", 11), width='120', anchor=W, bg='white').place(x=0, y=570)
                        return
                else:
                    Label(screen1, text="Please enter valid email id", fg="red", font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
                    return
            else:
                Label(screen1, text="Please enter valid Full name", fg="red", font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
                return
    else:
        Label(screen1, text="Please fill all the details", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
        return    
        
def login_verify():
   
    global agentID
    try:
        connection = pymysql.connect(host="localhost", user="root", passwd="", database="sales") # database connection
    except:
        messagebox.showerror("Error","Can't Connect to the database at this moment \nMake Sure Wamp server is installed properly or \nconnection is established while clicking on application")
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="sales")
    cursor = connection.cursor()
    select_query =  "SELECT * FROM agent_details where email = '" + username_verify.get() + "' AND password = '" + password_verify.get() + "';" # queries for retrieving values
    cursor.execute(select_query) # executing the queries
    agent_info = cursor.fetchall()
    connection.commit() # commiting the connection then closing it.
    connection.close() # closing the connection of the database                    
    if agent_info:
        messagebox.showinfo("Congratulation", "Login Successfull") # displaying message for successful login
        agentID = agent_info[0][0]
        welcome_page(agent_info) # opening welcome window
    else:
        messagebox.showerror("Error", "Invalid Username or Password") # displaying message for invalid
            
def register():
    global screen1, fullname, email, password, repassword, country, gender, tnc # making all entry field variable global
    fullname = StringVar()
    email = StringVar()
    password = StringVar()
    repassword = StringVar()
    country = StringVar()
    gender = IntVar()
    tnc = IntVar()
    screen1 = Toplevel(screen)
    adjustWindow(screen1)
    screen1.title("Registeration")
    screen1.configure(bg='light blue')
    Label(screen1, text="Registration Form", width='32', height="2", font=("Calibri", 22, 'bold'), fg='white', bg="black").pack()
    Label(screen1, text="Full Name:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=160)
    Entry(screen1, textvar=fullname).place(x=260, y=160)
    Label(screen1, text="Email ID:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=210)
    Entry(screen1, textvar=email).place(x=260, y=210)
    Label(screen1, text="Gender:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=260)
    Radiobutton(screen1, text="Male", variable=gender, value=1, bg='#174873').place(x=260, y=260)
    Radiobutton(screen1, text="Female", variable=gender, value=2, bg='#174873').place(x=330, y=260)
    Label(screen1, text="Country:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=310)
    list1 = ['INDIA', 'USA','UK', 'AUSTRALIA']
    droplist = OptionMenu(screen1,country, *list1)
    droplist.config(width=17)
    country.set('--select your country--')
    droplist.place(x=260, y=305)
    Label(screen1, text="Password:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=360)
    Entry(screen1, textvar=password, show="*").place(x=260, y=360)
    Label(screen1, text="Re-Password:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=90, y=410)
    entry_4 = Entry(screen1, textvar=repassword, show="*")
    entry_4.place(x=260, y=410)
    
    Button(screen1, text='Submit', width=20, font=("Open Sans", 13, 'bold'), bg='red', fg='white',command=register_user).place(x=130, y=470)

def insights():
    #root=Tk()
    root = Toplevel(screen)
    root.title("Insights for SunVille")
    #adjustWindow(root)
    root.geometry("400x600")
    root.configure(background='Slate blue')
    def graph1():
        
        def soldvleased(year):
            leased=0
            owned=0
            test = pd.read_excel("D:\Python Internship\Dataset.xlsx",header=8)
            for row in test.itertuples(index=False):
                if row[0]==year:
                    temp=row[7]*10000
                else:
                    temp=row[7]
                if row[9]=='Leased':
                    leased=leased+temp
                elif row[9]=='Owned':
                    owned=owned+temp
                    
            print("THE LAND OWNED IN   SQM ",int(owned),"sqm")
            print("THE LAND LEASED IN   SQM ",int(leased),"sqm")        
            labels = 'Owned', 'Leased'
            sizes = [owned, leased]
            #sizes = [owned, leased]
            messagebox.showinfo("Information","owned:"+str(sizes[0])+" SQ-M" " Leased:"+str(sizes[1])+" SQ-M",parent=insight)
            #Label(root,text="owned:"+str(sizes[0])+" SQ-M" " Leased:"+str(sizes[1])+" SQ-M",fg="blue",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=10, y=100)
            fig1, ax1 = plt.subplots()
            #format(number) with "{:,}" as str to signal the use of a comma for a thousands separator and return a string with commas added to number .
            ax1.pie(sizes,labels=labels, startangle=90,autopct="%.1f%%",textprops={'fontsize': 20})
            
            ax1.axis('equal') 
            plt.show()
        
        def maxleasedarea():
            test = pd.read_excel("D:\Python Internship\Dataset.xlsx",header=8)
            di={"2017":0,"2018":0,"2019":0,"2020":0}
            for row in test.itertuples(index=False):
                if row[8]=='HA':
                    temp=row[7]*10000
                else:
                    temp=row[7]
                if (row[5]=='CA' or row[5]=='WS') and row[9]=='Leased':
                    di[str(row[0])]=di[str(row[0])]+temp
            Keymax = max(di, key=di.get) 
            print(Keymax)
            print("A")
            global year,insight   
            #insight=Tk()
            insight = Toplevel(screen)
            #adjustWindow(insight)
            insight.title("Choose Year")
            insight.configure(background='slate blue')
            chooseyear=Label(insight,width="500", height="2",text="Choose a Year for piechart" ,font=("Calibri", 22, 'bold'), fg='white', bg='#545454').pack()
            insight.geometry("500x500")
            #year=IntVar()
            def year2017():
                soldvleased(2017)
                plt.legend(loc='best',fontsize=12)
                plt.title("Owned Vs. Leased(2017)",fontsize=30)
                #plt.text(0.05,10,"owned:"+str(sizes[0])+" Leased:"+str(sizes[1]))
            def year2018():
                soldvleased(2018)
                plt.legend(loc='best',fontsize=12)  
                plt.title("Owned Vs. Leased(2018)",fontsize=30)
            def year2019():
                soldvleased(2019)
                plt.legend(loc='best',fontsize=12)
                plt.title("Owned Vs. Leased(2019)",fontsize=30)
            def year2020():
                soldvleased(2020)
                plt.legend(loc='best',fontsize=12)   
                plt.title("Owned Vs. Leased(2020)",fontsize=30)
            
              
            Button(insight,text="2017",command=year2017).place(x=10,y=90)
            Button(insight,text="2018",command=year2018).place(x=10,y=120)
            Button(insight,text="2019",command=year2019).place(x=10,y=150)
            Button(insight,text="2020",command=year2020).place(x=10,y=180)
            insight.mainloop()                 
            print("The best performer of 2017 is Subbaro and the amount of area sold in SQ-M is 2,15,080.56")
            print("The best performer of 2018 is Anderson and the amount of area sold in SQ-M is 105568.05")
            print("The best performer of 2019 is Mukesh and the amount of area sold in SQ-M is 106087.4492")
            print("B")
        maxleasedarea()  
    def graph2():
        excel_file='D:\Python Internship\Dataset.xlsx'
        test = pd.read_excel(io=excel_file,header=8)
        di={"2017":0,"2018":0,"2019":0,"2020":0}
        for row in test.itertuples(index=False):
            if row[8]=='HA':
                temp=row[7]*10000
            else:
                temp=row[7]
            if (row[5]=='CA' or row[5]=='WS') and row[9]=='Leased':
                di[str(row[0])]=di[str(row[0])]+temp
        Keymax = max(di, key=di.get) 
        fig, ax = plt.subplots(figsize =(10, 10))
        ax.bar(range(len(di)), list(di.values()), align='center',color='#ff22ff')
        for i in ax.patches:
            plt.text(i.get_x(), i.get_height(),str(round((i.get_height()), 2))+" SQ-M", fontsize = 20, fontweight ='bold', color ='black')
        plt.title("Maximum leased area",fontsize=30)    
        #plt.text(886876,886876,di)
        plt.xticks(range(len(di)), list(di.keys()),fontsize=14)
        plt.yticks(fontsize=14)
        print(di)
        #messagebox.showinfo("Information",di)
        #print("A")
        #print("B")
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='#ff22ff')
        plt.ylabel("Area in square metre",fontsize=20)
        plt.xlabel("Year",fontsize=20)
        plt.show()
        
    def graph3():
        con=connect(user="root",password="",host="localhost",database="sales")
        df=sql.read_sql('select AGENT_CODE, AGENT_NAME FROM agents',con)
        print(df)
        df.to_excel('D:\\Python Internship\\agent code and name.xlsx',index=False)
        dataset1="D:\\Python Internship\\Dataset.xlsx"
        dataset2="D:\\Python Internship\\agent code and name.xlsx"
        df1=pd.read_excel(dataset1,header=8)
        df2=pd.read_excel(dataset2,header=0)
        print(list(df2.iloc[:,0]))
        res=dict(zip(list(df2.iloc[:,1]),list(df2.iloc[:,0])))
        print(res)
        df3=df1.copy()
        df3['Agent_Code']=df3['Agent']
        df3["Agent_Code"].replace(
                        {'Alex': 'A003  ',
                         'Alford': 'A008  ',
                         'Anderson': 'A005  ',
                         'Benjamin': 'A009  ',
                         'Ivan': 'A004  ',
                         'Lucida': 'A012  ',
                         'McDen': 'A006  ',
                         'Mukesh': 'A002  ',
                         'Ramasundar     ': 'A007  ',
                         'Ramasundar     ': 'A007',
                         'Ravi Kumar': 'A011  ',
                         'Santakumar': 'A010  ',
                         'Subbarao': 'A001  '}, inplace=True)
        print(df3)
        df3=df3.to_excel("D:\\Python Internship\\Recent Dataset.xlsx")
        df4=pd.read_excel("D:\\Python Internship\\Recent Dataset.xlsx")
        property_owned=df4[df4['UoM']=='SQ-M']
        property_owned=property_owned[property_owned['Tenure']=='Owned']
        print(property_owned)
        property_owned_id=property_owned.to_excel("D:\\Python Internship\\propertyownedidsqm.xlsx")
        new_excel_owned=pd.read_excel("D:\\Python Internship\\propertyownedidsqm.xlsx")
        x1=new_excel_owned['Agent_Code']
        y=new_excel_owned['Area']
        fig, ax = plt.subplots(figsize =(10, 10))
        ax.bar(x1,y,align='center',color='red')
        plt.text(-0.5,6694.77,"6694.77 SQ-M",fontsize = 12, fontweight ='bold', color ='black')
        plt.text(0.5,12509.0,"12509.0 SQ-M",fontsize = 12, fontweight ='bold', color ='black')
        plt.text(1.5,45692.2,"45692.2 SQ-M",fontsize = 12, fontweight ='bold', color ='black')
        plt.text(2.5,23290.3,"23290.3 SQ-M",fontsize = 12, fontweight ='bold', color ='black')
        plt.text(3.5,12238.0,"12238.0 SQ-M",fontsize = 12, fontweight ='bold', color ='black')
        plt.text(4.5,18367.9,"18367.9 SQ-M",fontsize = 12, fontweight ='bold', color ='black')
        plt.text(5.5,29870.41,"29870.41 SQ-M",fontsize = 12, fontweight ='bold', color ='black')
        plt.text(6.5,13694.0,"13694.0 SQ-M",fontsize = 12, fontweight ='bold', color ='black')
        plt.text(7.5,8890.0,"8890.0 SQ-M",fontsize = 12, fontweight ='bold', color ='black')
        plt.text(0.07,-7550,"(Ramasundar)",fontsize=10,rotation=90, fontweight ='bold')
        plt.text(1.07,-5000,"(Alford)",fontsize=10,rotation=90, fontweight ='bold')
        plt.text(2.07,-5000,"(Lucida)",fontsize=10,rotation=90, fontweight ='bold')
        plt.text(3.07,-6000,"(Subbarao)",fontsize = 10,rotation=90, fontweight ='bold')
        plt.text(4.07,-4800,"(McDen)",fontsize = 10,rotation=90, fontweight ='bold')
        plt.text(5.07,-5700,"(Benjamin)",fontsize = 10,rotation=90, fontweight ='bold')
        plt.text(6.07,-5000,"(Mukesh)",fontsize = 10,rotation=90, fontweight ='bold')
        plt.text(7.07,-7500,"(Ravi Kumar)",fontsize = 10,rotation=90, fontweight ='bold')
        plt.text(8.07,-6000,"(Anderson)",fontsize = 10,rotation=90, fontweight ='bold')
        plt.yticks(fontsize=12)
        plt.xticks(rotation=90,fontsize=12)
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        # Customize the minor grid
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        #messagebox.showinfo("Best Performer","The best performer of 2017 is Subbaro and the amount of area sold in SQ-M is 2,15,080.56 \nThe best performer of 2018 is Anderson and the amount of area sold in SQ-M is 105568.05 \nThe best performer of 2019 is Mukesh and the amount of area sold in SQ-M is 106087.4492")
        #messagebox.showinfo("Information",res)
       
        plt.ylabel('Total Area owned by agent id in SQ-M',fontsize=20)
        plt.xlabel('Agents id',fontsize=20)
        plt.title("Property Insights",fontsize=30)
    def graph4():
        df1=pd.read_excel("D:/Python Internship/Recent Dataset.xlsx")
        cityleased=df1[df1['City']=='Chilliwack']
        cityleased=cityleased[cityleased['Tenure']=='Leased']
        cityleased=cityleased[cityleased['UoM']=='SQ-M']
        #print(cityleased)
        new_excel=cityleased.to_excel("Chilliwack city leased.xlsx",index=False)
        df2=pd.read_excel("Chilliwack city leased.xlsx",index=False)
        x=df2['Agent']
        y=df2['Area']
        fig, ax = plt.subplots(figsize =(10, 10))
        graph=ax.bar(x,y,align='center',color='#FFFF49')
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
        # Customize the minor grid
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        plt.text(0,1882.0,"1882.0 SQ-M",fontsize = 20, fontweight ='bold', color ='black')
        plt.text(1,1328.47,"1328.47 SQ-M",fontsize = 20, fontweight ='bold', color ='black')
        plt.xticks(rotation=90,fontsize=14)
        plt.ylabel('Total Area Sold by agents',fontsize=20)
        plt.xlabel('My Agents',fontsize=20)
        plt.title("Property Insights: Chilliwack's Analysis",fontsize=30)
        plt.yticks(fontsize=14)
        #plt.legend("Area",loc='best')
        plt.show()
        
    def graph5():
        excel_file='D:\\Python Internship\\Dataset.xlsx'
        test = pd.read_excel(excel_file,header=8)
        di={};
        for row in test.itertuples(index=False):
            if row[8]=='HA':
                temp=row[7]*10000
            else:
                temp=row[7]
            if di.get(str(row[11]).strip())==None:
                di[str(row[11]).strip()]=temp
            elif row[0]!=2020:
                di[str(row[11]).strip()]=di.get(str(row[11]).strip())+temp
        #fig = plt.figure()
        #ax = fig.add_axes([1,0,1,1])
        fig, ax = plt.subplots(figsize =(16, 9)) 
        agents = list(di.keys())
        land = list(di.values())
        ax.barh(agents,land)
        for i in ax.patches:
            plt.text(i.get_width(), i.get_y(),str(round((i.get_width()), 2))+" SQ-M",fontsize = 15, fontweight ='bold',color ='black') 
        plt.yticks(rotation=45,fontsize=14)
        plt.xlabel("Land owned/leased in SQ-M",fontsize=20)
        plt.ylabel("Agents",fontsize=20)
        plt.xticks(fontsize=14)
        plt.title("Best Perfomer",fontsize=30)
        #plt.title(-2,55000,"Best performer is Mukesh")
        messagebox.showinfo("Best Performer","Best performer is Mukesh",parent=root)
        
        plt.show()
        
    def graph6():
        excel_file='D:\Python Internship\Dataset.xlsx'
        test = pd.read_excel(io=excel_file,header=8)
        ans={"2017":0,"2018":0,"2019":0,"2020":0}
        for row in test.itertuples(index=False):
            if row[8]=='HA':
                temp=row[7]*10000
            else:
                temp=row[7]
            if row[1]=='JUL':
                if row[9]=='Owned':
                    ans[str(row[0])]=ans[str(row[0])]+temp
                     
        #fig = plt.figure()
        #ax = fig.add_axes([0,0,1,1])
        fig, ax = plt.subplots(figsize =(10, 10))
        agents = list(ans.keys())
        land = list(ans.values())
        plt.ylabel("Land owned(in SQ-M)",fontsize=20)
        plt.xlabel("Year",fontsize=20)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.title("Insights for july month",fontsize=30)
        #plt.bar(agents,land)
        ax.bar(agents,land,color='#8000ff')
        #print(ans)
        for i in ax.patches:
            plt.text(i.get_x(), i.get_height(),str(round((i.get_height()), 2))+" SQ-M", fontsize = 20, fontweight ='bold', color ='black')
        #messagebox.showinfo("Information",ans)
    
    def graph7():
        con=connect(user="root",password="",host="localhost",database="sales")
        df=sql.read_sql('select ORD_DATE,ORD_AMOUNT,ADVANCE_AMOUNT FROM orders ORDER BY ORD_DATE ASC',con)
        df.to_excel('D:\\Python Internship\\Order Received.xlsx',index=False)
        df1=pd.read_excel('D:\\Python Internship\\Order Received.xlsx',index=False)
        print(df.head())
        x=df1[['ORD_DATE']]
        y=df1[['ORD_AMOUNT']]
        z=df1[['ADVANCE_AMOUNT']]
        plt.plot(x,y,'ro-',color="#0066ff")
        #plt.legend(loc='upper left')
        plt.plot(x,z,'ro-')
        #plt.legend(loc='upper right')
        plt.xticks(rotation=90,fontsize=10)
        plt.yticks(fontsize=10)
        #plt.text('Order received for order amount',xy=(1,2),xytext=(2, 2),textcoords='offset points', arrowprops=dict(arrowstyle='-|>'))
        #plt.fill(x, y, "b", x, z, "r") 
        #plt.legend()
        #plt.subplots(figsize =(10, 10))
        plt.xlabel("Year",fontsize=15)
        plt.ylabel("Money",fontsize=15)
        plt.title("Time Series",fontsize=30)
        plt.show()
        #plt.legend(loc='center')
        
       
    sl=Button(root,text="Graph for Sold Vs Leased",bg="yellow",fg="black",command=graph1).place(x=10,y=20)   
    ml=Button(root,text="Graph for Max leased Area in CA & WS",bg="yellow",fg="black",command=graph2).place(x=10,y=60)    
    do=Button(root,text="Graph for owned property with reference to agent id",bg="yellow",fg="black",command=graph3).place(x=10,y=100)   
    cmd=Button(root,text="Chilliwack max. deals for lease",bg="yellow",fg="black",command=graph4).place(x=10,y=140) 
    bp=Button(root,text="Best Performer",bg="yellow",fg="black",command=graph5).place(x=10,y=180)    
    area=Button(root,text="Area sold for July month",bg="yellow",fg="black",command=graph6).place(x=10,y=220)     
    tsa=Button(root,text="Time series Analysis",bg="yellow",fg="black",command=graph7).place(x=10,y=260)      
    root.mainloop()
def confirm_new_password():
    global password1_verify,password2_verify
    password1_verify=StringVar()
    password2_verify=StringVar()
    q1=password1_verify
    #and len(password1_verify.get())>=8 and len(password2_verify.get())>=8
    if password1_verify.get() == password2_verify.get():
        messagebox.showinfo("Changing password","Password matched",parent=screen8)
        mydb = mysql.connector.connect(host="localhost",user="root",password="",database="sales")
        mycursor=mydb.cursor()
        sql="UPDATE agent_details, set password='qwertyui' where password='1234' or password='12345678'"
        mycursor.execute(sql)
        mydb.commit()
        
    else:
        messagebox.showerror("Bust","Password mismatch or length must be greater or equal to 8",parent=screen8)
def validate_forgot_password():
    #email = StringVar()
    global password1_verify,password2_verify
    password1_verify=StringVar()
    password2_verify=StringVar()
    email2.get()
    if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email2.get()):
        mydb = mysql.connector.connect(host="localhost",user="root",password="",database="sales")
        cursor = mydb.cursor()
        q1=email2.get()
        query="SELECT * FROM agent_details WHERE email LIKE '%"+q1+"%'"
        cursor.execute(query)
        already_reg=cursor.fetchall()
        if already_reg:
            messagebox.showinfo("Verification","Email Verified!",parent=screen8)
            Label(screen8, text="New Password * ", font=("Open Sans", 10, 'bold'), bg='light blue', fg='#174873').pack()
            Label(text="", bg='light blue').pack()
            Entry(screen8, textvar=password1_verify, show="*").pack()
            Label(screen8, text="Confirm New Password * ", font=("Open Sans", 10, 'bold'), bg='light blue', fg='#174873').pack()
            Label(text="", bg='light blue').pack()
            Entry(screen8, textvar=password2_verify, show="*").pack()
            Label(text="", bg='light blue').pack()
            Button(screen8, text="Change", bg="green", width=10, height=1,font=("Open Sans", 10, 'bold'), fg='white',command=confirm_new_password).pack()
            
        else:
            messagebox.showerror("Bust!","Email not registered!",parent=screen8)
    else:        
        messagebox.showerror("Bust!","invalid email id",parent=screen8)

        
        
        
        
def forgot_password():
    global screen8,email2
    email2 = StringVar()
    screen8=Toplevel(screen)
    screen8.title("Forgot Password")
    adjustWindow(screen8)
    screen8.configure(bg='light blue')
    Label(screen8, text="FORGOT PASSWORD", width="500", height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#545454').pack()
    Label(text="", bg='light blue').pack()
    Label(screen8, text="Please enter email ID as username for resetting password",bg='light blue',fg='red').pack()
    Label(text="", bg='light blue').pack()
    Label(screen8, text="Username", font=("Open Sans", 10, 'bold'), bg='light blue', fg='#174873').pack()
    Label(text="", bg='light blue').pack()
    Entry(screen8, textvar=email2).pack()
    Label(text="", bg='light blue').pack()
    Button(screen8, text="OK", bg="red", width=10, height=1,font=("Open Sans", 10, 'bold'), fg='white',command=validate_forgot_password).pack()
    Button(screen8,text="BACK TO LOGIN PAGE",bg='red',fg='white',width=35, height=1,font=("Open Sans", 10, 'bold'),command=i_quit2).place(x=370,y=500)
def main_screen():
    global screen, username_verify, password_verify
    screen = Tk()  # initializing the tkinter window
    username_verify = StringVar()
    password_verify = StringVar()
    adjustWindow(screen) 
    screen.title("Sunville properties")  # mentioning title of the window   # configuring the window
    screen.configure(bg='light blue')
    Label(screen, text="WELCOME TO SUNVILLE", width="500", height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#545454').pack()
    Label(text="", bg='light blue').pack() # for leaving a space in between
    Label(screen, text="Please enter details below to login",bg='light blue',fg='red').pack()
    Label(text="", bg='light blue').pack()
    Label(screen, text="Username", font=("Open Sans", 10, 'bold'), bg='light blue', fg='#174873').pack()
    Label(text="", bg='light blue').pack()
    e1=Entry(screen, textvar=username_verify).pack()
    Label(text="", bg='light blue').pack()
    Label(screen, text="Password * ", font=("Open Sans", 10, 'bold'), bg='light blue', fg='#174873').pack()
    Label(text="", bg='light blue').pack()
    Entry(screen, textvar=password_verify, show="*").pack()
    Label(text="", bg='light blue').pack()
    Button(screen, text="LOGIN", bg="red", width=10, height=1,font=("Open Sans", 10, 'bold'), fg='white',command=login_verify).pack()
    Label(text="", bg='light blue').pack()
    Label(text="-------------------------OR-------------------------", bg='light blue',fg='#174873').pack()
    Label(text="", bg='light blue').pack()
    Button(screen, text="Sign Up Here", height="1", width="20", bg='green', font=("Open Sans", 13, 'bold'), fg='white',command=register).pack()
    Label(text="", bg='light blue').pack()
    Button(screen, text="Forgot Password?", height="1", width="20", bg='blue', font=("Open Sans", 13, 'bold'), fg='white',command=forgot_password).pack()
    Label(text="", bg='light blue').pack()
    Button(screen, text="EXIT", height="1", width="20", bg='red', font=("Open Sans", 13, 'bold'), fg='white',command=i_quit).pack()
    screen.mainloop()
    
main_screen() 
