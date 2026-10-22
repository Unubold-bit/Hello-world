import tkinter as tk
from tkinter import ttk, messagebox
BG = "white"
current_question = 0
score = 0
selected_answer = 0
finished = False

def update_status():
    """Updates the question count, score counters, and progress bar dynamically."""
    if finished:
        question_number_label.config(text="Дууссан")
        score_label.config(text=f"Нийт оноо: {score}/{len(questions)}")
        progress["value"] = len(questions)
    else:
        question_number_label.config(text=f"Асуулт: {current_question + 1}/{len(questions)}")
        score_label.config(text=f"Оноо: {score}")
        progress["value"] = current_question

def show_questions():
    q_data = questions[current_question]
    selected_answer.set("unselected")
    
    question_label.config(text=q_data["question"])
    
    for button, option in zip(option_buttons, q_data["options"]):
        button.config(text=option, value=option, state="normal")
        
    last = (current_question == len(questions) - 1)
    
    btn_text = "Дуусгах" if last else "Дараах"
    next_button.config(text=btn_text, state="normal")
    update_status()

def next_question():
    global current_question, score, finished
    if finished:
        return
    answer = selected_answer.get()
    if answer == "unselected":
        messagebox.showwarning(
            "Анхааруулга", "Хариугаа сонгоно уу.", parent = window
        )
        return
    if answer == questions[current_question]["answer"]:
        score += 1
    current_question += 1
    if current_question < len(questions):
        show_questions()
    else:
        finished =  True
        update_status()
        next_button.config(state="disabled")
        show_result_popup()

def show_result_popup():
    """Creates a custom modal window displaying final results with a restart option."""
    global result_window
    result_window = tk.Toplevel(window)
    result_window.title("Үр дүн")
    result_window.geometry("300x200")
    result_window.resizable(False, False)
    percent = str((int(score/len(questions))*100))
    # Force focus onto the result pop-up window
    result_window.grab_set()
    
    tk.Label(
        result_window, 
        text=f"Таны нийт оноо: {score} / {len(questions)}", 
        font=("Arial", 14, "bold"), pady=20
    ).pack()
    if score > 7:
        tk.Label(
            result_window, text="Сайн байна!", font=("Arial", 10, "bold")
        )
    elif 4 < score <= 7:
        tk.Label(
                    result_window, text="Not bad, try hard!", font=("Arial", 10, "bold")
                )
    else:
        tk.Label(
                    result_window, text="Nah bro, GG!", font=("Arial", 10, "bold")
                )
        
    tk.Label(
        result_window, 
        text=percent,
        font=("Arial", 14)
    ).pack()
        
    tk.Button(
        result_window, 
        text="Дахин эхлүүлэх", 
        command=restart_quiz,
        bg="#E3F7D5",
        activebackground="#A9FD6D"
    ).pack(pady=10)

    tk.Button(
        result_window, 
        text="Гарах", 
        command=close_window,
        bg="#FFD6CE",
        activebackground="#FF846C"
    ).pack(pady=15)
    
def close_window():
    window.destroy()
    result_window.destroy()



def restart_quiz():
    global current_question, score, finished, result_window
    if result_window is not None:
        result_window.grab_release()
        result_window.destroy()
        result_window = None

    current_question = 0
    score = 0
    finished = False
    show_questions()
    window.focus_get()       

questions = [
    {
        "question": "List literal үүсгэх хаалт аль вэ?",
        "options": ["( )", "[ ]", "{ }", "< >"],
        "answer": "[ ]",
    },
    {
        "question": "Tuple үүсгэхэд ямар хаалт ашигладаг вэ?",
        "options": ["[ ]", "{ }", "( )", "< >"],
        "answer": "( )",
    },
    {
        "question": "Dictionary ямар хаалт ашигладаг вэ?",
        "options": ["( )", "[ ]", "{ }", "< >"],
        "answer": "{ }",
    },
    {
        "question": "Python дээр хувьсагчид утга оноох оператор аль вэ?",
        "options": ["==", "=", "!=", ">="],
        "answer": "=",
    },
    {
        "question": "Жагсаалтын хамгийн эхний элементийн индекс хэд вэ?",
        "options": ["0", "1", "-1", "2"],
        "answer": "0",
    },
    {
        "question": "Python дээр функц зарлах түлхүүр үг аль вэ?",
        "options": ["function", "define", "def", "func"],
        "answer": "def",
    },
    {
        "question": "Текстэн өгөгдлийн төрлийг аль нь илэрхийлэх вэ?",
        "options": ["int", "str", "float", "bool"],
        "answer": "str",
    },
    {
        "question": "Нөхцөл шалгахад ашигладаг түлхүүр үг аль вэ?",
        "options": ["for", "while", "if", "def"],
        "answer": "if",
    },
    {
        "question": "List-ийн төгсгөлд шинэ элемент нэмэхэд ямар метод ашиглах вэ?",
        "options": ["add()", "append()", "insert_end()", "push()"],
        "answer": "append()",
    },
    {
        "question": "List-ийн эхэнд шинэ элемент нэмэхэд ямар метод ашиглах вэ?",
        "options": ["add()", "append()", "insert()", "push()"],
        "answer": "insert()",
    },
]

window = tk.Tk()
window.title("Python Quiz")
window.geometry("600x600")
window.resizable(False, False)
window.configure(bg=BG)

status_frame = tk.Frame(window, bg="lightgray")

status_frame.pack(fill="x", padx=40)

question_number_label = tk.Label(status_frame, fg="black", font=("Arial", 11, "bold"))
question_number_label.pack(side="left", padx=10, pady=5)

score_label = tk.Label(status_frame, fg="black", font=("Arial", 11, "bold"))
score_label.pack(side="right", padx=10, pady=5)

progress = ttk.Progressbar(window, maximum=len(questions), mode="determinate")
progress.pack(fill="x", padx=40, pady=(12, 4))

question_label = tk.Label(
    window, text="", bg=BG, font=("Arial", 16, "bold"),
    wraplength=520, justify="left", anchor="w"
)
question_label.pack(fill="x", padx=40, pady=(18, 12))


selected_answer = tk.StringVar(master=window, value="")

options_frame = tk.Frame(window, bg=BG)
options_frame.pack(fill="x", padx=40, pady=10)

option_buttons = []
for _ in range(4):
    button = tk.Radiobutton(
        options_frame, variable=selected_answer, value="",
        anchor="w", font=("Arial", 13)
    )
    button.pack(fill="x", pady=6)
    option_buttons.append(button)

actions_frame = tk.Frame(window, bg=BG)
actions_frame.pack(fill="x", padx=40, pady=20)

next_button = ttk.Button(actions_frame, text="Дараах", command=next_question)
next_button.pack(side="right")


show_questions()

window.mainloop()