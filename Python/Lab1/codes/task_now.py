import tkinter as tk

length = 0

def demo():
    global length
    ac = entry.get()
    length = len(ac)
    label.config(text=f"Urt n: {length}")

def dele():
    entry.delete(0, tk.END)

window = tk.Tk()
window.title('My self-test')
window.geometry("350x400")

icon = tk.PhotoImage(file='instagram.png')
window.iconphoto(True, icon)

window.config(background="#82cdff")

entry = tk.Entry()
entry.config(font=('Ink Free', 30), width=15, bg="#d4d2a9")
entry.pack()
entry.insert(0, "Hello World!")
button = tk.Button(window, text="Click me!", command=demo)
button.config(font=('Arial', 10, 'bold'),
              activebackground="#1f70a7",
              activeforeground="#fdf03c",
              bg="#d3c7ff",
              fg="#ff8b68")

button.pack()

del_button = tk.Button(window, text="delete", command=dele)
del_button.pack(side='left')


label = tk.Label(window, text=f"Urt n: {length}")
label.config(font=('Times New Roman', 16, "bold"), relief="raised", bd=20)
label.pack()


window.mainloop()