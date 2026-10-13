# 04. Algorithm Development

Each algorithm uses the same logic as the Python implementation.

## Algorithm 1: Add a Book
**Input:** Book ID, title, author, publisher, category, ISBN, price, shelf number.  
**Output:** Confirmation or validation/duplicate message.
1. Start.
2. Read the book fields.
3. Remove unnecessary spaces and normalize title/category text.
4. Validate required fields, ISBN, and non-negative price.
5. Check each catalogue record for the same Book ID.
6. If the ID already exists, display a duplicate message and stop this operation.
7. Create a dictionary for the book; store ISBN components in a tuple and set availability to true.
8. Append the dictionary to the catalogue list.
9. Display success.
10. End the operation.

## Algorithm 2: Search by Title
**Input:** Search title. **Output:** Matching book record(s) or not-found message.
1. Start.
2. Read and normalize the search title.
3. Create an empty results list.
4. Visit each book in the catalogue.
5. If its title matches without case sensitivity, append it to results.
6. If results are empty, display “Book Not Found”; otherwise display all matches.
7. End.

## Algorithm 3: Display All Books
**Input:** Current catalogue. **Output:** All records or an empty-catalogue message.
1. Start.
2. Check whether the catalogue is empty.
3. If empty, display the message.
4. Otherwise, display each book's fields.
5. End.

## Algorithm 4: Update a Book
**Input:** Book ID, allowed field, new value. **Output:** Update confirmation or not-found/invalid-field message.
1. Start.
2. Read the Book ID and search the catalogue.
3. If no record is found, display “Book Not Found”.
4. Otherwise show the supported update fields and read a field/value.
5. Validate the value for the selected field.
6. Update the selected dictionary field; for ISBN, store validated components as a tuple.
7. Display confirmation.
8. End.

## Algorithm 5: Remove Duplicate Categories
**Input:** Catalogue category fields. **Output:** Unique categories.
1. Start.
2. Create a list of category strings from all records.
3. Convert the list into a set.
4. Sort the unique values for readable output.
5. Display the values.
6. End.

## Algorithm 6: Count Available Books
**Input:** Catalogue. **Output:** Integer count.
1. Start.
2. Set count to zero.
3. For every book, check its availability value.
4. If available, increase count by one.
5. Display count.
6. End.

## Algorithm 7: Find Books by Author
**Input:** Author name. **Output:** Matching records or no-match message.
1. Start.
2. Read and normalize the author name.
3. Create an empty matches list.
4. Visit every book and compare author names without case sensitivity.
5. Append matching records.
6. Display matches or a no-match message.
7. End.

## Algorithm 8: Sort Titles Alphabetically
**Input:** Catalogue. **Output:** Sorted list of titles.
1. Start.
2. Copy the titles into a new list.
3. Sort the list without changing the catalogue order.
4. Display the sorted titles.
5. End.

## Algorithm 9: Display Available Books
**Input:** Catalogue. **Output:** Available records or no-available-books message.
1. Start.
2. Create an empty results list.
3. Add each record whose availability is true.
4. Display the results or an appropriate empty message.
5. End.

## Algorithm 10: Borrow or Return a Book
**Input:** Book ID and action. **Output:** Updated availability or explanation.
1. Start.
2. Find the record using Book ID.
3. If not found, display “Book Not Found”.
4. If borrowing, check availability. If already borrowed, report that it is unavailable; otherwise set availability to false.
5. If returning, check availability. If already available, report that; otherwise set availability to true.
6. Display the result.
7. End.

## Algorithm 11: Main Menu and Exit
**Input:** Menu choice. **Output:** Operation result and program termination when Exit is selected.
1. Start.
2. Display the menu.
3. Read the choice.
4. If the choice matches an operation, call that operation.
5. If the choice is Exit, display a closing message and stop.
6. If the choice is invalid, display an error message.
7. Repeat from Step 2 while the program is running.
