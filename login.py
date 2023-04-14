import tkinter as tk

users = []

def register():
    username = username_entry.get()
    password = password_entry.get()
    for user in users:
        if user['username'] == username:
            message_label.config(text="Username already exists. Please choose a different username.", fg="red")
            return
    new_user = {'username': username, 'password': password}
    users.append(new_user)
    message_label.config(text="Registration successful!", fg="green")
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def login():
    username = username_entry.get()
    password = password_entry.get()
    for user in users:
        if user['username'] == username and user['password'] == password:
            message_label.config(text="Login successful!", fg="green")
            return
    message_label.config(text="Incorrect username or password. Please try again.", fg="red")

root = tk.Tk()
root.title("Twitter Clone")

background_image = tk.PhotoImage(file="twitter1.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relx=.5, rely=0.2, anchor="center")
background_label_width = background_image.width() // 2
background_label_height = background_image.height() // 2
background_label.config(width=background_label_width, height=background_label_height)

username_label = tk.Label(root, text="Username", font=("Helvetica", 14), bg="#ffffff", fg="#1da1f2")
username_label.place(relx=0.5, rely=0.3, anchor="center")
username_entry = tk.Entry(root, font=("Helvetica", 14))
username_entry.place(relx=0.5, rely=0.37, anchor="center")

password_label = tk.Label(root, text="Password", font=("Helvetica", 14), bg="#ffffff", fg="#1da1f2")
password_label.place(relx=0.5, rely=0.45, anchor="center")
password_entry = tk.Entry(root, show="*", font=("Helvetica", 14))
password_entry.place(relx=0.5, rely=0.52, anchor="center")

login_button = tk.Button(root, text="Log in", font=("Helvetica", 14), bg="#1da1f2", fg="#ffffff", command=login)
login_button.place(relx=0.5, rely=0.6, anchor="center", width=200, height=40)
register_button = tk.Button(root, text="Sign up", font=("Helvetica", 14), bg="#ffffff", fg="#1da1f2", command=register, borderwidth=0)
register_button.place(relx=0.5, rely=0.7, anchor="center", width=200, height=40)

message_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#ffffff")
message_label.place(relx=0.5, rely=0.8, anchor="center")

root.mainloop()
