import tkinter as tk

BG = "white"
NAME = "student"
PASSWORD = "123456"

# Global reference to keep track of the error message label so it can be cleared/reset
error_label = None


def check():
    global error_label
    n = name_entry.get()
    p = password_entry.get()

    if n == NAME and p == PASSWORD:
        # Clear any existing error messages before switching
        if error_label:
            error_label.destroy()
            error_label = None
        # Reset entry background colors
        name_entry.config(bg="white")
        password_entry.config(bg="white")

        # Hide login screen and open dashboard
        frame.pack_forget()
        dashboard()
    else:
        gg()
        # Prevent compounding duplicate error labels on multiple failed attempts
        if error_label:
            error_label.destroy()

        error_label = tk.Label(
            frame,
            text="Name or password is incorrect, try again!",
            font=("Times new roman", 11),
            anchor="e",
            fg="red",
            bg=BG,
        )
        error_label.grid(row=3, column=1, sticky="w", padx=(15, 0), pady=(5, 0))

        name_entry.config(bg="#ffd3d3")
        password_entry.config(bg="#ffd3d3")
        name_entry.focus_set()


def gg():
    name_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


def dashboard():
    global ss_f
    ss_f = tk.Frame(root)
    ss_f.config(bg=BG)
    # Changed from .grid() to .pack() to match root container rules
    ss_f.pack(fill="both", expand=True, pady=30, padx=30)

    hlabel = tk.Label(
        ss_f,
        text="DASHBOARD",
        font=("Times new roman", 20, "bold"),
        fg="#000853",
        bg=BG,
    )
    hlabel.grid(row=2, column=1, padx=(10, 0), pady=(15, 0), sticky="w")

    sub_label = tk.Label(
        ss_f,
        text="Hello student!",
        font=("Times new roman", 16),
        anchor="e",
        fg="#000000",
        bg=BG,
    )
    sub_label.grid(row=3, column=1, sticky="w", padx=(15, 0), pady=(10, 0))

    name_label = tk.Label(
        ss_f,
        text="You entered successfully!",
        font=("Times new roman", 10),
        anchor="e",
        fg="#009933",
        bg=BG,
    )
    name_label.grid(row=4, column=1, sticky="w", padx=(15, 0), pady=(5, 0))

    o_label = tk.Label(
        ss_f,
        text="Students",
        font=("Times new roman", 13),
        anchor="center",
        fg="#09005E",
        bg="#cbccff",
        width=28,
    )
    o_label.grid(row=5, column=1, sticky="ew", padx=(15, 0), pady=(15, 5))

    s_label = tk.Label(
        ss_f,
        text="Subjects",
        font=("Times new roman", 13),
        anchor="center",
        fg="#09005E",
        bg="#cbccff",
        width=28,
    )
    s_label.grid(row=6, column=1, sticky="ew", padx=(15, 0), pady=(5, 0))

    l_button = tk.Button(
        ss_f,
        text="Log out",
        bg="#1f87ff",
        fg=BG,
        width=30,
        font=("Times new roman", 13),
        command=logout,
    )
    l_button.grid(row=9, column=1, padx=(15, 0), pady=(30, 0))


def showy():
    if x.get() == 1:
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


def logout():
    # Hide the dashboard frame and destroy it from memory
    ss_f.pack_forget()
    ss_f.destroy()

    # Re-display the login page frame using .pack()
    frame.pack(fill="both", expand=True, pady=30, padx=30)
    gg()


root = tk.Tk()
root.geometry("400x500")
root.overrideredirect(True)

# Custom title bar (uses pack)
title_bar = tk.Frame(root, bg="#2563eb", height=35)
title_bar.pack(fill="x")

title_label = tk.Label(
    title_bar,
    text="Student System",
    bg="#2563eb",
    fg="white",
    font=("Arial", 11, "bold"),
)
title_label.pack(side="left", padx=10)

close_button = tk.Button(
    title_bar, text="X", bg="#2563eb", fg="white", bd=0, command=root.destroy
)
close_button.pack(side="right", padx=8)


# Window dragging mechanics
def start_move(event):
    root.x = event.x
    root.y = event.y


def move_window(event):
    x_coord = root.winfo_pointerx() - root.x
    y_coord = root.winfo_pointery() - root.y
    root.geometry(f"+{x_coord}+{y_coord}")


title_bar.bind("<Button-1>", start_move)
title_bar.bind("<B1-Motion>", move_window)
title_label.bind("<Button-1>", start_move)
title_label.bind("<B1-Motion>", move_window)

# Login Frame Setup (Changed to .pack to align with title_bar layout manager rules)
frame = tk.Frame(root)
frame.config(bg=BG)
frame.pack(fill="both", expand=True, pady=30, padx=30)

label = tk.Label(
    frame,
    text="STUDENT SYSTEM",
    font=("Times new roman", 20, "bold"),
    fg="#000853",
    bg=BG,
)
label.grid(row=2, column=1, padx=(10, 0), pady=(15, 0))

sub_label = tk.Label(
    frame, text="Enter your info", font=("Times new roman", 13), anchor="e", fg="#000000", bg=BG
)
sub_label.grid(row=3, column=1, sticky="w", padx=(15, 0))

name_label = tk.Label(
    frame, text="Name", font=("Times new roman", 13), anchor="e", fg="#000000", bg=BG
)
name_label.grid(row=4, column=1, sticky="w", padx=(15, 0), pady=(5, 0))

name_entry = tk.Entry(frame, width=40)
name_entry.grid(row=5, column=1, padx=(15, 0), pady=(5, 0))

password_label = tk.Label(
    frame, text="Password", font=("Times new roman", 13), anchor="e", fg="#000000", bg=BG
)
password_label.grid(row=6, column=1, sticky="w", padx=(15, 0), pady=(5, 0))

password_entry = tk.Entry(frame, width=40, show="*")
password_entry.grid(row=7, column=1, padx=(15, 0), pady=(5, 0))

x = tk.IntVar(value=0)

vision = tk.Checkbutton(
    frame, text="Show password", variable=x, onvalue=1, offvalue=0, command=showy
)
vision.grid(row=8, column=1, padx=(15, 0), pady=(15, 0), sticky="w")

button = tk.Button(
    frame,
    text="Log in",
    bg="#1f87ff",
    fg=BG,
    width=30,
    font=("Times new roman", 13),
    command=check,
)
button.grid(row=9, column=1, padx=(15, 0), pady=(15, 0))

aside = tk.Label(
    frame,
    text="Сургалтын demo систем",
    bg=BG,
    fg="#dddddd",
    font=("Times, new roman", 10),
)
aside.grid(row=10, column=1, padx=(24, 0), pady=(5, 0))

root.mainloop()

