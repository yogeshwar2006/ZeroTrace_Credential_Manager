from password_utils import hash_password

# ---------------- REGISTER ---------------- #

def register_user(username, password):
    with open("users.txt", "a") as file:
        file.write(username + "," + hash_password(password) + "\n")

# ---------------- LOGIN ---------------- #

def login_user(username, password):
    try:
        with open("users.txt", "r") as file:
            users = file.readlines()

        for user in users:
            stored_username, stored_password = user.strip().split(",")

            if username == stored_username and hash_password(password) == stored_password:
                return True

        return False

    except FileNotFoundError:
        return False
