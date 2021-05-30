from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", font=("Arial", 15), bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=200,
                                                     text="TEXT",
                                                     font=("Arial", 15, "italic"),
                                                     fill=THEME_COLOR)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image,
                                   highlightthickness=0,
                                   bg=THEME_COLOR,
                                   relief=FLAT,
                                   padx=20,
                                   pady=20,
                                   command=self.false_command)

        self.false_button.grid(column=1, row=2, pady=20)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image,
                                  highlightthickness=0,
                                  bg=THEME_COLOR,
                                  relief=FLAT,
                                  padx=20,
                                  pady=20,
                                  command=self.true_command)

        self.true_button.grid(column=0, row=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've reached the end of quiz with {self.quiz.score} point.")

            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_command(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_command(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")

        elif not is_right:
            self.canvas.config(bg="red")

        self.window.after(500, self.get_next_question)
