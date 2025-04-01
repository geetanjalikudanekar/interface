import tkinter as tk

root = tk.Tk()

# Load an image (make sure the file path is correct and the image is in .png format)
icon = tk.PhotoImage(file="C:/Users/vaibk/OneDrive/Desktop/Harris-Logo_Website.png")  # Replace "icon.png" with your image file's name

# Create a button with the image
button = tk.Button(root, image=icon, text="Click Me", compound="top")  # 'compound' positions text relative to the image
button.pack(pady=10)

# Create a label with the image
label = tk.Label(root, image=icon, text="Hello!", compound="bottom")  # Display text below the image
label.pack(pady=10)

root.mainloop()
