import tkinter as tk


def submit():
    username = entry.get()
    print(f"Hello '{username}'?")


def delete():
    entry.delete(0, tk.END) # deletes the line of text

def backspace():
    entry.delete(len(entry.get())-1, tk.END) # delets the last character of the line
window = tk.Tk()

submit = tk.Button(window, text='submit', command=submit)
submit.pack(side='right')

delete = tk.Button(window, text='delete', command=delete)
delete.pack(side='right')

backspace = tk.Button(window, text='backspace', command=backspace)
backspace.pack(side='right')

entry = tk.Entry()
entry.config(font=("Ink Free", 50))
entry.config(bg="#AAFF22")
entry.config(fg="#4FB9FF")
entry.insert(0, "Bat")
#entry.config(state='disabled')
entry.config(width=10)
#entry.config(show='*')
entry.pack()
window.mainloop()