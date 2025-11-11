import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Form")
root.geometry("300x250")

# --- Labels and Entry fields ---
tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email:").pack(pady=5)
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Age:").pack(pady=5)
age_entry = tk.Entry(root)
age_entry.pack()

# --- Function to handle submit ---
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    result_label.config(text=f"Name: {name}\nEmail: {email}\nAge: {age}")

# --- Submit Button ---
submit_btn = tk.Button(root, text="Submit", command=submit_form)
submit_btn.pack(pady=10)

# --- Label to show result ---
result_label = tk.Label(root, text="", fg="blue")
result_label.pack(pady=10)

# Run the window
root.mainloop()
