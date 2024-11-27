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

    def close_window(self):
        self.destroy()
        self.quit()