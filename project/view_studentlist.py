from tkinter import *
import tkinter.messagebox as mb
import tkcalendar as cal
import session
from importlib import reload
root=Tk()
root.geometry('650x550')
photo1=PhotoImage(file='pictures/7.png')
back=Label(root,image=photo1)
back.pack(fill='both',expand='yes')
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
con=MySQLdb.connect('localhost','root','root','project')
cursor=con.cursor()
ccid=session.getCid()

batch_from=0
batch_to=0
cursor.execute("select * from company where company_id='%d'"%(ccid))
t2=cursor.fetchone()

if t2 !=None:
 
    
    batch_from=t2[16]
    batch_to=t2[17]
    
print(batch_from,batch_to)    
cursor.execute('select * from student where batch_from="%d" and batch_to="%d"'%(batch_from,batch_to))
t=cursor.fetchall()
def call():
    global cb_dict
    
    con=MySQLdb.connect('localhost','root','root','project')
    cursor=con.cursor()
    try:
        cid=session.getCid()
        
        dat=d.get()
        for k,v in cb_dict.items():
            if(v.get()==1):
                cursor.execute('insert into placed_info(cid,u_id,date) values("%d","%s","%s")'%(cid,k,dat))
                con.commit()
        b=mb.showinfo('information','Record Inserted')
        root.destroy()
        
    except Exception as e:
        print(e)
    con.close()
    
try:
    l1=Label(back,text='University ID',width=20,padx=10,pady=10,bd=5,bg='silver')
    l1.grid(row=0,column=0)
    l2=Label(back,text='Student Name',width=20,padx=10,pady=10,bd=5,bg='silver')
    l2.grid(row=0,column=1)
    l3=Label(back,text='Current Date',width=20,padx=10,pady=10,bd=5,bg='silver')
    l3.grid(row=0,column=2)
    la=Label(back,text='',width=20,padx=10,pady=10,bd=5,bg='silver')
    la.grid(row=0,column=3)
   
    r=1
    cb_dict={}
    for row in t:
        l4=Label(back,text=row[0],width=20,padx=10,pady=10,bd=5,bg='white')
        l4.grid(row=r,column=0)        
        l5=Label(back,text=row[1],width=20,padx=10,pady=10,bd=5,bg='white')
        l5.grid(row=r,column=1)
        d=cal.DateEntry(back,width=10)
        d.grid(row=r,column=2)
        n1=IntVar()
        cb1=Checkbutton(back,variable=n1)
        cb1.grid(row=r,column=3)
        cb_dict[row[0]]=n1
        r=r+1       
       
except Exception as e:
    print('exception',e)
con.close()

bt2=Button(back,text='Update',width=10,bd=5,font='times 12',command=call)
bt2.grid(row=r,column=3)
