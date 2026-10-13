"""Automated tests for the Smart Library Management System."""
import contextlib
import io
import unittest
from unittest.mock import patch
import main


class LibraryTests(unittest.TestCase):
    def setUp(self):
        main.library.clear()
        main.seed_sample_books()

    def test_sample_catalogue_has_three_books(self):
        self.assertEqual(len(main.library), 3)

    def test_find_title_case_insensitive(self):
        matches = [b for b in main.library if b["title"].casefold() == "dune"]
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["book_id"], "B1002")

    def test_unique_categories_discards_duplicates(self):
        self.assertEqual(main.unique_categories(), {"Fiction", "Sci-Fi"})

    def test_count_available_books(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            main.count_available_books()
        self.assertIn("Available books: 2", output.getvalue())

    def test_isbn_valid(self):
        self.assertEqual(main.validate_isbn("978-0-13-468599-1"), ("978", "0134685991"))

    def test_isbn_invalid(self):
        with self.assertRaises(ValueError):
            main.validate_isbn("12345")

    def test_duplicate_book_id_rejected(self):
        answers = iter(["B1001"])
        output = io.StringIO()
        with patch("builtins.input", side_effect=lambda _: next(answers)), contextlib.redirect_stdout(output):
            main.add_book()
        self.assertEqual(len(main.library), 3)
        self.assertIn("already exists", output.getvalue())

    def test_borrow_then_return(self):
        book = main.find_by_id("B1001")
        self.assertTrue(book["available"])
        with patch("builtins.input", side_effect=["B1001", "B"]), contextlib.redirect_stdout(io.StringIO()):
            main.borrow_or_return()
        self.assertFalse(book["available"])
        with patch("builtins.input", side_effect=["B1001", "R"]), contextlib.redirect_stdout(io.StringIO()):
            main.borrow_or_return()
        self.assertTrue(book["available"])

    def test_empty_catalogue_display(self):
        main.library.clear()
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            main.display_books()
        self.assertIn("No books to display", output.getvalue())

    def test_unknown_id(self):
        self.assertIsNone(main.find_by_id("UNKNOWN"))

    def test_sort_titles_does_not_reorder_catalogue(self):
        original_ids = [book["book_id"] for book in main.library]
        with contextlib.redirect_stdout(io.StringIO()):
            main.sort_titles()
        self.assertEqual([book["book_id"] for book in main.library], original_ids)


if __name__ == "__main__":
    unittest.main(verbosity=2)
