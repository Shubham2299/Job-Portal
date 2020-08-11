from tkinter import *
import session
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
cursor.execute('select * from student')
t=cursor.fetchall()
def student_view(uid):
    session.setUid(uid)
    root.destroy()
    import view_student
    
try:
    l1=Label(back,text='University ID',width=20,padx=10,pady=10,bd=5,bg='silver')
    l1.grid(row=0,column=0)
    l2=Label(back,text='Student Name',width=20,padx=10,pady=10,bd=5,bg='silver')
    l2.grid(row=0,column=1)
    l3=Label(back,text='Branch',width=20,padx=10,pady=10,bd=5,bg='silver')
    l3.grid(row=0,column=2)
    la=Label(back,text='',width=20,padx=10,pady=10,bd=5,bg='silver')
    la.grid(row=0,column=3)
    r=1
    for row in t:
        l4=Label(back,text=row[0],width=20,padx=10,pady=10,bd=5,bg='white')
        l4.grid(row=r,column=0)
        l5=Label(back,text=row[1],width=20,padx=10,pady=10,bd=5,bg='white')
        l5.grid(row=r,column=1)
        l6=Label(back,text=row[2],width=20,padx=10,pady=10,bd=5,bg='white')
        l6.grid(row=r,column=2)
        bta=Button(back,text='Show Info',width=10,bd=5,font='times 10')
        bta.config(command=lambda uid=row[0]:student_view(uid))
        bta.grid(row=r,column=3)
        r=r+1
except Exception as e:
    print('exception',e)
con.close()
