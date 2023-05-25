import tkinter as tk
from io import BytesIO
from tkinter import ttk
from ttkthemes import ThemedStyle
from PIL import ImageTk, Image
import urllib.request
import random

# Function to evaluate the expression
def evaluate_expression():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to handle button clicks
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("425x500")
window.resizable(False, False)

# Apply a themed style to the window
style = ThemedStyle(window)
style.set_theme("arc")

# Load background image from URL
background_url = "https://i.pinimg.com/736x/0a/40/bf/0a40bfa373ce7d545ddcedc96ccb1184.jpg"
background_image_data = urllib.request.urlopen(background_url).read()
background_image = ImageTk.PhotoImage(Image.open(BytesIO(background_image_data)))

# Create the background label
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create the entry field
entry = ttk.Entry(window, font=("Arial", 20), justify="right")
entry.place(x=20, y=20, width=360, height=60)

# Create the button grid
buttons_frame = ttk.Frame(window)
buttons_frame.place(x=20, y=100)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 0
col = 0

for button in buttons:
    if button == '=':
        button_style = 'equal.TButton'
        button_width = 6
        button_command = evaluate_expression
    elif button == '0':
        button_style = 'zero.TButton'
        button_width = 6
        button_command = lambda: button_click(0)
    else:
        button_style = 'normal.TButton'
        button_width = 6
        button_command = lambda button=button: button_click(button)

    ttk.Button(buttons_frame, text=button, style=button_style, width=button_width, command=button_command).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Create the clear button
ttk.Button(window, text="Clear", style='clear.TButton', command=clear_entry).place(x=20, y=350, width=360, height=40)

# Animation
animation_frame = tk.Frame(window, bg="black")
animation_frame.place(x=20, y=400, width=360, height=90)

animation_label = tk.Label(animation_frame, text="Calculator", font=("Arial", 24, "bold"), fg="white", bg="black")
animation_label.pack(pady=10)

# Create the owner label
owner_label = tk.Label(window, text="Made By Coderet D Looper", font=("Arial", 12), fg="white", bg="black")
owner_label.place(x=20, y=460)

# Function to generate random color
def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return '#%02x%02x%02x' % (r, g, b)

# Function to animate the label color
def animate_label():
    color = generate_random_color()
    animation_label.config(fg=color)
    window.after(500, animate_label)

# Start the label animation
animate_label()

# Configure the styles
style.configure('TButton', font=('Arial', 14), foreground='black')
style.configure('equal.TButton', foreground='black', background='#000000')
style.configure('zero.TButton', foreground='black', background='#000000')
style.configure('clear.TButton', foreground='black', background='#000000')

# Run the main loop
window.mainloop()
