import unittest
from year import validate_year_form, calculate_year


class SimpleTest(unittest.TestCase):
    """ Testing validate_year_form() from year.py """

    def test_year_input(self):
        """ Testing if validate_year() will recongnize the presence of letters in user input. """

        form = validate_year_form("1555j")
        self.assertEqual(form, "Malformed input!")


class FuturDateTest(unittest.TestCase):
    """ Testing calculate_year() from year.py """

    def test_year_input(self):
        """ Testing if calculate_year() will recongnize if the user has entered a futur date. """

        futur_error = calculate_year(3215)
        self.assertEqual(futur_error["error"], "Futur date!!")


if __name__ == "__main__":
    unittest.main()
