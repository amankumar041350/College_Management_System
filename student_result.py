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

        b3=Button(detail_frame,text="Show Result",command=self.search_data,fg="red",bd=4,relief=GROOVE,width=10,bg="sky blue",font=("times new roman",15,"bold"))
        b3.place(x=40,y=240)


        

        table_frame=Frame(root,bd=4,bg="white",relief=GROOVE)
        table_frame.place(x=280,y=40,height=650,width=1210)

        scroll_x=Scrollbar(detail_frame,orient=HORIZONTAL)
        self.student_table=ttk.Treeview(table_frame,columns=("roll_no","Name","class","gender","contact","dob","address","std_password","sub1","Mo1","Tm1","sub2","Mo2","Tm2","sub3","Mo3","Tm3","sub4","Mo4","Tm4","sub5","Mo5","Tm5","sub6","Mo6","Tm6","sub7","Mo7","Tm7","sub8","Mo8","Tm8"),xscrollcommand=scroll_x.set)
        
        b1=Button(root,command=self.back,text="Back",fg="red",bd=4,relief=GROOVE,width=10,bg="sky blue",font=("times new roman",30,"bold"))
        b1.place(x=40,y=750,width=200,height=50)
        
        b2=Button(root,command=self.close,text="Close",fg="red",bd=4,relief=GROOVE,width=10,bg="sky blue",font=("times new roman",30,"bold"))
        b2.place(x=1290,y=750,width=200,height=50)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_x.config(command=self.student_table.xview)
        self.student_table['show']='headings'
        self.student_table.pack(fill=BOTH,expand=1)



        hide=Frame(table_frame,bg="white")
        hide.place(x=0,y=1,height=640,width=160)

        self.student_table.heading("roll_no",text="")
        self.student_table.heading("Name",text="")
        self.student_table.heading("class",text="")

        self.student_table.heading ("gender",text="")
        self.student_table.heading ("contact",text="")
        self.student_table.heading ("dob",text="")
        self.student_table.heading ("address",text="")
        self.student_table.heading ("std_password",text="")


        self.student_table.column ("gender",width=0)
        self.student_table.column ("contact",width=0)
        self.student_table.column ("dob",width=0)
        self.student_table.column ("address",width=0)
        self.student_table.column ("std_password",width=0)
      

      # showable

        self.student_table.column ("Name",width=0)
        self.student_table.column ("roll_no",width=0)
        self.student_table.column ("class",width=0)





        self.student_table.heading("sub1",text="Subject")
        self.student_table.heading("Mo1",text="OM")
        self.student_table.heading("Tm1",text="TM")
        self.student_table.heading("sub2",text="Sub")
        self.student_table.heading("Mo2",text="OM")
        self.student_table.heading("Tm2",text="TM")
        self.student_table.heading("sub3",text="Sub")
        self.student_table.heading("Mo3",text="OM")
        self.student_table.heading("Tm3",text="TM")
        self.student_table.heading("sub4",text="Sub")
        self.student_table.heading("Mo4",text="OM")
        self.student_table.heading("Tm4",text="TM")
        self.student_table.heading("sub5",text="Sub")
        self.student_table.heading("Mo5",text="OM")
        self.student_table.heading("Tm5",text="TM")
        self.student_table.heading("sub6",text="Sub")
        self.student_table.heading("Mo6",text="OM")
        self.student_table.heading("Tm6",text="TM")
        self.student_table.heading("sub7",text="Sub")
        self.student_table.heading("Mo7",text="OM")
        self.student_table.heading("Tm7",text="TM")
        self.student_table.heading("sub8",text="Sub")
        self.student_table.heading("Mo8",text="OM")
        self.student_table.heading("Tm8",text="TM")


        self.student_table.column ("sub1",width=100)
        self.student_table.column ("sub2",width=100)
        self.student_table.column ("sub3",width=100)
        self.student_table.column ("sub4",width=100)
        self.student_table.column ("sub5",width=100)
        self.student_table.column ("sub6",width=100)
        self.student_table.column ("sub7",width=100)
        self.student_table.column ("sub8",width=100)
        self.student_table.column ("Mo1",width=50)
        self.student_table.column ("Mo2",width=50)
        self.student_table.column ("Mo3",width=50)
        self.student_table.column ("Mo4",width=50)
        self.student_table.column ("Mo5",width=50)
        self.student_table.column ("Mo6",width=50)
        self.student_table.column ("Mo7",width=50)
        self.student_table.column ("Mo8",width=50)
        self.student_table.column ("Tm1",width=50)
        self.student_table.column ("Tm2",width=50)
        self.student_table.column ("Tm3",width=50)
        self.student_table.column ("Tm4",width=50)
        self.student_table.column ("Tm5",width=50)
        self.student_table.column ("Tm6",width=50)
        self.student_table.column ("Tm7",width=50)
        self.student_table.column ("Tm8",width=50)

    



     


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