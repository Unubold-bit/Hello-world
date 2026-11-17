import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style()
style.theme_use("clam")   # чухал, доор тайлбарласан

# Мөр, багана (өгөгдлийн хэсэг)
style.configure("Treeview",
                background="#1e1e2e",
                foreground="white",
                fieldbackground="#e9e9ec",   # хоосон хэсгийн дэвсгэр
                rowheight=28,
                font=("Arial", 11))

# Толгой (heading)
style.configure("Treeview.Heading",
                background="#313244",
                foreground="white",
                font=("Arial", 11, "bold"))

# Сонгосон мөрийн өнгө
style.map("Treeview",
          background=[("selected", "#89b4fa")],
          foreground=[("selected", "black")])

tree = ttk.Treeview(root, columns=("name", "score"), show="headings")
tree.heading("name", text="Нэр")
tree.heading("score", text="Оноо")
tree.pack(fill="both", expand=True)

root.mainloop()