import tkinter
import random
import pandas
import time

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *

random_french = {}
to_learn = {}

try:
    # Generate random French and English word on UI
    data = pandas.read_csv("french_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def random_fren():
    global random_french, flip_timer
    windows.after_cancel(flip_timer)
    random_french = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_french["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = windows.after(3000, func=flip_card)


# flip the card
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_french["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)


# check cards if you already known
def is_known():
    to_learn.remove(random_french)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    random_fren()


# UI
# card_front = PhotoImage(file="card_front.png")
# card_back = PhotoImage(file="card_back.png")
# right = PhotoImage(file="right.png")
# wrong = PhotoImage(file="wrong.png")

windows = Tk()
windows.title(" FlashCard ")
windows.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = windows.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="card_front.png")
right = PhotoImage(file="right.png")
card_back = PhotoImage(file="card_back.png")
wrong = PhotoImage(file="wrong.png")

try:
    card_background = canvas.create_image(400, 263, image=card_front)
    canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
    canvas.grid(column=1, row=0, columnspan=2)

    # labels
    card_title = canvas.create_text(400, 150, text="", font=("Arial", 20, "italic"))
    card_word = canvas.create_text(400, 263, text="", font=("Arial", 40, "bold"))
    # card_title.place(x=350, y=180)
    # card_word.place(x=320, y=243)

    # flip_card()
    # button

    right_button = Button(image=right, highlightthickness=0, command=is_known)
    right_button.grid(padx=50, column=2, row=1)

    wrong_button = Button(image=wrong, highlightthickness=0, command=random_fren)
    wrong_button.grid(padx=50, column=1, row=1)

    random_fren()

# flip_card()
except tkinter.TclError:
    print("Invalid Input")

windows.mainloop()
