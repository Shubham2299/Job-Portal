from tkinter import *
import tkinter.messagebox as mb
import session
root=Tk()
root.geometry('720x640')
photo1=PhotoImage(file='pictures/main.png')
back=Label(root,image=photo1)
back.pack(fill='both',expand='yes')
photo2=PhotoImage(file='pictures/4.png')
l1=Label(back,image=photo2)
l1.grid(row=0,column=0,pady=10,padx=5)
def student():
    root.destroy()
    import login_panel
def tpo():
    root.destroy()
    import login_panel2
l2=Label(back,text='WELCOME TO\n UNIVERSITY',font='times 24 bold',fg='white',bg='black')
l2.grid(row=0,column=2,pady=20)

l2=Label(back,text='LOGIN PANEL',font='times 22 bold',fg='white',bg='black')
l2.grid(row=1,column=2,pady=20)

bt1=Button(back,text='STUDENT\nLOGIN',font='times 10 bold',bd=5,width=10,command=student)
bt1.grid(row=2,column=1,pady=20)

bt2=Button(back,text='TPO/Dean\nLOGIN',font='times 10 bold',bd=5,width=10,command=tpo)
bt2.grid(row=2,column=3,pady=20)

photo3=PhotoImage(file='pictures/11.png')
l3=Label(back,image=photo3)
l3.grid(row=3,column=2,pady=10)

l4=Label(back,text='Our University is a full-fledged university\n established by the Punjab State Legislature\n and is recognized by University Grants Commission \nunder Section 2(f) with the right to confer degrees as per \nSection 22(1) of the UGC Act, 1956.',font='times 11',bg='black',fg='white',height=10,width=45)
l4.grid(row=4,column=2,pady=10)

