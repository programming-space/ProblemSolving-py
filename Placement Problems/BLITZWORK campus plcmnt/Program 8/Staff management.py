import tkinter as tk
from tkinter import messagebox

class StaffManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Staff Information Management System")

        # Variables to store staff information
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.qualifications_var = tk.StringVar()
        self.role_var = tk.StringVar()
        self.contact_var = tk.StringVar()

        # Create labels and entry widgets for staff information
        tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.name_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.age_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Qualifications:").grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.qualifications_var).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Role:").grid(row=3, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.role_var).grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Contact:").grid(row=4, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.contact_var).grid(row=4, column=1, padx=10, pady=5)

        # Create buttons for adding and updating staff
        tk.Button(root, text="Add Staff", command=self.add_staff).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Update Staff", command=self.update_staff).grid(row=6, column=0, columnspan=2, pady=10)

    def add_staff(self):
        # Get staff information from entry widgets
        name = self.name_var.get()
        age = self.age_var.get()
        qualifications = self.qualifications_var.get()
        role = self.role_var.get()
        contact = self.contact_var.get()

        # Display staff information (you can replace this with storing the information in a database)
        messagebox.showinfo("Staff Information", f"Name: {name}\nAge: {age}\nQualifications: {qualifications}\nRole: {role}\nContact: {contact}")

        # Clear entry widgets
        self.clear_entries()

    def update_staff(self):
        # Get staff information from entry widgets
        name = self.name_var.get()
        age = self.age_var.get()
        qualifications = self.qualifications_var.get()
        role = self.role_var.get()
        contact = self.contact_var.get()

        # Display staff information (you can replace this with updating the information in a database)
        messagebox.showinfo("Staff Information", f"Updated Information:\nName: {name}\nAge: {age}\nQualifications: {qualifications}\nRole: {role}\nContact: {contact}")

        # Clear entry widgets
        self.clear_entries()

    def clear_entries(self):
        # Clear entry widgets
        self.name_var.set("")
        self.age_var.set("")
        self.qualifications_var.set("")
        self.role_var.set("")
        self.contact_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = StaffManagementApp(root)
    root.mainloop()
