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



      
        b2=Button(root,cursor="hand2",command=details,text="My Details",fg="red",bg="lightgray",font=("times new roman",25)).place(x=600,y=175,width=350,height=60)
        b3=Button(root,cursor="hand2",command=result,text="Results",fg="red",bg="lightgray",font=("times new roman",25)).place(x=600,y=275,width=350,height=60)
        b4=Button(root,cursor="hand2",command=change_pass,text="Change Password",fg="red",bg="lightgray",font=("times new roman",25)).place(x=600,y=375,width=350,height=60)
        b5=Button(root,cursor="hand2",command=back,text="back",fg="black",bg="lightgray",font=("times new roman",25)).place(x=1100,y=675,width=350,height=60)
        b6=Button(root,cursor="hand2",command=home,text="Home",fg="black",bg="lightgray",font=("times new roman",25)).place(x=100,y=675,width=350,height=60)

def home():
         root.destroy()
         os.system('python main.py')
        
def back():
         root.destroy()
         os.system('python student_login.py')

def change_pass():
         root.destroy()
         os.system('python forgot_pass_student.py')

def details():
         root.destroy()
         os.system('python student_details.py')


def result():
         root.destroy()
         os.system('python student_result.py')







root=Tk()
obj=student(root)
root.mainloop()