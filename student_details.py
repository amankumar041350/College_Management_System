import tkinter
from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import os
from tkinter import ttk
import pymysql


class home:
    def __init__(self,root):
      
        self.root=root
        self.root.title("Sidharth Degree College Nadaun")
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (w,h))
        
        
          
        
        # bg image
        self.bg=ImageTk.PhotoImage(file="images/bg2.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)

        

        self.passwod_var=StringVar()
        self.rollno_var=StringVar()



        detail_frame=Frame(root,bd=4,bg="white",relief=GROOVE)
        detail_frame.place(x=40,y=40,height=700,width=1450)

        roll=Label(detail_frame,text="Enter Roll No",font=("times new roman",20,"bold"),bg="white",fg="red")
        roll.place(x=0,y=0)
        
        txt_roll=Entry(detail_frame,textvariable=self.rollno_var,bd=4,relief=GROOVE,font=("arial",15,"bold"))
        txt_roll.place(x=0,y=60)

        passwod=Label(detail_frame,text="Enter Password",font=("times new roman",20,"bold"),bg="white",fg="red")
        passwod.place(x=0,y=120)
        
        txt_password=Entry(detail_frame,show="*",textvariable=self.passwod_var,bd=4,relief=GROOVE,font=("arial",15,"bold"))
        txt_password.place(x=0,y=180)

        b3=Button(detail_frame,text="Show Details",command=self.search_data,fg="red",bd=4,relief=GROOVE,width=10,bg="sky blue",font=("times new roman",15,"bold"))
        b3.place(x=40,y=240)


        

        table_frame=Frame(root,bd=4,bg="white",relief=GROOVE)
        table_frame.place(x=280,y=40,height=650,width=1210)

        scroll_x=Scrollbar(detail_frame,orient=HORIZONTAL)
        self.student_table=ttk.Treeview(table_frame,columns=("roll_no","Name","class","gender","contact","dob","address"),xscrollcommand=scroll_x.set)
        
        b1=Button(root,command=self.back,text="Back",fg="red",bd=4,relief=GROOVE,width=10,bg="sky blue",font=("times new roman",30,"bold"))
        b1.place(x=40,y=750,width=200,height=50)
        
        b2=Button(root,command=self.close,text="Close",fg="red",bd=4,relief=GROOVE,width=10,bg="sky blue",font=("times new roman",30,"bold"))
        b2.place(x=1290,y=750,width=200,height=50)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_x.config(command=self.student_table.xview)
        self.student_table['show']='headings'
        self.student_table.pack(fill=BOTH,expand=1)


        self.student_table.heading("roll_no",text="Roll No")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("class",text="Class")

        self.student_table.heading ("gender",text="Gender")
        self.student_table.heading ("contact",text="Contact")
        self.student_table.heading ("dob",text="D.O.B")
        self.student_table.heading ("address",text="Address")

        
    
     #functions


    def back(self):
     root.destroy()
     os.system("python student_portal.py")

    def close(self):
     root.destroy()

    def search_data(self):
        if self.rollno_var.get()=="" or self.passwod_var.get()=="":
                messagebox.showerror("Error","All Fields Are Requried",parent=root)
        else:
             con=pymysql.connect(host="localhost",user="root",password="root",database="clg")
             cur=con.cursor()
             cur.execute("select * from students where roll_no=%s and std_password=%s",(self.rollno_var.get(),self.passwod_var.get()))
             rows=cur.fetchone()
             if rows==None:
              messagebox.showerror("Error","Wrong ROLL NO/PASSWORD")
             else:
                con=pymysql.connect(host="localhost",user="root",password="root",database="clg")
                cur=con.cursor()
                cur.execute("select * from students where roll_no=%s and std_password=%s",(self.rollno_var.get(),self.passwod_var.get()))
                rows=cur.fetchall()
                if len(rows)!=0:
                  self.student_table.delete(*self.student_table.get_children())
                  for row in rows:
                    self.student_table.insert('',END,values=row)
                  con.commit()
                  messagebox.showinfo("Success ","Record Displayed Successfully")
                
             con.close()
             
        

















root=Tk()
obj=home(root)
root.mainloop()