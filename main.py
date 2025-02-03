import tkinter as tk

# Function to update the text on the screen
def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)  # Clear the screen
    entry.insert(0, current + value)

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())  # Execute the mathematical expression
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

# Input screen
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

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
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=calculate)
    elif text == "C":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=clear)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda value=text: on_button_click(value))
    button.grid(row=row, column=col)

# Start the main loop
root.mainloop()
