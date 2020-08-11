from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as mb
from importlib import reload
import datetime
import session
root=Tk()
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
con=MySQLdb.connect('localhost','root','root','project')
cursor=con.cursor()
root.geometry('1200x1200+100+100')
photo1=PhotoImage(file='pictures/b.png')
back=Label(root,image=photo1)
back.pack(fill='both',expand='yes')
try:
    uid=session.getUid()
    cursor.execute('select * from student where uid="%s"'%(uid))
    r=cursor.fetchone()
    if r != None:
        l4=Label(back,text=r[0],width=20,font='times 16 bold',bg='black',fg='white')
        l4.grid(row=2,column=1)
        l5=Label(back,text=r[1],width=20,font='times 16 bold',bg='black',fg='white')
        l5.grid(row=2,column=4)
        l6=Label(back,text=r[2],width=20,font='times 16 bold',bg='black',fg='white')
        l6.grid(row=3,column=1)
        l7=Label(back,text=r[3],width=50,font='times 11 bold',bg='black',fg='white')
        l7.grid(row=3,column=4)
        frame=Frame(back,bg='black')
        frame.grid(row=4,column=1)
        l8=Label(frame,text=r[4],width=10,font='times 12 bold',bg='black',fg='white')
        l8.grid(row=0,column=2)
        l9=Label(frame,text=r[5],width=10,font='times 12 bold',bg='black',fg='white')
        l9.grid(row=0,column=4)
        frame1=Frame(back,bg='black')
        frame1.grid(row=4,column=4)
        la=Label(frame1,text=r[6],width=5,font='times 12 bold',bg='black',fg='white')
        la.grid(row=0,column=2)
        lb=Label(frame1,text=r[7],width=5,font='times 12 bold',bg='black',fg='white')
        lb.grid(row=0,column=4)
        lc=Label(frame1,text=r[8],width=5,font='times 12 bold',bg='black',fg='white')
        lc.grid(row=0,column=6)
        ld=Label(back,text=r[9],width=40,height=5,font='times 14 bold',bg='black',fg='white')
        ld.grid(row=5,column=1)
        le=Label(back,text=r[10],width=40,height=5,font='times 14 bold',bg='black',fg='white')
        le.grid(row=5,column=4)
        lf=Label(back,text=r[11],width=20,font='times 15 bold',bg='black',fg='white')
        lf.grid(row=6,column=1)
        lg=Label(back,text=r[13],width=20,font='times 16 bold',bg='black',fg='white')
        lg.grid(row=6,column=4)
except Exception as e:
    print('exception',e)
    con.close()    

def end():
    root.destroy()
    import student_home
    reload(student_home)
photo2=PhotoImage(file='pictures/4.png')
l1=Label(back,image=photo2)
l1.grid(row=0,column=0,pady=20)

l2=Label(back,text='STUDENT PROFILE',font='times 20 bold',bg='black',fg='white')
l2.grid(row=1,column=2,pady=20)

l3=Label(back,text='University ID',font='times 16 bold',bg='black',fg='white')
l3.grid(row=2,column=0,pady=20)

l4=Label(back,text='Student Name',font='times 16 bold',bg='black',fg='white')
l4.grid(row=2,column=3,pady=20)

l5=Label(back,text='Branch',font='times 16 bold',bg='black',fg='white')
l5.grid(row=3,column=0,pady=20)

l6=Label(back,text='Course',font='times 16 bold',bg='black',fg='white')
l6.grid(row=3,column=3,pady=20)

l7=Label(back,text='Batch',font='times 16 bold',bg='black',fg='white')
l7.grid(row=4,column=0,pady=20)

l8=Label(frame,text='From',font='times 14 bold',bg='black',fg='white')
l8.grid(row=0,column=1)


l9=Label(frame,text='To',font='times 14 bold',bg='black',fg='white')
l9.grid(row=0,column=3)

l10=Label(back,text='Percentage',font='times 16 bold',bg='black',fg='white')
l10.grid(row=4,column=3,pady=20)

l11=Label(frame1,text='10th',font='times 14 bold',bg='black',fg='white')
l11.grid(row=0,column=1,pady=10)

l12=Label(frame1,text='12th',font='times 14 bold',bg='black',fg='white')
l12.grid(row=0,column=3,pady=10)

l13=Label(frame1,text='Graduation',font='times 14 bold',bg='black',fg='white')
l13.grid(row=0,column=5,pady=10)

l14=Label(back,text='Area of Interest',font='times 16 bold',bg='black',fg='white')
l14.grid(row=5,column=0,pady=20)

l14=Label(back,text='Preferred Comapanies',font='times 16 bold',bg='black',fg='white')
l14.grid(row=5,column=3,pady=20)

l15=Label(back,text='Email ID',font='times 16 bold',bg='black',fg='white')
l15.grid(row=6,column=0,pady=20)

l16=Label(back,text='Contact',font='times 16 bold',bg='black',fg='white')
l16.grid(row=6,column=3,pady=20)

bt1=Button(back,text='Back to Home',bd=5,width=15,font='times 14',command=end)
bt1.grid(row=7,column=2,pady=20)





