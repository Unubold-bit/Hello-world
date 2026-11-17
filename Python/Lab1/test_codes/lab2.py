import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

root.resizable(False, False)
display = tk.Entry(root)
display.grid(row=0, column=0, columnspan=4)

cancel_btn = tk.Button(root, text="⌫")
cancel_btn.grid(row=1, column=0)

clean_btn = tk.Button(root, text="AC")
clean_btn.grid(row=1, column=1)

per_btn = tk.Button(root, text="%")
per_btn.grid(row=1, column=2)

div_btn = tk.Button(root, text="/")
div_btn.grid(row=1, column=3)

seven_btn = tk.Button(root, text="7")
seven_btn.grid(row=2, column=0)

eight_btn = tk.Button(root, text="8")
eight_btn.grid(row=2, column=1)

nine_btn = tk.Button(root, text="9")
nine_btn.grid(row=2, column=2)

mult_btn = tk.Button(root, text="x")
mult_btn.grid(row=2, column=3)






root.mainloop()