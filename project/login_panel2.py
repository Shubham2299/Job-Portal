from tkinter import *
import tkinter.messagebox as mb
import tkinter.ttk as ttk
import session
root=Tk()
root.geometry('500x525')
photo1=PhotoImage(file='pictures/6.png')
back=Label(root,image=photo1)
back.pack(fill='both',expand='yes')
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb


def call():
    con=MySQLdb.connect('localhost','root','root','project')
    cursor=con.cursor()
    a=e2.get()
    b=e3.get()
    c=cbb.get()
    session.setDeg(c)
    try:
        cursor.execute('select * from tpo_dean where username="%s" and password="%s" and designation="%s"'%(a,b,c))
        t=cursor.fetchone()
        if t!=None:
            if c=='TPO':
                root.destroy()
                import tpo_home
            else:
                root.destroy()
                import dean_home
        else:
            b=mb.showinfo('information','Invalid User')
        
    except Exception as e:
        print('exception',e)
    con.close()
    
photo2=PhotoImage(file='pictures/4.png')
l0=Label(back,image=photo2)
l0.grid(row=0,column=0,pady=10,padx=5)

l1=Label(back,text='WELCOME TO\nUNIVERSITY',font='times 16 bold',bg='white')
l1.grid(row=0,column=1,pady=20)


l2=Label(back,text='Username',font='times 16 bold',bg='white')
l2.grid(row=2,column=0,pady=20)
e2=Entry(back,width=30,justify='center',font='times 16')
e2.grid(row=2,column=1,ipady=10)

l3=Label(back,text='Password',font='times 16 bold',bg='white')
l3.grid(row=3,column=0,pady=20)
e3=Entry(back,width=30,justify='center',font='times 16',show='*')
e3.grid(row=3,column=1,ipady=10)

l3=Label(back,text='Designation',font='times 16 bold')
l3.grid(row=4,column=0,pady=20)
l=['TPO','Dean']
cbb=ttk.Combobox(back,values=l,width=25,font='times 16',justify='center')
cbb.grid(row=4,column=1,ipady=10)

bt1=Button(back,text='Login',bd=5,width=10,font='times 14',command=call)
bt1.grid(row=5,column=1,pady=20)
