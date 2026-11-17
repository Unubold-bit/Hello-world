import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3


conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    ovog TEXT,
    name TEXT,
    course TEXT)
""")


root = tk.Tk()
root.title("Student Management UI")
root.geometry("600x350")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)

ovog = tk.Label(root, text="Овог")
ovog.grid(row=0, column=0)

ovog_e = tk.Entry(root, width=50)
ovog_e.grid(row=0, column=1)

name_l = tk.Label(root, text="Нэр")
name_l.grid(row=1, column=0)

name_e = tk.Entry(root, width=50)
name_e.grid(row=1, column=1)

course_l = tk.Label(root, text="Курс")
course_l.grid(row=2, column=0)

n = tk.StringVar()
course_cb = ttk.Combobox(root, width=27, textvariable=n, state="readonly")

course_cb['values'] = ('1',
                       '2',
                       '3',
                       '4',
                       '5')

course_cb.grid(row=2, column=1)
course_cb.current(3)
#Tree configuration

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading",
                 background="#5d89e0",
                 foreground="#535353",
                 fieldbackground="#5874b6",
                 font=("Arial", 11, "bold"))

tree = ttk.Treeview(root, columns=("ID", "Ovog", "name", "course"), show="headings", height=10)

tree = ttk.Treeview(root, columns=("ID", "Ovog", "name", "course"), show="headings", height=10)

tree.heading("ID", text="ID")
tree.heading("Ovog", text="Овог")
tree.heading("name", text="Нэр")
tree.heading("course", text="Курс")

# Set explicit widths so the total fits within your 600px window
tree.column("ID", width=60, anchor="center")
tree.column("Ovog", width=190, anchor="w")
tree.column("name", width=190, anchor="center")
tree.column("course", width=120, anchor="center")

tree.grid(row=3, column=0, columnspan=4, padx=15, pady=5, sticky="ew")


def gett():
    global cursor, conn
    ovg = ovog_e.get().strip()
    name = name_e.get().strip()
    course = course_cb.get()

    cursor.execute(
        "SELECT id FROM students"
    )
    
    rows = cursor.fetchall()
    print(rows)

    id_list = []
    for row in rows:  
        for i in row:
            id_list.append(i)


    if check():
        cursor.execute(
            "INSERT INTO students (ovog, name, course) VALUES (?, ?, ?)",
            (ovg, name, course)
        )
        conn.commit()
        tree.insert("", tk.END, values=((1 if len(id_list) == 0 else id_list[-1]+1), ovg, name, course))

    else:
        pass

def check():
    global cursor, conn
    ovg = ovog_e.get().strip()
    name = name_e.get().strip()
    course = course_cb.get()
    a = (ovg, name, course)
    cursor.execute(
        "SELECT ovog, name, course FROM students"
    )
    ll = cursor.fetchall()
    if a in ll:
        response = messagebox.askquestion("Repeated", "It's saved on database. Are you sure save it again?")
        if response == "yes":
            return True
        else:
            return False
    
def delete_selected():
    global curson, conn
    selected = tree.selection()

add_button = tk.Button(root,
                        text="Нэмэх",
                        bg="#005586",
                        fg="white",
                        width=15,
                        height=1,
                        command=gett)

add_button.grid(row=4, column=0, padx=(60, 0), pady=(10, 10))

del_button = tk.Button(root,
                        text="Устгах",
                        bg="#005586",
                        fg="white",
                        width=15,
                        height=1,
                        command=delete_selected)

del_button.grid(row=4, column=1, padx=(10, 0), pady=(10, 10))

root.mainloop()    
