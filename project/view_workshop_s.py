from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as mb
import tkcalendar as cal
from importlib import reload
import session
root=Tk()
root.geometry('1000x1000+100+100')
photo1=PhotoImage(file='pictures/7.png')
back=Label(root,image=photo1)
back.pack(fill='both',expand='yes')
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
con=MySQLdb.connect('localhost','root','root','project')
cursor=con.cursor()
try:
    cid=session.getCid()
    cursor.execute('select * from workshop where cid="%d"'%(cid))
    r=cursor.fetchone()
    if r != None:
        name=Label(back,text=r[0],width=20,font='times 16 bold',)
        name.grid(row=1,column=1)
        
        web=Label(back,text=r[1],width=20,font='times 14 bold')
        web.grid(row=1,column=4)

        txt2=Text(back,width=40,height=10,font='times 8 bold')
        txt2.grid(row=6,column=1)
        txt2.insert('1.0',r[2])
        txt2.config(state=DISABLED)
        
        frame3=Frame(back)
        frame3.grid(row=3,column=1)
        date=Label(frame3,text=r[3],width=10,font='times 14 bold')
        date.grid(row=0,column=0)

        frame8=Frame(back)
        frame8.grid(row=3,column=4,columnspan=5)
        tim=Label(frame8,text=r[4],width=10,font='times 14 bold')
        tim.grid(row=0,column=0)

        branch=Label(back,text=r[5],width=20,font='times 14 bold')
        branch.grid(row=4,column=1)

        batch=Label(back,text=r[6],width=20,font='times 14 bold')
        batch.grid(row=4,column=4)

        duration=Label(back,text=r[7],width=20,font='times 14 bold')
        duration.grid(row=5,column=1)

        topic=Label(back,text=r[8],width=20,font='times 14 bold')
        topic.grid(row=5,column=4)

        certificate=Label(back,text=r[9],width=20,font='times 14 bold')
        certificate.grid(row=6,column=4)

        fee=Label(back,text=r[10],width=20,font='times 14 bold')
        fee.grid(row=2,column=4)

        nos=Label(back,text=r[11],width=20,font='times 14 bold')
        nos.grid(row=2,column=1)

except Exception as e:
    print('exception',e)
    con.close()

def call():
    root.destroy()
    import student_view_workshops
    reload(student_view_workshops)
photo2=PhotoImage(file='pictures/4.png')
l1=Label(back,image=photo2)
l1.grid(row=0,column=0,pady=15)

l2=Label(back,text='WORKSHOP INFORMATION ',font='times 16 bold')
l2.grid(row=0,column=2,pady=15)

l3=Label(back,text='Company Name',font='times 14 bold')
l3.grid(row=1,column=0,pady=15)


l4=Label(back,text='Official\nWebsite',font='times 14 bold')
l4.grid(row=1,column=3,pady=15)

l5=Label(back,text='Profile',font='times 14 bold')
l5.grid(row=6,column=0,pady=18)


l10=Label(back,text='Reporting Date',font='times 14 bold')
l10.grid(row=3,column=0,pady=15)



lq=Label(back,text='Reporting Time',font='times 14 bold')
lq.grid(row=3,column=3,pady=15)

l8=Label(back,text='Branch',font='times 16 bold')
l8.grid(row=4,column=0,pady=20)


l9=Label(back,text='Batch',font='times 16 bold')
l9.grid(row=4,column=3,pady=5)

l10=Label(back,text='Duration',font='times 16 bold')
l10.grid(row=5,column=0,pady=20)


la=Label(back,text='Topic',font='times 16 bold')
la.grid(row=5,column=3,pady=20)


lb=Label(back,text='Certificate',font='times 16 bold')
lb.grid(row=6,column=3,pady=20)


lb=Label(back,text='Fee (Rs.)',font='times 16 bold')
lb.grid(row=2,column=3,pady=20)


lc=Label(back,text='Number of Students',font='times 16 bold')
lc.grid(row=2,column=0,pady=20)


photo9=PhotoImage(file='pictures/5b.png')
bt1=Button(back,image=photo9,width=80,bd=5,command=call)
bt1.grid(row=7,column=2)


