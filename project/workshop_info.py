from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as mb
import tkcalendar as cal
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
def call(event):
    a=e3.get()
    b=e4.get()
    c=txt1.get('1.0','end')
    e=d.get()
    hr=cbb1.get()
    mn=cbb2.get()
    ap=n5.get()
    time=''
    time=hr+":"+mn+" "+ap
    f=e8.get()
    g=e9.get()
    y=e10.get()
    x=cbb8.get()
    duration=''
    duration=y+" "+x
    h=ea.get()
    i=n3.get()
    j=eb.get()
    k=int(ec.get())
    try:
        cursor.execute('insert into workshop(name,web,profile,reporting_date,reporting_time,branch,batch,duration,topic,certificate,fee,no_of_students) values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%d")'%(a,b,c,e,time,f,g,duration,h,i,j,k))
        con.commit()
        b=mb.showinfo('information','record inserted into database')
        
    except Exception as e:
        con.rollback()
        print('exception',e)
    con.close()

photo2=PhotoImage(file='pictures/4.png')
l1=Label(back,image=photo2)
l1.grid(row=0,column=0,pady=15)

l2=Label(back,text='WORKSHOP INFORMATION FORM',font='times 16 bold')
l2.grid(row=0,column=2,pady=15)

l3=Label(back,text='Company Name',font='times 14 bold')
l3.grid(row=1,column=0,pady=15)
e3=Entry(back,width=40,justify='center',font='times 14')
e3.grid(row=1,column=1,ipady=10)

l4=Label(back,text='Official\nWebsite',font='times 14 bold')
l4.grid(row=1,column=3,pady=15)
e4=Entry(back,width=50,justify='center',font='times 14')
e4.grid(row=1,column=4,ipady=10)

l5=Label(back,text='Profile',font='times 14 bold')
l5.grid(row=6,column=0,pady=18)
txt1=Text(back,width=50,height=10)
txt1.grid(row=6,column=1)

l10=Label(back,text='Reporting Date',font='times 14 bold')
l10.grid(row=3,column=0,pady=15)
frame3=Frame(back)
frame3.grid(row=3,column=1)
dd=Label(frame3,text='Choose Date',font='times 10 bold')
dd.grid(row=0,column=0)
bb=Label(frame3,text=' ',font='times 12 bold')
bb.grid(row=0,column=1)
d=cal.DateEntry(frame3,width=10)
d.grid(row=0,column=2,ipady=5)


lq=Label(back,text='Reporting Time',font='times 14 bold')
lq.grid(row=3,column=3,pady=15)
frame8=Frame(back)
frame8.grid(row=3,column=4,columnspan=5)
h=['00','01','02','03','04','05','06','07','08','09']
for i in range(10,13):
    h.append(i)
cbb1=ttk.Combobox(frame8,value=h,width=5)
cbb1.grid(row=0,column=0)
a=Label(frame8,text=':',font='times 12 bold')
a.grid(row=0,column=1)
m=['00','01','02','03','04','05','06','07','08','09']
for i in range(10,61):
    m.append(i)
cbb2=ttk.Combobox(frame8,value=m,width=5)
cbb2.grid(row=0,column=2)
n5=StringVar()
rb1=Radiobutton(frame8,text='AM',font='times 10 bold',variable=n5,value='am')
rb1.grid(row=0,column=3)
rb2=Radiobutton(frame8,text='PM',font='times 10 bold',variable=n5,value='pm')
rb2.grid(row=0,column=4)

l8=Label(back,text='Branch',font='times 16 bold')
l8.grid(row=4,column=0,pady=20)
e8=Entry(back,width=40,justify='center',font='times 14')
e8.grid(row=4,column=1,ipady=10)

l9=Label(back,text='Batch',font='times 16 bold')
l9.grid(row=4,column=3,pady=5)
e9=Entry(back,width=40,justify='center',font='times 14')
e9.grid(row=4,column=4,ipady=10)

l10=Label(back,text='Duration',font='times 16 bold')
l10.grid(row=5,column=0,pady=20)
frame2=Frame(back)
frame2.grid(row=5,column=1)
e10=Entry(frame2,width=10)
e10.grid(row=0,column=0)
aa=Label(frame2,text=' ',font='times 12 bold')
aa.grid(row=0,column=1)
h=['day(s)','hour(s)']
cbb8=ttk.Combobox(frame2,value=h,width=10)
cbb8.grid(row=0,column=2)

la=Label(back,text='Topic',font='times 16 bold')
la.grid(row=5,column=3,pady=20)
ea=Entry(back,width=40,justify='center',font='times 14')
ea.grid(row=5,column=4,ipady=10)

lb=Label(back,text='Certificate',font='times 16 bold')
lb.grid(row=6,column=3,pady=20)
frame4=Frame(back)
frame4.grid(row=6,column=4)
n3=StringVar()
rb1=Radiobutton(frame4,text='Yes',font='times 12',variable=n3,value='yes')
rb1.grid(row=0,column=0)
rb2=Radiobutton(frame4,text='No',font='times 12',variable=n3,value='no')
rb2.grid(row=0,column=1)

lb=Label(back,text='Fee (Rs.)',font='times 16 bold')
lb.grid(row=2,column=3,pady=20)
eb=Entry(back,width=40,justify='center',font='times 14')
eb.grid(row=2,column=4,ipady=10)

lc=Label(back,text='Number of Students',font='times 16 bold')
lc.grid(row=2,column=0,pady=20)
ec=Entry(back,width=40,justify='center',font='times 14')
ec.grid(row=2,column=1,ipady=10)

bt1=Button(back,text='SUBMIT',font='times 12 bold',width=10,bd=5)
bt1.config(command=lambda bt=bt1:call(bt))
bt1.grid(row=8,column=2)

