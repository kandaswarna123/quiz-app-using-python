import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self):
        self.quiz_data = [
            {
                "question": "What is the capital of France?",
                "options": ["Berlin", "Madrid", "Paris", "Rome"],
                "answer": "Paris"
            },
            {
                "question": "What is 2 + 2?",
                "options": ["3", "4", "5", "6"],
                "answer": "4"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "answer": "Jupiter"
            }
        ]
        self.current_question_index = 0
        self.score = 0 
        self.window = tk.Tk()
        self.window.title("Quiz Application")


# ui element creation
        self.question_label = tk.Label(self.window, text="", wraplength=400, font=("Arial", 14))
        self.question_label.pack(pady=20)
        self.options_frame = tk.Frame(self.window)
        self.options_frame.pack(pady=10)
        
        self.option_buttons = []

        for i in range(4):
            btn = tk.Button(self.options_frame, text="", width=20, command=lambda idx=i: self.check_answer(idx))
            btn.grid(row=i, column=0, pady=5)
            self.option_buttons.append(btn)
        self.next_question_button = tk.Button(self.window, text="Next Question",width=30, command=self.next_question)
        self.next_question_button.pack(pady=10)
    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index == len(self.quiz_data):
            messagebox.showinfo("Quiz Finished", "Your score is" +str(self.score))
            self.window.quit()
        else:
            self.load_question()
           
            
            
    def check_answer(self, selected_option):
        question_data = self.quiz_data[self.current_question_index]
        # quiz data stores the correct answer under the key 'answer'
        correct_answer = question_data["answer"]
        # selected_option is an index; get the option text
        selected_text = question_data["options"][selected_option]

        if selected_text == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "You selected the correct answer.")
        else:
            messagebox.showerror("Wrong!", f"The correct answer was: {correct_answer}")

        # advance to next question or finish the quiz
        self.current_question_index += 1
        if self.current_question_index < len(self.quiz_data):
            self.load_question()
        else:
            messagebox.showinfo(
                "Quiz Finished", f"Your score: {self.score}/{len(self.quiz_data)}"
            )
            self.window.quit()
        
    def load_question(self):
        question_data = self.quiz_data[self.current_question_index]
        self.question_label.config(text=question_data["question"])
        options = question_data["options"]
        for i in range(4):
            self.option_buttons[i].config(text=options[i])

    def start_quiz(self):
        self.load_question()
        self.window.mainloop()


quiz_app = QuizApp()
quiz_app.start_quiz()
        