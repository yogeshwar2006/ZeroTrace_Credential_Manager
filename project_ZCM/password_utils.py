import random
import string
import re
import hashlib

# ---------------- HASH FUNCTION ---------------- #

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ---------------- PASSWORD VALIDATION ---------------- #

def validate_password_format(password):
    if len(password) < 8 or len(password) > 13:
        return "Password must be 8 to 13 characters."

    if not re.search(r"[A-Z]", password):
        return "Must contain at least 1 Capital letter."

    if not re.search(r"[a-z]", password):
        return "Must contain at least 1 Small letter."

    if not re.search(r"[0-9]", password):
        return "Must contain at least 1 Number."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Must contain at least 1 Special character."

    return "Valid"

# ---------------- PASSWORD STRENGTH ---------------- #

def strength_meter(password):
    score = 0
    if len(password) >= 8: score += 20
    if re.search(r"[A-Z]", password): score += 20
    if re.search(r"[a-z]", password): score += 20
    if re.search(r"[0-9]", password): score += 20
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): score += 20
    return score

# ---------------- PASSWORD GENERATOR ---------------- #

def generate_secure_password():
    characters = string.ascii_letters + string.digits + string.punctuation

    while True:
        length = random.randint(8, 13)
        password = ''.join(random.choice(characters) for _ in range(length))
        if validate_password_format(password) == "Valid":
            return password
