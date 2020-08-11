from tkinter import *
import tkinter.ttk as ttk
import session
root=Tk()
root.geometry('550x550')
photo1=PhotoImage(file='pictures/7.png')
back=Label(root,image=photo1)
back.pack(fill='both',expand='yes')
def student():
    uid=e1.get()
    session.setUid(uid)
    root.destroy()
    import view_student
def company():
    month=cbb1.get()
    session.setMon(month)
    root.destroy()
    import search_company
def placement():
    year=cbb2.get()
    session.setYear(year)
    root.destroy()
    import search_placements
photo3=PhotoImage(file='pictures/4.png')
la=Label(back,image=photo3)
la.grid(row=0,column=0,pady=10,padx=5)

lb=Label(back,text='Search companies arriving at a specific month:',font='times 14')
lb.grid(row=1,column=1,pady=10)
l1=['01','02','03','04','05','06','07','08','09','10','11','12']
cbb1=ttk.Combobox(back,values=l1,justify='center',font='times 14')
cbb1.grid(row=2,column=1,pady=10)
bt1=Button(back,text='Show',bd=5,font='times 10',command=company)
bt1.grid(row=2,column=2)

lb=Label(back,text='Search Student by University ID:',font='times 14')
lb.grid(row=3,column=1,pady=10)
e1=Entry(back,justify='center',font='times 14')
e1.grid(row=4,column=1,pady=10)
bt2=Button(back,text='Show',bd=5,font='times 10',command=student)
bt2.grid(row=4,column=2)

lb=Label(back,text='Search placements by year ( 20__ ):',font='times 14')
lb.grid(row=5,column=1,pady=10)
l1=['02','03','04','05','06','07','08','09']
for i in range(10,25):
    l1.append(i)
cbb2=ttk.Combobox(back,values=l1,justify='center',font='times 14')
cbb2.grid(row=6,column=1,pady=10)
bt3=Button(back,text='Show',bd=5,font='times 10',command=placement)
bt3.grid(row=6,column=2)
