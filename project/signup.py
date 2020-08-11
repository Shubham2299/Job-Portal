from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as mb
from importlib import reload
import session
root=Tk()
root.geometry('600x650+100+100')
photo1=PhotoImage(file='pictures/2.png')
back=Label(root,image=photo1)
back.pack(fill='both',expand='yes')

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
con=MySQLdb.connect('localhost','root','root','project')
cursor=con.cursor()
def call(event):
    uid=session.getUid()
    a=e3.get()
    b=e4.get()
    z=e5.get()
    c=e6.get()
    try:
        if b==z:
            cursor.execute('update student set email="%s",password="%s",contact="%s" where uid="%s"'%(a,b,c,uid  ))
            con.commit()
            b=mb.showinfo('information','Record Inserted')
        else:
            b=mb.showerror('Error','password does not match')
    except Exception as e:
        con.rollback()
        print('exception',e)
    con.close()
    root.destroy()
    import login_panel
    reload(login_panel)
photo2=PhotoImage(file='pictures/4.png')
l1=Label(back,image=photo2)
l1.grid(row=0,column=0,pady=10)

l2=Label(back,text='Sign Up',font='times 22 bold')
l2.grid(row=1,column=1,pady=20)

l3=Label(back,text='Email ID',font='times 16')
l3.grid(row=2,column=0,pady=20)
e3=Entry(back,width=35,font='times 14',justify="center")
e3.grid(row=2,column=1,ipady=10)

l4=Label(back,text='Password',font='times 16')
l4.grid(row=3,column=0,pady=20)
e4=Entry(back,width=35,font='times 14',justify="center",show='*')
e4.grid(row=3,column=1,ipady=10)

l5=Label(back,text='Confirm Password',font='times 16')
l5.grid(row=4,column=0,pady=20)
e5=Entry(back,width=35,font='times 14',justify="center",show='*')
e5.grid(row=4,column=1,ipady=10)

l4=Label(back,text='Mobile Number',font='times 16')
l4.grid(row=5,column=0,pady=20)
frame=Frame(back)
frame.grid(row=5,column=1,columnspan=1)
a0=['+91','+61','+1','+234']
cbb=ttk.Combobox(frame,values=a0,width=5)
cbb.grid(row=0,column=0,ipady=9)
l6=Label(frame,text=' ')
l6.grid(row=0,column=1)
e6=Entry(frame,width=35,font='times 14',justify="center")
e6.grid(row=0,column=2,ipady=10)

bt1=Button(back,text='Sign In',width=10,bd=5,font='times 14')
bt1.config(command=lambda bt=bt1:call(bt))
bt1.grid(row=6,column=1,pady=20)
