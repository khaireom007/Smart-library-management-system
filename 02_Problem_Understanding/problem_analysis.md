# Problem Analysis: Eight Core Problems

This document follows the assignment's four-question breakdown: inputs, expected output, required data, appropriate data structure, and processing steps.

## 1. Store Details of Multiple Books
- **Inputs:** Book ID, title, author, publisher, category, ISBN, price, shelf number.
- **Expected output:** Confirmation when a valid, unique record is stored.
- **Required data:** All fields belonging to a book.
- **Appropriate structure:** Dictionary for one record; list for the catalogue; tuple for ISBN parts.
- **Processing:** Validate fields, reject duplicate IDs, create dictionary, append to list.

## 2. Search Books by Title
- **Inputs:** Title or phrase supplied by the user.
- **Expected output:** Matching record(s), or “Book Not Found”.
- **Required data:** Book titles and associated records.
- **Appropriate structure:** List of dictionaries and a list for matches; strings for comparison.
- **Processing:** Normalize and compare titles without case sensitivity.

## 3. Display All Available Books
- **Inputs:** Current catalogue.
- **Expected output:** Every record marked available, or an empty-result message.
- **Required data:** Each record's availability field.
- **Appropriate structure:** List of dictionaries and a filtered list.
- **Processing:** Traverse the catalogue and collect records whose availability is true.

## 4. Remove Duplicate Book Categories
- **Inputs:** Category from every book.
- **Expected output:** Each category appears once.
- **Required data:** Category strings.
- **Appropriate structure:** List to collect values and set to remove duplicates.
- **Processing:** Collect categories, convert to set, sort for readable display.

## 5. Maintain Author Information
- **Inputs:** Author name and catalogue.
- **Expected output:** Matching books and a unique author list.
- **Required data:** Author fields from records.
- **Appropriate structure:** Strings, list of dictionaries, set for unique authors.
- **Processing:** Search author names case-insensitively; collect matching records; use a set for unique author reporting.

## 6. Count the Number of Available Books
- **Inputs:** Current catalogue.
- **Expected output:** Integer count of records marked available.
- **Required data:** Availability Boolean from each record.
- **Appropriate structure:** List of dictionaries and an integer counter.
- **Processing:** Start count at zero, traverse records, increment for each available record, display count.

## 7. Organize Books According to Genre
- **Inputs:** Current catalogue and each book's category.
- **Expected output:** Unique genres and titles/records grouped by category where needed.
- **Required data:** Category and title fields.
- **Appropriate structure:** Dictionary records, strings, sets for unique categories, lists for grouped records.
- **Processing:** Identify unique categories and use each category to select matching records. The menu provides unique categories; the same fields can be filtered for a category.

## 8. Maintain Complete Book Information
- **Inputs:** All fields for a new book or an update request.
- **Expected output:** A complete, readable record with updated values when valid.
- **Required data:** Book ID, title, author, publisher, category, ISBN, availability, price, shelf number, publication details.
- **Appropriate structure:** Dictionary for one complete record; list for the catalogue; tuple for fixed ISBN/publication data.
- **Processing:** Create a dictionary with named fields, locate it by ID for updates, validate new values, and display the record.
