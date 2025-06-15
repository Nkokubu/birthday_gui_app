import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_birthday():
    birth_input = entry.get()
    try:
        birth_date = datetime.strptime(birth_input, "%Y-%m-%d").date()
        today = datetime.today().date()

        # Calculate age
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        # Next birthday
        next_birthday = birth_date.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)

        days_until = (next_birthday - today).days

        result = f"🎂 You are {age} years old!\n" \
                 f"⏳ Your next birthday is in {days_until} day(s)! 🎉"

        result_label.config(text=result)
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter date in YYYY-MM-DD format.")

# GUI setup
root = tk.Tk()
root.title("🎉 Birthday Countdown App")
root.geometry("400x250")
root.resizable(False, False)

# Title label
title = tk.Label(root, text="🎈 Birthday Countdown 🎈", font=("Helvetica", 16, "bold"))
title.pack(pady=10)

# Entry
entry_label = tk.Label(root, text="Enter your birthdate (YYYY-MM-DD):", font=("Helvetica", 12))
entry_label.pack()
entry = tk.Entry(root, font=("Helvetica", 12), width=20, justify='center')
entry.pack(pady=5)

# Button
calc_button = tk.Button(root, text="Calculate 🎂", font=("Helvetica", 12), command=calculate_birthday)
calc_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 12), fg="blue")
result_label.pack(pady=10)

# Start GUI
root.mainloop()
