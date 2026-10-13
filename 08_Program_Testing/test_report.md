# 08. Program Testing Report

## Testing Objectives
Verify catalogue operations, data-structure behaviour, input validation, and expected responses for normal, boundary, duplicate, and invalid cases.

## Methodology
The project includes automated tests using Python's standard `unittest` framework. Tests isolate the in-memory catalogue and verify returned values or captured console output. Run them from `07_Python_Programming` with `python -m unittest discover -s ../08_Program_Testing -v`.

## Test Cases and Results
The actual results below are populated after executing the included test suite in the build environment.

| ID | Test | Expected result |
|---|---|---|
| T01 | Load sample catalogue | Three sample records are present |
| T02 | Search for “dune” with different capitalization | Dune record matches |
| T03 | Extract categories | Set contains Fiction and Sci-Fi once each |
| T04 | Count available records | Count is 2 for sample data |
| T05 | Validate correctly formatted 13-digit ISBN | Returns two-part tuple |
| T06 | Validate short/invalid ISBN | Raises a clear validation error |
| T07 | Add duplicate Book ID | Record is rejected and catalogue count stays unchanged |
| T08 | Borrow then return an available book | Availability changes False, then True |
| T09 | Display an empty catalogue | Friendly message; no crash |
| T10 | Search for unknown ID | No record is returned |
| T11 | Sort titles | Titles display alphabetically and catalogue order remains unchanged |

## Execution Results

- **Executed command:** `python -m unittest discover -s ../08_Program_Testing -v`
- **Actual result:** 11 tests passed, 0 failed.
- **Pass/fail status:** All 11 automated tests passed in the build environment.
- **Bugs identified and corrected:** No failures were observed in the included automated suite. This does not replace a manual interactive demonstration on the student's computer.
- **Limitations:** Automated tests cover the core operations listed above. Menu navigation and all possible malformed interactive sequences should also be demonstrated manually before submission.

## Trace Table: Adding a Book
| Step | Action | Expected state/result |
|---|---|---|
| 1 | Catalogue begins with sample records | Three records present |
| 2 | Enter a new unique ID | Duplicate check returns false |
| 3 | Validate required fields, ISBN, and price | Valid values accepted |
| 4 | Build dictionary record | Related fields stay in one record |
| 5 | Append to catalogue list | Catalogue has one additional record |
| 6 | Display confirmation | “Book added successfully.” |

## Trace Table: Remove Duplicate Categories
| Step | Action | Result |
|---|---|---|
| 1 | Read category from each sample book | Fiction, Sci-Fi, Fiction |
| 2 | Convert values to a set | Fiction and Sci-Fi only |
| 3 | Sort for display | Fiction, Sci-Fi |

## Trace Table: Count Available Books
| Book ID | Availability | Count after checking |
|---|---|---:|
| B1001 | True | 1 |
| B1002 | True | 2 |
| B1003 | False | 2 |
| **Final output** |  | **Available books: 2** |
