import tkinter as tk
from tkinter import messagebox, simpledialog

# In-memory contact storage as a dictionary
contacts = {}

# Add contact
def add_contact():
    name = name_var.get().strip()
    phone = phone_var.get().strip()
    email = email_var.get().strip()

    if name == "" or phone == "" or email == "":
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    contacts[name] = {"Phone": phone, "Email": email}
    messagebox.showinfo("Success", f"Contact '{name}' added successfully.")
    clear_entries()
    show_contacts()

# Show all contacts
def show_contacts():
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        contact_list.insert(tk.END, f"{name} - {info['Phone']} - {info['Email']}")

# Delete selected contact
def delete_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Select Contact", "Please select a contact to delete.")
        return
    contact_str = contact_list.get(selected[0])
    name = contact_str.split(" - ")[0]
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Deleted", f"Contact '{name}' deleted.")
        show_contacts()

# Edit selected contact
def edit_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Select Contact", "Please select a contact to edit.")
        return
    contact_str = contact_list.get(selected[0])
    name = contact_str.split(" - ")[0]

    if name in contacts:
        new_phone = simpledialog.askstring("Edit Phone", f"Enter new phone for {name}:", initialvalue=contacts[name]['Phone'])
        new_email = simpledialog.askstring("Edit Email", f"Enter new email for {name}:", initialvalue=contacts[name]['Email'])
        if new_phone and new_email:
            contacts[name] = {"Phone": new_phone, "Email": new_email}
            messagebox.showinfo("Updated", f"Contact '{name}' updated.")
            show_contacts()

# Clear input fields
def clear_entries():
    name_var.set("")
    phone_var.set("")
    email_var.set("")

# GUI setup
window = tk.Tk()
window.title("Contact Management System")
window.geometry("500x400")
window.configure(bg="#e3f2fd")

# Input Fields
name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()

tk.Label(window, text="Name:", bg="#e3f2fd").pack()
tk.Entry(window, textvariable=name_var, width=40).pack()

tk.Label(window, text="Phone:", bg="#e3f2fd").pack()
tk.Entry(window, textvariable=phone_var, width=40).pack()

tk.Label(window, text="Email:", bg="#e3f2fd").pack()
tk.Entry(window, textvariable=email_var, width=40).pack()

# Buttons
tk.Button(window, text="Add Contact", command=add_contact, bg="#4caf50", fg="white").pack(pady=5)
tk.Button(window, text="Edit Contact", command=edit_contact, bg="#2196f3", fg="white").pack(pady=5)
tk.Button(window, text="Delete Contact", command=delete_contact, bg="#f44336", fg="white").pack(pady=5)

# Contact List
tk.Label(window, text="Contact List:", bg="#e3f2fd", font=("Arial", 12, "bold")).pack(pady=10)
contact_list = tk.Listbox(window, width=60)
contact_list.pack()

# Start with empty list
show_contacts()

window.mainloop()