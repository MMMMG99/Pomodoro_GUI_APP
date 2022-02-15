from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer1 = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer1)
    canvas.itemconfig(timer_text, text='00:00')
    check.config(text='')
    timer.config(text='Timer', )


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        timer.config(text='Long break', fg=PINK)
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer.config(text='Short Break', fg=RED)
        countdown(SHORT_BREAK_MIN * 60)
    else:
        timer.config(text='Work', fg=GREEN)
        countdown(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_minute = count // 60
    count_seconds = count % 60

    if count_minute < 10:
        count_minute = f'0{count_minute}'

    if count_seconds < 10:
        count_seconds = f'0{count_seconds}'

    canvas.itemconfig(timer_text, text=f'{count_minute}:{count_seconds}')

    if count > 0:
        global timer1
        timer1 = window.after(1000, countdown, count - 1)
    else:
        if reps % 2 == 0:
            alta_eticheta = check.cget('text')
            noua_valoare = alta_eticheta + '✓'
            check.config(text=noua_valoare)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Rosia productiva")
window.config(padx=100, pady=50, bg=YELLOW)


#canvas widget
#putem pune lucruri unele peste altele

timer = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), bg=YELLOW, fg=GREEN)
timer.grid(row=0, column=1)

check = Label(bg=YELLOW, fg=GREEN)
check.grid(row=3, column=1)

start = Button(text = 'Start', highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text = 'Reset', highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
poza_rosie = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=poza_rosie)
timer_text = canvas.create_text(100, 132, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

window.mainloop()