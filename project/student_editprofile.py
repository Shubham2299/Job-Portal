from tkinter import *
from importlib import reload
import session
root=Tk()
root.geometry('1300x750+20+20')
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

photo1=PhotoImage(file='pictures/b.png')
back=Label(root,image=photo1)
back.pack(fill='both',expand='yes')

def call():
    con=MySQLdb.connect('localhost','root','root','project')
    cursor=con.cursor()
    a=e2.get()
    b=txt1.get('1.0','end')
    c=txt2.get('1.0','end')
    d=e5.get()
    e=e6.get()
    f=float(e7.get())
    try:
        uid=session.getUid()
        cursor.execute('update student set name="%s",percentage_grad="%f",interest="%s",preference="%s",email="%s",contact="%s" where uid="%s"'%(a,f,b,c,d,e,uid))
        con.commit()
        b=mb.showinfo('information','Record Updated')
        root.destroy()
        import student_home
        reload(student_home)
    except Exception as e:
        con.rollback()
        print('exception',e)
    con.close()

photo3=PhotoImage(file='pictures/4.png')
la=Label(back,image=photo3)
la.grid(row=0,column=0,pady=10,padx=5)

l1=Label(back,text='EDIT PROFILE',font='times 22 bold',bg='black',fg='white')
l1.grid(row=1,column=2,pady=20)

l2=Label(back,text='Student Name',font='times 16',bg='black',fg='white')
l2.grid(row=2,column=0,pady=20)
e2=Entry(back,width=30,justify='center',font='times 16')
e2.grid(row=2,column=1,ipady=10)

l3=Label(back,text='Area Of\nInterest',font='times 16',bg='black',fg='white')
l3.grid(row=3,column=0,pady=20)
txt1=Text(back,width=35,height=10,font='times 12')
txt1.grid(row=3,column=1,pady=20)

l4=Label(back,text='Prefered\nCompanies',font='times 16',bg='black',fg='white')
l4.grid(row=3,column=3,pady=20)
txt2=Text(back,width=35,height=10,font='times 12')
txt2.grid(row=3,column=4,pady=20)

l7=Label(back,text='Percentage ( Graduation )',font='times 16',bg='black',fg='white')
l7.grid(row=5,column=0,pady=20)
e7=Entry(back,width=10,justify='center',font='times 14')
e7.grid(row=5,column=1,ipady=10)

l5=Label(back,text='Email',font='times 16',bg='black',fg='white')
l5.grid(row=4,column=0,pady=20)
e5=Entry(back,width=35,justify='center',font='times 14')
e5.grid(row=4,column=1,ipady=10)

l6=Label(back,text='Contact',font='times 16',bg='black',fg='white')
l6.grid(row=4,column=3,pady=20)
e6=Entry(back,width=30,justify='center',font='times 16')
e6.grid(row=4,column=4,ipady=10)

bt1=Button(back,text='UPDATE',bd=5,width=10,font='times 14',command=call)
bt1.grid(row=6,column=2)

