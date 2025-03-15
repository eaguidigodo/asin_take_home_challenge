import unittest
import os
from main import standardize_date as sd
from main import import_data

class TestCornerCases(unittest.TestCase):
    def test_standardize(self):
        self.assertEqual(sd("1984-09-21"), "1984-09-21")
        self.assertEqual(sd("03/13/1971"), "1971-03-13")
        self.assertEqual(sd("03-05-2004"), "2004-03-05")
        self.assertEqual(sd("21/11/1971"), "1971-11-21")

    def test_import_data(self):
        pass

unittest.main()