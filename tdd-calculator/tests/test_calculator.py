"""
Tests for the Calculator class functionality.
"""
import unittest
from calculator.calculator import Calculator

class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()
    
    def test_initialization(self):
        """Test calculator initialization."""
        self.assertEqual(self.calc.result, 0)
    
    def test_add_two_numbers(self):
        """Test adding two numbers."""
        result = self.calc.add(3, 5)
        self.assertEqual(result, 8)
        self.assertEqual(self.calc.result, 8)
    
    def test_add_to_result(self):
        """Test adding to current result."""
        self.calc.result = 5
        result = self.calc.add(3)
        self.assertEqual(result, 8)
        self.assertEqual(self.calc.result, 8)
    
    def test_subtract_two_numbers(self):
        """Test subtracting two numbers."""
        result = self.calc.subtract(10, 4)
        self.assertEqual(result, 6)
        self.assertEqual(self.calc.result, 6)
    
    def test_subtract_from_result(self):
        """Test subtracting from current result."""
        self.calc.result = 10
        result = self.calc.subtract(4)
        self.assertEqual(result, 6)
        self.assertEqual(self.calc.result, 6)
    
    def test_multiply_two_numbers(self):
        """Test multiplying two numbers."""
        result = self.calc.multiply(3, 4)
        self.assertEqual(result, 12)
        self.assertEqual(self.calc.result, 12)
    
    def test_multiply_result(self):
        """Test multiplying current result."""
        self.calc.result = 3
        result = self.calc.multiply(4)
        self.assertEqual(result, 12)
        self.assertEqual(self.calc.result, 12)
    
    def test_divide_two_numbers(self):
        """Test dividing two numbers."""
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)
        self.assertEqual(self.calc.result, 5)
    
    def test_divide_result(self):
        """Test dividing current result."""
        self.calc.result = 10
        result = self.calc.divide(2)
        self.assertEqual(result, 5)
        self.assertEqual(self.calc.result, 5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises error."""
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
        
        self.calc.result = 10
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(0)
    
    def test_clear(self):
        """Test clearing the calculator."""
        self.calc.result = 10
        result = self.calc.clear()
        self.assertEqual(result, 0)
        self.assertEqual(self.calc.result, 0)
    
    def test_square_root(self):
        """Test square root calculation."""
        result = self.calc.square_root(16)
        self.assertEqual(result, 4)
        self.assertEqual(self.calc.result, 4)
    
    def test_square_root_of_result(self):
        """Test square root of current result."""
        self.calc.result = 16
        result = self.calc.square_root()
        self.assertEqual(result, 4)
        self.assertEqual(self.calc.result, 4)
    
    def test_square_root_of_negative(self):
        """Test square root of negative number raises error."""
        with self.assertRaises(ValueError):
            self.calc.square_root(-4)
    
    def test_power(self):
        """Test power calculation."""
        result = self.calc.power(2, 3)
        self.assertEqual(result, 8)
        self.assertEqual(self.calc.result, 8)
    
    def test_power_of_result(self):
        """Test raising current result to a power."""
        self.calc.result = 2
        result = self.calc.power(3)
        self.assertEqual(result, 8)
        self.assertEqual(self.calc.result, 8)
    
    def test_chain_operations(self):
        """Test chaining multiple operations."""
        self.calc.add(5, 3)  # result = 8
        self.calc.multiply(2)  # result = 16
        self.calc.subtract(6)  # result = 10
        self.calc.divide(2)  # result = 5
        self.assertEqual(self.calc.result, 5)

if __name__ == '__main__':
    unittest.main()