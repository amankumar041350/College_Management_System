import tkinter
from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import ttk
import pymysql
import os

class home:
    def __init__(self,root) -> None:
        self.root=root
        self.root.title("Sidharth Degree College Nadaun")
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (w,h))
        

       
        # bg image
        self.bg=ImageTk.PhotoImage(file="images/bg2.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)
        title=Label(self.root,text="Staff Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)



        # sql varriables

        self.id_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.txt_adress_var=StringVar()
        self.search_by=StringVar()
        self.txt_search=StringVar()
        

        #  manage frame

        manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        manage_frame.place(x=20,y=100,width=450,height=700)

        m_title=Label(manage_frame,text="Manage Staff",font=("times new roman",30,"bold"),bg="White",fg="red")
        m_title.grid(row=0,columnspan=2,pady=20)

        id=Label(manage_frame,text="Staff ID",font=("times new roman",20,"bold"),bg="White",fg="red")
        id.grid(row=1,column=0,pady=10,padx=20,sticky="w")


        txt_id=Entry(manage_frame,textvariable=self.id_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_id.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        name=Label(manage_frame,text="Name",font=("times new roman",20,"bold"),bg="White",fg="red")
        name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(manage_frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        email=Label(manage_frame,text="Email",font=("times new roman",20,"bold"),bg="White",fg="red")
        email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

    

        email=Entry(manage_frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        gender=Label(manage_frame,text="Gender",font=("times new roman",20,"bold"),bg="White",fg="red")
        gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(manage_frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state="readonly")
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        contact=Label(manage_frame,text="Contact",font=("times new roman",20,"bold"),bg="White",fg="red")
        contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_contact=Entry(manage_frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        dob=Label(manage_frame,text="D.O.B",font=("times new roman",20,"bold"),bg="White",fg="red")
        dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_dob=Entry(manage_frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        adress=Label(manage_frame,text="Address",font=("times new roman",20,"bold"),bg="White",fg="red")
        adress.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        txt_adress=Entry(manage_frame,textvariable=self.txt_adress_var,width=29,font=("",10),bd=5,relief=GROOVE)
        txt_adress.grid(row=7,column=1,pady=10,padx=20,sticky="w")
        

        #button frame

        btn_frame=Frame(manage_frame,bd=4,relief=RIDGE,bg="#F5F5DC")
        btn_frame.place(x=10,y=600,width=430)
        add_btn=Button(btn_frame,command=self.add_employee,text="Add",width=10,relief=GROOVE).grid(row=0,column=0,padx=10,pady=10)
        update=Button(btn_frame,command=self.data_update,text="Update",width=10,relief=GROOVE).grid(row=0,column=1,padx=13,pady=10)
        delete=Button(btn_frame,command=self.delete_data,text="Delete",width=10,relief=GROOVE).grid(row=0,column=2,padx=13,pady=10)
        clear=Button(btn_frame,command=self.clear,text="Clear",width=10,relief=GROOVE).grid(row=0,column=3,padx=13,pady=10)
    



        #  detail frame

        detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        detail_frame.place(x=500,y=100,width=1000,height=700)

        lbl_search=Label(detail_frame,text="Search By",font=("times new roman",20,"bold"),bg="White",fg="red")
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")


        combo_search=ttk.Combobox(detail_frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state="readonly")
        combo_search['values']=("ID","Name","Contact","Email")
        combo_search.grid(row=0,column=1,pady=10,padx=20,sticky="w")

        txt_search=Entry(detail_frame,textvariable=self.txt_search,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        srch_btn=Button(detail_frame,command=self.search_data,text="Search",width=10,pady=5,relief=GROOVE).grid(row=0,column=3,pady=10,padx=10)
        clear_btn=Button(detail_frame,command=self.clear1,text="Clear",width=10,pady=5,relief=GROOVE).grid(row=0,column=5,pady=10,padx=10)
        show_btn=Button(detail_frame,command=self.data_fetch,text="Show All",width=10,pady=5,relief=GROOVE).grid(row=0,column=4,pady=10,padx=10)
        back_btn=Button(detail_frame,command=self.back,text="Back",font=("times new roman",10,"bold"),width=10,pady=5,relief=GROOVE,bg="red").grid(row=0,column=6,pady=10,padx=10)



        ### table frame


        table_frame=Frame(detail_frame,bd=4,relief=RIDGE,bg="white")
        table_frame.place(x=10,y=70,width=950,height=580)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("id","Name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("id",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("email",text="email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("dob",text="D.O.B")
        self.student_table.heading("address",text="Address")
        self.student_table.column ("id",width=100)
        self.student_table.column ("Name",width=100)
        self.student_table.column ("email",width=100)
        self.student_table.column ("gender",width=100)
        self.student_table.column ("contact",width=100)
        self.student_table.column ("dob",width=100)
        self.student_table.column ("address",width=200)

        self.student_table['show']='headings'
        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.data_fetch()
    def add_employee(self):
        if self.id_var.get()=="" or self.email_var.get()=="" or self.name_var.get()=="" or self.email_var.get()==""or self.gender_var.get()==""or self.contact_var.get()==""or self.dob_var.get()==""or self.txt_adress_var.get()=="":
            messagebox.showerror("Error","All Fields are Requried")

        else:
            con=pymysql.connect(host="localhost",user="root",password="root",database="clg")
            cur=con.cursor()
            cur.execute("select * from employee where id=%s",self.id_var.get())
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","ID Already Exist,--try with another ID.. ")
            else:
                answer=messagebox.askyesno("Confirm","Are you sure?")
                
                if answer>0:
                 con=pymysql.connect(host="localhost",user="root",password="root",database="clg")
                 cur=con.cursor()
                 cur.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s)",(self.id_var.get(),
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.txt_adress_var.get()
                                                                            ))
                 con.commit()
                 self.data_fetch()
                 self.clear()
                 con.close()
                 messagebox.showinfo("Success","Record Added")
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="root",database="clg")
        cur=con.cursor()
        cur.execute("select * from employee")
    def data_fetch(self):
        con=pymysql.connect(host="localhost",user="root",password="root",database="clg")
        cur=con.cursor()
        cur.execute("select * from employee")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.id_var.set("")  
        self.name_var.set("")  
        self.email_var.set("")  
        self.gender_var.set("")  
        self.contact_var.set("")  
        self.dob_var.set("")  
        self.txt_adress_var.set("")  
    

    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        row=content['values']
        self.id_var.set(row[0])  
        self.name_var.set(row[1])  
        self.email_var.set(row[2])  
        self.gender_var.set(row[3])  
        self.contact_var.set(row[4])  
        self.dob_var.set(row[5])  
        self.txt_adress_var.set(row[6])  
    
    def data_update(self):
          
          if self.id_var.get()=="" or self.email_var.get()=="" or self.name_var.get()=="" or self.email_var.get()==""or self.gender_var.get()==""or self.contact_var.get()==""or self.dob_var.get()==""or self.txt_adress_var.get()=="":
            
            messagebox.showerror("error","All Fields Are Requried")
          elif self.id_var.get()!="":
            con=pymysql.connect(host="localhost",user="root",password="root",database="clg")
            cur=con.cursor()
            cur.execute("select * from employee where id=%s",self.id_var.get())
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","No Member Found ")

            else:
                answer=messagebox.askyesno("Confirm","Are you sure?")
                
                if answer>0:
            
            
                    cur.execute("update employee set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where id=%s",(
                                                                                    
                                                                                    self.name_var.get(),
                                                                                    self.email_var.get(),
                                                                                    self.gender_var.get(),
                                                                                    self.contact_var.get(),
                                                                                    self.dob_var.get(),
                                                                                    self.txt_adress_var.get(),
                                                                                    self.id_var.get()
                                                                                    ))
                    con.commit()
                    self.data_fetch()
                    self.clear()
                    con.close()
                    messagebox.showinfo("Success","Record Updated ")


    def delete_data(self):
        
        answer=messagebox.askyesno("Confirm","Are you sure?")
                
        if answer>0:
        
                con=pymysql.connect(host="localhost",user="root",password="root",database="clg")
                cur=con.cursor()
                cur.execute("delete from employee where id=%s",self.id_var.get())
                con.commit()
                self.data_fetch()
                messagebox.showinfo("Success","Record Deleted Succussfully")
                self.clear()
                self.clear()

    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="root",database="clg")
        cur=con.cursor()
        cur.execute("select * from employee where "+str(self.search_by.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear1(self):
        self.search_by.set("")  
        self.txt_search.set("")  

    def back(self):
        root.destroy()
        os.system("python admin_portal.py")

         

        




        
       



root=Tk()
obj=home(root)
root.mainloop()