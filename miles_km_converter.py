from tkinter import *


def on_calculate_btn_click():
    miles = float(user_input.get())
    km = round((miles * 1.609), 1)
    value_label.config(text=km)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=300)
window.config(padx=50, pady=50)

user_input = Entry(font=20)
# user_input.config(padx=20, pady=20)
user_input.grid(column=1, row=0)


miles_label = Label(text="Miles")
miles_label.config(padx=20, pady=20)
miles_label.grid(column=2, row=0)


is_equal_to_label = Label(text="is equal to")
is_equal_to_label.config(padx=20, pady=20)
is_equal_to_label.grid(column=0, row=1)


value_label = Label(text="0")
value_label.config(padx=20, pady=20, font=20)
value_label.grid(column=1, row=1)


km_label = Label(text="Km")
km_label.config(padx=20, pady=20)
km_label.grid(column=2, row=1)


calculate_btn = Button(text="Calculate", command=on_calculate_btn_click)
# calculate_btn.config(padx=20, pady=20)
calculate_btn.grid(column=1, row=2)


window.mainloop()
