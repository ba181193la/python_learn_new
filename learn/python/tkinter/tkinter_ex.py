# import tkinter as tk

# window = tk.Tk()

# window.title("My First App")
# window.geometry("400x300")

# label = tk.Label(
#     window,
#     text="Hello Bala!"
# )

# label.pack()

# window.mainloop()
import tkinter as tk


def calculate_salary():
    name = name_input.get()
    salary = float(salary_input.get())
    hike = float(hike_input.get())

    hike_amount = salary * hike / 100
    new_salary = salary + hike_amount

    result.config(
        text=f"{name}'s New Salary: ₹{new_salary:.2f}"
    )


window = tk.Tk()

window.title("Employee Salary Calculator")
window.geometry("400x350")


# Employee Name
tk.Label(
    window,
    text="Employee Name"
).pack()

name_input = tk.Entry(window)
name_input.pack()


# Basic Salary
tk.Label(
    window,
    text="Basic Salary"
).pack()

salary_input = tk.Entry(window)
salary_input.pack()


# Hike Percentage
tk.Label(
    window,
    text="Hike Percentage"
).pack()

hike_input = tk.Entry(window)
hike_input.pack()


# Calculate Button
tk.Button(
    window,
    text="Calculate Salary",
    command=calculate_salary
).pack()


# Result
result = tk.Label(
    window,
    text=""
)

result.pack()


window.mainloop()