import tkinter
from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import os
class student:
    def __init__(self,root) -> None:
        self.root=root
        self.root.title("Sidharth Degree College Nadaun")
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (w,h))

# bg image
        self.bg=ImageTk.PhotoImage(file="images/bg2.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)


        b1=Button(root,command=student_management,cursor="hand2",text="View/Edit Student",fg="red",bg="lightgray",font=("times new roman",25)).place(x=600,y=75,width=350,height=60)
        b2=Button(root,cursor="hand2",command=employee_management,text="View/Edit Staff",fg="red",bg="lightgray",font=("times new roman",25)).place(x=600,y=175,width=350,height=60)
        b3=Button(root,cursor="hand2",command=edit_result,text="View/Edit  Result",fg="red",bg="lightgray",font=("times new roman",25)).place(x=600,y=275,width=350,height=60)
        b4=Button(root,cursor="hand2",command=forgot_pass,text="Change Password",fg="red",bg="lightgray",font=("times new roman",25)).place(x=600,y=375,width=350,height=60)
        b5=Button(root,cursor="hand2",command=back,text="back",fg="black",bg="lightgray",font=("times new roman",25)).place(x=1100,y=675,width=350,height=60)
        b6=Button(root,cursor="hand2",command=home,text="Home",fg="black",bg="lightgray",font=("times new roman",25)).place(x=100,y=675,width=350,height=60)

def home():
         root.destroy()
         os.system('python main.py')
        
def back():
         root.destroy()
         os.system('python admin_login.py')

def student_management():
         root.destroy()
         os.system('python edit_student.py')

def employee_management():
         root.destroy()
         os.system('python edit_staff.py')

def forgot_pass():
         root.destroy()
         os.system('python forgot_pass.py')

def edit_result():
         root.destroy()
         os.system('python edit_result.py')
        
        





root=Tk()
obj=student(root)
root.mainloop()