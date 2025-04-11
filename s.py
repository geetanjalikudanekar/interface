import tkinter as tk
<<<<<<< HEAD

# Create the main window
root = tk.Tk()
root.title("Form Alignment Example")

# Create labels and entry fields
labels = ["Name:", "Email:", "Phone:"]
for i, label_text in enumerate(labels):
    # Add the label
    tk.Label(root, text=label_text, anchor="e", width=10).grid(row=i, column=0, padx=10, pady=5, sticky="e")

    # Add the entry
    tk.Entry(root, width=30).grid(row=i, column=1, padx=10, pady=5)

# Add a submit button
tk.Button(root, text="Submit").grid(row=len(labels), column=1, pady=10)
=======
from tkinter import ttk

# Function to reset the ComboBox to its default value
def reset_to_default():
    # Set the default value for the ComboBox
    combobox.set(default_value)

# Create the main window
root = tk.Tk()
root.title("ComboBox Default Example")

# Define the default value
default_value = "Select an item"

# Create a ComboBox with some items
combobox = ttk.Combobox(root, values=["Bun", "Bread", "Croissant"])
combobox.set(default_value)  # Set the default value at the start
combobox.pack(pady=10)

# Add a button to trigger the reset function
reset_button = tk.Button(root, text="Reset to Default", command=reset_to_default)
reset_button.pack(pady=10)
>>>>>>> 9e186adc4a20edb0de5c6a37148401fe86f29fe9

# Run the application
root.mainloop()