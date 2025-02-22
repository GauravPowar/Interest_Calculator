import tkinter as tk
from tkinter import ttk, messagebox

def clear_entry(event):
    if event.widget.get() in default_texts.values():
        event.widget.delete(0, tk.END)

def reset_result():
    result_label.config(text="", fg="black")

def calculate_interest():
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
                result_label.config(text=f"Simple Interest: {result:.2f}", fg="green")
            elif P is None:
                P = (result * 100) / (R * T)
                result_label.config(text=f"Principal: {P:.2f}", fg="blue")
            elif R is None:
                R = (result * 100) / (P * T)
                result_label.config(text=f"Rate: {R:.2f}%", fg="blue")
            elif T is None:
                T = (result * 100) / (P * R)
                result_label.config(text=f"Time: {T:.2f} years", fg="blue")
        else:
            if result is None:
                result = P * (1 + R / 100) ** T
                result_label.config(text=f"Compound Amount: {result:.2f}", fg="green")
            elif P is None:
                P = result / (1 + R / 100) ** T
                result_label.config(text=f"Principal: {P:.2f}", fg="blue")
            elif R is None:
                R = ((result / P) ** (1 / T) - 1) * 100
                result_label.config(text=f"Rate: {R:.2f}%", fg="blue")
            elif T is None:
                T = (result / P) ** (1 / (1 + R / 100))
                result_label.config(text=f"Time: {T:.2f} years", fg="blue")
    except (ValueError, TypeError):
        messagebox.showerror("Error", "Please enter valid numeric values.")

def toggle_dark_mode():
    bg_color = "#2E2E2E" if dark_mode_var.get() else "#F5F5F5"
    fg_color = "#FFFFFF" if dark_mode_var.get() else "#000000"
    button_bg = "#555" if dark_mode_var.get() else "#DDD"
    result_label.config(bg=bg_color, fg=fg_color)
    root.config(bg=bg_color)
    main_frame.config(bg=bg_color)
    for widget in main_frame.winfo_children():
        try:
            widget.config(bg=bg_color, fg=fg_color)
            if isinstance(widget, ttk.Button):
                widget.config(style="TButton")
        except tk.TclError:
            pass

root = tk.Tk()
root.title("Interest Calculator")
root.geometry("400x450")
root.resizable(False, False)
root.configure(bg="#F5F5F5")

dark_mode_var = tk.BooleanVar()
interest_type_var = tk.StringVar(value="Simple Interest")
time_unit_var = tk.StringVar(value="Years")

default_texts = {
    "principal": "Enter Principal",
    "rate": "Enter Rate (% p.a.)",
    "time": "Enter Time",
    "result": "Enter Interest/Amount"
}

style = ttk.Style()
style.configure("TButton", font=("Arial", 10, "bold"), padding=5, background="#DDD")
style.configure("TLabel", background="#F5F5F5", font=("Arial", 10))

main_frame = tk.Frame(root, padx=15, pady=15, bg="#F5F5F5")
main_frame.pack(expand=True, fill=tk.BOTH)

ttk.Label(main_frame, text="Interest Type:").pack()
interest_type_menu = ttk.Combobox(main_frame, textvariable=interest_type_var, values=["Simple Interest", "Compound Interest"])
interest_type_menu.pack()

def create_entry(placeholder):
    entry = ttk.Entry(main_frame, font=("Arial", 10))
    entry.insert(0, placeholder)
    entry.bind("<FocusIn>", clear_entry)
    entry.pack(pady=5, ipady=3)
    return entry

principal_entry = create_entry(default_texts["principal"])
rate_entry = create_entry(default_texts["rate"])
time_entry = create_entry(default_texts["time"])

ttk.Label(main_frame, text="Time Unit:").pack()
time_unit_menu = ttk.Combobox(main_frame, textvariable=time_unit_var, values=["Years", "Months", "Days"])
time_unit_menu.pack()

result_entry = create_entry(default_texts["result"])

ttk.Button(main_frame, text="Calculate", command=calculate_interest).pack(pady=10)

toggle_dark_button = ttk.Checkbutton(main_frame, text="Dark Mode", variable=dark_mode_var, command=toggle_dark_mode)
toggle_dark_button.pack()

result_label = tk.Label(main_frame, text="", font=("Arial", 12, "bold"), bg="#F5F5F5")
result_label.pack(pady=10)

root.mainloop()
