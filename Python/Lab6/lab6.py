import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Student Management UI")
root.geometry("600x350")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

style = ttk.Style()

style.configure("Treeview.Heading",
                 background="#5d89e0",
                 foreground="#535353",
                 fieldbackground="#f2f6ff",
                 font=("Arial", 11, "bold"))

tree = ttk.Treeview(root, columns=("name", "course"), show="headings", height=10)
#Tree configuration
tree.heading("name",text="Нэр")
tree.heading("course", text="Курс")
tree.column("name", width=100, anchor="center")
tree.column("course", width=100, anchor="center")

tree.insert("", "end", values=("Бат", 4))
tree.insert("", "end", values=("Саруул", 4))
tree.grid(row=1, column=0, columnspan=2, padx=15, pady=5)

def on_selected():
    selected = tree.selection()
    if selected:
        values = tree.item(selected[0], "values")
        return values

add_button = tk.Button(root,
                        text="Нэмэх",
                        bg="#005586",
                        fg="white",
                        width=15,
                        height=1)

add_button.grid(row=2, column=1, sticky="w", padx=(10, 0))

root.mainloop()