"""
This module provides a function to check the syntax of a Python script.
"""

import sys
import ast
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class SyntaxChecker:
    """
    A class to check the syntax of Python scripts.
    """

    def __init__(self):
        """
        Initializes the SyntaxChecker class.
        """
        self.logger = logging.getLogger(__name__)

    def check(self, filename: str) -> bool:
        """
        Check if the given Python script is syntactically correct.
        
        Parameters:
        filename (str): The path to the Python script.
        
        Returns:
        bool: True if the script is syntactically correct, False otherwise.
        
        Raises:
            FileNotFoundError: If the file does not exist.
            SyntaxError: If the file contains syntax errors.
        """
        try:
            with open(filename, 'r') as file:
                file_content = file.read()
            ast.parse(file_content)
            return True
        except FileNotFoundError as e:
            self.logger.error(f"File not found: {e}")
            return False
        except SyntaxError as e:
            self.logger.error(f"Syntax error: {e}")
            return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python SyntaxChecker.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    checker = SyntaxChecker()
    result = checker.check(filename)
    print(f"Syntax check result: {result}")
