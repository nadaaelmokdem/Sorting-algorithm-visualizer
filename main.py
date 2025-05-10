# main.py
import tkinter as tk
from gui import SortingAppTkinter

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingAppTkinter(root)
    root.mainloop()
