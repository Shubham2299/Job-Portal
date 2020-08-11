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
photo1=PhotoImage(file='pictures/2.png')
back=Label(root,image=photo1)
back.pack(fill='both',expand='yes')


photo2=PhotoImage(file='pictures/4.png')
l1=Label(back,image=photo2)
l1.grid(row=0,column=0,pady=20)
def call(event):
    a=e3.get()
    b=e4.get()
    c=e5.get()
    d=cbb0.get()
    e=int(cbb.get())
    f=int(cbb1.get())
    g=float(e7.get())
    h=float(e8.get())
    i=float(e9.get())
    j=txt.get('1.0','end')
    k=txt1.get('1.0','end')
    try:
        cursor.execute('insert into student(uid,name,branch,course,batch_from,batch_to,percentage_10,percentage_12,percentage_grad,interest,preference) values("%s","%s","%s","%s","%d","%d","%f","%f","%f","%s","%s")'%(a,b,c,d,e,f,g,h,i,j,k))
        con.commit()
    except Exception as e:
        con.rollback()
        print('exception',e)
    con.close()
    session.setUid(a)
    root.destroy()
    import signup

l2=Label(back,text='STUDENT REGISTRATION FORM',font='times 17 bold')
l2.grid(row=1,column=2,pady=20)

l3=Label(back,text='University ID',font='times 16 bold')
l3.grid(row=2,column=0,pady=20)
e3=Entry(back,width=35,font='times 14',justify="center")
e3.grid(row=2,column=1,ipady=8)

l4=Label(back,text='Student Name',font='times 16 bold')
l4.grid(row=2,column=3,pady=20)
e4=Entry(back,width=35,font='times 14',justify="center")
e4.grid(row=2,column=4,ipady=10)

l5=Label(back,text='Branch',font='times 16 bold')
l5.grid(row=3,column=0,pady=20)
e5=Entry(back,width=35,font='times 14',justify="center")
e5.grid(row=3,column=1,ipady=10)

l6=Label(back,text='Course',font='times 16 bold')
l6.grid(row=3,column=3,pady=20)
a0=['Bachelors of Computer Science Technology(BTech)','Bachelors of Computer Application(BCA)','Masters of Computer Science Technology(MTech)']
cbb0=ttk.Combobox(back,values=a0,width=50)
cbb0.grid(row=3,column=4,ipady=10)

l7=Label(back,text='Batch',font='times 16 bold')
l7.grid(row=4,column=0,pady=20)
frame=Frame(back)
frame.grid(row=4,column=1)
l8=Label(frame,text='From',font='times 14 bold')
l8.grid(row=0,column=1)
a1=[]
for i in range(2000,datetime.datetime.now().year+1):
    a1.append(i)
cbb=ttk.Combobox(frame,values=a1)
cbb.grid(row=0,column=2)

l9=Label(frame,text='To',font='times 14 bold')
l9.grid(row=0,column=3)
a2=[]
for i in range(2002,datetime.datetime.now().year+5):
    a2.append(i)
cbb1=ttk.Combobox(frame,values=a2)
cbb1.grid(row=0,column=4)



l10=Label(back,text='Percentage',font='times 16 bold')
l10.grid(row=4,column=3,pady=20)
frame1=Frame(back)
frame1.grid(row=4,column=4)
l11=Label(frame1,text='10th',font='times 14 bold')
l11.grid(row=0,column=1,pady=10)
e7=Entry(frame1,width=10,font='times 10',justify="center")
e7.grid(row=0,column=2)
l12=Label(frame1,text='12th',font='times 14 bold')
l12.grid(row=0,column=3,pady=10)
e8=Entry(frame1,width=10,font='times 10',justify="center")
e8.grid(row=0,column=4)
l13=Label(frame1,text='Graduation',font='times 14 bold')
l13.grid(row=0,column=5,pady=10)
e9=Entry(frame1,width=10,font='times 10',justify="center")
e9.grid(row=0,column=6)


l14=Label(back,text='Area of Interest',font='times 16 bold')
l14.grid(row=5,column=0,pady=20)
txt=Text(back,width=50,height=10)
txt.grid(row=5,column=1)

l14=Label(back,text='Preferred Comapanies',font='times 16 bold')
l14.grid(row=5,column=3,pady=20)
txt1=Text(back,width=45,height=10)
txt1.grid(row=5,column=4)

photo3=PhotoImage(file='pictures/5.png')
bt1=Button(back,width=80,text='Next',image=photo3,bd=5,font='times 14 bold')
bt1.config(command=lambda bt=bt1:call(bt))
bt1.grid(row=7,column=2,pady=50)



    
