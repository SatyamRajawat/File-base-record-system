from tkinter import*
from tkinter import messagebox
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("File Based Record System")
        self.root.geometry("1350x700+0+0")

        self.uname=StringVar()
        self.password=StringVar()

        F1=Frame(self.root,bd=10,relief=GROOVE)
        F1.place(x=450,y=150,height=350)

        title=Label(F1,text="Login System",font=("times",30,"bold")).grid(row=0,columnspan=2,pady=20)

        lbluser=Label(F1,text="Username",font=("times",25,"bold")).grid(row=1,column=0,padx=10,pady=10)
        txtuser=Entry(F1,bd=7,textvariable=self.uname,relief=GROOVE,width=25,font="arial 15 bold").grid(row=1,column=1,padx=10,pady=10)

        lblpass=Label(F1,text="Password",font=("times",25,"bold")).grid(row=2,column=0,padx=10,pady=10)
        txtpass=Entry(F1,bd=7,show="*",textvariable=self.password,relief=GROOVE,width=25,font="arial 15 bold").grid(row=2,column=1,padx=10,pady=10)

        btnlog=Button(F1,text="Login",font="arial 15 bold",bd=7,width=10,command=self.login).place(x=10,y=250)
        btnreset=Button(F1,text="Reset",font="arial 15 bold",bd=7,width=10,command=self.reset).place(x=170,y=250)
        btnexit=Button(F1,text="Exit",font="arial 15 bold",bd=7,width=10,command=self.exit).place(x=330,y=250)

    def login(self):
        if self.uname.get()=="" or self.password.get()=="": 
            messagebox.showerror("Error","All fields ar required!!")

        elif self.uname.get()=="admin" and self.password.get()=="admin":
            # messagebox.showin fo("Successfull",f"Welcome {self.uname.get()}")
            self.root.destroy()
            import software
            software.File_App()

        else:
            messagebox.showerror("Error","Invalid Useranme or Password!!")

    def reset(self):
        self.uname.set("")
        self.password.set("")

    def exit(self):
        option=messagebox.askyesno("Exit","Do you realy want to exit")
        if option > 0:
            self.root.destroy()
        else:
            return

root=Tk()
ob=Login(root)
root.mainloop()