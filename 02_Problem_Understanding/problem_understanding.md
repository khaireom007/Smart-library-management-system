# 02. Understanding the Problem

## Explanation
The system needs to manage a collection containing many book records. Each record includes a unique book ID, title, author, publisher, category, ISBN, availability, price, and shelf number. The assignment emphasizes choosing data structures for their intended purposes.

## Existing Process or Approach
The assignment states that the Unit 1 version used variables and basic control structures and could realistically handle one book or one transaction at a time. Unit 2 extends this to collections. No other real-world library process is specified in the assignment.

## Problems with the Earlier Approach
- Separate variables do not scale well for many books.
- Related values can become difficult to keep associated with the correct book.
- Searching and reporting across many records becomes cumbersome.
- Duplicate categories and authors are harder to identify without a suitable collection.

## Information Managed
- Book ID (unique identifier)
- Title, author, publisher, and category
- ISBN components
- Availability status
- Price and shelf number

## Expected Behaviour
The program presents a menu, accepts a valid choice, performs the requested operation, displays a result, and returns to the menu until Exit is selected. Duplicate book IDs are rejected. Searches that do not match display a clear message.

## Inputs
Menu selection; book details; search title or author; book ID and field/value for updates; and values for the standalone data-structure demonstrations.

## Processing
Validate and normalize input; search records; add or update dictionaries; traverse the catalogue list; create sets for unique values; sort title lists; count available records; and format readable output.

## Outputs
Book details, success/error messages, available-book lists, matching search results, sorted titles, unique categories/authors, counts, and demonstration outputs.

## Data-Structure Choices
| Structure | Use in this project | Reason |
|---|---|---|
| String | Titles, names, categories, IDs, messages | Text processing and comparison |
| List | Master catalogue and search results | Ordered, changeable collection |
| Tuple | ISBN components and fixed publication details | Ordered and immutable |
| Set | Unique categories and authors | Automatically removes duplicates |
| Dictionary | One complete book record | Named key-value fields |

## Constraints and Assumptions
- The program is console-based and uses the Python standard library only.
- The catalogue is in memory; persistence is outside the assignment's stated scope.
- Book IDs are unique within the current session.
- ISBN is represented as a tuple of two text components; the application validates a 13-digit ISBN after removing hyphens and spaces.
- Price must be non-negative. Availability is represented as a Boolean value.
- The assignment provides a sample record and operations but does not specify institutional policies such as fines or borrowing limits; these are not invented.
