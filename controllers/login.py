import customtkinter as ctk
from tkinter import messagebox

class Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.protocol("WM_DELETE_WINDOW", self.close_window)
        self.geometry("600x400+50+50")
        self.resizable(False, False)


    def close_window(self):
        self.destroy()
        self.quit()