from tkinter import *
import os
root=Tk()
root.geometry('650x760')
import tkinter.filedialog as fd
photo1=PhotoImage(file='pictures/b.png')
back=Label(root,image=photo1)
back.pack(fill='both',expand='yes')
import session
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

import tkinter.messagebox as mb
from importlib import reload
photo3=PhotoImage(file='pictures/4.png')
la=Label(back,image=photo3)
la.grid(row=0,column=0,pady=10,padx=5)
path=''
menubar=Menu(back)
root.config(menu=menubar)

filemenu=Menu(menubar,tearoff=0,activebackground='grey')
menubar.add_cascade(label='Menu',menu=filemenu)
def my():
    root.destroy()
    import student_myprofile
def edit():
    root.destroy()
    import student_editprofile
def change():
    root.destroy()
    import student_changepwd
def out():
    root.destroy()
    import login_panel
    reload(login_panel)
def view1():
    root.destroy()
    import student_view_companies
def view2():
    root.destroy()
    import student_view_internships
def view3():
    root.destroy()
    import student_view_workshops
def view4():
    root.destroy()
    import student_view_placements
def selectPic(event):
    global path
    global photo2
    global l1
    path=fd.askopenfilename()
    photo2=PhotoImage(file=path)
    l1.config(image=photo2)
    
def call():
    global path
    con=MySQLdb.connect('localhost','root','root','project')
    cursor=con.cursor()
    uid=session.getUid()
    if (not os.path.exists('student')):
        os.mkdir('student')
    dest_path="student/"+uid+".png"
    f=open(path,'rb')
    data=f.read()
    f.close()
    f2=open(dest_path,'wb')
    f2.write(data)
    f2.close()
    try:
        cursor.execute('update student set image="%s" where uid="%s"'%(dest_path,uid))
        con.commit()
        mb.showinfo("Info","Pic Uploaded Successfully")
    except Exception as e:
        con.rollback()
        print('exception',e)
    con.close()

filemenu.add_command(label='My Profile',command=my)
filemenu.add_command(label='Edit Profile',command=edit)
filemenu.add_command(label='Change Password',command=change)
filemenu.add_separator()
filemenu.add_command(label='Logout',command=out)

viewmenu=Menu(menubar,tearoff=0,activebackground='grey')
menubar.add_cascade(label='View',menu=viewmenu)
viewmenu.add_command(label='Companies',command=view1)
viewmenu.add_command(label='Interships',command=view2)
viewmenu.add_command(label='Workshops',command=view3)
viewmenu.add_command(label='Placements',command=view4)
lq=Label(back,text='WELCOME',font='times 22 bold',bg='black',fg='white')
lq.grid(row=0,column=2)
frame9=Frame(back,bg='black')
frame9.grid(row=1,column=2,pady=20)
photo2=PhotoImage(file='pictures/a.png')
l1=Label(frame9,image=photo2,height=300,width=250,bg='black')
l1.grid(row=0,column=0,pady=20)
l0=Label(frame9,text=' ',bg='black')
l0.grid(row=0,column=1)
photo6=PhotoImage(file='pictures/change.png')
l9=Label(frame9,image=photo6,bg='black')
l9.grid(row=0,column=2)
l9.bind('<Button-1>',selectPic)


con=MySQLdb.connect('localhost','root','root','project')
cursor=con.cursor()
try:
    uid=session.getUid()
    cursor.execute('select image from student where uid="%s"'%(uid))
    r=cursor.fetchone()
    if r!=None:
        photo2=PhotoImage(file=r[0])
        l1.config(image=photo2)

except Exception as e:
    print(e)

con.close()    



bt1=Button(back,text='Change Picture',bd=5,font='times 12',justify='center',command=call)
bt1.grid(row=2,column=2,pady=20)

l2=Label(back,text='Feedback',font='times 14')
l2.grid(row=3,column=2,pady=5)
txt=Text(back,height=5,width=50)
txt.grid(row=4,column=2,pady=5)

