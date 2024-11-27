import customtkinter as ctk

class Style:
    def __init__(self):
        pass

    # Center Window
    def center_window(self, width, height):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        return f"{width}x{height}+{x}+{y}"
    
    