"""
GUI implementation for the calculator.
"""
import tkinter as tk
from tkinter import ttk
from calculator.calculator import Calculator

class CalculatorGUI:
    """
    Graphical user interface for the calculator using tkinter.
    """
    def __init__(self, root):
        """
        Initialize the calculator GUI.
        
        Args:
            root: tkinter root window
        """
        self.root = root
        self.root.title("TDD Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # Set theme and style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Calculator instance
        self.calculator = Calculator()
        
        # Variables
        self.current_input = tk.StringVar(value="0")
        self.operation = None
        self.first_number = None
        self.start_new_input = True
        
        # Create and place widgets
        self._create_widgets()
        self._place_widgets()
    
    def _create_widgets(self):
        """Create all the widgets for the calculator."""
        # Display
        self.display_frame = ttk.Frame(self.root)
        self.display = ttk.Entry(
            self.display_frame, 
            textvariable=self.current_input,
            font=('Arial', 24),
            justify='right',
            state='readonly'
        )
        
        # Button frames
        self.buttons_frame = ttk.Frame(self.root)
        
        # Define buttons
        self.buttons = {}
        button_texts = [
            'C', '√', 'x²', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '±', '='
        ]
        
        for text in button_texts:
            self.buttons[text] = ttk.Button(
                self.buttons_frame, 
                text=text,
                width=4,
                command=lambda t=text: self._button_click(t)
            )
    
    def _place_widgets(self):
        """Place all widgets in the window."""
        # Display
        self.display_frame.pack(fill='x', padx=5, pady=5)
        self.display.pack(fill='x', padx=5, pady=5)
        
        # Buttons
        self.buttons_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Place buttons in grid
        button_positions = {
            'C': (0, 0), '√': (0, 1), 'x²': (0, 2), '/': (0, 3),
            '7': (1, 0), '8': (1, 1), '9': (1, 2), '*': (1, 3),
            '4': (2, 0), '5': (2, 1), '6': (2, 2), '-': (2, 3),
            '1': (3, 0), '2': (3, 1), '3': (3, 2), '+': (3, 3),
            '0': (4, 0), '.': (4, 1), '±': (4, 2), '=': (4, 3)
        }
        
        for text, (row, col) in button_positions.items():
            self.buttons[text].grid(row=row, column=col, padx=3, pady=3, sticky='nsew')
            
        # Configure rows and columns to expand proportionally
        for i in range(5):
            self.buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            self.buttons_frame.columnconfigure(i, weight=1)

    def _button_click(self, button_text):
        """
        Handle button clicks.
        
        Args:
            button_text (str): Text of the clicked button
        """
        # Get current display value
        current = self.current_input.get()
        
        # Handle different button types
        if button_text.isdigit() or button_text == '.':
            self._handle_digit_or_decimal(button_text)
        elif button_text in ('+', '-', '*', '/'):
            self._handle_operation(button_text, current)
        elif button_text == '=':
            self._handle_equals(current)
        elif button_text == 'C':
            self._handle_clear()
        elif button_text == '±':
            self._handle_negate(current)
        elif button_text == '√':
            self._handle_square_root(current)
        elif button_text == 'x²':
            self._handle_square(current)
    
    def _handle_digit_or_decimal(self, button_text):
        """Handle digit or decimal point input."""
        if self.start_new_input:
            self.current_input.set(button_text if button_text != '.' else '0.')
            self.start_new_input = False
        else:
            current = self.current_input.get()
            # Only add decimal if there isn't one already
            if button_text == '.' and '.' in current:
                return
            self.current_input.set(current + button_text)
    
    def _handle_operation(self, operation, current):
        """Handle mathematical operation."""
        if self.first_number is not None and not self.start_new_input:
            self._handle_equals(current)
        
        try:
            self.first_number = float(current)
            self.operation = operation
            self.start_new_input = True
        except ValueError:
            self.current_input.set("Error")
            self.start_new_input = True
    
    def _handle_equals(self, current):
        """Handle equals button press."""
        if self.operation is None or self.first_number is None:
            return
        
        try:
            second_number = float(current)
            
            # Perform calculation
            if self.operation == '+':
                result = self.calculator.add(self.first_number, second_number)
            elif self.operation == '-':
                result = self.calculator.subtract(self.first_number, second_number)
            elif self.operation == '*':
                result = self.calculator.multiply(self.first_number, second_number)
            elif self.operation == '/':
                result = self.calculator.divide(self.first_number, second_number)
            
            # Format and display result
            if result.is_integer():
                self.current_input.set(str(int(result)))
            else:
                self.current_input.set(str(result))
                
            # Reset operation state
            self.first_number = None
            self.operation = None
            self.start_new_input = True
            
        except ZeroDivisionError:
            self.current_input.set("Error: Div by 0")
            self.start_new_input = True
        except ValueError:
            self.current_input.set("Error")
            self.start_new_input = True
    
    def _handle_clear(self):
        """Handle clear button press."""
        self.calculator.clear()
        self.current_input.set("0")
        self.first_number = None
        self.operation = None
        self.start_new_input = True
    
    def _handle_negate(self, current):
        """Handle negation of current value."""
        try:
            value = float(current)
            result = -value
            if result.is_integer():
                self.current_input.set(str(int(result)))
            else:
                self.current_input.set(str(result))
        except ValueError:
            self.current_input.set("Error")
            self.start_new_input = True
    
    def _handle_square_root(self, current):
        """Handle square root operation."""
        try:
            value = float(current)
            result = self.calculator.square_root(value)
            if result.is_integer():
                self.current_input.set(str(int(result)))
            else:
                self.current_input.set(str(result))
            self.start_new_input = True
        except ValueError:
            self.current_input.set("Error")
            self.start_new_input = True
    
    def _handle_square(self, current):
        """Handle squaring the current value."""
        try:
            value = float(current)
            result = self.calculator.power(value, 2)
            if result.is_integer():
                self.current_input.set(str(int(result)))
            else:
                self.current_input.set(str(result))
            self.start_new_input = True
        except ValueError:
            self.current_input.set("Error")
            self.start_new_input = True