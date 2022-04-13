import tkinter as tk
from tkinter import Frame, ttk
import tkinter.font as font

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


root = tk.Tk()
root.title("Leap year tester")


# font
font.nametofont("TkDefaultFont").configure(size=15)


# Tests if the year given is a leap year
from leap_year_tester import is_leap_year
year_input = tk.Entry()
year_output = tk.StringVar()

def button_action():
        year = year_input.get()
        year = int(year)
        if is_leap_year(year):
            year_output.set("Yes it is")
        else:
            year_output.set("No it's not")

test_button = tk.Button(text='Test if leap year', command=button_action)

# borders
main = ttk.Frame(root, padding=(30, 15))
main.grid()

root.columnconfigure(0, weight=1)

# Theme
style = ttk.Style(root)
print(style.theme_names())
print(style.theme_use('xpnative'))



# Widgets
year_label = ttk.Label(main, text="Year: ")
year_input = ttk.Entry(main, width=10, font=15)
leapyear_label = ttk.Label(main, text="is it a leap year?")
leapyear_display = ttk.Label(main, textvariable=year_output)
test_button = ttk.Button(main, text="Test", command=button_action)


# Layout
year_label.grid(column=0, row=0, sticky="w", padx=5, pady=5)
year_input.grid(column=1, row=0, sticky="EW", padx=5, pady=5)
year_input.focus()

leapyear_label.grid(column=0, row=1, sticky="w", padx=5, pady=5)
leapyear_display.grid(column=1, row=1, sticky="EW", padx=5, pady=5)

test_button.grid(column=0, row=2, columnspan=2, sticky="EW", padx=5, pady=5)


root.mainloop()