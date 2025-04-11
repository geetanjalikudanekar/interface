import tkinter as tk

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

# Run the application
root.mainloop()