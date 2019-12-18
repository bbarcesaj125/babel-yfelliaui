import unittest
from year import validate_year_form


class SimpleTest(unittest.TestCase):
    """ Testing validate_year_form() from year.py """

    def test_year_input(self):
        """ Testing if validate_year will recongnize the presence of letters in user input. """

        form = validate_year_form("1555j")
        self.assertEqual(form, "Malformed input!")


if __name__ == "__main__":
    unittest.main()
