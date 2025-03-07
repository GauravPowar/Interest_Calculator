import tkinter as tk
import random

# Funny messages
funny_messages = [
    "That's cute! 😆",
    "Try aiming higher! 🚀",
    "Even my pet goldfish can count higher! 🐠",
    "Is that your final answer? 😜",
    "Math is hard, isn't it? 🤓",
    "You call that a number? 😂",
    "Even a snail moves faster than this calculation! 🐌",
    "Oof, too low! Try again! 😬"
]

def append_value(value):
    entry_var.set(entry_var.get() + str(value))
    message_label.config(text="")

def clear_display():
    entry_var.set("")
    message_label.config(text="")

def calculate():
    try:
        expression = entry_var.get().replace("%", "/100")
        result = eval(expression)
        if result < 100:
            message_label.config(text=random.choice(funny_messages))
        entry_var.set(result)
    except:
        entry_var.set("Error")
        message_label.config(text="")

# GUI Setup
root = tk.Tk()
root.title("Funny Calculator")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4)

message_label = tk.Label(root, text="", font=("Arial", 12), fg="red")
message_label.grid(row=1, column=0, columnspan=4)

buttons = [
    ("AC", 2, 0, clear_display), ("(", 2, 1, lambda: append_value("(")), (")", 2, 2, lambda: append_value(")")), ("%", 2, 3, lambda: append_value("%")),
    ("7", 3, 0, lambda: append_value("7")), ("8", 3, 1, lambda: append_value("8")), ("9", 3, 2, lambda: append_value("9")), ("/", 3, 3, lambda: append_value("/")),
    ("4", 4, 0, lambda: append_value("4")), ("5", 4, 1, lambda: append_value("5")), ("6", 4, 2, lambda: append_value("6")), ("*", 4, 3, lambda: append_value("*")),
    ("1", 5, 0, lambda: append_value("1")), ("2", 5, 1, lambda: append_value("2")), ("3", 5, 2, lambda: append_value("3")), ("-", 5, 3, lambda: append_value("-")),
    ("0", 6, 0, lambda: append_value("0")), (".", 6, 1, lambda: append_value(".")), ("=", 6, 2, calculate), ("+", 6, 3, lambda: append_value("+"))
]

for (text, row, col, cmd) in buttons:
    tk.Button(root, text=text, font=("Arial", 16), command=cmd, width=5, height=2).grid(row=row, column=col)

root.mainloop()
