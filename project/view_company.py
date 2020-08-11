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
    cursor.execute('select * from company where company_id="%d"'%(cid))
    r=cursor.fetchone()
    if r != None:
        la=Label(back,text=r[0],width=20,font='times 16 bold',)
        la.grid(row=1,column=1)
        
        lb=Label(back,text=r[1],width=20,font='times 14 bold')
        lb.grid(row=1,column=4)
        
        frame1=Frame(back)
        frame1.grid(row=2,column=1)
        l4=Label(frame1,text='10th %',font='times 14 bold')
        l4.grid(row=0,column=1,pady=5)

        l5=Label(frame1,text='12th %',font='times 14 bold')
        l5.grid(row=0,column=3,pady=5)

        l6=Label(frame1,text='Graduation',font='times 14 bold')
        l6.grid(row=0,column=5,pady=5)

        l7=Label(frame1,text='Branch',font='times 14 bold')
        l7.grid(row=1,column=1,pady=5)
        lq=Label(frame1,text='-')
        lq.grid(row=1,column=5)
        l8=Label(frame1,text='Batch',font='times 14 bold')
        l8.grid(row=1,column=3,pady=5)
        lc=Label(frame1,text=r[2],width=5,font='times 10 bold')
        lc.grid(row=0,column=2)
        ld=Label(frame1,text=r[3],width=5,font='times 10 bold')
        ld.grid(row=0,column=4)
        le=Label(frame1,text=r[4],width=5,font='times 10 bold')
        le.grid(row=0,column=6)
        lf=Label(frame1,text=r[5],width=8,font='times 10 bold')
        lf.grid(row=1,column=2)
        lg=Label(frame1,text=r[16],width=8,font='times 10 bold')
        lg.grid(row=1,column=4)
        lg=Label(frame1,text=r[17],width=8,font='times 10 bold')
        lg.grid(row=1,column=6)
        
        lh=Label(back,text=r[6],width=20,font='times 16 bold')
        lh.grid(row=2,column=4)
        
        li=Label(back,text=r[7],width=20,font='times 16 bold')
        li.grid(row=3,column=1)
        
        lj=Label(back,text=r[8],width=20,font='times 16 bold')
        lj.grid(row=3,column=4)
        
        frame3=Frame(back)
        frame3.grid(row=4,column=1)
        lk=Label(frame3,text=r[9],width=10,font='times 14 bold')
        lk.grid(row=0,column=0)
        
        frame2=Frame(back)
        frame2.grid(row=4,column=4)
        ll=Label(frame2,text=r[10],width=10,font='times 14 bold')
        ll.grid(row=0,column=0)
        
        txt2=Text(back,width=35,height=8,font='times 12 bold')
        txt2.grid(row=5,column=1)
        txt2.insert('1.0',r[11])
        txt2.config(state=DISABLED)
        txt1=Text(back,width=40,height=10,font='times 8 bold')
        txt1.grid(row=5,column=4)
        txt1.insert('1.0',r[12])
        txt1.config(state=DISABLED)

        lo=Label(back,text=r[13],width=20,font='times 16 bold')
        lo.grid(row=6,column=1)
        
        lp=Label(back,text=r[14],width=20,font='times 16 bold')
        lp.grid(row=6,column=4)

except Exception as e:
    print('exception',e)
    con.close()

def call():
    root.destroy()
    import tpo_view_companies
    reload(tpo_view_companies)
photo2=PhotoImage(file='pictures/4.png')
l1=Label(back,image=photo2)
l1.grid(row=0,column=0,pady=15)

l2=Label(back,text='COMPANY INFORMATION',font='times 16 bold')
l2.grid(row=0,column=2,pady=15)

l3=Label(back,text='Company Name',font='times 14 bold')
l3.grid(row=1,column=0,pady=15)


l3=Label(back,text='Eligibility Criteria',font='times 14 bold')
l3.grid(row=2,column=0,pady=15)



l9=Label(back,text='Field',font='times 14 bold')
l9.grid(row=3,column=0,pady=15)


l10=Label(back,text='Package Offered (Rs.)',font='times 14 bold')
l10.grid(row=6,column=0,pady=15)


l10=Label(back,text='Reporting Date',font='times 14 bold')
l10.grid(row=4,column=0,pady=15)





l11=Label(back,text='Reporting Time',font='times 14 bold')
l11.grid(row=4,column=3,pady=15)


l12=Label(back,text='Selection Procedure',font='times 14 bold')
l12.grid(row=5,column=0,pady=15)


l19=Label(back,text='Job\nLocations',font='times 14 bold')
l19.grid(row=6,column=3,pady=15)


l13=Label(back,text='Profile',font='times 14 bold')
l13.grid(row=5,column=3,pady=15)


l14=Label(back,text='Official\nWebsite',font='times 14 bold')
l14.grid(row=1,column=3,pady=15)

l15=Label(back,text='Designation',font='times 14 bold')
l15.grid(row=2,column=3,pady=15)


l16=Label(back,text='Number of\nVacancies',font='times 14 bold')
l16.grid(row=3,column=3,pady=15)

photo9=PhotoImage(file='pictures/5b.png')
bt1=Button(back,image=photo9,width=80,bd=5,command=call)
bt1.grid(row=7,column=2)


    



