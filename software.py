from tkinter import *
from tkinter import ttk,messagebox
import os
class File_App:
    def __init__(self):
        self.root=Tk()
        self.root.title("File Based Record System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="File Based Record System",bd=10,pady=10,relief=GROOVE,font=("times",35,"bold")).pack(fill=X)

        Student_Frame=Frame(self.root,bd=10,relief=GROOVE)
        Student_Frame.place(x=20,y=100,height=450)

        stitle=Label(Student_Frame,text="Student Details",font="times 30 bold").grid(row=0,columnspan=4,pady=20)
        # ========= All Variable ==============
        self.s_id=StringVar()
        self.name=StringVar()
        self.course=StringVar()
        self.address=StringVar()
        self.city=StringVar()
        self.contact=StringVar()
        self.date=StringVar()
        self.degree=StringVar()
        self.proof=StringVar()
        self.payment=StringVar()
        # ============== Student details ==========================
        lblsid=Label(Student_Frame,text="Student ID",font="times 20 bold").grid(row=1,column=0,pady=10,padx=10,sticky='w')
        txtsid=Entry(Student_Frame,bd=7,textvariable=self.s_id,relief=GROOVE,width=25,font="arial 15 bold").grid(row=1,column=1,padx=10,pady=10)
        lblcontact=Label(Student_Frame,text="Contact No",font="times 20 bold").grid(row=1,column=2,pady=10,padx=10,sticky='w')
        txtsid=Entry(Student_Frame,bd=7,textvariable=self.contact,relief=GROOVE,width=25,font="arial 15 bold").grid(row=1,column=3,padx=10,pady=10)

        lblname=Label(Student_Frame,text="Name",font="times 20 bold").grid(row=2,column=0,pady=10,padx=10,sticky='w')
        txtname=Entry(Student_Frame,bd=7,textvariable=self.name,relief=GROOVE,width=25,font="arial 15 bold").grid(row=2,column=1,padx=10,pady=10)
        lbldate=Label(Student_Frame,text="Date(dd/mm/yyyy)",font="times 20 bold").grid(row=2,column=2,pady=10,padx=10,sticky='w')
        txtdate=Entry(Student_Frame,bd=7,textvariable=self.date,relief=GROOVE,width=25,font="arial 15 bold").grid(row=2,column=3,padx=10,pady=10)

        lblcourse=Label(Student_Frame,text="Course",font="times 20 bold").grid(row=3,column=0,pady=10,padx=10,sticky='w')
        txtcourse=Entry(Student_Frame,bd=7,textvariable=self.course,relief=GROOVE,width=25,font="arial 15 bold").grid(row=3,column=1,padx=10,pady=10)
        

        lbladd=Label(Student_Frame,text="Address",font="times 20 bold").grid(row=4,column=0,pady=10,padx=10,sticky='w')
        txtadd=Entry(Student_Frame,bd=7,textvariable=self.address,relief=GROOVE,width=25,font="arial 15 bold").grid(row=4,column=1,padx=10,pady=10)
        
        lblcity=Label(Student_Frame,text="City",font="times 20 bold").grid(row=5,column=0,pady=10,padx=10,sticky='w')
        txtcity=Entry(Student_Frame,bd=7,textvariable=self.city,relief=GROOVE,width=25,font="arial 15 bold").grid(row=5,column=1,padx=10,pady=10)

        lbldegree=Label(Student_Frame,text="Select Degree",font="times 20 bold").grid(row=3,column=2,pady=10,padx=10,sticky='w')
        lblidproof=Label(Student_Frame,text="ID Proof",font="times 20 bold").grid(row=4,column=2,pady=10,padx=10,sticky='w')
        lblpaymode=Label(Student_Frame,text="Payment Mode",font="times 20 bold").grid(row=5,column=2,pady=10,padx=10,sticky='w')

        degreecombo=ttk.Combobox(Student_Frame,width=20,font="arial 18 bold",textvariable=self.degree,state="readonly")
        degreecombo['values']=("BCA","MCA","Btech","MBA","Mtech")
        degreecombo.grid(row=3,column=3,padx=10,pady=10)

        idcombo=ttk.Combobox(Student_Frame,width=20,font="arial 18 bold",textvariable=self.proof,state="readonly")
        idcombo['values']=("Aadhar Card","PAN Card","Driving Licence","Voter Card")
        idcombo.grid(row=4,column=3,padx=10,pady=10)

        paymentcombo=ttk.Combobox(Student_Frame,width=20,font="arial 18 bold",textvariable=self.payment,state="readonly")
        paymentcombo['values']=("Cash","NEFT","Internet Banking","Credit Card","UPI","Debit Card")
        paymentcombo.grid(row=5,column=3,padx=10,pady=10)
        
        # ============== Buttons =======================================
        btnFrame=Frame(self.root,bd=10,relief=GROOVE)
        btnFrame.place(x=10,y=570)

        btnsave=Button(btnFrame,text="Save",font="arial 15 bold",bd=7,width=18,command=self.save_data).grid(row=0,column=0,padx=12,pady=10)
        btndelete=Button(btnFrame,text="Delete",font="arial 15 bold",bd=7,width=18,command=self.delete).grid(row=0,column=1,padx=12,pady=10)
        btnclear=Button(btnFrame,text="Clear",font="arial 15 bold",bd=7,width=18,command=self.clear).grid(row=0,column=2,padx=12,pady=10)
        btnlogout=Button(btnFrame,text="Logout",font="arial 15 bold",bd=7,width=18,command=self.logout).grid(row=0,column=3,padx=12,pady=10)
        btnexit=Button(btnFrame,text="Exit",font="arial 15 bold",bd=7,width=18,command=self.exit_fun).grid(row=0,column=4,padx=12,pady=10)

        # ============= File Frames ==========================
        file_Frame=Frame(self.root,bd=10,relief=GROOVE)
        file_Frame.place(x=1040,y=100,width=300,height=450)

        ftitle=Label(file_Frame,text="All Files",font="Arial 20 bold",bd=5,relief=GROOVE).pack(side=TOP,fill=X)

        scroll_y=Scrollbar(file_Frame,orient=VERTICAL)
        self.file_list=Listbox(file_Frame,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.file_list.yview)
        self.file_list.pack(fill=BOTH,expand=1)

        # =====================
        self.file_list.bind("<ButtonRelease-1>",self.get_data)
        self.show_files()
        # =========================
        self.root.mainloop()
    def save_data(self):
        present="no"
        if self.s_id.get()=="":
            messagebox.showerror("Error","Student Id must be required")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0] == self.s_id.get():
                        present="yes"
                if present=="yes":
                    ask=messagebox.askyesno("Update","file already existe \nDo you want to update it?")
                    if ask>0:
                        self.save_files()
                        messagebox.showinfo("Update","Record has Updated Succesfully!!")
                        self.show_files()
                else:
                    self.save_files()
                    messagebox.showinfo("Save","Record has Save Succesfully!!")
                    self.show_files()
            else:
                self.save_files()
                messagebox.showinfo("Save","Record has Save Succesfully!!")
                self.show_files()
                       
    def save_files(self):
        f=open("files/"+str(self.s_id.get())+".txt","w")
        f.write(
            str(self.s_id.get())+","+
            str(self.name.get())+","+
            str(self.course.get())+","+
            str(self.address.get())+","+
            str(self.city.get())+","+
            str(self.contact.get())+","+
            str(self.date.get())+","+
            str(self.degree.get())+","+
            str(self.proof.get())+","+
            str(self.payment.get())
            )
        f.close()
    
    
    def show_files(self):
        files=os.listdir("files/")
        self.file_list.delete(0,END)
        if len(files)>0:
            for i in files:
                self.file_list.insert(END,i)

    def get_data(self,ev):
        get_curser=self.file_list.curselection()
        f1=open("files/"+self.file_list.get(get_curser))
        value=[]
        for f in f1:
            value=f.split(",")
            # print(value)
        self.s_id.set(value[0])
        self.name.set(value[1])
        self.course.set(value[2])
        self.address.set(value[3])
        self.city.set(value[4])
        self.contact.set(value[5])
        self.date.set(value[6])
        self.degree.set(value[7])
        self.proof.set(value[8])
        self.payment.set(value[9])
    
    def clear(self):
        self.s_id.set("")
        self.name.set("")
        self.course.set("")
        self.address.set("")
        self.city.set("")
        self.contact.set("")
        self.date.set("")
        self.degree.set("")
        self.proof.set("")
        self.payment.set("")

    def delete(self):
        present="no"
        if self.s_id.get()=="":
            messagebox.showerror("Error","Student Id must be required")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0] == self.s_id.get():
                        present="yes"
                if present=="yes":
                    ask=messagebox.askyesno("Delete","Do you really want to delete?")
                    if ask>0:
                        os.remove("files/"+self.s_id.get()+".txt")
                        messagebox.showinfo("Success","Deleted Successfully!!")
                        self.show_files()
                else:
                    messagebox.showerror("Error","File not found")
            else:
                messagebox.showerror("Error","Files not Available")

    def exit_fun(self):
        option=messagebox.askyesno("Exit","Do you realy want to exit")
        if option > 0:
            self.root.destroy()
        else:
            return
    def logout(self):
        self.root.destroy()
        import login

