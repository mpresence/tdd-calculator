"""
Script to run all calculator tests.
"""
import unittest

if __name__ == '__main__':
    # Load all tests from the tests directory
    test_suite = unittest.defaultTestLoader.discover('tests')
    
    # Run the tests
    unittest.TextTestRunner().run(test_suite)