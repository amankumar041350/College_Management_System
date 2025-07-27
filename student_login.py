import tkinter
from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import pymysql

class home:
    def __init__(self,root) -> None:
        self.root=root
        self.root.title("Sidharth Degree College Nadaun")
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (w,h))
        

        #working    
        def login_function():
            if self.root.txt_pass.get()=="" or self.root.txt_user.get()=="":
                messagebox.showerror("Error","All Fields Are Requried",parent=root)
            else:
             con=pymysql.connect(host="localhost",user="root",password="root",database="clg")
             cur=con.cursor()
             cur.execute("select * from students where roll_no=%s and std_password=%s",(self.root.txt_user.get(),self.root.txt_pass.get()))
             row=cur.fetchone()
             if row==None:
                messagebox.showerror("Error","Wrong ID/Password")
             else:
                messagebox.showinfo("Success","Welcome")
                login()
            

        # bg image
        self.bg=ImageTk.PhotoImage(file="images/bg_1.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)
       


        Frame_login=Frame(root,bg="White")
        Frame_login.place(x=300,y=300,height=440,width=900)




        title=Label(Frame_login,text="Student Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc=Label(Frame_login,text="Student Login Area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)
 
        lbl_user=Label(Frame_login,text="Roll No",font=("Goudy old style",15,"bold"),fg="#d77337",bg="white").place(x=90,y=140)
        self.root.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.root.txt_user.place(x=90,y=170,width=350,height=50)

        lbl_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="#d77337",bg="white").place(x=90,y=220)
        self.root.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray",show="*")
        self.root.txt_pass.place(x=90,y=250,width=350,height=50)

        
        Login_Button=Button(self.root,cursor="hand2",command=login_function,text="Login",fg="black",bg="lightgray",font=("times new roman",20)).place(x=385,y=650,width=180,height=40)
        
        Back_Button=Button(self.root,cursor="hand2",command=back,text="Back",fg="black",bg="lightgray",font=("times new roman",20)).place(x=950,y=650,width=180,height=40)
        
    

def back():
         root.destroy()
         os.system('python main.py')
        


def login():
    root.destroy()
    os.system('python student_portal.py')



 
        








root=Tk()
obj=home(root)
root.mainloop()