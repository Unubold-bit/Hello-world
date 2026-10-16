import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

frame = tk.Frame(root)
frame.grid(row=0, column=0)

display = tk.Entry(frame)
display.grid(row=0, column=0, columnspan=2)

cancel_btn = tk.Button(frame, text="X")
cancel_btn.grid(row=0, column=0)



root.mainloop()