from tkinter import *

window = Tk()
window.title("Learning labels")

photo = PhotoImage(file='instagram.png')

window.iconphoto(True, photo)


label = Label(window,
               text="Hello",
                 font=('Arial', 40, 'bold'), 
                 fg='#00ff00',
                   bg='black', relief=RAISED,
                     bd=10, 
                     padx=20, 
                     pady=20, 
                     image=photo,
                     compound='bottom')
#label.place(x=100, y=100)
label.pack()


window.mainloop()