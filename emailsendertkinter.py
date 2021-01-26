from tkinter import *
import smtplib as s
import tkinter.messagebox as mess
root=Tk()
root.geometry("500x600")
root.title("Email sender")
root.config(bg="#2c3e50")
a=StringVar()
b=StringVar()
c=StringVar()
d=StringVar()
e=StringVar()
def automation():
    
   
    aa=a.get()
    bb=b.get()
    cc=c.get()
    dd=d.get()
    ee=e.get()
    # print(aa,bb,cc,dd,ee)
    try:

        ob=s.SMTP("smtp.gmail.com",587)#making server
        ob.starttls()#making encryption
        ob.login(aa,bb)
    

        subject=cc
        body=ee
        message="subject:{}\n\n{}".format(subject,body)
        # print(message)
    
        ob.sendmail("ss",dd,message)
        print("sent sucessfully")
        mess.showinfo("sucess..","sent sucessfully...")
        ls.config(text="sent sucessfully...")
        
        sl.config(text="")
    except:
        mess.showerror("oops!","plz enter data correctly or check your internet")
        sl.config(text="oops! plz check your connection\nor enter data properly...")
        
        ls.config(text="")
    b.set("")

def safal():
    mess.showinfo("information","Note: plz use internet for running...")

        


    
    

f1=Frame(root, bg="#e74c3c", borderwidth=4, relief=SUNKEN)
f1.pack(side=LEFT,fill="y")
l1=Label(f1,text="Email",font="serif 8 bold",bg="#0984e3")
l1.grid(row=0,column=0,ipady=7,ipadx=48)
e1=Entry(f1,textvariable=a)
e1.grid(row=0,column=1,ipady=7,ipadx=35)
l3=Label(f1,text="password",font="serif 8 bold",bg="#00cec9")
l3.grid(row=1,column=0,ipady=7,ipadx=35)
e2=Entry(f1,show="*",textvariable=b)
e2.grid(row=1,column=1,ipady=7,ipadx=35)

l2=Label(f1,text="Subject",font="serif 8 bold",bg="#6c5ce7")
l2.grid(row=2,column=0,ipady=9,ipadx=43)
e3=Entry(f1,textvariable=c)
e3.grid(row=2,column=1,ipady=9,ipadx=35)

l4=Label(f1,text="Send To",font="serif 8 bold",bg="#2d3436")
l4.grid(row=3,column=0,ipady=9,ipadx=41)
e4=Entry(f1,textvariable=d)
e4.grid(row=3,column=1,ipady=9,ipadx=35)

l5=Label(f1,text="Message",font="serif 8 bold",bg="#74b9ff")
l5.grid(row=5,column=0,ipady=30,ipadx=38)
e5=Entry(f1,bg="#d63031",fg="white",textvariable=e)
e5.grid(row=5,column=1,ipady=30,ipadx=35)

but=Button(f1,text="send",bg="#2ecc71",fg="#34495e",cursor="plus",font="serif 12 bold",bd=3,command=automation)
but.place(x=105,y=240,width=130,height=30)
ls=Label(f1,text="",bg="#e74c3c",fg="white",font="serif 19 bold")
ls.place(x=94,y=290)
sl=Label(f1,text="",bg="#e74c3c",fg="black",font="serif 9 bold")
sl.place(x=90,y=290)

buti=Button(root,text="information",bitmap="info",bd=3,bg="#c7ecee",cursor="pirate",width=25,command=safal)
buti.pack(side=TOP,pady=12)

but2=Button(root,text="Quit",relief=RAISED,bg="#182C61",fg="white",font="serif 12 bold",cursor="circle",command=root.quit)
but2.pack(side=BOTTOM,fill="both")

vv=Label(f1,bg="#e74c3c",text="Developed By Safal and Aayush...",fg="white",font="serif 13 bold")
vv.place(x=40,y=450)
root.mainloop()