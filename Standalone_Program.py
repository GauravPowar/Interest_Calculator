import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_interest():
    try:
        P = float(principal_entry.get()) if principal_entry.get() else None
        R = float(rate_entry.get()) if rate_entry.get() else None
        T = float(time_entry.get()) if time_entry.get() else None
        time_unit = time_unit_var.get()
        result = float(result_entry.get()) if result_entry.get() else None

        if time_unit == "Months":
            T = T / 12
        elif time_unit == "Days":
            T = T / 365
        
        if interest_type_var.get() == "Simple Interest":
            if not result:
                result = (P * R * T) / 100
                result_label.config(text=f"Simple Interest: {result:.2f}")
            elif not P:
                P = (result * 100) / (R * T)
                result_label.config(text=f"Principal: {P:.2f}")
            elif not R:
                R = (result * 100) / (P * T)
                result_label.config(text=f"Rate: {R:.2f}%")
            elif not T:
                T = (result * 100) / (P * R)
                result_label.config(text=f"Time: {T:.2f} years")
        else:
            if not result:
                result = P * (1 + R / 100) ** T
                result_label.config(text=f"Compound Amount: {result:.2f}")
            elif not P:
                P = result / (1 + R / 100) ** T
                result_label.config(text=f"Principal: {P:.2f}")
            elif not R:
                R = (result / P) ** (1 / T) - 1
                result_label.config(text=f"Rate: {R * 100:.2f}%")
            elif not T:
                T = (result / P) ** (1 / (1 + R / 100))
                result_label.config(text=f"Time: {T:.2f} years")
    except Exception as e:
        messagebox.showerror("Error", "Please enter valid numbers.")

def toggle_dark_mode():
    if dark_mode_var.get():
        root.config(bg="#222")
        for widget in root.winfo_children():
            widget.config(bg="#222", fg="white")
    else:
        root.config(bg="white")
        for widget in root.winfo_children():
            widget.config(bg="white", fg="black")

root = tk.Tk()
root.title("Interest Calculator")
root.geometry("350x400")

interest_type_var = tk.StringVar(value="Simple Interest")
time_unit_var = tk.StringVar(value="Years")
dark_mode_var = tk.BooleanVar()

# Widgets
interest_type_menu = ttk.Combobox(root, textvariable=interest_type_var, values=["Simple Interest", "Compound Interest"])
interest_type_menu.pack()

principal_entry = tk.Entry(root)
principal_entry.pack()
principal_entry.insert(0, "Enter Principal")

rate_entry = tk.Entry(root)
rate_entry.pack()
rate_entry.insert(0, "Enter Rate (% p.a.)")

time_entry = tk.Entry(root)
time_entry.pack()
time_entry.insert(0, "Enter Time")

time_unit_menu = ttk.Combobox(root, textvariable=time_unit_var, values=["Years", "Months", "Days"])
time_unit_menu.pack()

result_entry = tk.Entry(root)
result_entry.pack()
result_entry.insert(0, "Enter Interest/Amount")

calculate_button = tk.Button(root, text="Calculate", command=calculate_interest)
calculate_button.pack()

toggle_dark_button = tk.Checkbutton(root, text="Dark Mode", variable=dark_mode_var, command=toggle_dark_mode)
toggle_dark_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
