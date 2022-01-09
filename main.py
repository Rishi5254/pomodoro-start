from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer= None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_count():
    window.after_cancel(timer)
    timer_t.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    check_mark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global reps
    reps += 1
    work_min = WORK_MIN * 15
    short_break = SHORT_BREAK_MIN * 5
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break)
        timer_t.config(text="Break")
    elif reps % 2 == 0:
        count_down(short_break)
        timer_t.config(text="Break")
    else:
        count_down(work_min)
        timer_t.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_count()
        marks = ""
        for n in range(math.floor(reps/2)):
            marks += "✓"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
imag = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=imag)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start",bg="white", font=(FONT_NAME, 12, "bold"), highlightthickness=0, command= start_count)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg="white", font=(FONT_NAME, 12, "bold"), highlightthickness=0, command= reset_count)
reset_button.grid(column=2, row=2)

timer_t = Label(text="Timer", fg=PINK,bg= YELLOW, font=(FONT_NAME, 40, "bold"))
timer_t.grid(column=1, row=0)

check_mark = Label(fg=GREEN, font=(FONT_NAME, 13, "normal"))
check_mark.grid(column=1, row=3)

window.mainloop()
