"""Smart Library Management System - Unit 2 data structures project.

The catalogue is stored in memory as a list of dictionaries. The program
demonstrates strings, lists, tuples, sets, and dictionaries using only the
Python standard library.
"""

import re

# Each dictionary is one book; the list is the complete catalogue.
library = []

UPDATE_FIELDS = ("title", "author", "publisher", "category", "isbn", "price", "shelf_number")


def normalize_text(value):
    """Trim whitespace and normalize repeated spaces in user-entered text."""
    return " ".join(value.strip().split())


def validate_isbn(value):
    """Return a two-part immutable tuple for a valid 13-digit ISBN."""
    digits = value.replace("-", "").replace(" ", "")
    if len(digits) != 13 or not digits.isdigit():
        raise ValueError("ISBN must contain exactly 13 digits (hyphens are allowed).")
    return (digits[:3], digits[3:])


def find_by_id(book_id):
    """Return the matching book dictionary, or None when it is absent."""
    target = normalize_text(book_id).casefold()
    for book in library:
        if book["book_id"].casefold() == target:
            return book
    return None


def format_book(book):
    """Format one record consistently for console output."""
    isbn_text = "-".join(book["isbn"])
    status = "Available" if book["available"] else "Borrowed"
    return (
        f'ID: {book["book_id"]} | Title: {book["title"]} | '
        f'Author: {book["author"]} | Publisher: {book["publisher"]} | '
        f'Category: {book["category"]} | ISBN: {isbn_text} | '
        f'Price: {book["price"]:.2f} | Shelf: {book["shelf_number"]} | '
        f'Status: {status}'
    )


def read_nonempty(prompt):
    """Read text and reject empty input."""
    while True:
        value = normalize_text(input(prompt))
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def read_price(prompt="Price: "):
    """Read a non-negative price, rejecting non-numeric and negative values."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value < 0:
                print("Price cannot be negative.")
                continue
            return value
        except ValueError:
            print("Enter a valid number, such as 12.50.")


def add_book():
    """Validate a new record and append it unless its ID already exists."""
    print("\n--- Add a Book ---")
    book_id = read_nonempty("Book ID: ")
    if find_by_id(book_id):
        print("Book ID already exists. Record not added.")
        return

    title = read_nonempty("Title: ").title()
    author = read_nonempty("Author: ").title()
    publisher = read_nonempty("Publisher: ").title()
    category = read_nonempty("Category: ").title()
    isbn_input = read_nonempty("13-digit ISBN (hyphens allowed): ")
    try:
        isbn = validate_isbn(isbn_input)
    except ValueError as error:
        print(f"Invalid ISBN: {error} Record not added.")
        return
    price = read_price()
    shelf_number = read_nonempty("Shelf number: ").upper()

    library.append({
        "book_id": book_id.upper(),
        "title": title,
        "author": author,
        "publisher": publisher,
        "category": category,
        "isbn": isbn,  # tuple: ISBN components are fixed after validation
        "available": True,
        "price": price,
        "shelf_number": shelf_number,
        "publication_details": (None, "Not specified", publisher),
    })
    print("Book added successfully.")


def display_books(records=None, heading="Book Records"):
    """Display records from the supplied list or from the whole catalogue."""
    if records is None:
        records = library
    print(f"\n--- {heading} ---")
    if not records:
        print("No books to display.")
        return
    for record in records:
        print(format_book(record))


def search_by_title():
    """Search all records by title, ignoring capitalization."""
    title = read_nonempty("Enter title to search: ").casefold()
    matches = [book for book in library if book["title"].casefold() == title]
    if matches:
        display_books(matches, "Title Search Results")
    else:
        print("Book Not Found.")


def search_by_author():
    """Display every book whose author matches the entered name."""
    author = read_nonempty("Enter author name: ").casefold()
    matches = [book for book in library if book["author"].casefold() == author]
    if matches:
        display_books(matches, "Books by Author")
    else:
        print("No books found for this author.")


def update_book():
    """Update one supported field after locating a record by Book ID."""
    book_id = read_nonempty("Enter Book ID to update: ")
    book = find_by_id(book_id)
    if book is None:
        print("Book Not Found.")
        return
    print("Fields:", ", ".join(UPDATE_FIELDS))
    field = read_nonempty("Field to update: ").lower()
    if field not in UPDATE_FIELDS:
        print("Invalid field. No changes made.")
        return
    try:
        if field == "isbn":
            new_value = validate_isbn(read_nonempty("New ISBN: "))
        elif field == "price":
            new_value = read_price("New price: ")
        elif field == "title":
            new_value = read_nonempty("New title: ").title()
        elif field == "author":
            new_value = read_nonempty("New author: ").title()
        elif field == "publisher":
            new_value = read_nonempty("New publisher: ").title()
        elif field == "category":
            new_value = read_nonempty("New category: ").title()
        else:
            new_value = read_nonempty("New shelf number: ").upper()
    except ValueError as error:
        print(f"Invalid value: {error}")
        return
    book[field] = new_value
    print("Book updated successfully.")


def unique_categories():
    """Return a set of category strings, automatically removing duplicates."""
    return {book["category"] for book in library}


def unique_authors():
    """Return a set of author names, automatically removing duplicates."""
    return {book["author"] for book in library}


def display_unique_categories():
    categories = sorted(unique_categories(), key=str.casefold)
    print("Unique categories:", ", ".join(categories) if categories else "None")


def display_unique_authors():
    authors = sorted(unique_authors(), key=str.casefold)
    print("Unique authors:", ", ".join(authors) if authors else "None")


def count_available_books():
    """Count records whose available field is True."""
    count = 0
    for book in library:
        if book["available"] is True:
            count += 1
    print(f"Available books: {count}")


def display_available_books():
    """Filter and display books currently marked available."""
    available = [book for book in library if book["available"] is True]
    display_books(available, "Available Books")


def sort_titles():
    """Sort a separate title list so the catalogue order is unchanged."""
    titles = [book["title"] for book in library]
    titles.sort(key=str.casefold)
    print("Titles in alphabetical order:")
    if not titles:
        print("No titles available.")
    else:
        print("\n".join(titles))


def borrow_or_return():
    """Change availability after checking the current state of the book."""
    book_id = read_nonempty("Book ID: ")
    book = find_by_id(book_id)
    if book is None:
        print("Book Not Found.")
        return
    action = read_nonempty("Enter B to borrow or R to return: ").upper()
    if action == "B":
        if not book["available"]:
            print("This book is already borrowed.")
        else:
            book["available"] = False
            print("Book borrowed successfully.")
    elif action == "R":
        if book["available"]:
            print("This book is already marked available.")
        else:
            book["available"] = True
            print("Book returned successfully.")
    else:
        print("Invalid action. Enter B or R.")


def string_methods_demo():
    """Demonstrate common string operations listed in the assignment."""
    title = "  the great gatsby  "
    clean_title = title.strip()
    sample = "Dune,Emma,1984"
    print("\n--- String Demonstration ---")
    print("Original:", repr(title))
    print("strip():", clean_title)
    print("upper():", clean_title.upper())
    print("lower():", clean_title.lower())
    print("title():", clean_title.title())
    print("capitalize():", clean_title.capitalize())
    print("index/slice:", clean_title[0], clean_title[4:9])
    print("concatenation:", clean_title + " - classic")
    print("f-string:", f"Title: {clean_title.title()}")
    print("split():", sample.split(","))
    print("join():", " | ".join(sample.split(",")))
    print("replace():", clean_title.replace("gatsby", "Gatsby"))
    print("find():", clean_title.find("great"))
    print("count():", "banana".count("a"))
    print("startswith():", clean_title.startswith("the"))
    print("endswith():", "Emma.pdf".endswith(".pdf"))
    print("Escape characters: first line\\nsecond line\\t(tab)")


def list_methods_demo():
    """Demonstrate list methods required by the assignment."""
    books = ["1984", "Dune", "Emma"]
    print("\n--- List Demonstration ---")
    print("Starting list:", books)
    books.append("Atomic Habits")
    print("append():", books)
    books.insert(0, "The Hobbit")
    print("insert():", books)
    books.extend(["Python Basics", "Dune"])
    print("extend():", books)
    print("index():", books.index("Emma"))
    print("count():", books.count("Dune"))
    books.remove("Dune")
    print("remove():", books)
    removed = books.pop(0)
    print("pop():", removed, "|", books)
    books.sort(key=str.casefold)
    print("sort():", books)
    books.reverse()
    print("reverse():", books)
    print("Indexing:", books[0] if books else "empty", "| last:", books[-1] if books else "empty")
    print("Slice:", books[:2])


def tuple_demo():
    """Demonstrate tuple packing, unpacking, methods, and immutability."""
    isbn = ("978", "0134685991")
    publication = (2020, "3rd Edition", "Pearson")
    prefix, code = isbn
    year, edition, publisher = publication
    print("\n--- Tuple Demonstration ---")
    print("ISBN tuple:", isbn)
    print("Unpacked ISBN:", prefix, code)
    print("Publication tuple:", publication)
    print("Unpacked publication:", year, edition, publisher)
    print("count():", isbn.count("978"))
    print("index():", isbn.index("0134685991"))
    print("Tuples are immutable; the program does not attempt to modify one.")


def set_demo():
    """Demonstrate set de-duplication and set operations."""
    categories = {"Fiction", "Sci-Fi", "Fiction", "History"}
    other_categories = {"History", "Science", "Biography"}
    print("\n--- Set Demonstration ---")
    print("Unique categories:", sorted(categories))
    print("add():", end=" ")
    categories.add("Technology")
    print(sorted(categories))
    print("union():", sorted(categories | other_categories))
    print("intersection():", sorted(categories & other_categories))
    print("difference():", sorted(categories - other_categories))
    print("membership ('Fiction'):", "Fiction" in categories)
    categories.discard("Technology")
    print("discard():", sorted(categories))


def dictionary_demo():
    """Demonstrate dictionary keys, values, items, get, update, pop, and popitem."""
    book = {
        "book_id": "DEMO1", "title": "Dune", "author": "Frank Herbert",
        "category": "Sci-Fi", "available": True, "price": 14.50
    }
    print("\n--- Dictionary Demonstration ---")
    print("keys():", list(book.keys()))
    print("values():", list(book.values()))
    print("items():", list(book.items()))
    print("get():", book.get("price", 0))
    book.update({"available": False})
    print("update():", book["available"])
    removed_value = book.pop("price")
    print("pop(): removed price", removed_value)
    removed_pair = book.popitem()
    print("popitem(): removed", removed_pair)
    print("Remaining record:", book)


def data_structure_demos():
    """Run all five data-structure demonstrations."""
    string_methods_demo()
    list_methods_demo()
    tuple_demo()
    set_demo()
    dictionary_demo()


def seed_sample_books():
    """Load a small, clearly identified sample catalogue for first-run use."""
    if library:
        return
    library.extend([
        {
            "book_id": "B1001", "title": "1984", "author": "George Orwell",
            "publisher": "Secker & Warburg", "category": "Fiction",
            "isbn": ("978", "0451524935"), "available": True,
            "price": 9.99, "shelf_number": "A-01",
            "publication_details": (1949, "First Edition", "Secker & Warburg")
        },
        {
            "book_id": "B1002", "title": "Dune", "author": "Frank Herbert",
            "publisher": "Chilton Books", "category": "Sci-Fi",
            "isbn": ("978", "0441172719"), "available": True,
            "price": 14.50, "shelf_number": "B-04",
            "publication_details": (1965, "First Edition", "Chilton Books")
        },
        {
            "book_id": "B1003", "title": "The Great Gatsby", "author": "F. Scott Fitzgerald",
            "publisher": "Scribner", "category": "Fiction",
            "isbn": ("978", "0743273565"), "available": False,
            "price": 10.99, "shelf_number": "A-14",
            "publication_details": (1925, "First Edition", "Scribner")
        },
    ])


def display_menu():
    """Display the main menu."""
    print("""
========== SMART LIBRARY MANAGEMENT SYSTEM ==========
1. Add a book
2. Display all books
3. Search by title
4. Search by author
5. Update book details
6. Display available books
7. Count available books
8. Display unique categories
9. Display unique authors
10. Sort titles alphabetically
11. Borrow or return a book
12. Demonstrate data structures
0. Exit
======================================================
""")


def main():
    """Run the menu loop until the user selects Exit."""
    seed_sample_books()
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        operations = {
            "1": add_book,
            "2": lambda: display_books(heading="All Books"),
            "3": search_by_title,
            "4": search_by_author,
            "5": update_book,
            "6": display_available_books,
            "7": count_available_books,
            "8": display_unique_categories,
            "9": display_unique_authors,
            "10": sort_titles,
            "11": borrow_or_return,
            "12": data_structure_demos,
        }
        if choice == "0":
            print("Thank you for using the Smart Library Management System.")
            break
        operation = operations.get(choice)
        if operation is None:
            print("Invalid menu choice. Please select an option from the menu.")
        else:
            operation()


if __name__ == "__main__":
    main()
