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
    uid=session.getUid()
    cursor.execute('select * from student where uid="%s"'%(uid))
    r=cursor.fetchone()
    if r != None:
        uid=Label(back,text=r[0],width=20,font='times 16 bold')
        uid.grid(row=2,column=1)

        sname=Label(back,text=r[1],width=20,font='times 16 bold')
        sname.grid(row=2,column=4)

        branch=Label(back,text=r[2],width=20,font='times 16 bold')
        branch.grid(row=3,column=1)

        course=Label(back,text=r[3],width=50,font='times 10 bold')
        course.grid(row=3,column=4)

        frame=Frame(back)
        frame.grid(row=4,column=1)
        l8=Label(frame,text='From',font='times 14 bold')
        l8.grid(row=0,column=1)
        l9=Label(frame,text='To',font='times 14 bold')
        l9.grid(row=0,column=3)
        bfrom=Label(frame,text=r[4],width=10,font='times 14 bold')
        bfrom.grid(row=0,column=2)
        bto=Label(frame,text=r[5],width=10,font='times 14 bold')
        bto.grid(row=0,column=4)

        frame1=Frame(back)
        frame1.grid(row=4,column=4)
        l11=Label(frame1,text='10th',font='times 14 bold')
        l11.grid(row=0,column=1,pady=10)
        l12=Label(frame1,text='12th',font='times 14 bold')
        l12.grid(row=0,column=3,pady=10)
        l13=Label(frame1,text='Graduation',font='times 14 bold')
        l13.grid(row=0,column=5,pady=10)
        p10=Label(frame1,text=r[6],width=10,font='times 14 bold')
        p10.grid(row=0,column=2)
        p12=Label(frame1,text=r[7],width=10,font='times 14 bold')
        p12.grid(row=0,column=4)
        pgrad=Label(frame1,text=r[8],width=10,font='times 14 bold')
        pgrad.grid(row=0,column=6)

        interest=Text(back,width=30,height=9,font='times 16 bold')
        interest.grid(row=5,column=1)
        interest.insert('1.0',r[9])
        interest.config(state=DISABLED)

        prefer=Text(back,width=30,height=9,font='times 16 bold')
        prefer.grid(row=5,column=4)
        prefer.insert('1.0',r[10])
        prefer.config(state=DISABLED)

        email=Label(back,text=r[11],width=20,font='times 16 bold')
        email.grid(row=6,column=1)

        cont=Label(back,text=r[13],width=20,font='times 16 bold')
        cont.grid(row=6,column=4)
        

        
except Exception as e:
    print('exception',e)
    con.close()

def call():
    root.destroy()
    import tpo_view_students
    reload(tpo_view_students)
photo2=PhotoImage(file='pictures/4.png')
l1=Label(back,image=photo2)
l1.grid(row=0,column=0,pady=15)

l2=Label(back,text='STUDENT INFORMATION',font='times 17 bold')
l2.grid(row=1,column=2,pady=20)

l3=Label(back,text='University ID',font='times 16 bold')
l3.grid(row=2,column=0,pady=20)


l4=Label(back,text='Student Name',font='times 16 bold')
l4.grid(row=2,column=3,pady=20)


l5=Label(back,text='Branch',font='times 16 bold')
l5.grid(row=3,column=0,pady=20)

l6=Label(back,text='Course',font='times 16 bold')
l6.grid(row=3,column=3,pady=20)


l7=Label(back,text='Batch',font='times 16 bold')
l7.grid(row=4,column=0,pady=20)

''''''



l10=Label(back,text='Percentage',font='times 16 bold')
l10.grid(row=4,column=3,pady=20)

''''''



l14=Label(back,text='Area of Interest',font='times 16 bold')
l14.grid(row=5,column=0,pady=20)


l14=Label(back,text='Preferred Comapanies',font='times 16 bold')
l14.grid(row=5,column=3,pady=20)

l14=Label(back,text='Email ID',font='times 16 bold')
l14.grid(row=6,column=0,pady=20)

l14=Label(back,text='Contact',font='times 16 bold')
l14.grid(row=6,column=3,pady=20)


photo9=PhotoImage(file='pictures/5b.png')
bt1=Button(back,image=photo9,width=80,bd=5,command=call)
bt1.grid(row=7,column=2)


    



