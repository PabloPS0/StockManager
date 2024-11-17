import sys, os
# Add the parent directory of the project to the system path to allow importing modules from it
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.login import Login

# Create an instance of the StockManagerApp class and start the application
if __name__ == "__main__":
    app = Login()
    app.mainloop()