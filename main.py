import tkinter as tk
from tkinter import messagebox
from utils import load_users, save_users, load_purchases, save_purchases
from ui import register_user, login

# Initialize users and purchases globally
users = []
purchases = []

# Load data
load_users()
load_purchases()

# Main Application window
root = tk.Tk()
root.title("SuperGuard - Учет клиентов")
root.geometry("400x300")

# Header with logo and title
header_frame = tk.Frame(root, bg="#4CAF50")
header_frame.pack(fill="x")

title_label = tk.Label(header_frame, text="SuperGuard", font=("Arial", 24), fg="white", bg="#4CAF50")
title_label.pack(pady=10)

register_button = tk.Button(root, text="Регистрация", command=lambda: register_user(root, users), font=("Arial", 16), bg="#2196F3", fg="white")
register_button.pack(pady=20)

login_button = tk.Button(root, text="Вход", command=lambda: login(root, users, purchases), font=("Arial", 16), bg="#4CAF50", fg="white")
login_button.pack(pady=20)

root.mainloop()
