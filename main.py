from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FF5F9E"
RED = "#CD0404"
GREEN = "#5F8D4E"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    updat_label('Timer', GREEN)
    updat_checkmark()


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_min = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        updat_label("Break", RED)
        count_down(long_break_sec)
        reps = 0
    elif reps % 2 == 0:
        updat_label("Break", PINK)
        count_down(short_break_sec)
    else:
        updat_label("Work", GREEN)
        count_down(work_min)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def updat_label(text, color):
    title_label.config(text=text, fg=color)


def updat_checkmark():
    symbol = ''
    work_sessions = math.floor(reps/2)
    for _ in range(work_sessions):
        symbol += '✔'
    check_label.config(text=symbol)


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        updat_checkmark()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(
    file='./tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)


title_label = Label(text="Timer", bg=YELLOW, font=(
    FONT_NAME, 20, 'bold'), fg=GREEN)
title_label.grid(row=0, column=1)

start_button = Button(text="Start", command=start_timer, font=(
    FONT_NAME, 10, 'bold'), highlightthickness=0)
start_button.grid(row=2, column=0)

reset_label = Button(text="Reset", font=(FONT_NAME, 10, 'bold'),
                     highlightthickness=0, command=reset_timer)
reset_label.grid(row=2, column=2)

check_label = Label(bg=YELLOW, font=(FONT_NAME, 10, 'bold'), fg=GREEN)
check_label.grid(row=3, column=1)


window.mainloop()
