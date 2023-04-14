def login():
    username = username_entry.get()
    password = password_entry.get()

    # check if username and password are filled
    if not username or not password:
        message_label.config(text="Please fill all fields.")
        return

    # check if user exists in the database
    for user in users:
        if user['username'] == username:
            # check if password matches
            if user['password'] == password:
                message_label.config(text="Login successful!", fg="green")
                # do something after successful login, e.g. open a new window
                return
            else:
                message_label.config(text="Incorrect password.")
                return

    message_label.config(text="User does not exist.")
