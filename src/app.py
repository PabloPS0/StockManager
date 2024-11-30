import sys, os
# Add the parent directory of the project to the system path to allow importing modules from it
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.lobby import StockManager  # A classe do lobby principal

def main():
    # Inicializa o Lobby como ponto de partida da aplicação
    app = StockManager()
    app.mainloop()

if __name__ == "__main__":
    main()
