from tkinter import *
import hashlib





def save_info():
  mail = Mail.get()
  password = Password.get()
  password = password.encode(encoding='UTF-8',errors='strict')
  password = hashlib.sha256(password)
  password = password.hexdigest()
  file = open("data.txt", "w")
  file.write("Email: "+ mail + "   ")
  file.write("encryption: " + password + "    ")
  print(" your info has been registered successfully")
  file.close()

screen = Tk()
screen.geometry("500x500")
screen.title("Python Form")
heading = Label(text = "encryption", bg = "grey", fg = "black", width = "500", height = "3")
heading.pack()

mail_text = Label(text="Mail")
password_text = Label(text="Password")
mail_text.place(x = 15, y = 80)
password_text.place(x = 15, y = 160)

Mail = Entry(width = "30")
Password = Entry(width = "30")


Mail.place(x = 20, y = 100)
Password.place(x = 20, y = 180)


register = Button(screen,text = "Register", width = "30", height = "2", command = save_info, bg = "grey")
register.place(x = 15, y = 290)

screen.mainloop()
