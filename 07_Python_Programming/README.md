# Python Program

## Smart Library Management System
A console-based Python project demonstrating collection management with strings, lists, tuples, sets, and dictionaries.

## Requirements
- Python 3.8 or later
- No third-party packages

## Run
From this folder, execute:

```bash
python main.py
```

The program loads three sample books at startup to make searching, filtering, counting, and set operations demonstrable immediately. New books and changes remain in memory only for the current run.

## Menu
The menu supports adding, displaying, searching, updating, filtering available books, counting availability, listing unique categories/authors, sorting titles, borrowing/returning books, and demonstrations of the five built-in data structures.

## Notes
- Book IDs must be unique.
- ISBN input must contain 13 digits; hyphens and spaces are ignored.
- Price must be a non-negative number.
- The ISBN is stored as a tuple of two strings.
