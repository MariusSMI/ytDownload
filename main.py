from tkinter import *
from src.app import App

if __name__ == "__main__":
    root = Tk()
    app = App(root, "500x300", "#1e1e1e", False)
    root.mainloop()
