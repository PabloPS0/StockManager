import customtkinter as ctk
from styles.window import Style

class Menu(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Menu")
        self.protocol("WM_DELETE_WINDOW", self.close_window)
        self.geometry(Style.center_window(self, 3200, 2800))
        self.resizable(False, False)
        
        # Theme configuration
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

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

    def close_window(self):
        self.destroy()
        self.quit()