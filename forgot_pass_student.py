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


        

        def login_function():
            
            if self.txt_1.get()=="" or self.txt_2.get()=="" or self.txt_3.get()=="":
                messagebox.showerror("Error","All Fields Are Requried")
                
            else:
             con=pymysql.connect(host="localhost",user="root",password="root",database="clg")
             cur=con.cursor()
             cur.execute("select * from students where std_password=%s",self.txt_1.get())
             row=cur.fetchone()
             if row==None:
                messagebox.showerror("Error","wrong Current Password ")
             elif self.txt_2.get()!= self.txt_3.get():
                messagebox.showerror("Error","New password and Confirm Password should be same")
             else:
                 answer=messagebox.askyesno("Confirm","Are you sure?")
                
                 if answer>0:

                        cur.execute("update students set std_password=%s where std_password=%s",(
                                                                                        
                                                                                        self.txt_3.get(),
                                                                                        self.txt_1.get()
                                                                                        ))


                    
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success","Password Changed Successfully ") 
                        root.destroy()
                        os.system("python student_portal.py")
                        
                    
            
    
                        
        

       
        # bg image
        self.bg=ImageTk.PhotoImage(file="images/bg2.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)
        

        f1=Frame(self.root,bd=4,relief=GROOVE,bg="white")
        f1.place(x=450,y=100,height=600,width=600)

        lbl_1=Label(f1,text="Current password",bg="white",fg="red",font=("times new roman",20,"bold"))
        lbl_1.place(x=20,y=40)
        
        self.txt_1=Entry(f1,font=("times new roman",15),bg="#E0EEEE",bd=4,relief=GROOVE)
        self.txt_1.place(x=330,y=40)

        lbl_2=Label(f1,text="New password",bg="white",fg="red",font=("times new roman",20,"bold"))
        lbl_2.place(x=20,y=140)

        self.txt_2=Entry(f1,show="*",font=("times new roman",15),bg="#E0EEEE",bd=4,relief=GROOVE)
        self.txt_2.place(x=330,y=140)

        lbl_3=Label(f1,text="Confirm password",bg="white",fg="red",font=("times new roman",20,"bold"))
        lbl_3.place(x=20,y=240)

        self.txt_3=Entry(f1,show="*",font=("times new roman",15),bg="#E0EEEE",bd=4,relief=GROOVE)
        self.txt_3.place(x=330,y=240)


        #button

       

        b2=Button(f1,text="Change Password",command=login_function,font=("times new roman",15,"bold"),fg="black",bg="light gray",bd=4,relief=GROOVE)
        b2.place(x=200,y=340)

        b3=Button(f1,text="Back",width=10,command=back,font=("times new roman",15,"bold"),fg="black",bg="light gray",bd=4,relief=GROOVE)
        b3.place(x=20,y=500)

        b4=Button(f1,text="Close",command=root.destroy,width=10,font=("times new roman",15,"bold"),fg="black",bg="light gray",bd=4,relief=GROOVE)
        b4.place(x=420,y=500)

def back():
    root.destroy()
    os.system('python student_portal.py')


   



    
    





root=Tk()
obj=home(root)
root.mainloop()