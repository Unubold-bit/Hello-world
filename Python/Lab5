import tkinter as tk;
from tkinter import messagebox, ttk

# Initialize root window
root = tk.Tk()
root.geometry("300x400")
root.config(bg="#BAE9FF")
root.title("Student System")
root.resizable(False, False)

# Configure a frame inside root
st_frame = tk.Frame(root)
st_frame.grid(row=0, column=0)
st_frame.config(bg="#F5F2F2")

main_label = tk.Label(st_frame, text="STUDENT SYSTEM", font=("Arial", 20, "bold"), anchor="e")
main_label.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10)
oo = tk.Label(st_frame, text="Нэвтрэх мэдээллээ оруулна уу?")
oo.grid(row=1, column=0)

name = tk.Frame(st_frame).grid(row=3, column=0)
label = tk.Label(name, text="Хэрэглэгчийн нэр")
label.grid(row=4, column=0)

ner = tk.Entry(name).grid(row=5, column=0)

label = tk.Label(name, text="Нууц үг")
label.grid(row=6, column=0)

ner = tk.Entry(name).grid(row=7, column=0)

button = tk.Checkbutton(name, text="Нууц үг харуулах", variable="").grid(row=8, column=0)

last_button = tk.Button(name, text="Нэвтрэх", anchor="center", relief="flat", bg="#3895ff").grid(row=9, column=0)
# Start the application loop
root.mainloop()



