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
         
        # variables----
        self.sub_1=StringVar()
        self.sub_2=StringVar()
        self.sub_3=StringVar()
        self.sub_4=StringVar()
        self.sub_5=StringVar()
        self.sub_6=StringVar()
        self.sub_7=StringVar()
        self.sub_8=StringVar()
          
        self.mo_1=StringVar()
        self.mo_2=StringVar()
        self.mo_3=StringVar()
        self.mo_4=StringVar()
        self.mo_5=StringVar()
        self.mo_6=StringVar()
        self.mo_7=StringVar()
        self.mo_8=StringVar()
         
        self.tm_1=StringVar()
        self.tm_2=StringVar()
        self.tm_3=StringVar()
        self.tm_4=StringVar()
        self.tm_5=StringVar()
        self.tm_6=StringVar()
        self.tm_7=StringVar()
        self.tm_8=StringVar()
        self.roolno=StringVar()
        

        

        
        
        #frame Search
        
        self.search_f=Frame(root,bg="white",bd=4,relief=GROOVE)
        self.search_f.place(x=40,y=40,height=750,width=1450)
        
        roll=Label(self.search_f,text="Enter Roll No",font=("times new roman",20,"bold"),bg="white",fg="red")
        roll.grid(padx=30,pady=20,row=0,column=0)
        
        txt_roll=Entry(self.search_f,bd=4,textvariable=self.roolno,relief=GROOVE,font=("arial",15,"bold"))
        txt_roll.grid(padx=30,pady=20,row=0,column=1)
        
        b1=Button(self.search_f,command=self.search_data,text="Search",fg="red",bd=4,relief=GROOVE,width=10,bg="sky blue")
        b1.grid(padx=30,pady=20,row=0,column=2)
        
        b2=Button(self.search_f,command=self.add_result,text="ADD/Update",fg="red",bd=4,relief=GROOVE,width=10,bg="sky blue")
        b2.grid(padx=30,pady=20,row=0,column=3)



        b3=Button(self.search_f,command=self.clear,text="Clear",fg="red",bd=4,relief=GROOVE,width=10,bg="sky blue")
        b3.grid(padx=30,pady=20,row=0,column=4)
        
        b4=Button(self.search_f,command=self.back_btn,text="Back",fg="black",bd=4,relief=GROOVE,width=10,bg="red")
        b4.grid(padx=30,pady=20,row=0,column=5)
        
        b5=Button(self.search_f,command=self.data_fetch,text="Show All",fg="red",bd=4,relief=GROOVE,width=10,bg="sky blue")
        b5.grid(padx=30,pady=20,row=1,column=5)


               
        sub=Label(self.search_f,text="Subject Name",font=("times new roman",20,"bold"),bg="white",fg="red")
        sub.grid(padx=30,pady=20,row=1,column=0)
        
        marks=Label(self.search_f,text="Marks Obtained",font=("times new roman",20,"bold"),bg="white",fg="red")
        marks.grid(padx=30,pady=20,row=1,column=1)
        
        total_marks=Label(self.search_f,text="Total Marks",font=("times new roman",20,"bold"),bg="white",fg="red")
        total_marks.grid(padx=30,pady=20,row=1,column=2)
        
        
        self.e1=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.sub_1,font=("arial",15,"bold")).grid(padx=30,pady=20,row=3,column=0)
        self.e2=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.mo_1,font=("arial",15,"bold")).grid(padx=30,pady=20,row=3,column=1)
        self.e3=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.tm_1,font=("arial",15,"bold")).grid(padx=30,pady=20,row=3,column=2)
        self.e4=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.sub_2,font=("arial",15,"bold")).grid(padx=30,pady=20,row=4,column=0)
        self.e5=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.mo_2,font=("arial",15,"bold")).grid(padx=30,pady=20,row=4,column=1)
        self.e6=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.tm_2,font=("arial",15,"bold")).grid(padx=30,pady=20,row=4,column=2)
        self.e7=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.sub_3,font=("arial",15,"bold")).grid(padx=30,pady=20,row=5,column=0)
        self.e8=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.mo_3,font=("arial",15,"bold")).grid(padx=30,pady=20,row=5,column=1)
        self.e9=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.tm_3,font=("arial",15,"bold")).grid(padx=30,pady=20,row=5,column=2)
        self.e10=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.sub_4,font=("arial",15,"bold")).grid(padx=30,pady=20,row=6,column=0)
        self.e11=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.mo_4,font=("arial",15,"bold")).grid(padx=30,pady=20,row=6,column=1)
        self.e12=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.tm_4,font=("arial",15,"bold")).grid(padx=30,pady=20,row=6,column=2)
        self.e13=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.sub_5,font=("arial",15,"bold")).grid(padx=30,pady=20,row=7,column=0)
        self.e14=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.mo_5,font=("arial",15,"bold")).grid(padx=30,pady=20,row=7,column=1)
        self.e15=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.tm_5,font=("arial",15,"bold")).grid(padx=30,pady=20,row=7,column=2)
        self.e16=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.sub_6,font=("arial",15,"bold")).grid(padx=30,pady=20,row=8,column=0)
        self.e17=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.mo_6,font=("arial",15,"bold")).grid(padx=30,pady=20,row=8,column=1)
        self.e18=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.tm_6,font=("arial",15,"bold")).grid(padx=30,pady=20,row=8,column=2)
        self.e19=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.sub_7,font=("arial",15,"bold")).grid(padx=30,pady=20,row=9,column=0)
        self.e20=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.mo_7,font=("arial",15,"bold")).grid(padx=30,pady=20,row=9,column=1)
        self.e21=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.tm_7,font=("arial",15,"bold")).grid(padx=30,pady=20,row=9,column=2)
        self.e22=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.sub_8,font=("arial",15,"bold")).grid(padx=30,pady=20,row=10,column=0)
        self.e23=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.mo_8,font=("arial",15,"bold")).grid(padx=30,pady=20,row=10,column=1)
        self.e24=Entry(self.search_f,bd=4,relief=GROOVE,textvariable=self.tm_8,font=("arial",15,"bold")).grid(padx=30,pady=20,row=10,column=2)
        




        #table frame   




        table_frame=Frame(self.search_f,bg="white",bd=4,relief=GROOVE)
        table_frame.place(x=900,y=170,height=560,width=500)


        detail_lbl=Label(self.search_f,text="Student Details",font=("times new roman",20,"bold"),bg="white",fg="red")
        detail_lbl.grid(padx=30,pady=20,row=1,column=4)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        self.student_table=ttk.Treeview(table_frame,columns=("roll_no","Name","class","gender","contact","dob","address","std_password","sub1","Mo1","Tm1","sub2","Mo2","Tm2","sub3","Mo3","Tm3","sub4","Mo4","Tm4","sub5","Mo5","Tm5","sub6","Mo6","Tm6","sub7","Mo7","Tm7","sub8","Mo8","Tm8"),xscrollcommand=scroll_x.set)

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
        self.student_table.heading ("std_password",text="Password")

        self.student_table.heading("sub1",text="Sub")
        self.student_table.heading("Mo1",text="MO")
        self.student_table.heading("Tm1",text="TM")
        self.student_table.heading("sub2",text="Sub")
        self.student_table.heading("Mo2",text="MO")
        self.student_table.heading("Tm2",text="TM")
        self.student_table.heading("sub3",text="Sub")
        self.student_table.heading("Mo3",text="MO")
        self.student_table.heading("Tm3",text="TM")
        self.student_table.heading("sub4",text="Sub")
        self.student_table.heading("Mo4",text="MO")
        self.student_table.heading("Tm4",text="TM")
        self.student_table.heading("sub5",text="Sub")
        self.student_table.heading("Mo5",text="MO")
        self.student_table.heading("Tm5",text="TM")
        self.student_table.heading("sub6",text="Sub")
        self.student_table.heading("Mo6",text="MO")
        self.student_table.heading("Tm6",text="TM")
        self.student_table.heading("sub7",text="Sub")
        self.student_table.heading("Mo7",text="MO")
        self.student_table.heading("Tm7",text="TM")
        self.student_table.heading("sub8",text="Sub")
        self.student_table.heading("Mo8",text="MO")
        self.student_table.heading("Tm8",text="TM")
       
       


        self.student_table.column ("gender",width=50)
        self.student_table.column ("contact",width=100)
        self.student_table.column ("dob",width=100)
        self.student_table.column ("address",width=200)
        self.student_table.column ("std_password",width=100)
      

      # showable

        self.student_table.column ("Name",width=100)
        self.student_table.column ("roll_no",width=100)
        self.student_table.column ("class",width=100)
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

        self.data_fetch()
        self.student_table.bind("<ButtonRelease>",self.get_cursor)

    def back_btn(self):
        root.destroy()
        os.system("python admin_portal.py")

        

    def add_result(self):
     
        if self.roolno.get()=="":
            messagebox.showerror("Error","Enter Roll no")
        elif self.roolno.get()!="":
           con=pymysql.connect(host="localhost",user="root",password="root",database="clg")
           cur=con.cursor()
           cur.execute("select * from students where roll_no=%s",self.roolno.get())
           row=cur.fetchone()
           if row==None:
                messagebox.showerror("Error","Student Not Found--- Check the roll_no again ")
           else:
                answer=messagebox.askyesno("Confirm","Are you sure?")
                
                if answer>0:
                    
                
      
                 cur.execute("update students set sub1=%s,om1=%s,tm1=%s,sub2=%s,om2=%s,tm2=%s,sub3=%s,om3=%s,tm3=%s,sub4=%s,om4=%s,tm4=%s,sub5=%s,om5=%s,tm5=%s,sub6=%s,om6=%s,tm6=%s,sub7=%s,om7=%s,tm7=%s,sub8=%s,om8=%s,tm8=%s where roll_no=%s",(
                                                                                                                                                                                                                                                        self.sub_1.get(),
                                                                                                                                                                                                                                                        self.mo_1.get(),
                                                                                                                                                                                                                                                        self.tm_1.get(),
                                                                                                                                                                                                                                                        self.sub_2.get(),
                                                                                                                                                                                                                                                        self.mo_2.get(),
                                                                                                                                                                                                                                                        self.tm_2.get(),
                                                                                                                                                                                                                                                        self.sub_3.get(),
                                                                                                                                                                                                                                                        self.mo_3.get(),
                                                                                                                                                                                                                                                        self.tm_3.get(),
                                                                                                                                                                                                                                                        self.sub_4.get(),
                                                                                                                                                                                                                                                        self.mo_4.get(),
                                                                                                                                                                                                                                                        self.tm_4.get(),
                                                                                                                                                                                                                                                        self.sub_5.get(),
                                                                                                                                                                                                                                                        self.mo_5.get(),
                                                                                                                                                                                                                                                        self.tm_5.get(),
                                                                                                                                                                                                                                                        self.sub_6.get(),
                                                                                                                                                                                                                                                        self.mo_6.get(),
                                                                                                                                                                                                                                                        self.tm_6.get(),
                                                                                                                                                                                                                                                        self.sub_7.get(),
                                                                                                                                                                                                                                                        self.mo_7.get(),
                                                                                                                                                                                                                                                        self.tm_7.get(),
                                                                                                                                                                                                                                                        self.sub_8.get(),
                                                                                                                                                                                                                                                        self.mo_8.get(),
                                                                                                                                                                                                                                                        self.tm_8.get(),
                                                                                                                                                                                                                                                        self.roolno.get()
                                                                                                                                                                                                                                                        ))
                   
                 con.commit()
                 con.close()
                 self.data_fetch()
                 self.clear()
                 messagebox.showinfo("Success","Record added successfully")

    def clear(self):
        self.sub_1.set("")  
        self.sub_2.set("")
        self.sub_3.set("")
        self.sub_4.set("")
        self.sub_5.set("")
        self.sub_6.set("")
        self.sub_7.set("")
        self.sub_8.set("")

        self.mo_1.set("")
        self.mo_2.set("")
        self.mo_3.set("")
        self.mo_4.set("")
        self.mo_5.set("")
        self.mo_6.set("")
        self.mo_7.set("")
        self.mo_8.set("")

        self.tm_1.set("")
        self.tm_2.set("")
        self.tm_3.set("")
        self.tm_4.set("")
        self.tm_5.set("")
        self.tm_6.set("")
        self.tm_7.set("")
        self.tm_8.set("")
        self.roolno.set("")
        
    

    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="root",database="clg")
        cur=con.cursor()
        cur.execute("select * from students where roll_no=%s",self.roolno.get())
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
            
        con.close()

    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        row=content['values']
        self.roolno.set(row[0])
        self.sub_1.set(row[8])  
        self.mo_1.set(row[9])  
        self.tm_1.set(row[10])  
        self.sub_2.set(row[11])  
        self.mo_2.set(row[12])  
        self.tm_2.set(row[13])  
        self.sub_3.set(row[14])  
        self.mo_3.set(row[15])
        self.tm_3.set(row[16])
        self.sub_4.set(row[17])  
        self.mo_4.set(row[18])
        self.tm_4.set(row[19])
        self.sub_5.set(row[20])  
        self.mo_5.set(row[21])
        self.tm_5.set(row[22])
        self.sub_6.set(row[23])  
        self.mo_6.set(row[24])
        self.tm_6.set(row[25])
        self.sub_7.set(row[26])  
        self.mo_7.set(row[27])
        self.tm_7.set(row[28])
        self.sub_8.set(row[29])  
        self.mo_8.set(row[30])
        self.tm_8.set(row[31])


    def data_fetch(self):
        con=pymysql.connect(host="localhost",user="root",password="root",database="clg")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()








root=Tk()
obj=home(root)
root.mainloop()