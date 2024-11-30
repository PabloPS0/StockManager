import customtkinter as ctk
from styles.window import Style

class Register(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Register")
        self.protocol("WM_DELETE_WINDOW", self.close_window)
        self.geometry(Style.center_window(self, 3200, 2800))
        self.maxsize(3200, 2800)
        self.minsize(800, 600)

        self.resizable(False, False)
        
        # Theme configuration
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.create_container()
        self.create_widgets()

    # Create the container
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

    # Create the widgets
    def create_widgets(self):
        name_app = ctk.CTkLabel(self.top_frame, text="Register", font=("Arial", 24))
        name_app.pack(pady=20, padx=10)

    def back_to_lobby(self):
        self.destroy()  # Fecha a janela de Login
        from controllers.lobby import StockManager
        StockManager()  # Reabre o Lobby


    def close_window(self):
        self.destroy()
        self.quit()