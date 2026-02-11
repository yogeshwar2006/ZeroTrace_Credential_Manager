import customtkinter as ctk
from tkinter import messagebox
from password_utils import *
from auth import *

# ---------------- APP SETTINGS ---------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("720x680")
app.title("ZeroTrace Credential Manager")

# ---------------- ANIMATED BACKGROUND ---------------- #

bg_colors = ["#1a1a1a", "#111111", "#0f0f0f", "#151515"]
color_index = 0

def animate_background():
    global color_index
    app.configure(fg_color=bg_colors[color_index])
    color_index = (color_index + 1) % len(bg_colors)
    app.after(2000, animate_background)

animate_background()

# ---------------- REGISTER FUNCTION ---------------- #

def register():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Error", "Fill all fields")
        return

    validation = validate_password_format(password)

    if validation != "Valid":
        messagebox.showwarning("Invalid Password", validation)
        return

    register_user(username, password)
    messagebox.showinfo("Success", "User Registered Successfully!")

# ---------------- LOGIN FUNCTION ---------------- #

def login():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Error", "Fill all fields")
        return

    validation = validate_password_format(password)

    if validation != "Valid":
        messagebox.showwarning("Invalid Format", validation)
        return

    if login_user(username, password):
        messagebox.showinfo("Login Success", f"Welcome {username}")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

# ---------------- PASSWORD GENERATOR ---------------- #

def generate_password():
    password = generate_secure_password()
    entry_generated.delete(0, "end")
    entry_generated.insert(0, password)

    score = strength_meter(password)
    messagebox.showinfo("Generated", f"Strength: {score}%")

def copy_password():
    app.clipboard_clear()
    app.clipboard_append(entry_generated.get())
    messagebox.showinfo("Copied", "Password Copied")

# ---------------- UI DESIGN ---------------- #

main_frame = ctk.CTkFrame(app, corner_radius=20)
main_frame.pack(pady=40, padx=40, fill="both", expand=True)

ctk.CTkLabel(main_frame,
             text="ZeroTrace Credential Manager",
             font=("Arial", 24, "bold")).pack(pady=20)

entry_username = ctk.CTkEntry(main_frame,
                              placeholder_text="Username",
                              width=320)
entry_username.pack(pady=10)

# -------- PASSWORD FIELD WITH EYE -------- #

password_container = ctk.CTkFrame(main_frame,
                                  width=320,
                                  height=40,
                                  corner_radius=10)
password_container.pack(pady=10)
password_container.pack_propagate(False)

entry_password = ctk.CTkEntry(password_container,
                              placeholder_text="Password",
                              show="*",
                              border_width=0)
entry_password.pack(side="left", fill="both", expand=True, padx=(10,0))

password_visible = False

def toggle_password():
    global password_visible
    if password_visible:
        entry_password.configure(show="*")
        password_visible = False
    else:
        entry_password.configure(show="")
        password_visible = True

    eye_button.configure(text="🙈")
    app.after(150, lambda: eye_button.configure(text="👁"))

eye_button = ctk.CTkButton(password_container,
                           text="👁",
                           width=40,
                           fg_color="transparent",
                           hover_color="#333333",
                           command=toggle_password)

eye_button.pack(side="right", padx=5)

# ---------------- BUTTONS ---------------- #

login_btn = ctk.CTkButton(main_frame,
                          text="Login",
                          width=220,
                          height=45,
                          fg_color="#1f1f1f",
                          corner_radius=15,
                          command=login)
login_btn.pack(pady=10)

register_btn = ctk.CTkButton(main_frame,
                             text="Register",
                             width=220,
                             height=45,
                             fg_color="#2b2b2b",
                             corner_radius=15,
                             command=register)
register_btn.pack(pady=10)

# ---------------- GENERATOR SECTION ---------------- #

ctk.CTkLabel(main_frame,
             text="Generate Secure Password",
             font=("Arial", 18)).pack(pady=20)

entry_generated = ctk.CTkEntry(main_frame, width=320)
entry_generated.pack(pady=10)

ctk.CTkButton(main_frame,
              text="Generate Password",
              width=220,
              height=45,
              fg_color="#000000",
              hover_color="#333333",
              corner_radius=15,
              command=generate_password).pack(pady=10)

ctk.CTkButton(main_frame,
              text="Copy to Clipboard",
              width=220,
              height=45,
              fg_color="#222222",
              corner_radius=15,
              command=copy_password).pack(pady=10)

app.mainloop()
