# test_huggingfacespaces.py
"""
Tests for HuggingFaceSpaces module.
"""

import unittest
from huggingfacespaces import HuggingFaceSpaces

class TestHuggingFaceSpaces(unittest.TestCase):
    """Test cases for HuggingFaceSpaces class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HuggingFaceSpaces()
        self.assertIsInstance(instance, HuggingFaceSpaces)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HuggingFaceSpaces()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
