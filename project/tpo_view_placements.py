from tkinter import *
import tkinter.messagebox as mb
import tkcalendar as cal
import session
import os
from importlib import reload
root=Tk()
root.geometry('700x600')
photo1=PhotoImage(file='pictures/7.png')
back=Label(root,image=photo1)
back.pack(fill='both',expand='yes')
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
con=MySQLdb.connect('localhost','root','root','project')
cursor=con.cursor()
cursor.execute('select p.u_id,s.name,p.date,c.name,c.package from placed_info as p ,student as s,company as c where p.u_id=s.uid and p.cid=c.company_id')
t=cursor.fetchall()
def call():
    root.destroy()
    import tpo_home
    reload(tpo_home)
try:
    l1=Label(back,text='University ID',width=20,padx=10,pady=10,bd=5,bg='silver')
    l1.grid(row=0,column=0)
    l2=Label(back,text='Student Name',width=20,padx=10,pady=10,bd=5,bg='silver')
    l2.grid(row=0,column=1)
    l3=Label(back,text='Date of Placement',width=20,padx=10,pady=10,bd=5,bg='silver')
    l3.grid(row=0,column=2)
    la=Label(back,text='Company Name',width=20,padx=10,pady=10,bd=5,bg='silver')
    la.grid(row=0,column=3)
    lb=Label(back,text='Package Offered',width=20,padx=10,pady=10,bd=5,bg='silver')
    lb.grid(row=0,column=4)
   
    r=1
    
    for row in t:
        
        l4=Label(back,text=row[0],width=20,padx=10,pady=10,bd=5,bg='white')
        l4.grid(row=r,column=0)        
        l5=Label(back,text=row[1],width=20,padx=10,pady=10,bd=5,bg='white')
        l5.grid(row=r,column=1)
        l6=Label(back,text=row[2],width=20,padx=10,pady=10,bd=5,bg='white')
        l6.grid(row=r,column=2)
        l7=Label(back,text=row[3],width=20,padx=10,pady=10,bd=5,bg='white')
        l7.grid(row=r,column=3)
        l8=Label(back,text=row[4],width=20,padx=10,pady=10,bd=5,bg='white')
        l8.grid(row=r,column=4)
        r=r+1
except Exception as e:
    print(e)
    
con.close()
bt=Button(back,text='Back to Home',width=18,font='times 11',bd=5,command=call)
bt.grid(row=r,column=2)
