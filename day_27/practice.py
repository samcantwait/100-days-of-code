import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

FONT = ("Poiret One", 16, "bold")

miles = tkinter.Entry(width=10)
miles.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles", font=FONT, padx=10, pady=10)
miles_label.grid(column=2, row=0)

equals_label = tkinter.Label(text="is equal to", font=FONT, padx=10, pady=10)
equals_label.grid(column=0, row=1)

km_total = tkinter.Label(font=FONT, padx=10, pady=10)
km_total.grid(column=1, row=1)

km = tkinter.Label(font=FONT, text="Km", padx=10, pady=10)
km.grid(column=2, row=1)


def calculate():
    total_miles = float(miles.get())
    converted_miles = round(total_miles * 1.60934)
    km_total.config(text=converted_miles)


button = tkinter.Button(text="Calculate", command=calculate, padx=10, pady=10)
button.grid(column=1, row=2)

window.mainloop()
