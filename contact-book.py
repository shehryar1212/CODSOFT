import tkinter as tk
from tkinter import messagebox

class ContactManager(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Contact Manager")
        self.geometry("500x300")

        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        self.label_name = tk.Label(self, text="Name:",font="System 15 bold")
        self.label_name.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_phone = tk.Label(self, text="Phone:",font="System 15 bold")
        self.label_phone.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_phone = tk.Entry(self)
        self.entry_phone.grid(row=1, column=1, padx=5, pady=5)

        self.label_email = tk.Label(self, text="Email:",font="System 15 bold")
        self.label_email.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_email = tk.Entry(self)
        self.entry_email.grid(row=2, column=1, padx=5, pady=5)

        self.label_address = tk.Label(self, text="Address:",font="System 15 bold")
        self.label_address.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.entry_address = tk.Entry(self)
        self.entry_address.grid(row=3, column=1, padx=5, pady=5)

        self.button_add = tk.Button(self, text="Add Contact", command=self.add_contact,font="System 15 bold")
        self.button_add.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.button_view = tk.Button(self, text="View Contact List", command=self.view_contacts,font="System 15 bold")
        self.button_view.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.label_search = tk.Label(self, text="Search:",font="System 15 bold")
        self.label_search.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.entry_search = tk.Entry(self)
        self.entry_search.grid(row=6, column=1, padx=5, pady=5)

        self.button_search = tk.Button(self, text="Search", command=self.search_contact,font="System 15 bold")
        self.button_search.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if name and phone:
            self.contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
            messagebox.showinfo("Success", "Contact added successfully.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and phone number are required.")

    def view_contacts(self):
        if self.contacts:
            contacts_list = "\n".join([f"Name: {contact['Name']}, Phone: {contact['Phone']}" for contact in self.contacts])
            messagebox.showinfo("Contacts", contacts_list)
        else:
            messagebox.showinfo("Contacts", "No contacts available.")

    def search_contact(self):
        search_term = self.entry_search.get()
        if search_term:
            search_results = [contact for contact in self.contacts if search_term in contact["Name"] or search_term in contact["Phone"]]
            if search_results:
                result_str = "\n".join([f"Name: {contact['Name']}, Phone: {contact['Phone']}" for contact in search_results])
                messagebox.showinfo("Search Results", result_str)
            else:
                messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            messagebox.showerror("Error", "Please enter a search term.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

if __name__ == "__main__":
    app = ContactManager()
    app.mainloop()
