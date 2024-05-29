import tkinter as tk
from tkinter import messagebox

# Function to handle login button click
def login():
    username = username_entry.get()
    password = password_entry.get()

    # For demonstration, let's check if the username and password are not empty
    if username and password:
        messagebox.showinfo("Login Successful", "Welcome back, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Please enter both username and password.")

# Create the main window
root = tk.Tk()
root.title("Instagram Login")

# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Login button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()
