from PIL import Image, ImageTk
import tkinter as tk

window = tk.Tk()
window.geometry("500x500")
window.title("Income Calculator")

biweekly_label = tk.Label(text="Bi-Weekly Income")
biweekly_label.grid(column=0, row=1)

biweekly_entry = tk.Entry()
biweekly_entry.grid(column=1, row=1)

weekly_label = tk.Label(text="Weekly Income")
weekly_label.grid(column=0, row=3)

weekly_entry = tk.Entry()
weekly_entry.grid(column=1, row=3)

hourly_label = tk.Label(text="Hourly Income")
hourly_label.grid(column=0, row=5)

hourly_entry = tk.Entry()
hourly_entry.grid(column=1, row=5)


class Resident:
    def __init__(self, income):
        self.income = income

    def biweekly(self):
        income = float(biweekly_entry.get())
        annual = income * 26
        monthly = annual / 12
        return "$ {} a month".format(round(monthly, 2))

    def weekly(self):
        income = float(weekly_entry.get())
        annual = income * 52
        monthly = annual / 12
        return "$ {} a month".format(round(monthly, 2))

    def hourly(self):
        income = float(hourly_entry.get())
        week = income * 40
        annual = week * 52
        monthly = annual / 12
        return "$ {} a month".format(round(monthly, 2))


def calculate_biweekly_income():
    wage = Resident(biweekly_entry)

    text_answer = tk.Text(master=window, height=5, width=20)
    text_answer.grid(column=1, row=7)
    text_answer.insert(tk.END, wage.biweekly())


def calculate_weekly_income():
    wage = Resident(weekly_entry)

    text_answer = tk.Text(master=window, height=5, width=20)
    text_answer.grid(column=1, row=7)
    text_answer.insert(tk.END, wage.weekly())


def calculate_hourly_income():
    wage = Resident(hourly_entry)

    text_answer = tk.Text(master=window, height=5, width=20)
    text_answer.grid(column=1, row=7)
    text_answer.insert(tk.END, wage.hourly())


calculate_biweekly_button = tk.Button(bg='light green', bd=3, text="Calculate", command=calculate_biweekly_income)
calculate_biweekly_button.grid(column=1, row=2, pady=(10, 10))

calculate_weekly_button = tk.Button(bg='light green', bd=3, text="Calculate", command=calculate_weekly_income)
calculate_weekly_button.grid(column=1, row=4, pady=(10, 10))

calculate_hourly_button = tk.Button(bg='light green', bd=3, text="Calculate", command=calculate_hourly_income)
calculate_hourly_button.grid(column=1, row=6, pady=(10, 10))

image = Image.open('/Users/chala/Downloads/income_calculator_app.jpg')
image.thumbnail((250, 200), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0, pady=(10, 20))


window.mainloop()