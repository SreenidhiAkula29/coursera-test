from tkinter import *
from tkinter.messagebox import askyesno
from tkinter.ttk import *
a=Tk()
a.geometry("600x600")
l1=Label(a,text="Metro ticket booking",font=("Arial Bold",30))
l1.grid(column=1,row=0)
l2=Label(a,text="Name",font=("Arial Bold",10))
l2.grid(column=0,row=1)
l3=Label(a,text="from",font=("Arial Bold",10))
l3.grid(column=0,row=2)
l4=Label(a,text="to",font=("Arial Bold",10))
l4.grid(column=0,row=3)
l5=Label(a,text="tickets",font=("Arial Bold",10))
l5.grid(column=0,row=4)
l6=Label(a,text="do you want cab?",font=("Arial Bold",10))
l6.grid(column=0,row=5)
e1=Entry(a,width=15)
e1.grid(column=1,row=1)
fs=["select","JNTUH","KPHB","MYP"]
f=StringVar()
d1=OptionMenu(a,f,*fs)
d1.grid(column=1,row=2)
ts=["select","JNTUH","KPHB","MYP"]
t=StringVar()
d2=OptionMenu(a,t,*ts)
d2.grid(column=1,row=3)
tickets=["select",1,2,3,4,5]
ti=IntVar()
d3=OptionMenu(a,ti,*tickets)
d3.grid(column=1,row=4)
def yes():
    l6=Label(a,text="drop",font=("Arial Bold",10))
    l6.grid(column=0,row=6)
    e2=Entry(a,width=15)
    e2.grid(column=1,row=6)
    def book():
        n=e1.get()#name
        fsn=f.get()#from station
        tsn=t.get()# to station
        ticket=ti.get()#tickets
        bill=40*ticket
        drop=e2.get()
        ans=askyesno("confirmation","Hello"+n+
                     "/n **Metro** \n From:"+fsn+
                     "\n To:"+tsn+"\n Tickets:"+str(ticket)+
                     "\n bill:"+str(bill)+
                     "\n Cab details \n from:"+tsn+
                     "\n To:"+drop+
                     "\n Confirm ?")
        if ans:
            messagebox.showinfo("","done")
        else:
            messagebox.showinfo("","cancelled")
    b3=Button(a,text="BOOK",command=book)
    b3.grid(column=1,row=7)
b1=Button(a,text="Yes",command=yes) 
b1.grid(column=1,row=5)   
def no():
    n=e1.get()
    fsn=f.get()
    tsn=t.get()
    ticket=ti.get()
    bill=40*ticket
    ans=askyesno("confirmation","Hello"+n+
                 "/n **Metro** \n From:"+fsn+
                 "\n To:"+tsn+"\n Tickets:"+str(ticket)+
                 "\n bill:"+str(bill)+
                 "\n Confirm ?")
    if ans:
        messagebox.showinfo("","done")
    else:
        messagebox.showinfo("","cancelled")
b2=Button(a,text="No",command=no)
b2.grid(column=2,row=5)       
a.mainloop()