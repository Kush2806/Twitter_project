def register():
    register_window = tk.Toplevel(root)
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

        # Check if new password meets complexity requirements
        if len(new_password) < 8:
            return "Password must be at least 8 characters long."
        if not any(char.isdigit() for char in new_password):
            return "Password must contain at least one digit."
        if not any(char.isupper() for char in new_password):
            return "Password must contain at least one uppercase letter."
        if not any(char.islower() for char in new_password):
            return "Password must contain at least one lowercase letter."

        # Check if new password matches confirm password
        if new_password != confirm_password:
            return "Passwords do not match."

        # Check if mobile no. is valid
        if not mobile_no.isnumeric() or len(mobile_no) != 10:
            return "Mobile number is invalid."
        
        # Check if username is already taken
        for user in users:
            if user['username'] == username:
                return "Username already taken."

        # if validation is successful, add user to the database
        new_user = {'username': username, 'mobile_no': mobile_no, 'password': new_password}
        users.append(new_user)
        register_window.destroy()
        message_label.config(text="Registration successful!", fg="green")

    save_button = tk.Button(register_window, text="Save", font=("Helvetica", 14), bg="#1da1f2", fg="#ffffff", command=save_data)
    save_button.pack(pady=20)