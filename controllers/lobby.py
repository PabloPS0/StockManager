import customtkinter as ctk
from styles.window import Style

class StockManager(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(Style.center_window(self, 3200, 2800))
        self.title("Stock Manager")
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
        name_app = ctk.CTkLabel(self.top_frame, text="Stock Manager", font=("Arial", 24))
        name_app.pack(pady=20, padx=10)
    
        # Button
        enter_button = ctk.CTkButton(self.mid_frame, text="Enter", command=self.openenter)
        enter_button.pack(pady=10, padx=10)
        
        register_button = ctk.CTkButton(self.mid_frame, text="Register", command=self.openregister)
        register_button.pack(pady=10, padx=10)

    def openenter(self):
        from controllers.login import Login
        login_window = Login()
        login_window.mainloop()
        self.close_window()

    def openregister(self):
        from controllers.register import Register
        register_window = Register()
        register_window.mainloop()
        self.close_window()

    def close_window(self):
        self.destroy()
        self.quit()