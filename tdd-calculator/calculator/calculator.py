"""
Core calculator functionality.
"""

class Calculator:
    """
    Calculator class that provides basic arithmetic operations.
    """
    def __init__(self):
        """Initialize the calculator."""
        self.result = 0
    
    def add(self, a, b=None):
        """
        Add two numbers or add a number to the current result.
        
        Args:
            a (float): First number
            b (float, optional): Second number. If None, adds to current result.
            
        Returns:
            float: Result of addition
        """
        if b is None:
            self.result += a
        else:
            self.result = a + b
        return self.result
    
    def subtract(self, a, b=None):
        """
        Subtract second number from first or subtract from current result.
        
        Args:
            a (float): First number
            b (float, optional): Second number. If None, subtracts from current result.
            
        Returns:
            float: Result of subtraction
        """
        if b is None:
            self.result -= a
        else:
            self.result = a - b
        return self.result
    
    def multiply(self, a, b=None):
        """
        Multiply two numbers or multiply current result.
        
        Args:
            a (float): First number
            b (float, optional): Second number. If None, multiplies current result.
            
        Returns:
            float: Result of multiplication
        """
        if b is None:
            self.result *= a
        else:
            self.result = a * b
        return self.result
    
    def divide(self, a, b=None):
        """
        Divide first number by second or divide current result.
        
        Args:
            a (float): First number
            b (float, optional): Second number. If None, divides current result.
            
        Returns:
            float: Result of division
            
        Raises:
            ZeroDivisionError: If attempting to divide by zero
        """
        if b is None:
            if a == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            self.result /= a
        else:
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            self.result = a / b
        return self.result
    
    def clear(self):
        """
        Reset the calculator result to zero.
        
        Returns:
            float: 0
        """
        self.result = 0
        return self.result
    
    def square_root(self, a=None):
        """
        Calculate the square root of a number or current result.
        
        Args:
            a (float, optional): Number to find square root of. If None, uses current result.
            
        Returns:
            float: Square root result
            
        Raises:
            ValueError: If attempting to find square root of negative number
        """
        import math
        
        if a is None:
            a = self.result
            
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
            
        self.result = math.sqrt(a)
        return self.result
    
    def power(self, a, b=None):
        """
        Raise a number to a power or raise current result to a power.
        
        Args:
            a (float): Base or exponent (if b is None)
            b (float, optional): Exponent. If None, raises current result to power a.
            
        Returns:
            float: Result of exponentiation
        """
        if b is None:
            self.result = self.result ** a
        else:
            self.result = a ** b
        return self.result