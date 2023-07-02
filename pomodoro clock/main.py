import tkinter as tk
# from playsound import playsound

window = tk.Tk()
window.config(padx=50, pady=20, bg="Black")
window.title("Pomodoro")
window.minsize(height=500, width=500)

WORK_TIME = 25
SHORT_BREAK = 5
LONG_BREAK = 20
reps = 0
timer = ""


def count_down(count):
    mins = int(count / 60)
    secs = int(count % 60)
    if secs < 10:
        secs = f"0{secs}"
    canvas.itemconfig(clock_text, text=f"{mins} : {secs}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        timer_logic()


def timer_logic():
    global reps
    reps += 1
    if reps % 8 == 0:
        Heading_text.config(text="Long Break")
        Marks_label.config(text="✔ ✔ ✔ ✔")
        count_down(LONG_BREAK * 60)
    elif reps % 2 == 0:
        Heading_text.config(text="Short Break")
        # playsound("blue.mp3")
        Marks_label.config(text="✔ " * int(reps / 2))
        count_down(SHORT_BREAK * 60)
    else:
        Heading_text.config(text="Work")
        count_down(WORK_TIME * 60)


def start_timer():
    global reps
    if reps > 0:
        reset_timer()
    timer_logic()


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    Heading_text.config(text="Timer")
    canvas.itemconfig(clock_text, text="00 : 00")
    Marks_label.config(text="")


# =======================================LABEL==========================================#
Heading_text = tk.Label(text="Timer", font=("Arial", 50, "bold"), bg='black', fg="IndianRed")
Heading_text.grid(column=1, row=0)

# =======================================CANVAS==========================================#
canvas = tk.Canvas(width=320, height=160, bg="black", highlightthickness=0)
canvas.grid(column=1, row=1, padx=35, pady=20)
photo = tk.PhotoImage(file="clock-removebg-preview.png")
canvas.create_image(160, 85, image=photo)
clock_text = canvas.create_text(160, 75, text="00 : 00", fill="Blue", font=("Arial", 50, "normal"))

# =======================================MARKS==========================================#
Marks_label = tk.Label(text="", font=("Arial", 20, "bold"), bg='black', fg="LawnGreen")
Marks_label.grid(column=1, row=3)

# =======================================BUTTONS==========================================#
start_button = tk.Button(text="START", command=start_timer, activeforeground="red", bg="Pink", fg="blue",
                         highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="RESET", command=reset_timer, activeforeground="red", bg="Pink", fg="blue",
                         highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()
