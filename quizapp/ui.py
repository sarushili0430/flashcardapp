import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():
    
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        #Window Config
        self.window = tk.Tk()
        self.window.title("Quizller")
        self.window.config(background=THEME_COLOR,padx=20,pady=20)
        #Image Loading
        checkmark_img = tk.PhotoImage(file="images/true.png")
        crossmark_img = tk.PhotoImage(file="images/false.png")
        #UI Modules
        self.scoreboard = tk.Label(text=f"Score: {self.quiz.score}",font=("Arial",15,"normal"),background=THEME_COLOR,foreground="white")
        self.question_box = tk.Canvas(height=250,width=300)
        self.question_text = self.question_box.create_text(150,125,text="test",font=("Arial",20,"italic"),width=280)
        self.check_button = tk.Button(image=checkmark_img,command=lambda: self.CheckAnswer("True"))
        self.cross_button = tk.Button(image=crossmark_img,command=lambda: self.CheckAnswer("False"))
        #UI Layout
        self.scoreboard.grid(column=1,row=0,pady=20)
        self.question_box.grid(column=0,row=1,columnspan=2,pady=20)
        self.check_button.grid(column=0,row=2,pady=20)
        self.cross_button.grid(column=1,row=2,pady=20)
        
        self.get_next_question()

        self.window.mainloop()

    def PrintScoreboard(self):
        self.scoreboard.config(text=f"Score: {self.quiz.score}")

    def CheckAnswer(self,answer):
        if self.quiz.check_answer(answer):
            self.give_feedback(True)
        else:
            self.give_feedback(False)
    
    def get_next_question(self):
        try:
            q_text = self.quiz.next_question()
        except IndexError:
            self.question_box.itemconfig(tagOrId=self.question_text,text="Gameover!")
            self.check_button.config(state="disabled")
            self.cross_button.config(state="disabled")
        else:
            self.question_box.itemconfig(tagOrId=self.question_text,text=q_text)
        finally:
            self.question_box.config(bg="white")
    
    def give_feedback(self,isRight):
        if isRight:
            self.question_box.config(bg="green")
        else:
            self.question_box.config(bg="red")
        self.question_box.after(1000,func=self.get_next_question)
        self.PrintScoreboard()
        self.question_box.update()


