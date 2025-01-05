# Syntax Checker

This module provides a function to check the syntax of a Python script.

## Features

- Check if a Python script is syntactically correct.
- Can be used as a module or a standalone script.
- Well-documented with logging for better debugging.

## Installation

```bash
poetry install
```

## Usage

### As a Module

```python
from SyntaxChecker import SyntaxChecker

checker = SyntaxChecker()
result = checker.check("path/to/your/script.py")
print(result)
```

### As a Standalone Script

```bash
python SyntaxChecker.py path/to/your/script.py
```

## Tests

To run the tests, use the following command:

```bash
pytest
```
