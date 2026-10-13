# 03. Requirement Analysis

## Functional Requirements
| ID | Requirement |
|---|---|
| FR-01 | Add a book record after validating fields and checking for a duplicate Book ID. |
| FR-02 | Display all records, with a clear message if the catalogue is empty. |
| FR-03 | Search for a book by title without case sensitivity. |
| FR-04 | Search for all books by author. |
| FR-05 | Update supported fields of a book selected by Book ID. |
| FR-06 | Display only books whose availability is true. |
| FR-07 | Count available books. |
| FR-08 | Display unique categories and unique authors using sets. |
| FR-09 | Display book titles in alphabetical order. |
| FR-10 | Demonstrate string, list, tuple, set, and dictionary operations required by Unit 2. |
| FR-11 | Continue displaying the menu until the user chooses Exit. |
| FR-12 | Reject invalid values and unknown menu options without crashing. |

## Non-Functional Requirements
- **Simplicity:** menu labels and messages are beginner-friendly.
- **Ease of use:** each operation prompts for the required fields.
- **Accuracy:** search, count, and availability outputs reflect the current catalogue.
- **Reliability:** invalid inputs are handled with messages and the menu continues.
- **Maintainability:** functions have meaningful names and comments.

## Software Requirements
- Python 3.8 or later (standard library only).
- A terminal or command prompt.
- A text editor or Python IDE.

## Hardware Requirements
Any computer capable of running Python 3.8 or later; keyboard and display. No specialized hardware is required.

## Input Requirements
Book ID and book fields; menu option; title or author search term; update field and value; and demonstration inputs where requested. Text inputs are stripped of surrounding spaces. Numeric price and year-like fields are validated as applicable.

## Output Requirements
Readable catalogue records, search results, confirmation/error messages, available-book list, available-book count, sorted titles, unique values, and data-structure demonstration output.

## System Constraints
- No database or permanent file storage.
- No graphical user interface or web application.
- No third-party dependencies.
- Duplicate Book IDs are not permitted.
- Set display order is not guaranteed; displayed unique values are sorted for readability.
