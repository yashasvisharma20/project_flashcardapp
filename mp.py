from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont

def check_answer():
    global index, score, keys, questions
    answer = answer_entry.get()
    answer_entry.delete(0, END)
    
    feedback_label.config(text="", fg="black")  # Clear previous feedback
    
    if answer.lower() == questions[keys[index]].lower():
        score += 1
        feedback_label.config(text="Correct!", fg="green")
    else:
        feedback_label.config(text=f"Wrong! The correct answer is: {questions[keys[index]]}", fg="red")
    
    index += 1
    if index < len(keys):
        question_label.config(text=keys[index])
    else:
        check_button.config(state=DISABLED)
        question_label.config(text=f"Your final score is: {score} / {len(keys)}")

root = Tk()
root.title("flashcard App")
root["bg"] = "Light Yellow"
root.geometry("850x450")
l1= Label(root, text="Welcome To Flashcard App", bg="White", fg="Brown", font=("Arial Bold",22))
l1.pack()
questions = {
    "What is the capital of India?": "New Delhi",
    "What is the largest animal?": "Blue Whale",
    "Who is the prime minister of India?": "Narendra Modi",
    "What is the smallest planet in the solar system?" : "Mercury",
    "Who is the author of Harry Potter series?": "J.K. Rowling",
    "What is the name of the largest bone in the human body?": "Femur"
}

keys = list(questions.keys())
index = 0
score = 0

question_label = Label(root, text=keys[index], font=("Arial", 16),bg="Sky Blue", fg="Brown", wraplength=300)
question_label.pack(pady=20)

answer_entry = Entry(root, font=("Arial", 14))
answer_entry.pack()

check_button = Button(root, text="Check", font=("Arial", 14),bg="Sky Blue",fg="Brown", command=check_answer)
check_button.pack(pady=10)

feedback_label = Label(root, text="", font=("Arial", 14))
feedback_label.pack()

root.mainloop()
