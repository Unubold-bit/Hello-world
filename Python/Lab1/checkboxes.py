import tkinter as tk

def show():
    if x.get() == 1 and y.get() == 1:
        label.config(text='I love programming')
    else:
        label.config(text='I love one of python or java whatsoever..')        
window = tk.Tk()

x = tk.IntVar()
y = tk.IntVar()
checkbox = tk.Checkbutton(window, text='Python', variable=x, onvalue=1, offvalue=0, command=show)
checkbox.pack()

checkboxy = tk.Checkbutton(window, text='jave', variable=y, onvalue=1, offvalue=0, command=show)
checkboxy.pack()

label = tk.Label(window, text='hi')
label.pack()
window.mainloop()