import customtkinter as ctk
from styles.window import Style

class Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(Style.center_window(self, 3200, 2800))
        self.title("Login")
        self.protocol("WM_DELETE_WINDOW", self.close_window)
        self.maxsize(3200, 2800)
        self.minsize(800, 600)
        
        # Prevent resizing
        self.resizable(False, False)

        # Theme configuration
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Call the functions
        self.create_container()
        self.create_widgets()
    

    def create_container(self):
        # Top Frame (por exemplo, pode conter entradas e botões principais)
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(fill=ctk.X, pady=5, padx=5)
        
        # Mid Frame (pode conter listboxes, labels, etc.)
        self.mid_frame = ctk.CTkFrame(self)
        self.mid_frame.pack(fill=ctk.BOTH, expand=True)
        
        # Bottom Frame (pode conter botões de ações)
        self.bottom_frame = ctk.CTkFrame(self)
        self.bottom_frame.pack(fill=ctk.X, pady=5, padx=5)

    def create_widgets(self):
        name_app = ctk.CTkLabel(self.top_frame, text="Login", font=("Arial", 24))
        name_app.pack(pady=20, padx=10)
        

        # Text Entries
        entry_email_or_user = ctk.CTkEntry(self.mid_frame, placeholder_text="Email/User:", width=200)
        entry_email_or_user.pack(pady=5, padx=10)
        entry_password = ctk.CTkEntry(self.mid_frame, placeholder_text="Password:", show="*", width=200)
        entry_password.pack(pady=10, padx=10) 

        # Button
        confirm_button = ctk.CTkButton(self.bottom_frame, text="Confirm", command=self.confirm)
        confirm_button.pack(pady=10)    

        label_register = ctk.CTkButton(self.bottom_frame, text="Don't have an account? Register now", font=("Arial", 12), text_color="lightblue", fg_color="transparent", hover_color="#222222", command=self.open_register)
        label_register.pack(pady=5, padx=10)
    def confirm(self):
        # Login logic 
        print("Login successful")

    def open_register(self):
        # Open register window
        pass

    def close_window(self):
        self.destroy()
        self.quit()