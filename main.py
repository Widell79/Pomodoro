import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# ---------------------------- GLOBALS ------------------------------- #

reps = 0 # To count in TIMER MECHANISM
reset = None # To be able to reset timer in TIMER RESET / COUNTDOWN MECHANISM

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(reset)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps in [1, 3, 5, 7]:
        title_label.config(text="Work")
        count_down(work_sec)

    if reps in [2, 4, 6]:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)

    if reps == 8:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count /60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global reset
        reset = window.after(1000, count_down, count -1)
    else:
        timer()
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            check_label.config(text="✔")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

title_label = tkinter.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 42), pady=10, bg=YELLOW)
title_label.grid(column=1, row=0)

check_label = tkinter.Label(fg=GREEN, font=(FONT_NAME, 24, "bold"), bg=YELLOW)
check_label.grid(column=1, row=3)

start_button = tkinter.Button(text="Start", command=timer, bg="white", highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", command=reset_timer, bg="white", highlightthickness=0)
reset_button.grid(column=2, row=2)


window.mainloop()