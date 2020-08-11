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
    z=txt2.get('1.0','end')
    e=d.get()
    hr=cbb1.get()
    mn=cbb2.get()
    ap=n5.get()
    time=''
    time=hr+":"+mn+" "+ap
    f=e8.get()
    g=e9.get()
    dur=[]
    if n1.get()==1:
        dur.append(cb1['text'])    
    if n2.get()==1:
        dur.append(cb2['text'])
    duration=','.join(dur)
    h=n3.get()
    i=ex.get()
    j=e5.get()
    k=int(ey.get())
    m=int(ez.get())
    try:
        cursor.execute('insert into internship(name,web,profile,selection,reporting_date,reporting_time,branch,batch,duration,type,field,stipend,no_of_applicants,vacancies) values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%d","%d")'%(a,b,c,z,e,time,f,g,duration,h,i,j,k,m))
        con.commit()
        b=mb.showinfo('information','record inserted into database')
        
    except Exception as e:
        con.rollback()
        print('exception',e)
    con.close()


photo2=PhotoImage(file='pictures/4.png')
l1=Label(back,image=photo2)
l1.grid(row=0,column=0,pady=15)

l2=Label(back,text='INTERNSHIP INFORMATION FORM',font='times 16 bold')
l2.grid(row=0,column=2,pady=15)

l3=Label(back,text='Company Name',font='times 14 bold')
l3.grid(row=1,column=0,pady=15)
e3=Entry(back,width=40,justify='center',font='times 14')
e3.grid(row=1,column=1,ipady=10)

l4=Label(back,text='Official\nWebsite',font='times 14 bold')
l4.grid(row=1,column=3,pady=15)
e4=Entry(back,width=50,justify='center',font='times 12')
e4.grid(row=1,column=4,ipady=10)

l5=Label(back,text='Profile',font='times 14 bold')
l5.grid(row=2,column=0,pady=18)
txt1=Text(back,width=50,height=10)
txt1.grid(row=2,column=1)

lq=Label(back,text='Reporting Date',font='times 14 bold')
lq.grid(row=3,column=0,pady=15)
frame3=Frame(back)
frame3.grid(row=3,column=1)
dd=Label(frame3,text='Choose Date',font='times 10 bold')
dd.grid(row=0,column=0)
space=Label(frame3,text=' ')
space.grid(row=0,column=1)
d=cal.DateEntry(frame3,width=10)
d.grid(row=0,column=2,ipady=5)

l11=Label(back,text='Reporting Time',font='times 14 bold')
l11.grid(row=3,column=3,pady=15)
frame2=Frame(back)
frame2.grid(row=3,column=4,columnspan=5)
h=['00','01','02','03','04','05','06','07','08','09']
for i in range(10,13):
    h.append(i)
cbb1=ttk.Combobox(frame2,value=h,width=5)
cbb1.grid(row=0,column=0)
a=Label(frame2,text=':',font='times 12 bold')
a.grid(row=0,column=1)
m=['00','01','02','03','04','05','06','07','08','09']
for i in range(10,61):
    m.append(i)
cbb2=ttk.Combobox(frame2,value=m,width=5)
cbb2.grid(row=0,column=2)
n5=StringVar()
rb1=Radiobutton(frame2,text='AM',font='times 10 bold',variable=n5,value='am')
rb1.grid(row=0,column=3)
rb2=Radiobutton(frame2,text='PM',font='times 10 bold',variable=n5,value='pm')
rb2.grid(row=0,column=4)



l7=Label(back,text='Selection Procedure',font='times 14 bold')
l7.grid(row=2,column=3,pady=15)
txt2=Text(back,width=50,height=10)
txt2.grid(row=2,column=4)

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
n1=IntVar()
cb1=Checkbutton(frame2,text='6 Months',font='times 12',variable=n1)
cb1.grid(row=0,column=0)
n2=IntVar()
cb2=Checkbutton(frame2,text='6 Weeks',font='times 12',variable=n2)
cb2.grid(row=0,column=1)


l5=Label(back,text='Stipend (Rs.)',font='times 16 bold')
l5.grid(row=6,column=3,pady=20)
e5=Entry(back,width=40,justify='center',font='times 14')
e5.grid(row=6,column=4,ipady=10)

l10=Label(back,text='Internship Type',font='times 14 bold')
l10.grid(row=5,column=3,pady=15)
frame4=Frame(back)
frame4.grid(row=5,column=4)
n3=StringVar()
rb1=Radiobutton(frame4,text='Paid',font='times 12',variable=n3,value='paid')
rb1.grid(row=0,column=0)
rb2=Radiobutton(frame4,text='Unpaid',font='times 12',variable=n3,value='unpaid')
rb2.grid(row=0,column=1)

lx=Label(back,text='Field',font='times 14 bold')
lx.grid(row=6,column=0,pady=15)
ex=Entry(back,width=40,justify='center',font='times 14')
ex.grid(row=6,column=1,ipady=10)

ly=Label(back,text='Number of Applicants',font='times 14 bold')
ly.grid(row=7,column=0,pady=15)
ey=Entry(back,width=40,justify='center',font='times 14')
ey.grid(row=7,column=1,ipady=10)

lz=Label(back,text='Number of Vacancies',font='times 14 bold')
lz.grid(row=7,column=3,pady=15)
ez=Entry(back,width=40,justify='center',font='times 14')
ez.grid(row=7,column=4,ipady=10)

bt1=Button(back,text='SUBMIT',font='times 12 bold',width=10,bd=5)
bt1.config(command=lambda bt=bt1:call(bt))
bt1.grid(row=8,column=2)




