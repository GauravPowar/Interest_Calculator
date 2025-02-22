import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def clear_entry(event):
    """Clear default text when entry is clicked."""
    if event.widget.get() in default_texts.values():
        event.widget.delete(0, tk.END)

def reset_result():
    """Clear the result label for new calculations."""
    result_label.config(text="")

def calculate_interest():
    """Perform interest calculations based on user inputs."""
    reset_result()
    try:
        P = float(principal_entry.get()) if principal_entry.get() and principal_entry.get() not in default_texts.values() else None
        R = float(rate_entry.get()) if rate_entry.get() and rate_entry.get() not in default_texts.values() else None
        T = float(time_entry.get()) if time_entry.get() and time_entry.get() not in default_texts.values() else None
        result = float(result_entry.get()) if result_entry.get() and result_entry.get() not in default_texts.values() else None
        time_unit = time_unit_var.get()

        if T is not None:
            if time_unit == "Months":
                T = T / 12
            elif time_unit == "Days":
                T = T / 365

        if interest_type_var.get() == "Simple Interest":
            if result is None:
                result = (P * R * T) / 100
                result_label.config(text=f"Simple Interest: {result:.2f}")
            elif P is None:
                P = (result * 100) / (R * T)
                result_label.config(text=f"Principal: {P:.2f}")
            elif R is None:
                R = (result * 100) / (P * T)
                result_label.config(text=f"Rate: {R:.2f}%")
            elif T is None:
                T = (result * 100) / (P * R)
                result_label.config(text=f"Time: {T:.2f} years")
        else:
            if result is None:
                result = P * (1 + R / 100) ** T
                result_label.config(text=f"Compound Amount: {result:.2f}")
            elif P is None:
                P = result / (1 + R / 100) ** T
                result_label.config(text=f"Principal: {P:.2f}")
            elif R is None:
                R = ((result / P) ** (1 / T) - 1) * 100
                result_label.config(text=f"Rate: {R:.2f}%")
            elif T is None:
                T = (result / P) ** (1 / (1 + R / 100))
                result_label.config(text=f"Time: {T:.2f} years")
    except (ValueError, TypeError):
        messagebox.showerror("Error", "Please enter valid numeric values.")

def toggle_dark_mode():
    """Switch between dark and light mode."""
    bg_color = "#222" if dark_mode_var.get() else "white"
    fg_color = "white" if dark_mode_var.get() else "black"
    
    root.config(bg=bg_color)
    for widget in root.winfo_children():
        try:
            widget.config(bg=bg_color, fg=fg_color)
        except tk.TclError:  # Ignore widgets that don't support direct color changes
            pass

# Initialize main window
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("350x400")

# Variables
interest_type_var = tk.StringVar(value="Simple Interest")
time_unit_var = tk.StringVar(value="Years")
dark_mode_var = tk.BooleanVar()

# Default placeholder text dictionary
default_texts = {
    "principal": "Enter Principal",
    "rate": "Enter Rate (% p.a.)",
    "time": "Enter Time",
    "result": "Enter Interest/Amount"
}

# Widgets
interest_type_menu = ttk.Combobox(root, textvariable=interest_type_var, values=["Simple Interest", "Compound Interest"])
interest_type_menu.pack()

principal_entry = tk.Entry(root)
principal_entry.insert(0, default_texts["principal"])
principal_entry.bind("<FocusIn>", clear_entry)
principal_entry.pack()

rate_entry = tk.Entry(root)
rate_entry.insert(0, default_texts["rate"])
rate_entry.bind("<FocusIn>", clear_entry)
rate_entry.pack()

time_entry = tk.Entry(root)
time_entry.insert(0, default_texts["time"])
time_entry.bind("<FocusIn>", clear_entry)
time_entry.pack()

time_unit_menu = ttk.Combobox(root, textvariable=time_unit_var, values=["Years", "Months", "Days"])
time_unit_menu.pack()

result_entry = tk.Entry(root)
result_entry.insert(0, default_texts["result"])
result_entry.bind("<FocusIn>", clear_entry)
result_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_interest)
calculate_button.pack()

toggle_dark_button = tk.Checkbutton(root, text="Dark Mode", variable=dark_mode_var, command=toggle_dark_mode)
toggle_dark_button.pack()

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

root.mainloop()
