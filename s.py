import tkinter as tk
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

# Run the application
root.mainloop()