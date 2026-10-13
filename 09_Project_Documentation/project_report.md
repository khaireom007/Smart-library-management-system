# Smart Library Management System
## Data Structures and Collection Management using Python

### Cover Page
**Project Title:** Smart Library Management System – Data Structures and Collection Management using Python  
**Subject:** Python  
**Student Name:** Om Vijay Khaire  
**PRN:** 2126UMLM1078  
**Department:** AIML  
**College / University:** [Enter college name]  
**Academic Year:** [Enter academic year]  
**Faculty / Trainer:** [Enter faculty name]  
**GitHub Repository:** https://github.com/khaireom007/Smart-library-management-system

## Acknowledgment
I would like to thank my faculty and institution for providing the opportunity to study Python data structures and apply them to a library management problem. Personalize this section to acknowledge the people who supported the work.

## Abstract
The Smart Library Management System is a console-based Python project for organizing and managing multiple book records. It demonstrates strings, lists, tuples, sets, and dictionaries in a single application. A dictionary stores each book's fields, while a list stores the catalogue. Tuples represent fixed ISBN components, and sets provide unique categories and authors. The program supports adding, searching, updating, displaying, sorting, counting, and availability operations. It includes input validation and a menu-driven interface. Automated tests cover catalogue setup, title matching, duplicate IDs, ISBN validation, availability changes, empty-catalogue behaviour, and sorting. The project is limited to in-memory storage and standard-library Python.

## Table of Contents
1. Introduction
2. Problem Statement
3. Objectives and Scope
4. Requirement Analysis
5. Data Structure Selection
6. System Design
7. Algorithms
8. Flowcharts
9. Pseudocode
10. Python Implementation
11. Testing and Results
12. Sample Program Outputs
13. Limitations
14. Future Enhancements
15. Learning Reflection
16. Conclusion
17. References

## 1. Introduction
A library catalogue contains many related fields for every book. The Unit 2 assignment focuses on managing collections rather than relying on separate variables. This prototype uses Python's built-in collection types and a console menu.

## 2. Problem Statement
Develop a Python program that manages multiple book records, searches and filters them, updates details, removes duplicate category information, and produces simple reports. The implementation demonstrates strings, lists, tuples, sets, and dictionaries.

## 3. Objectives and Scope
Objectives are to maintain a structured catalogue, implement core operations, demonstrate data-structure methods, validate inputs, and test normal, boundary, and invalid cases. The scope is a local console prototype. Records are not saved between runs.

## 4. Requirement Analysis
Functional requirements include adding, displaying, searching, updating, sorting, filtering available books, counting available books, showing unique categories/authors, and borrowing/returning records. Non-functional requirements include simplicity, ease of use, accuracy, reliability, and readable code. Python 3.8 or later is recommended; no external libraries are required.

## 5. Data Structure Selection
| Structure | Implementation | Reason |
|---|---|---|
| String | Titles, author names, category, Book ID, shelf | Text and normalization |
| List | Catalogue, search matches, title lists | Ordered, changeable collection |
| Tuple | ISBN parts and publication details | Fixed ordered values |
| Set | Unique categories and authors | Removes duplicate values |
| Dictionary | Individual book records | Named fields accessed by key |

## 6. System Design
The main loop displays a menu and calls the selected operation. `library` is a list of dictionaries. Each dictionary contains `book_id`, `title`, `author`, `publisher`, `category`, `isbn`, `available`, `price`, `shelf_number`, and `publication_details`. The program starts with three sample records to demonstrate operations immediately. Changes exist only in memory.

## 7. Algorithms
Algorithms for adding, searching, displaying, updating, category de-duplication, counting availability, searching by author, sorting titles, filtering available books, borrowing/returning, and the menu loop are documented in `04_Algorithm_Development/algorithms.md`.

## 8. Flowcharts
The Mermaid source is in `05_Flowcharts_and_Workflow/flowcharts.mmd`. It covers the menu and major operations using start/end terminals, process steps, decisions, and input/output shapes.

## 9. Pseudocode
Structured English pseudocode for the same operations is available in `06_Pseudocode/pseudocode.md`.

## 10. Python Implementation
The main implementation is `07_Python_Programming/main.py`. It uses functions for catalogue operations and separate demonstration functions for the five data structures. It uses only the Python standard library.

## 11. Testing and Results
The automated suite is `08_Program_Testing/test_main.py`. It was executed in the build environment: **11 tests passed and 0 failed**. The test report contains test descriptions and trace tables. A manual interactive demonstration on the submission computer is still recommended.

## 12. Sample Program Outputs
- `Available books: 2` for the three initial sample records.
- `Unique categories: Fiction, Sci-Fi`.
- Searching for `dune` finds the Dune record regardless of letter case.
- A duplicate Book ID is rejected.
- An empty catalogue displays `No books to display.`

## 13. Limitations
Records are not persisted after the program exits. This is a single-user console prototype. ISBN validation checks 13-digit format, not the checksum. The sample catalogue is illustrative and is not a real institutional collection.

## 14. Future Enhancements
Possible future work includes file-based persistence, stronger ISBN checksum validation, separate member records, due dates and fine calculations if required by a future specification, and additional test cases. These are not part of the current implementation.

## 15. Learning Reflection
The project illustrates collection selection, iteration, conditional logic, input validation, function decomposition, and test verification. The accompanying reflection is an editable draft; personalize it with genuine learning experiences.

## 16. Conclusion
The project demonstrates how Python's five built-in data structures can work together to organize a library catalogue. The console menu implements core operations and the automated test suite verifies selected normal, boundary, and invalid cases.

## 17. References
1. Unit 2 assignment PDF: *Data Structures and Collection Management – Smart Library Management System* (provided course material).
2. Python Software Foundation, *Python 3 Documentation*, https://docs.python.org/3/
