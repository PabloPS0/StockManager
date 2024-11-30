import customtkinter as ctk
from styles.window import Style
import traceback as tb
import tkinter as tk
import sys

# Manipular exceções silenciosas
def silent_tkinter_error_handler(type, value, traceback):
    # Manipulador para ignorar erros irrelevantes do Tkinter
    if issubclass(type, tk.TclError):
        return  # Ignora erros do Tkinter (como eventos em widgets destruídos)
    if issubclass(type, KeyboardInterrupt) or issubclass(type, SystemExit):
        return  # Ignora interrupções ou saídas
    print(f"Erro inesperado: {value}")
    tb.print_exc()

# Define o manipulador de exceções global
sys.excepthook = silent_tkinter_error_handler

class StockManager(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.current_window = None  # Rastreamento da janela atual
        self.pending_events = []  # Lista para rastrear IDs de eventos agendados com `after`
        print(self.pending_events)

        # Window Config
        self.geometry(Style.center_window(self, 3200, 2800))
        self.title("Stock Manager")
        self.protocol("WM_DELETE_WINDOW", self.safe_destroy)
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
        enter_button = ctk.CTkButton(self.mid_frame, text="Enter", command=self.open_enter)
        enter_button.pack(pady=10, padx=10)
        
        register_button = ctk.CTkButton(self.mid_frame, text="Register", command=self.open_register)
        register_button.pack(pady=10, padx=10)
    

    def open_enter(self):
        self.open_window("login")

    def open_register(self):
        self.open_window("register")     

    def open_window(self, window_type):
        # Gerencia a abertura de janelas (Login ou Register)
        if self.current_window is None:
            self.cancel_pending_events()  # Cancela eventos antes de alternar
            self.safe_destroy() # Fecha o lobby
            if window_type == "login":
                from controllers.login import Login
                self.current_window = Login()
            elif window_type == "register":
                from controllers.register import Register
                self.current_window = Register()
            self.current_window.protocol("WM_DELETE_WINDOW", self.on_window_close)
            self.current_window.mainloop()  

    # Check if there is no open window
    def on_window_close(self):
        # Fecha a janela atual e redefine o controle
        if self.current_window is not None:
            self.current_window.destroy()
            self.current_window = None

    def cancel_pending_events(self):
        # Cancela todos os eventos pendentes registrados no after
        try:
            for event_id in self.cancel_pending_events:
                self.after_cancel(event_id)
            self.pending_events.clear() # Limpa a lista de eventos pendentes
        except Exception as e:
            print(f"Erro ao cancelar eventos pendentes: {e}")

    def schedule_event(self, delay, func, *args):
        """Agenda um evento e rastreia seu ID."""
        event_id = self.after(delay, func, *args)
        self.pending_events.append(event_id)  # Adiciona o ID do evento à lista

    def safe_destroy(self):
        # Cancela eventos pendentes antes de destruir a janela
        try:
            # Cancela todos os eventos agendados
            for widget in self.winfo_children():
                widget.after_cancel("all")
        except Exception as e:
            print(f"Erro ao cancelar eventos: {e}")
        finally:
            self.destroy()  # Destroi a janela
