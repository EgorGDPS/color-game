import tkinter as tk
import random
import tkinter.font as tkFont

colours = ['red', 'blue', 'green', 'pink', 'black', 'yellow', 'orange', 'cyan', 'purple', 'brown', 'silver']

top = tk.Tk()
top.title("Game")
top.geometry("700x500")
top.configure(bg='#C0C0C0')

text_color = ""
time_left = 0
score = 0

def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        T.config(text=f'Time: {time_left}')
        T.after(1000, countdown)
    else:
        T.config(text="Game Over")
        L.config(text=f"Score: {score}", fg="black")

def start_timer():
    clear_text()
    global time_left, score
    time_left = 30
    score = 0
    countdown()

def choose_random_color():
    return random.choice(colours)

def display_colored_text():
    global text_color
    text_color = choose_random_color()
    color_name = choose_random_color()
    while color_name == text_color:
        color_name = choose_random_color()
    L.config(text=color_name, fg=text_color)

def game_start():
    start_timer()
    display_colored_text()

def check_answer():
    global score
    entered_color = A.get("1.0", "end-1c").strip().lower()
    print(f'entered: {entered_color} correct {text_color.lower()}')
    if entered_color == text_color.lower():
        score += 1
        print("Correct!")
    else:
        print("Incorrect! The correct color is:", text_color)
    print("Score:", score)
    clear_text()

def clear_text():
    A.delete('1.0', 'end')  

def switch_color(e):
    check_answer()
    display_colored_text()

fontObj = tkFont.Font(size=20)

L = tk.Label(top, text="Click the button below to start the game", width=30, height=5, font=fontObj)
L.place(x=100, y=100)
L.configure(bg='#C0C0C0')

S = tk.Button(top, text='Start', command=game_start)
S.place(x=350, y=250)
S.configure(bg='#C0C0C0')

T = tk.Label(text="Time: 30")
T.place(x=350, y=300)
T.configure(bg='#C0C0C0')

L2 = tk.Label(text="Enter the color of the words")
L2.place(x=350, y=200)
L2.configure(bg='#C0C0C0')

A = tk.Text(height=1, width=10)
A.place(x=300, y=220)
A.configure(bg='#C0C0C0')

top.bind('<Return>', switch_color)

top.mainloop()



