import tkinter as tk
from tkinter import messagebox
import json
import os


class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        self.root.geometry("600x450")

        self.contacts = self.load_contacts()

        self.name_label = tk.Label(root, text="Name")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(root, width=50)
        self.name_entry.pack(pady=5)

        self.phone_label = tk.Label(root, text="Phone Number")
        self.phone_label.pack(pady=5)
        self.phone_entry = tk.Entry(root, width=50)
        self.phone_entry.pack(pady=5)

        self.email_label = tk.Label(root, text="Email Address")
        self.email_label.pack(pady=5)
        self.email_entry = tk.Entry(root, width=50)
        self.email_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=5)

        self.contacts_label = tk.Label(root, text="Contact List", font=('Helvetica', 12, 'bold'))
        self.contacts_label.pack(pady=10)

        self.contacts_listbox = tk.Listbox(root, width=80)
        self.contacts_listbox.pack(pady=10, fill=tk.BOTH, expand=True)
        self.contacts_listbox.bind('<<ListboxSelect>>', self.on_select)

        self.edit_button = tk.Button(root, text="Edit Contact", command=self.edit_contact)
        self.edit_button.pack(pady=5)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)

        self.populate_contacts()

    def load_contacts(self):
        if os.path.exists("contacts.json"):
            with open("contacts.json", "r") as file:
                return json.load(file)
        return []

    def save_contacts(self):
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file)

    def populate_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']} - {contact['email']}")
            self.contacts_listbox.insert(tk.END, "-" * 80)  # Add separator line

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if name and phone and email:
            self.contacts.append({"name": name, "phone": phone, "email": email})
            self.save_contacts()
            self.populate_contacts()
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "All fields are required.")

    def edit_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = selected_index[0] // 2  # Adjust for separator lines
            contact = self.contacts[index]

            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()

            if name and phone and email:
                self.contacts[index] = {"name": name, "phone": phone, "email": email}
                self.save_contacts()
                self.populate_contacts()
                self.clear_entries()
            else:
                messagebox.showwarning("Input Error", "All fields are required.")
        else:
            messagebox.showwarning("Selection Error", "No contact selected.")

    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = selected_index[0] // 2  # Adjust for separator lines
            del self.contacts[index]
            self.save_contacts()
            self.populate_contacts()
        else:
            messagebox.showwarning("Selection Error", "No contact selected.")

    def on_select(self, event):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = selected_index[0] // 2  # Adjust for separator lines
            contact = self.contacts[index]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, contact['name'])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, contact['phone'])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, contact['email'])

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
