from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.score_num = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config()
        self.text = self.canvas.create_text(150,
                                            125,
                                            width=280,
                                            text="Some Question Here",
                                            font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.score = Label(text="Score: 0")
        self.score.config(highlightthickness=0, bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        true_image = PhotoImage(file="/Users/suhani/Downloads/quizzler-app-start/images/true.png")
        self.true_button = Button(image=true_image, command=self.true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="/Users/suhani/Downloads/quizzler-app-start/images/false.png")
        self.false_button = Button(image=false_image, command=self.false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the quiz.")

    def true(self):
        is_correct = self.quiz_brain.check_answer("true")
        if is_correct:
            self.canvas.config(bg="green")
            self.window.after(1000, func=self.change_color)
            self.score_num += 1

        else:
            self.canvas.config(bg="red")
            self.window.after(1000, func=self.change_color)

    def false(self):
        is_correct = self.quiz_brain.check_answer("false")
        if is_correct:
            self.canvas.config(bg="green")
            self.window.after(1000, func=self.change_color)
            self.score += 1
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, func=self.change_color)

    def change_color(self):
        self.score.config(text=f"Score: {self.score_num}")
        self.canvas.config(bg="white")
        self.get_next_question()