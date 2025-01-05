import pytest
import sys
import os
from SyntaxChecker import SyntaxChecker



def test_check_valid_syntax():
    checker = SyntaxChecker()
    # Create a temporary valid Python file
    valid_content = """
import math

print(math.sqrt(16))
"""
    with open("valid_script.py", "w") as file:
        file.write(valid_content)
    result = checker.check("valid_script.py")
    assert result == True
    os.remove("valid_script.py")


def test_check_invalid_syntax():
    checker = SyntaxChecker()
    # Create a temporary invalid Python file
    invalid_content = """
import math

print(math.sqrt(16
"""
    with open("invalid_script.py", "w") as file:
        file.write(invalid_content)
    result = checker.check("invalid_script.py")
    assert result == False
    os.remove("invalid_script.py")


def test_check_file_not_found():
    checker = SyntaxChecker()
    result = checker.check("non_existent_file.py")
    assert result == False


def test_main_functionality():
    # Simulate command line arguments
    sys.argv = ['SyntaxChecker.py', 'valid_script.py']
    # Create a temporary valid Python file
    valid_content = """
import math

print(math.sqrt(16))
"""
    with open("valid_script.py", "w") as file:
        file.write(valid_content)
    # Capture the print output
    from io import StringIO
    import sys
    captured_output = StringIO()
    sys.stdout = captured_output
    try:
        import __main__
        __main__.main()
    except SystemExit:
        pass
    sys.stdout = sys.__stdout__
    assert "Syntax check result: True" in captured_output.getvalue()
    os.remove("valid_script.py")


class TestSyntaxChecker:
    def test_method_one(self):
        # Test code here
        pass

    def test_method_two(self):
        # Test code here
        pass
