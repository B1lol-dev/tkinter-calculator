import tkinter as tk
from tkinter import ttk

# Function to update the text on the screen
def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)  # Clear the screen
    entry.insert(0, current + value)

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())  # Evaluate the mathematical expression
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the screen
def clear():
    entry.delete(0, tk.END)

# Create the window
root = tk.Tk()
root.title("Calculator")

# Style for widgets
style = ttk.Style()
style.configure("TButton",
                font=("Arial", 18),
                padding=10,
                width=5,
                relief="flat",  # Flat buttons
                borderwidth=5)  # Button border thickness

# Style for the input field (Entry)
style.configure("TEntry",
                font=("Arial", 24),
                padding=10,
                relief="flat",
                background="#f0f0f0",  # Light background
                foreground="black",  # Black text color
                borderwidth=5)

# Style for the "=" button
style.configure("Equal.TButton",
                font=("Arial", 18),
                padding=10,
                width=5,
                relief="flat",
                background="#2196F3",  # Blue background color
                foreground="white",
                borderwidth=5)

# Input screen
entry = ttk.Entry(root, width=20, style="TEntry", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Calculator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        button = ttk.Button(root, text=text, command=calculate, style="Equal.TButton")
    elif text == "C":
        button = ttk.Button(root, text=text, command=clear)
    else:
        button = ttk.Button(root, text=text, command=lambda value=text: on_button_click(value))
    
    # Set styles for buttons
    button.grid(row=row, column=col, padx=5, pady=5)

# Set the background color of the window
root.configure(bg="#e3e3e3")

# Start the main loop
root.mainloop()
