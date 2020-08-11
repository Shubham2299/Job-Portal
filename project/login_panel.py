from tkinter import *
import tkinter.messagebox as mb
import session
root=Tk()
root.geometry('1500x600+10+100')
photo1=PhotoImage(file='pictures/b.png')
back=Label(root,image=photo1)
back.pack(fill='both',expand='yes')
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

def call():
    con=MySQLdb.connect('localhost','root','root','project')
    cursor=con.cursor()
    un=e4.get()
    pwd=e5.get()
    try:
        cursor.execute('select * from student where uid="%s" and password="%s"'%(un,pwd))
        t=cursor.fetchone()
        if t!=None:
            root.destroy()
            session.setUid(un)
            import student_home
        else:
            b=mb.showinfo('information','Invalid User')
        con.commit()
    except Exception as e:
        print('exception',e)
    con.close()
    
def cal2(event):
    root.destroy()
    import student_info
    

photo2=PhotoImage(file='pictures/4.png')
l1=Label(back,image=photo2)
l1.grid(row=0,column=0,pady=10,padx=5)

l2=Label(back,text='WELCOME TO\n UNIVERSITY',font='times 24 bold',fg='white',bg='black')
l2.grid(row=0,column=2,pady=20)

l2=Label(back,text='LOGIN PANEL',font='times 22 bold',fg='white',bg='black')
l2.grid(row=1,column=2,pady=20)

frame1=Frame(back,bg='black')
frame1.grid(row=2,column=1)
l3=Label(frame1,text='Already registered? Login here.',font='times 14',bg='black',fg='white')
l3.grid(row=0,column=0,pady=20)
l4=Label(frame1,text='University ID',font='times 16',bg='black',fg='white')
l4.grid(row=1,column=0,pady=20)
e4=Entry(frame1,width=35,justify='center',font='times 12')
e4.grid(row=1,column=2,ipady=9)
l5=Label(frame1,text='Password',font='times 16',bg='black',fg='white')
l5.grid(row=2,column=0,pady=20)
e5=Entry(frame1,width=35,justify='center',font='times 12',show='*')
e5.grid(row=2,column=2,ipady=9)
bt1=Button(frame1,text='Login',bd=5,font='times 14',command=call)
bt1.grid(row=3,column=1,pady=20,padx=5)

frame2=Frame(back,bg='black')
frame2.grid(row=2,column=3)
l3=Label(frame2,text='Not registered? Sign Up now!!',font='times 14',bg='black',fg='white')
l3.grid(row=0,column=0,pady=20)
l4=Label(frame2,text='Enrollment ID',font='times 16',bg='black',fg='white')
l4.grid(row=1,column=0,pady=20)
e6=Entry(frame2,width=35,justify='center',font='times 12')
e6.grid(row=1,column=1,ipady=9)
bt2=Button(frame2,text='Register',font='times 14',bd=5)
bt2.config(command=lambda bt=bt2:cal2(bt))
bt2.grid(row=2,column=0,pady=20)
