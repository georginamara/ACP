from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from afterlog import open_after_login


def check_login():
    username=user.get()
    password=code.get()

    if username == 'admin' and password == '1234':
        root.destroy()
        open_after_login()
    else:
        messagebox.showerror('Login Failed', 'Invalid credentials!')

root = Tk()
root.title('Login')
root.geometry('1050x650+0+0')
root.configure(bg='#fff')
root.resizable(False, False)


img_path = r"C:\Users\Lenovo\Desktop\eBarangay Certificates\logo.png"
img = Image.open(img_path)
img = img.resize((450, 450))
img = ImageTk.PhotoImage(img)
Label(root, image=img, bg='white').place(x=25, y=0)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Log In', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)


def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name==' ':
        user.insert(0,'Username')

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>', on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=code.get()
    if name==' ':
        code.insert(0, 'Password')


code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


Button(frame,width=39,pady=7,text='Log In',bg='#57a1f8',fg='white',border=0,command=check_login).place(x=35,y=204)
label = Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up = Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg="#57a1f8")
sign_up.place(x=215,y=270)



root.mainloop()
