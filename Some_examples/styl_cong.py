import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Style Example")

# Create a Style object
style = ttk.Style()

# Configure a style for buttons
style.configure("TButton",
                font=("Helvetica", 14, "bold"),
                foreground="white",
                background="blue",
                padding=10)

# Configure a style for labels
style.configure("TLabel",
                font=("Arial", 12, "italic"),
                foreground="green")

# Use the defined styles
button = ttk.Button(root, text="Styled Button")
button.pack(pady=10)

label = ttk.Label(root, text="Styled Label")
label.pack(pady=10)

root.mainloop()
