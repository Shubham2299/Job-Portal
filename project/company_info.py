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
    b=e14.get()
    c=int(e4.get())
    z=int(e5.get())
    e=int(e6.get())
    f=e7.get()
    h=e15.get()
    i=e9.get()
    j=e16.get()
    k=d.get()
    hr=cbb1.get()
    mn=cbb2.get()
    ap=n5.get()
    time=''
    time=hr+":"+mn+" "+ap
    m=txt1.get('1.0','end')
    n=txt2.get('1.0','end')
    o=e10.get()
    p=txt7.get('1.0','end')
    b_from=bfrom.get()
    b_to=bto.get()
    try:
        cursor.execute('insert into company(name,web,eligible_10,eligible_12,eligible_grad,eligible_branch,designation,field,vacancy,reporting_date,reporting_time,selection,profile,package,locations,batch_from,batch_to) values("%s","%s","%d","%d","%d","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%d","%d")'%(a,b,c,z,e,f,h,i,j,k,time,m,n,o,p,b_from,b_to))
        con.commit()
        b=mb.showinfo('information','record inserted into database')
        
    except Exception as e:
        con.rollback()
        print('exception',e)
    con.close()


photo2=PhotoImage(file='pictures/4.png')
l1=Label(back,image=photo2)
l1.grid(row=0,column=0,pady=15)

l2=Label(back,text='COMPANY INFO FORM',font='times 16 bold')
l2.grid(row=0,column=2,pady=15)

l3=Label(back,text='Company Name',font='times 14 bold')
l3.grid(row=1,column=0,pady=15)
e3=Entry(back,width=40,justify='center',font='times 14')
e3.grid(row=1,column=1,ipady=10)

l3=Label(back,text='Eligibility Criteria',font='times 14 bold')
l3.grid(row=2,column=0,pady=15)
frame1=Frame(back)
frame1.grid(row=2,column=1)
l4=Label(frame1,text='10th %',font='times 12 bold')
l4.grid(row=0,column=1,pady=5)
e4=Entry(frame1,width=10,justify='center',font='times 12')
e4.grid(row=0,column=2)
l5=Label(frame1,text='12th %',font='times 12 bold')
l5.grid(row=0,column=3,pady=5)
e5=Entry(frame1,width=10,justify='center',font='times 12')
e5.grid(row=0,column=4)
l6=Label(frame1,text='Graduation',font='times 12 bold')
l6.grid(row=0,column=5,pady=5)
e6=Entry(frame1,width=10,justify='center',font='times 12')
e6.grid(row=0,column=6)
l7=Label(frame1,text='Branch',font='times 12 bold')
l7.grid(row=1,column=1,pady=5)
e7=Entry(frame1,width=10,justify='center',font='times 12')
e7.grid(row=1,column=2)
l8=Label(frame1,text='Batch',font='times 12 bold')
l8.grid(row=1,column=3,pady=5)
bfrom=Entry(frame1,width=8,justify='center',font='times 12')
bfrom.grid(row=1,column=4)
lz=Label(frame1,text='-',font='times 14')
lz.grid(row=1,column=5)
bto=Entry(frame1,width=8,justify='center',font='times 12')
bto.grid(row=1,column=6)


l9=Label(back,text='Field',font='times 14 bold')
l9.grid(row=3,column=0,pady=15)
e9=Entry(back,width=40,justify='center',font='times 14')
e9.grid(row=3,column=1,ipady=10)

l10=Label(back,text='Package Offered (Rs.)',font='times 14 bold')
l10.grid(row=6,column=0,pady=15)
e10=Entry(back,width=40,justify='center',font='times 14')
e10.grid(row=6,column=1,ipady=10)

l10=Label(back,text='Reporting Date',font='times 14 bold')
l10.grid(row=4,column=0,pady=15)
frame3=Frame(back)
frame3.grid(row=4,column=1)
dd=Label(frame3,text='Choose Date',font='times 10 bold')
dd.grid(row=0,column=0)
space=Label(frame3,text=' ')
space.grid(row=0,column=1)
d=cal.DateEntry(frame3,width=10)
d.grid(row=0,column=2)



l11=Label(back,text='Reporting Time',font='times 14 bold')
l11.grid(row=4,column=3,pady=15)
frame2=Frame(back)
frame2.grid(row=4,column=4,columnspan=5)
h=['00','01','02','03','04','05','06','07','08','09']
for i in range(10,13):
    h.append(i)
cbb1=ttk.Combobox(frame2,value=h,width=5,justify='center')
cbb1.grid(row=0,column=0)
a=Label(frame2,text=':',font='times 12 bold')
a.grid(row=0,column=1)
m=['00','01','02','03','04','05','06','07','08','09']
for i in range(10,61):
    m.append(i)
cbb2=ttk.Combobox(frame2,value=m,width=5,justify='center')
cbb2.grid(row=0,column=2)
n5=StringVar()
rb1=Radiobutton(frame2,text='AM',font='times 10 bold',variable=n5,value='am')
rb1.grid(row=0,column=3)
rb2=Radiobutton(frame2,text='PM',font='times 10 bold',variable=n5,value='pm')
rb2.grid(row=0,column=4)


l12=Label(back,text='Selection Procedure',font='times 14 bold')
l12.grid(row=5,column=0,pady=15)
txt1=Text(back,width=45,height=10)
txt1.grid(row=5,column=1)

l19=Label(back,text='Job\nLocations',font='times 14 bold')
l19.grid(row=6,column=3,pady=15)
txt7=Text(back,width=50,height=5)
txt7.grid(row=6,column=4,pady=15)

l13=Label(back,text='Profile',font='times 14 bold')
l13.grid(row=5,column=3,pady=15)
txt2=Text(back,width=50,height=10)
txt2.grid(row=5,column=4)

l14=Label(back,text='Official\nWebsite',font='times 14 bold')
l14.grid(row=1,column=3,pady=15)
e14=Entry(back,width=50,justify='center',font='times 12')
e14.grid(row=1,column=4,ipady=10)

l15=Label(back,text='Designation',font='times 14 bold')
l15.grid(row=2,column=3,pady=15)
e15=Entry(back,width=40,justify='center',font='times 14')
e15.grid(row=2,column=4,ipady=10)

l16=Label(back,text='Number of\nVacancies',font='times 14 bold')
l16.grid(row=3,column=3,pady=15)
e16=Entry(back,width=40,justify='center',font='times 14')
e16.grid(row=3,column=4,ipady=10)

bt1=Button(back,text='Submit',width=10,bd=5,font='times 14 bold')
bt1.config(command=lambda bt=bt1:call(bt))
bt1.grid(row=7,column=2)

root.mainloop()
    



