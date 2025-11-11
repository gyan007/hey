import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

class ValidationFormApp:
    """
    A Tkinter GUI application for a user input form with validation.
    """
    
    def __init__(self, root):
        self.root = root
        self.root.title("User Validation Form")
        self.root.geometry("420x280")
        
        # Use the 'clam' theme for a slightly more modern look
        style = ttk.Style()
        style.theme_use('clam')

        # Create a main frame with padding
        main_frame = ttk.Frame(self.root, padding="20 20 20 20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights for resizing
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        # --- Model Variables ---
        # Create string variables to hold the content of the entry fields
        self.name = tk.StringVar()
        self.email = tk.StringVar()
        self.contact = tk.StringVar()
        self.pan = tk.StringVar()

        # --- Form Widgets ---
        
        # Name
        ttk.Label(main_frame, text="Name:").grid(row=0, column=0, sticky=tk.W, pady=5)
        name_entry = ttk.Entry(main_frame, width=40, textvariable=self.name)
        name_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))
        
        # Email
        ttk.Label(main_frame, text="Email:").grid(row=1, column=0, sticky=tk.W, pady=5)
        email_entry = ttk.Entry(main_frame, width=40, textvariable=self.email)
        email_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

        # Contact Number
        ttk.Label(main_frame, text="Contact No:").grid(row=2, column=0, sticky=tk.W, pady=5)
        contact_entry = ttk.Entry(main_frame, width=40, textvariable=self.contact)
        contact_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))
        
        # PAN Card
        ttk.Label(main_frame, text="PAN Card:").grid(row=3, column=0, sticky=tk.W, pady=5)
        pan_entry = ttk.Entry(main_frame, width=40, textvariable=self.pan)
        pan_entry.grid(row=3, column=1, sticky=(tk.W, tk.E))

        # Submit Button
        submit_button = ttk.Button(main_frame, text="Submit", command=self.submit_form)
        submit_button.grid(row=4, column=1, sticky=tk.E, pady=20)
        
        # Set focus to the first entry field
        name_entry.focus_set()

    def validate_email(self, email):
        """Validates email using regex."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email)

    def validate_contact(self, number):
        """Validates Indian contact number using regex."""
        pattern = r'^(\+91[\-\s]?)?[0]?[6-9]\d{9}$'
        return re.match(pattern, number)
        
    def validate_pan(self, pan):
        """Validates PAN card number using regex."""
        pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
        return re.match(pattern, pan)

    def submit_form(self):
        """
        Called when the submit button is pressed.
        Performs validation and shows appropriate messages.
        """
        # Get data from the StringVars
        name_val = self.name.get()
        email_val = self.email.get()
        contact_val = self.contact.get()
        pan_val = self.pan.get().upper() # PAN is always uppercase
        
        # --- Validation Chain ---
        
        # 1. Validate Name (simple non-empty check)
        if not name_val:
            messagebox.showerror("Validation Error", "Name field cannot be empty.")
            return
            
        # 2. Validate Email
        if not self.validate_email(email_val):
            messagebox.showerror("Validation Error", "Invalid Email format.")
            return
            
        # 3. Validate Contact
        if not self.validate_contact(contact_val):
            messagebox.showerror("Validation Error", "Invalid Contact Number.\n(Format: +91XXXXXXXXXX or XXXXXXXXXX)")
            return
            
        # 4. Validate PAN
        if not self.validate_pan(pan_val):
            messagebox.showerror("Validation Error", "Invalid PAN Card format.\n(Format: ABCDE1234F)")
            return

        # --- All Validations Passed ---
        success_message = (
            "Submission Successful!\n"
            f"\nName: {name_val}"
            f"\nEmail: {email_val}"
            f"\nContact: {contact_val}"
            f"\nPAN: {pan_val}"
        )
        messagebox.showinfo("Success", success_message)
        
        # Optionally, clear the form after successful submission
        self.clear_form()
        
    def clear_form(self):
        """Clears all entry fields."""
        self.name.set("")
        self.email.set("")
        self.contact.set("")
        self.pan.set("")

# --- Main execution ---
if __name__ == "__main__":
    root = tk.Tk()
    app = ValidationFormApp(root)
    root.mainloop()