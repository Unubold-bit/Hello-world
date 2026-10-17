import tkinter as tk
# Import the Image and ImageTk modules from Pillow
from PIL import Image, ImageTk 
count = 0
def click():
    global count
    count += 1
    label.config(text=count)

window = tk.Tk()
window.geometry("400x300")
window.title("Button now")

icon = tk.PhotoImage(file='apple-logo.png')
window.iconphoto(True, icon)

button = tk.Button(window, text='Click me!!!')
button.config(command=click) # performs call back of functions
button.config(activebackground='#FF8E47')
button.config(activeforeground="#E1DAFF")
button.config(font=('Ink Free', 50, 'bold'), bg='#EB66FF', fg='#FFE747')

# --- RESIZE LOGIC HERE ---
# 1. Open the image file using PIL
pil_image = Image.open('logo.png')

# 2. Resize to your desired width and height (e.g., 100x100)
resized_pil_image = pil_image.resize((100, 100), Image.Resampling.LANCZOS)

# 3. Convert it to a Tkinter-compatible photo image
image = ImageTk.PhotoImage(resized_pil_image)
# -------------------------

button.config(image=image)
button.config(compound='bottom')
#button.config(state='disabled') #  disabled button ('active'/'disabled')

label = tk.Label(window, text=count, font=('Monospace', 50))
label.pack()
button.pack()

# Keep a reference to the image so it doesn't get garbage-collected
button.image = image 

window.mainloop()  # Fixed your comment here (used '#' instead of '//')
