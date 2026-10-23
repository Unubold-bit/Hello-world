import tkinter as tk

BG="white"
NAME = "student"
PASSWORD = f"123456"

def check():
    n = name_entry.get()
    p = password_entry.get()
    if n == NAME and p == PASSWORD:
        dashboard()
        return
    else:
        gg()
        sub_label = tk.Label(frame, text="Name or password is incorrect, try again!", font=("Times new roman", 13), anchor="e", fg="#000000", bg=BG)
        sub_label.grid(row=3, column=1, sticky="w", padx=(15, 0), pady=(5, 0))

        name_entry.config(bg="#ffd3d3")
        password_entry.config(bg="#ffd3d3")
        name_entry.focus_set()

def gg():
    name_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


def dashboard():
    ss_f = tk.Frame(root)
    ss_f.config(bg=BG)
    ss_f.grid(row=1, column=1, columnspan=2, sticky="nsew", pady=30, padx=30)

    hlabel = tk.Label(ss_f, text="DASHBOARD", font=("Times new roman", 20, "bold"), fg="#000853", bg=BG)
    hlabel.grid(row=2, column=1, padx=(10, 0), pady=(15, 0), sticky="w")

    sub_label = tk.Label(ss_f, text="Hello student!", font=("Times new roman", 16), anchor="e", fg="#000000", bg=BG)
    sub_label.grid(row=3, column=1, sticky="w", padx=(15, 0), pady=(10, 0))

    name_label = tk.Label(ss_f, text="You entered successfully!", font=("Times new roman", 10), anchor="e", fg="#009933", bg=BG)
    name_label.grid(row=4, column=1, sticky="w", padx=(15, 0), pady=(5, 0))

    o_label = tk.Label(ss_f, text="Students", font=("Times new roman", 13), anchor="center", fg="#09005E", bg="#cbccff", width=28)
    o_label.grid(row=5, column=1, sticky="ew", padx=(15, 0), pady=(15, 5))

    s_label = tk.Label(ss_f, text="Subjects", font=("Times new roman", 13), anchor="center", fg="#09005E", bg="#cbccff", width=28)
    s_label.grid(row=6, column=1, sticky="ew", padx=(15, 0), pady=(5, 0))

    l_button = tk.Button(ss_f, 
                   text="Log out", 
                   bg="#1f87ff", 
                   fg=BG, 
                   width=30, 
                   font=("Times new roman", 13),
                   command=show_d
                   )
    l_button.grid(row=9, 
                  column=1, padx=(15, 0), pady=(30, 0))

def showy():
    if x.get() == 1:
        password_entry.config(show="")
        return
    else:
        password_entry.config(show="*")
        return

def show_d():
    frame.tkraise()
    gg()

root = tk.Tk()
root.geometry('400x500')

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

frame = tk.Frame(root)
frame.config(bg=BG)
frame.grid(row=1, column=1, columnspan=2, sticky="nsew", pady=30, padx=30)

label = tk.Label(frame, text="STUDENT SYSTEM", font=("Times new roman", 20, "bold"), fg="#000853", bg=BG)
label.grid(row=2, column=1, padx=(10, 0), pady=(15, 0))

sub_label = tk.Label(frame, text="Enter you info", font=("Times new roman", 13), anchor="e", fg="#000000", bg=BG)
sub_label.grid(row=3, column=1, sticky="w", padx=(15, 0))

name_label = tk.Label(frame, text="Name", font=("Times new roman", 13), anchor="e", fg="#000000", bg=BG)
name_label.grid(row=4, column=1, sticky="w", padx=(15, 0), pady=(5, 0))

name_entry = tk.Entry(frame, width=40)
name_entry.grid(row=5, column=1, padx=(15, 0), pady=(5, 0))

password_label = tk.Label(frame, text="Password", font=("Times new roman", 13), anchor="e", fg="#000000", bg=BG)
password_label.grid(row=6, column=1, sticky="w", padx=(15, 0), pady=(5, 0))

password_entry = tk.Entry(frame, width=40, show="*")
password_entry.grid(row=7, column=1, padx=(15, 0), pady=(5, 0))

x = tk.IntVar(value=0)

vision = tk.Checkbutton(frame,
                        text="Show password",
                        variable=x,
                        onvalue=1,
                        offvalue=0,
                        command=showy
                        )
vision.grid(row=8, column=1, padx=(15, 0),  pady=(15, 0), sticky="w")

button = tk.Button(frame, 
                text="Log in", 
                bg="#1f87ff", 
                fg=BG, 
                width=30, 
                font=("Times new roman", 13),
                command=check).grid(row=9, 
                column=1, padx=(15, 0), pady=(15, 0))

aside = tk.Label(frame, text="Сургалтын demo систем", bg=BG, fg="#dddddd", font=("Times, new roman", 10)).grid(row=10, column=1,  padx=(24, 0), pady=(5, 0))
root.mainloop()


