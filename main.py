from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        countdown(long_break_sec)
        title_label.config(text ="Break", fg=RED)

    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text ="Break", fg=PINK)

    else:
        countdown(work_sec)
        title_label.config(text="Work", fg=GREEN)


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    title_label.config(text="Timer", fg="white")
    checkmark_label.config(text="")


def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range (work_sessions):
            marks += "✅"
        checkmark_label.config(text=marks)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="black")


file = PhotoImage(file="tomato.png")

canvas = Canvas(width=220, height=224, bg="black", highlightthickness=0)
canvas.create_image(100, 112, image=file)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)


title_label = Label(text="Timer")
title_label.config(fg="white", bg="black", font=(FONT_NAME, 50, "normal"))
title_label.grid(column=1, row=0)

checkmark_label = Label(bg="black")
checkmark_label.grid(column=1, row=3)


start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()