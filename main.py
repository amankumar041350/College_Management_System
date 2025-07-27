import tkinter
from tkinter import*    
from PIL import Image,ImageTk
from tkinter import messagebox
import os



class home:
    def __init__(self,root):


        
        self.root=root
        self.root.title("Sidharth Degree College Nadaun")

        """ self.root.geometry("1500x800+0+0") """
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (w,h))

        
            

        # bg image
        self.bg=ImageTk.PhotoImage(file="images/main.jpg")
        self.background=Label(self.root,image=self.bg)
        self.background.place(x=0,y=0,relheight=1,relwidth=1)

        
        
        b1=Button(root,cursor="hand2",command=self.student_login,text="Student Login",fg="red",bg="lightgray",font=("times new roman",25))
        b1.place(x=100,y=350,width=350,height=60)
        
        b2=Button(root,command=self.admin,cursor="hand2",text="Admin Login",fg="red",bg="lightgray",font=("times new roman",25))
        b2.place(x=100,y=450,width=350,height=60)
        
        

        
        
    

    def admin(self):
         root.destroy()
         os.system('python admin_login.py')

    def student_login(self):
         root.destroy()
         os.system('python student_login.py')
    




root=Tk()
obj=home(root)
root.mainloop()