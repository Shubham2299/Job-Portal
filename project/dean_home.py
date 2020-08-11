from tkinter import *
import os
import tkinter.filedialog as fd
import session
import tkinter.messagebox as mb
from importlib import reload
path=''

root=Tk()
root.geometry('600x650')
photo1=PhotoImage(file='pictures/7.png')
back=Label(root,image=photo1)
back.pack(fill='both',expand='yes')
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
con=MySQLdb.connect('localhost','root','root','project')
cursor=con.cursor()



def view1():
    root.destroy()
    import tpo_view_companies
def out():
    root.destroy()
    import login_panel2
    reload(login_panel2)
def view4():
    root.destroy()
    import tpo_view_students
def view5():
    root.destroy()
    import tpo_view_placements

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
    d=session.getDeg()
    if (not os.path.exists('student')):
        os.mkdir('student')
    dest_path="student/"+d+".png"
    f=open(path,'rb')
    data=f.read()
    f.close()
    f2=open(dest_path,'wb')
    f2.write(data)
    f2.close()
    try:
        cursor.execute('update tpo_dean set image="%s" where designation="%s"'%(dest_path,d))
        con.commit()
        mb.showinfo("Info","Pic Uploaded Successfully")
    except Exception as e:
        con.rollback()
        print('exception',e)
    con.close()
    
photo3=PhotoImage(file='pictures/4.png')
la=Label(back,image=photo3)
la.grid(row=0,column=0,pady=10,padx=5)

menubar=Menu(back)
root.config(menu=menubar)



viewmenu=Menu(menubar,tearoff=0,activebackground='grey')
menubar.add_cascade(label='View',menu=viewmenu)
viewmenu.add_command(label='Companies',command=view1)

viewmenu.add_command(label='Students',command=view4)
viewmenu.add_command(label='Placements',command=view5)


frame9=Frame(back)
frame9.grid(row=1,column=2,pady=20)
photo2=PhotoImage(file='pictures/a.png')
l1=Label(frame9,image=photo2,height=300,width=250,bg='black')
l1.grid(row=0,column=0,pady=20)
l0=Label(frame9,text=' ')
l0.grid(row=0,column=1)
photo6=PhotoImage(file='pictures/change.png')
l9=Label(frame9,image=photo6)
l9.grid(row=0,column=2)
l9.bind('<Button-1>',selectPic)

con=MySQLdb.connect('localhost','root','root','project')
cursor=con.cursor()
try:
    de=session.getDeg()
    cursor.execute('select image from tpo_dean where designation="%s"'%(de))
    r=cursor.fetchone()
    if r!=None:
        photo2=PhotoImage(file=r[0])
        l1.config(image=photo2)

except Exception as e:
    print(e)

con.close()    


bt1=Button(back,text='Change Picture',bd=5,font='times 12',justify='center',command=call)
bt1.grid(row=2,column=2,pady=10)
bt2=Button(back,text='Logout',bd=5,font='times 10',justify='center',command=out)
bt2.grid(row=3,column=2)




