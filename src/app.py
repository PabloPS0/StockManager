import sys, os
# Add the parent directory of the project to the system path to allow importing modules from it
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.lobby import StockManager

# Create an instance of the StockManagerApp class and start the application
if __name__ == "__main__":
    app = StockManager()
    app.mainloop()