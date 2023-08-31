from tkinter import *
import math


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = ("Courier",35,"bold")
BIGGER_FONT=("Courier",40,"bold")
SMALLER_FONT=("Courier",20,"normal")
WORK = 25
SHORT_BREAK = 5
LONG_BREAK = 20
reps = 0
check_txt=""
timer=None

def countdown(count):
    '''The function that actually performs the countdown
    Checks if seconds or minutes are single digits it adds another 0 infront of them
    For every two repetitions a check mark is generated and printed on the screen'''
    global reps
    global check_txt
    min=math.floor(count/60)
    sec=count%60
    if sec<10:
        sec=f"0{sec}"
    if min<10:
        min=f"0{min}"
    canvas.itemconfig(tmr_txt, text=f"{min}:{sec}")
    if count>0:
        global timer
        timer=window.after(1000,countdown,count-1)
    else:
        start_countdown()
        work_sessions=math.floor(reps/2)
        for _ in range (work_sessions):
            check_txt+="✓"
        check_lbl.config(text=check_txt)

def start_countdown():
    '''starts countdown.
        if it is the 8th repetition the
        duration of the countdown gets changed to a long break
         otherwise if it is an even number it sets the short break time.
         finally if the reps is an odd number the countdown is set to the work duration
         '''
    global reps
    reps+=1
    if reps%8==0:
        tmr_lbl.config(fg=RED,text="Long Break")
        countdown(LONG_BREAK * 60)
    elif reps%2==0:
        tmr_lbl.config(fg=PINK,text="Break")
        countdown(SHORT_BREAK*60)
    else:
        tmr_lbl.config(fg=GREEN,text="Work")
        countdown(WORK * 60)

def reset_countdown():
    '''Resets the countdown. Cancels all running countdowns
        and resets the labels'''
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(tmr_txt, text="00:00")
    tmr_lbl.config(text="Timer")
    check_lbl.config(text="")
    reps=0



window=Tk()
window.title("Pomodoro App")
window.config(padx=50,pady=50, bg=YELLOW)
tmt_img=PhotoImage(file="./tomato.png")
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image=tmt_img)
canvas.grid(row=1,column=1)
tmr_txt=canvas.create_text(103, 112, text="00:00", fill="white", font=FONT)

tmr_lbl=Label(text="Timer",font=BIGGER_FONT,fg=GREEN,bg=YELLOW)
tmr_lbl.grid(row=0,column=1)

check_lbl=Label(fg=GREEN,bg=YELLOW,font=SMALLER_FONT)
check_lbl.grid(row=3,column=1)

start_button=Button(bg=YELLOW,text="Start",bd=0,command=start_countdown)
start_button.grid(row=2,column=0)

reset_button=Button(bg=YELLOW,text="Reset",command=reset_countdown,bd=0)
reset_button.grid(row=2,column=2)

window.mainloop()