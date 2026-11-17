from tkinter import *

window = Tk()
window.geometry("220x300")
window.title("My GUI")

icon = PhotoImage(file='instagram.png')
window.iconphoto(True, icon)
window.config(background="#dc8af2", cursor="heart")

window.mainloop()