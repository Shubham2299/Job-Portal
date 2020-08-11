from tkinter import *
import tkinter.messagebox as mb
from importlib import reload
import session
root=Tk()
root.geometry('650x600')
photo1=PhotoImage(file='pictures/6.png')
back=Label(root,image=photo1)
back.pack(fill='both',expand='yes')
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

def submit():
    con=MySQLdb.connect('localhost','root','root','project')
    cursor=con.cursor()
    a=e1.get()
    b=e2.get()
    c=e3.get()
    try:
        uid=session.getUid()
        cursor.execute('select password from student where uid="%s"'%(uid))
        t=cursor.fetchone()
        if a==b:
            b=mb.showerror('Error','New passwrd cannot be same as current password')
        else:
            if b==c:
                cursor.execute('update student set password="%s" where uid="%s"'%(c,uid))
                con.commit()
                b=mb.showinfo('information','Password Updated')
                root.destroy()
                import student_home
                reload(student_home)
            else:
                b=mb.showerror('Error','Password doesnt match')
    except Exception as e:
        con.rollback()
        print('exception',e)
    con.close()
    
photo2=PhotoImage(file='pictures/4.png')
l0=Label(back,image=photo2)
l0.grid(row=0,column=0,pady=10,padx=5)

l1=Label(back,text='Current Password',font='times 16 bold')
l1.grid(row=1,column=0,pady=20)
e1=Entry(back,width=30,justify='center',font='times 16')
e1.grid(row=1,column=1,ipady=10)

l2=Label(back,text='New Password',font='times 16 bold')
l2.grid(row=2,column=0,pady=20)
e2=Entry(back,width=30,justify='center',font='times 16',show='*')
e2.grid(row=2,column=1,ipady=10)

l3=Label(back,text='Confirm New\nPassword',font='times 16 bold')
l3.grid(row=3,column=0,pady=20)
e3=Entry(back,width=30,justify='center',font='times 16',show='*')
e3.grid(row=3,column=1,ipady=10)

bt1=Button(back,text='Submit',bd=5,width=10,font='times 14',command=submit)
bt1.grid(row=4,column=1,pady=20)
