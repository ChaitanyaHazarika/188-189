from tkinter import *
from firebase import firebase
from tkinter import messagebox
import hashlib

firebase= firebase.FirebaseApplication('https://python-d8348-default-rtdb.firebaseio.com/', None)

r_window= Tk()
r_window.geometry("400x400")

r_window.config(bg= "black")

loginusernameentry= ''
loginpasswordentry= ''

def login():
    global loginusernameentry
    global loginpasswordentry

    username= loginusernameentry.get()
    password= loginpasswordentry.get()

    encryptedpass= hashlib.md5(password.encode())
    hexapass= encryptedpass.hexdigest()

    getpass= firebase.get("/", username)
    print(hexapass)

    if getpass != None :
        if getpass == hexapass:
            messagebox.showinfo("Info", "Succesfull Login")
        else:
            messagebox.showinfo("Error", "CHECK UR PASS DUMBOO")

    else:
        messagebox.showinfo("error", "YOU ARE NOT REGISTEREDD DDUDDEEEE")

def register():
     
    password= passwordentry.get() 
    username= usernameentry.get()

    encryptedpass= hashlib.md5(password.encode())
    hexpassword= encryptedpass.hexdigest()

    print(hexpassword)
    put_data= firebase.put("/", username, hexpassword) 
    messagebox.showinfo("Info", "Successfully registered")
def loginwindow():
    global loginpasswordentry
    global loginusernameentry

    r_window.destroy()

    lwindow= Tk()
    lwindow.geometry("400x400")
    lwindow.config(bg= "blue")


    loginheadinglabel= Label(lwindow, text="Login")
    loginheadinglabel.place(relx= 0.5, rely= 0.2, anchor=CENTER)

    loginuserlabel= Label(lwindow, text="Username: ")
    loginuserlabel.place(relx= 0.3, rely= 0.4, anchor=CENTER)
    
    loginusernameentry= Entry(lwindow)
    loginusernameentry.place(relx= 0.6, rely=0.4, anchor=CENTER)

    loginpasswordentry= Entry(lwindow)
    loginpasswordentry.place(relx= 0.6, rely= 0.5, anchor= CENTER)

    labelp= Label(lwindow, text="Pass:")
    labelp.place(relx= 0.3, rely= 0.5, anchor=CENTER)

    btn= Button(lwindow,text="Login", bg= "lightblue", fg= "white", command=login, relief=FLAT)
    btn.place(relx= 0.5, rely= 0.65, anchor=CENTER)

    lwindow.mainloop()
hlabel= Label(r_window, text="register")
hlabel.place(relx= 0.5, rely= 0.2, ancho=CENTER)    

userlabel= Label(r_window, text="Username: ")
userlabel.place(relx= 0.3, rely= 0.4, anchor=CENTER)

usernameentry= Entry(r_window)
usernameentry.place(relx= 0.6, rely= 0.4, anchor=CENTER)

passlabel= Label(r_window, text="Password: ")
passlabel.place(relx= 0.3, rely= 0.5, anchor=CENTER)

passwordentry= Entry(r_window)
passwordentry.place(relx= 0.6, rely= 0.5, anchor=CENTER)

btn1= Button(r_window, text="SignUp", bg= "grey", fg="white", relief=FLAT, command=register)
btn1.place(relx=0.5, rely= 0.7, anchor=CENTER)

btn2= Button(r_window, text="Login", relief=FLAT, bg= "grey", fg="white", command=loginwindow)
btn2.place(relx= 0.9, rely= 0.06, anchor=CENTER)
r_window.mainloop()

