
import tkinter as tk
from tkinter import messagebox

# -----------------------------
# COMPUTER STUDIES QUIZ GAME
# -----------------------------

questions = [
    {
        "question": "Which component is known as the brain of the computer?",
        "options": ["Monitor", "CPU", "Keyboard", "Printer"],
        "answer": "CPU"
    },
    {
        "question": "Which device is used to enter text into a computer?",
        "options": ["Monitor", "Speaker", "Keyboard", "Projector"],
        "answer": "Keyboard"
    },
    {
        "question": "What does RAM stand for?",
        "options": [
            "Read Access Memory",
            "Random Access Memory",
            "Run All Memory",
            "Remote Access Machine"
        ],
        "answer": "Random Access Memory"
    },
    {
        "question": "Which of these is an operating system?",
        "options": ["Microsoft Word", "Linux", "Google Chrome", "Python"],
        "answer": "Linux"
    },
    {
        "question": "Which device displays visual output?",
        "options": ["Mouse", "Scanner", "Monitor", "Microphone"],
        "answer": "Monitor"
    },
    {
        "question": "Which of these is an example of an input device?",
        "options": ["Printer", "Speaker", "Keyboard", "Monitor"],
        "answer": "Keyboard"
    },
    {
        "question": "What is the main function of a printer?",
        "options": [
            "To print documents",
            "To store files",
            "To process data",
            "To browse the internet"
        ],
        "answer": "To print documents"
    },
    {
        "question": "Which number system does a computer use internally?",
        "options": ["Decimal", "Binary", "Roman", "Octal only"],
        "answer": "Binary"
    },
    {
        "question": "Which of these is a web browser?",
        "options": ["Python", "Linux", "Mozilla Firefox", "Microsoft Excel"],
        "answer": "Mozilla Firefox"
    },
    {
        "question": "What is the purpose of antivirus software?",
        "options": [
            "To create presentations",
            "To protect against malicious software",
            "To increase screen brightness",
            "To type documents"
        ],
        "answer": "To protect against malicious software"
    }
]


# -----------------------------
# MAIN APPLICATION
# -----------------------------

root = tk.Tk()
root.title("Computer Studies Quiz Game")
root.geometry("650x500")
root.resizable(False, False)
root.configure(bg="#F1F5F9")

current_question = 0
score = 0
answered = False


def clear_screen():
    """Remove all widgets from the window."""
    for widget in root.winfo_children():
        widget.destroy()


def show_welcome_screen():
    """Display the welcome screen."""
    clear_screen()

    tk.Label(
        root,
        text="COMPUTER STUDIES QUIZ",
        font=("Arial", 23, "bold"),
        bg="#F1F5F9",
        fg="#1E3A8A"
    ).pack(pady=(65, 15))

    tk.Label(
        root,
        text="Test your knowledge of computers!",
        font=("Arial", 13),
        bg="#F1F5F9",
        fg="#334155"
    ).pack(pady=10)

    tk.Label(
        root,
        text="10 questions | Multiple choice",
        font=("Arial", 11),
        bg="#F1F5F9",
        fg="#64748B"
    ).pack(pady=5)

    tk.Button(
        root,
        text="START QUIZ",
        font=("Arial", 13, "bold"),
        bg="#2563EB",
        fg="white",
        activebackground="#1D4ED8",
        activeforeground="white",
        width=18,
        command=start_quiz
    ).pack(pady=30)

    tk.Button(
        root,
        text="EXIT",
        font=("Arial", 10),
        width=12,
        command=root.destroy
    ).pack()


def start_quiz():
    """Reset the game and begin."""
    global current_question, score, answered

    current_question = 0
    score = 0
    answered = False

    show_question()


def show_question():
    """Display the current question and its answers."""
    global answered

    clear_screen()
    answered = False

    question_data = questions[current_question]

    tk.Label(
        root,
        text=f"QUESTION {current_question + 1} OF {len(questions)}",
        font=("Arial", 11, "bold"),
        bg="#F1F5F9",
        fg="#2563EB"
    ).pack(pady=(25, 8))

    tk.Label(
        root,
        text=f"Score: {score}",
        font=("Arial", 11),
        bg="#F1F5F9",
        fg="#334155"
    ).pack(pady=3)

    tk.Label(
        root,
        text=question_data["question"],
        font=("Arial", 14, "bold"),
        bg="#F1F5F9",
        fg="#0F172A",
        wraplength=570,
        justify="center"
    ).pack(pady=20)

    for option in question_data["options"]:
        tk.Button(
            root,
            text=option,
            font=("Arial", 11),
            width=43,
            bg="white",
            fg="#0F172A",
            activebackground="#DBEAFE",
            command=lambda choice=option: check_answer(choice)
        ).pack(pady=5)

    global feedback_label, next_button

    feedback_label = tk.Label(
        root,
        text="",
        font=("Arial", 11, "bold"),
        bg="#F1F5F9"
    )
    feedback_label.pack(pady=8)

    next_button = tk.Button(
        root,
        text="NEXT QUESTION",
        font=("Arial", 10, "bold"),
        bg="#2563EB",
        fg="white",
        activebackground="#1D4ED8",
        activeforeground="white",
        width=18,
        state="disabled",
        command=next_question
    )
    next_button.pack(pady=5)


def check_answer(choice):
    """Check the selected answer and update the score."""
    global score, answered

    if answered:
        return

    answered = True
    correct_answer = questions[current_question]["answer"]

    if choice == correct_answer:
        score += 1
        feedback_label.config(
            text="Correct! Well done!",
            fg="#15803D"
        )
    else:
        feedback_label.config(
            text=f"Incorrect. Answer: {correct_answer}",
            fg="#DC2626"
        )

    next_button.config(state="normal")


def next_question():
    """Move to the next question or show the results."""
    global current_question

    current_question += 1

    if current_question < len(questions):
        show_question()
    else:
        show_results()


def show_results():
    """Display the final score and allow replay."""
    clear_screen()

    percentage = (score / len(questions)) * 100

    if percentage >= 80:
        message = "Excellent work!"
    elif percentage >= 50:
        message = "Good effort! Keep practising."
    else:
        message = "Keep learning. You can improve!"

    tk.Label(
        root,
        text="QUIZ COMPLETED!",
        font=("Arial", 23, "bold"),
        bg="#F1F5F9",
        fg="#1E3A8A"
    ).pack(pady=(65, 20))

    tk.Label(
        root,
        text=f"Your score: {score} / {len(questions)}",
        font=("Arial", 18, "bold"),
        bg="#F1F5F9",
        fg="#0F172A"
    ).pack(pady=10)

    tk.Label(
        root,
        text=f"Percentage: {percentage:.0f}%",
        font=("Arial", 14),
        bg="#F1F5F9",
        fg="#334155"
    ).pack(pady=5)

    tk.Label(
        root,
        text=message,
        font=("Arial", 13),
        bg="#F1F5F9",
        fg="#15803D"
    ).pack(pady=12)

    tk.Button(
        root,
        text="PLAY AGAIN",
        font=("Arial", 11, "bold"),
        bg="#2563EB",
        fg="white",
        activebackground="#1D4ED8",
        activeforeground="white",
        width=18,
        command=show_welcome_screen
    ).pack(pady=15)

    tk.Button(
        root,
        text="EXIT",
        width=12,
        command=root.destroy
    ).pack()


# Start the application
show_welcome_screen()
root.mainloop()
