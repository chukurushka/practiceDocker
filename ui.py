import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from utils import save_users, save_purchases

# Register a new user
def register_user(root, users):
    def save_user():
        username = username_entry.get()
        password = password_entry.get()
        full_name = full_name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        address = address_entry.get()
        role = role_var.get()

        if not any(user['username'] == username for user in users):
            users.append({
                "username": username,
                "password": password,
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "address": address,
                "role": role
            })
            save_users()
            register_window.destroy()
        else:
            error_label.config(text="Пользователь с таким именем уже существует")

    register_window = tk.Toplevel(root)
    register_window.title("Регистрация пользователя")
    register_window.geometry("400x500")
    register_window.configure(bg="#e1f5fe")

    # Widgets
    full_name_label = tk.Label(register_window, text="ФИО:", font=("Arial", 14), bg="#e1f5fe")
    full_name_label.pack(pady=10)
    full_name_entry = tk.Entry(register_window, font=("Arial", 14))
    full_name_entry.pack(pady=10)

    email_label = tk.Label(register_window, text="Email:", font=("Arial", 14), bg="#e1f5fe")
    email_label.pack(pady=10)
    email_entry = tk.Entry(register_window, font=("Arial", 14))
    email_entry.pack(pady=10)

    phone_label = tk.Label(register_window, text="Телефон:", font=("Arial", 14), bg="#e1f5fe")
    phone_label.pack(pady=10)
    phone_entry = tk.Entry(register_window, font=("Arial", 14))
    phone_entry.pack(pady=10)

    address_label = tk.Label(register_window, text="Адрес:", font=("Arial", 14), bg="#e1f5fe")
    address_label.pack(pady=10)
    address_entry = tk.Entry(register_window, font=("Arial", 14))
    address_entry.pack(pady=10)

    username_label = tk.Label(register_window, text="Логин:", font=("Arial", 14), bg="#e1f5fe")
    username_label.pack(pady=10)
    username_entry = tk.Entry(register_window, font=("Arial", 14))
    username_entry.pack(pady=10)

    password_label = tk.Label(register_window, text="Пароль:", font=("Arial", 14), bg="#e1f5fe")
    password_label.pack(pady=10)
    password_entry = tk.Entry(register_window, show="*", font=("Arial", 14))
    password_entry.pack(pady=10)

    role_label = tk.Label(register_window, text="Роль:", font=("Arial", 14), bg="#e1f5fe")
    role_label.pack(pady=10)
    role_var = tk.StringVar(register_window)
    role_var.set("client")
    role_dropdown = ttk.Combobox(register_window, textvariable=role_var, values=["client", "employee"], font=("Arial", 14))
    role_dropdown.pack(pady=10)

    save_button = tk.Button(register_window, text="Зарегистрировать", command=save_user, font=("Arial", 14), bg="#4CAF50", fg="white")
    save_button.pack(pady=20)

    error_label = tk.Label(register_window, text="", fg="red", font=("Arial", 14), bg="#e1f5fe")
    error_label.pack(pady=10)

# Log in a user
def login(root, users, purchases):
    def authenticate():
        username = username_entry.get()
        password = password_entry.get()

        for user in users:
            if user["username"] == username and user["password"] == password:
                if user["role"] == "client":
                    show_client_ui(user, purchases)
                    login_window.destroy()
                    return
                elif user["role"] == "employee":
                    show_employee_ui(user, purchases)
                    login_window.destroy()
                    return

        login_error_label.config(text="Неправильный логин или пароль")

    login_window = tk.Toplevel(root)
    login_window.title("Вход")
    login_window.geometry("400x300")
    login_window.configure(bg="#e1f5fe")

    # Widgets
    username_label = tk.Label(login_window, text="Логин:", font=("Arial", 14), bg="#e1f5fe")
    username_label.pack(pady=10)
    username_entry = tk.Entry(login_window, font=("Arial", 14))
    username_entry.pack(pady=10)

    password_label = tk.Label(login_window, text="Пароль:", font=("Arial", 14), bg="#e1f5fe")
    password_label.pack(pady=10)
    password_entry = tk.Entry(login_window, show="*", font=("Arial", 14))
    password_entry.pack(pady=10)

    login_button = tk.Button(login_window, text="Войти", command=authenticate, font=("Arial", 14), bg="#4CAF50", fg="white")
    login_button.pack(pady=20)

    login_error_label = tk.Label(login_window, text="", fg="red", font=("Arial", 14), bg="#e1f5fe")
    login_error_label.pack(pady=10)

# Other UI functions for client and employee would go here (show_client_ui, show_employee_ui)
