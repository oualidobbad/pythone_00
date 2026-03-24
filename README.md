# pythone_00

Python Module 00: introductory exercises covering syntax fundamentals, type manipulation, string formatting, and basic control flow across 8 exercises (ex0–ex7).

## Project Overview
- What it does: provides progressive Python exercises from "Hello World" to string manipulation, type casting, and simple function definitions.
- Use cases: first contact with Python for C/C++ developers transitioning from 42 projects.
- Problem solved: builds Python fluency through isolated, focused exercises.

## Architecture & Design
- 8 exercise directories (`ex0/`–`ex7/`), each containing a single `.py` file.
- Subject PDF (`en.subject00.pdf`) provides exercise specifications.
- Each exercise is self-contained — no imports between exercises.

## Core Concepts
- Python 3 basics: `print()`, f-strings, `input()`, type annotations.
- String operations: slicing, `join`, `split`, formatting.
- Control flow: `if/elif/else`, `for`, `while`, `range()`.
- Functions: `def`, default arguments, return values.
- Type casting: `int()`, `str()`, `float()`, `type()`.

### Example: string manipulation
```python
# Typical exercise pattern
def format_name(first, last):
    return f"{last.upper()}, {first.capitalize()}"

print(format_name("oualid", "obbad"))  # OBBAD, Oualid
```

## Installation & Setup
- Requires Python 3 (3.8+ recommended).
- Run any exercise: `python3 ex0/exercise.py`.

## Usage Guide
- Follow the subject PDF for exercise specifications.
- Work through exercises sequentially (ex0 → ex7).

## Technical Notes
- Pure Python — no pip dependencies.
- Exercises focus on standard library only.

## Improvements & Future Work
- Add pytest unit tests per exercise.
- Include type hints and docstrings for documentation practice.

## Author
Oualid Obbad (@oualidobbad)