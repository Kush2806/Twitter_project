import tkinter as tk

users = []

def register():
    register_window = tk.Toplevel(main_window)
    register_window.title("Registration Form")
    register_window.geometry("1000x500")

    username_label = tk.Label(register_window, text="Username")
    username_label.pack(pady=10)
    username_entry = tk.Entry(register_window)
    username_entry.pack(pady=5)

    mobile_label = tk.Label(register_window, text="Mobile No.")
    mobile_label.pack(pady=10)
    mobile_entry = tk.Entry(register_window)
    mobile_entry.pack(pady=5)

    new_password_label = tk.Label(register_window, text="New Password")
    new_password_label.pack(pady=10)
    new_password_entry = tk.Entry(register_window, show="*")
    new_password_entry.pack(pady=5)

    confirm_password_label = tk.Label(register_window, text="Confirm Password")
    confirm_password_label.pack(pady=10)
    confirm_password_entry = tk.Entry(register_window, show="*")
    confirm_password_entry.pack(pady=5)

    def save_data():
        username = username_entry.get()
        mobile_no = mobile_entry.get()
        new_password = new_password_entry.get()
        confirm_password = confirm_password_entry.get()

        if not username or not mobile_no or not new_password or not confirm_password:
            return "Please fill all fields."

        if len(new_password) < 8:
            return "Password must be at least 8 characters long."
        if not any(char.isdigit() for char in new_password):
            return "Password must contain at least one digit."
        if not any(char.isupper() for char in new_password):
            return "Password must contain at least one uppercase letter."
        if not any(char.islower() for char in new_password):
            return "Password must contain at least one lowercase letter."

        if new_password != confirm_password:
            return "Passwords do not match."

        if not mobile_no.isnumeric() or len(mobile_no) != 10:
            return "Mobile number is invalid."
        
        for user in users:
            if user['username'] == username:
                return "Username already taken."

        new_user = {'username': username, 'mobile_no': mobile_no, 'password': new_password}
        users.append(new_user)
        register_window.destroy()
        message_label.config(text="Registration successful!", fg="green")

    save_button = tk.Button(register_window, text="Save", font=("Helvetica", 14), bg="#1da1f2", fg="#ffffff", command=save_data)
    save_button.pack(pady=20)

def login():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        message_label.config(text="Please fill all fields.")
        return

    for user in users:
        if user['username'] == username:
            if user['password'] == password:
                message_label.config(text="Login successful!", fg="green")
                return
            else:
                message_label.config(text="Incorrect password.")
                return

    message_label.config(text="User does not exist.Please Sign up First!!")

main_window = tk.Tk()
main_window.title("Twitter Clone")
main_window.geometry("800x600")

background_image = tk.PhotoImage(file="twitter1.png")
background_label = tk.Label(main_window, image=background_image)
background_label.place(relx=.5, rely=0.2, anchor="center")
background_label_width = background_image.width() // 2
background_label_height = background_image.height() // 2
background_label.config(width=background_label_width, height=background_label_height)

username_label = tk.Label(main_window, text="Username", font=("Helvetica", 14), bg="#ffffff", fg="#1da1f2")
username_label.place(relx=0.5, rely=0.3, anchor="center")
username_entry = tk.Entry(main_window, font=("Helvetica", 14))
username_entry.place(relx=0.5, rely=0.37, anchor="center")

password_label = tk.Label(main_window, text="Password", font=("Helvetica", 14), bg="#ffffff", fg="#1da1f2")
password_label.place(relx=0.5, rely=0.45, anchor="center")
password_entry = tk.Entry(main_window, show="*", font=("Helvetica", 14))
password_entry.place(relx=0.5, rely=0.52, anchor="center")

login_button = tk.Button(main_window, text="Log in", font=("Helvetica", 14), bg="#1da1f2", fg="#ffffff", command=login)
login_button.place(relx=0.5, rely=0.6, anchor="center", width=200, height=40)

register_button = tk.Button(main_window, text="Sign up", font=("Helvetica", 14), bg="#ffffff", fg="#1da1f2", command=register, borderwidth=0)
register_button.place(relx=0.5, rely=0.7, anchor="center", width=200, height=40)

message_label = tk.Label(main_window, text="", font=("Helvetica", 12), bg="#ffffff")
message_label.place(relx=0.5, rely=0.8, anchor="center")

main_window.mainloop()

register_button = tk.Button(main_window, text="Sign up", font=("Helvetica", 14), bg="#ffffff", fg="#1da1f2", command=register, borderwidth=0)
register_button.place(relx=0.5, rely=0.7, anchor="center", width=200, height=40)

message_label = tk.Label(main_window, text="", font=("Helvetica", 12), bg="#ffffff")
message_label.place(relx=0.5, rely=0.8, anchor="center")

main_window.mainloop()
