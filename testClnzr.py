#!/usr/b)in/env python
import unittest
import clnzr

class TestClnzr(unittest.TestCase):

    def setUp(self):
        self.test_file = clnzr.retrieve_file('test.txt')
        self.test_list = clnzr.get_lines(self.test_file)
        self.test_list = clnzr.remove_trailing_whitespace(self.test_list)


    def test_retrieve_file(self):
        self.assertIsNotNone(self.test_file)

    def test_getlines(self):
        self.assertIsNotNone(self.test_list)

    def test_remove_trailing_whitespace(self):
        self.assertNotIn("\n", self.test_list[0])

    def test_write_clean_file(self):
        self.test_list = clnzr.retrieve_lines_from_file('test.txt')
        self.clean_list = clnzr.reformat_lines(self.test_list)
        clnzr.write_clean_file('test.txt', self.clean_list)

    def test_retrieve_lines_from_file(self):
        self.test_list = clnzr.retrieve_lines_from_file('test.txt')
        self.assertIsNotNone(self.test_list)

    def test_reformat_lines(self):
        self.test_list = clnzr.retrieve_lines_from_file('test.txt')
        self.clean_list = clnzr.reformat_lines(self.test_list)
        self.assertIn('\n', self.clean_list[0])

    def tearDown(self):
        self.test_file.close()

if __name__ == "__main__":
    unittest.main()