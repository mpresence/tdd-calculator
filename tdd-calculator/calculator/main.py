"""
Main entry point for the calculator application.
"""
import tkinter as tk
from calculator.gui import CalculatorGUI

def main():
    """Start the calculator application."""
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()